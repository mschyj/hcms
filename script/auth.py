import requests,os,ConfigParser
import json

home=os.environ['HOME']
config=ConfigParser.ConfigParser()
config.read(home+"/.hwcc/config")
username=config.get("cloud/hwc","username")
password=config.get("cloud/hwc","password")
domain_name=config.get("cloud/hwc","user_domain_name")
project_name=config.get("cloud/hwc","project_name")
auth_url=config.get("cloud/hwc","auth_url")

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

