# encoding:UTF-8
import requests,os,ConfigParser,json,time
import re
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
class Session:
    def __init__(self):
        home = os.environ['HOME']
        self.config = ConfigParser.ConfigParser()
        self.path = home+"/.hwcc/config"
        self.config.read(self.path)
        sections = self.config.sections()
        cloud_section = None
        for section in sections:
            if  re.match(r'cloud',section) is not None:
                cloud_section = section
        username_encrypt = self.config.get(cloud_section,"username")
        self.username = self._decrypt( username_encrypt )
        password_encrypt = self.config.get(cloud_section,"password")
        self.password = self._decrypt( password_encrypt )
        self.domain_name = self.config.get(cloud_section,"user_domain_name")
        self.project_name = self.config.get(cloud_section,"project_name")
        self.auth_url = self.config.get(cloud_section,"auth_url")
        self.project_id = self.config.get("sfs","project_id")
        self.sfs_endpoint = self.config.get("sfs","sfs_endpoint")
        self.sfs_name = self.config.get("sfs","sfs_name")
        self.sfs_size = self.config.get("sfs","sfs_size")
        self.sfs_vpc_id = self.config.get("sfs","sfs_vpc_id")
        self.is_create_sfs = self.config.get("sfs","is_create_sfs")
    def _decrypt(self,text):
        cryptor = AES.new('1234567890123456',AES.MODE_CBC,b'0000000000000000')
        try:
            plain_text = cryptor.decrypt(a2b_hex(text))
            return plain_text.rstrip('+')
        except TypeError,e:
            print "Your username/password seems not be encrypted:" + e.message

    def auth(self):
        '''
        Auth function,send auth payload to keystone service
        '''
    
        auth_headers = {
            'Content-Type': 'application/json;charset=utf8',
        }
    
        auth_para = {
          "auth": {
            "identity": {
              "methods": [
                "password"
              ],
              "password": {
                "user": {
                  "name":self.username,
                  "password":self.password,
                  "domain": {
                    "name":self.domain_name
                  }
                }
              }
            },
            "scope": {
              "project": {
                "name": self.project_name
              }
            }
          }
        } 
        
        auth_para=json.dumps(auth_para)
        try:
            auth_response = requests.post('%s/auth/tokens'%self.auth_url, headers=auth_headers, data=auth_para)
        except requests.ConnectionError as msg:
            raise ResponseError(str(msg))
    
        if auth_response.status_code != 201 and auth_response.status_code !=200:
            raise ResponseError("{0} status , msg:{1}".format(auth_response.status_code,auth_response.content))
    	try:
    	    token = auth_response.headers['X-Subject-Token']
    	except:
    	    raise ResponseError("cannot find token in headers")
    	self.token = token
    def query_all_sfs(self):
        '''
        query all sfs infos,return whether exists same name avilable sfs 
        
        '''
        query_all_sfs_headers = {
            'X-Auth-Token': self.token,
            'Content-Type': 'application/json'
        } 
        try:
            query_all_sfs_response = requests.get('https://%s/v2/%s/shares/detail'%(self.sfs_endpoint,self.project_id), headers=query_all_sfs_headers)
        except requests.ConnectionError as msg:
            raise ResponseError(str(msg))
        if query_all_sfs_response.status_code != 201 and query_all_sfs_response.status_code !=200 :
            raise ResponseError("{0} status , msg:{1}".format(query_all_sfs_response.status_code,query_all_sfs_response.content))
        query_all_sfs_response = query_all_sfs_response.json()    
        for sfs_info in query_all_sfs_response['shares']:
            if sfs_info["name"] == self.sfs_name and sfs_info["status"] == "available":
                export_location =  sfs_info["export_locations"][0]
                self.config.set("sfs","global_var_sfs_export_location",export_location)
                self.config.set("setup/ansible-slurm","global_var_sfs_export_location",export_location)
                self.config.write(open(self.path,"w"))
                return True
            else:
                return False

    
    def create_sfs(self):
        '''
        create sfs function , create sfs with no vpc

        '''
        create_sfs_headers = {
            'X-Auth-Token': self.token,
            'Content-Type': 'application/json'
        }
        create_sfs_para = {
            "share": {
            "share_type": None,
            "name": self.sfs_name,
            "snapshot_id": None,
            "description": "test description",
            "share_proto": "NFS",
            "share_network_id": None,
            "size": self.sfs_size,
            "is_public": False
             }
        }
        create_sfs_para=json.dumps(create_sfs_para)
        try:
            createsfs_response = requests.post('https://%s/v2/%s/shares'%(self.sfs_endpoint,self.project_id), headers=create_sfs_headers, data=create_sfs_para)
        except requests.ConnectionError as msg:
            raise ResponseError(str(msg))
        if createsfs_response.status_code != 201 and createsfs_response.status_code !=200 :
            raise ResponseError("{0} status , msg:{1}".format(createsfs_response.status_code,createsfs_response.content))
        createsfs_response = createsfs_response.json()
        self.share_id = createsfs_response["share"]["links"][0]["href"].split("/")[6]


    def add_vpc_for_sfs(self):
        '''
        add vpc for sfs function
        
        '''       

        add_vpc_headers = {
            'X-Auth-Token': self.token,
            'Content-Type': 'application/json'
        }

        add_vpc_para = {
            "os-allow_access": {
                "access_to": self.sfs_vpc_id,
                "access_type": "cert",
                "access_level": "rw"
            }
        }         
        add_vpc_para=json.dumps(add_vpc_para)
        try:
            addvpc_response = requests.post('https://%s/v2/%s/shares/%s/action'%(self.sfs_endpoint,self.project_id,self.share_id), headers=add_vpc_headers, data=add_vpc_para)
        except requests.ConnectionError as msg:
            raise ResponseError(str(msg))
        if addvpc_response.status_code != 201 and addvpc_response.status_code !=200 :
            raise ResponseError("{0} status , msg:{1}".format(addvpc_response.status_code,addvpc_response.content))
        addvpc_response = addvpc_response.json()


    def query_sfs_info(self):
        
       '''      
       query sfs export location
       
       '''
       query_sfs_headers = {
            'X-Auth-Token': self.token,
            'Content-Type': 'application/json'
        }

       try:
           sfsinfo_response = requests.get('https://%s/v2/%s/shares/%s'%(self.sfs_endpoint,self.project_id,self.share_id), headers=query_sfs_headers)
       except requests.ConnectionError as msg:
           raise ResponseError(str(msg))
       if sfsinfo_response.status_code != 201 and sfsinfo_response.status_code !=200 :
           raise ResponseError("{0} status , msg:{1}".format(sfsinfo_response.status_code,sfsinfo_response.content))
       sfsinfo_response = sfsinfo_response.json()
       export_location = sfsinfo_response["share"]["export_locations"][0]
       self.config.set("sfs","global_var_sfs_export_location",export_location)
       self.config.set("setup/ansible-slurm","global_var_sfs_export_location",export_location)
       self.config.write(open(self.path,"w"))   


    def create_sfs_all(self):
        self.auth()
        if not self.is_create_sfs:
            return 
        else:
            self.auth()
            if not self.query_all_sfs():
                self.create_sfs()
                time.sleep(5)
                self.add_vpc_for_sfs()
                self.query_sfs_info()
            time.sleep(5)
            if not self.has_config():
                print "create sfs fail,kill the hwcc process"
                os.system('kill -s 9 `pgrep hwcc`')

    def has_config(self):
        sfs_export_location = self.config.get("setup/ansible-slurm","global_var_sfs_export_location")
        print sfs_export_location
        if sfs_export_location is not None:
            return True
        else:
            return False


class ResponseError(Exception):
    pass
if __name__ == "__main__":
    session = Session()
    session.create_sfs_all()   
