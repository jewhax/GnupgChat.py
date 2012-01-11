#!/usr/bin/python
import gnupg
import sys

def decryptS():
 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 encrypted_data = raw_input()
 encrypted_string = str(encrypted_data)
 decrypted_data = gpg.decrypt(encrypted_string, passphrase='YOUR_PASSWORD')
 print 'ok: ', decrypted_data.ok
 print 'status: ', decrypted_data.status
 print 'standerd error: ', decrypted_data.stderr
 print 'decrypted string: ', decrypted_data.data
def main():
 decryptS()
if __name__ == '__main':
 main()
