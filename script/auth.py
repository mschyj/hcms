import requests,os,ConfigParser
import json

home=os.environ['HOME']
config=ConfigParser.ConfigParser()
config.read(home+"/.elasticluster/config")
username=config.get("cloud/catalyst","username")
password=config.get("cloud/catalyst","password")
domain_name=config.get("cloud/catalyst","user_domain_name")
project_name=config.get("cloud/catalyst","project_name")
auth_url=config.get("cloud/catalyst","auth_url")

headers = {
    'Content-Type': 'application/json;charset=utf8',
}

data = {
  "auth": {
    "identity": {
      "methods": [
        "password"
      ],
      "password": {
        "user": {
          "name": username,
          "password":password,
          "domain": {
            "name": domain_name
          }
        }
      }
    },
    "scope": {
      "project": {
        "name": project_name
      }
    }
  }
} 

data=json.dumps(data)

response = requests.post('%s/auth/tokens'%auth_url, headers=headers, data=data)

print response

