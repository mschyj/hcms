#!/user/bin/env python

import sys
import os
import ConfigParser

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
    config=ConfigParser.ConfigParser()
    config.read(home + "/.hwcc/config")
    config.set("cloud/hwc", "username", sec_username)
    config.set("cloud/hwc", "password", sec_password)
    config.write(open(home + "/.hwcc/config","w")) 
    print "The config file has been updated"
