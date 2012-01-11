#!/usr/bin/python
import gnupg
import sys

def encryptFile():
 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 data=open(sys.argv[1], 'rb')
 with data as f:
    status = gpg.encrypt_file(
        f, recipients=['YOUR@MAIL.COM'],
        output='encrypted_FILE.txt.gpg')

 print 'ok: ', status.ok
 print 'status: ', status.status
 print 'standerd error: ', status.stderr

def main():
 encryptFile()
if __name__ == '__main__':
 main()

