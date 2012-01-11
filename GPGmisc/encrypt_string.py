#!/usr/bin/python
import gnupg
#
#ENCRYPT STRING WITH YOUR OWN GNUPG PUB
#
def encryptS():
 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 unencrypted_string = raw_input('Enter Text to encrypt:')
 encrypted_data = gpg.encrypt(unencrypted_string, 'YOUREMAIL@ME.COM')
 encrypted_string = str(encrypted_data)
 print 'ok: ', encrypted_data.ok
 print 'status: ', encrypted_data.status
 print 'standerd error: ', encrypted_data.stderr
 print 'unencrypted_string: ', unencrypted_string
 print 'encrypted_string: ', encrypted_string
def main():
 encryptS()
if __name__ == '__main__':
 main()
