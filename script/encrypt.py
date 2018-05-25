#!/user/bin/env python

import sys
import os
import subprocess

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
class AESCrypto():
    def __init__(self):
        self.key = '1234567890123456' 
        self.mode = AES.MODE_CBC

    def encrypt(self,text):
        if len(text)%16!=0:
            text=text+str((16-len(text)%16)*'+')
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        try:
            plain_text  = cryptor.decrypt(a2b_hex(text))
            return plain_text.rstrip('+')
        except TypeError,e:
            print "Your username/password is not encrypted:" + e.message
if __name__ == '__main__':
    username = raw_input("Please input your username of your cloud provider: ")
    password = raw_input("Please input your password of your cloud provider: ")
    pc = AESCrypto() 
    sec_username = pc.encrypt(username)
    sec_password = pc.encrypt(password)
    print "The encrypted username is: " + sec_username
    print "The encrypted password is: " + sec_password
    home=os.environ['HOME']
    config=home + "/.hwcc/config"
    sed_cmd1="sed -i '/username =/c username = " + sec_username + "' " + config
    sed_cmd2="sed -i '/password =/c password = " + sec_password + "' " + config
    subprocess.call(sed_cmd1,shell=True)
    subprocess.call(sed_cmd2,shell=True)
    print "The config file has been updated"
