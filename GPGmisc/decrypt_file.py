#!/usr/bin/python

import gnupg
import sys


def decryptTHATshit():

 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 with open(sys.argv[1], 'rb') as f:
    status = gpg.decrypt_file(f, passphrase='YOUR_PASSWORD', output='DECRYPTED.txt')

 print 'ok: ', status.ok
 print 'status: ', status.status
 print 'standerd error: ', status.stderr

def main():
 decryptTHATshit()

if __name__ == '__main__':
 try:
  if len(sys.argv[1]) > 1: 
   main()
 except:
  print "Usage:" , sys.argv[0] , "File2decrypt"
