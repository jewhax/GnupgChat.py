#!/usr/bin/python
##########################################################################
##YOU NEED TO ADD FINGERPRINT ID EX. '4543342ETRTIEVRFMVOTVMOEMV3455325'##
##########################################################################
import gnupg
import sys

def encryptP():
 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 data=open(sys.argv[1], 'rb')
 with data as f:
     status = gpg.encrypt_file(
         f, recipients=['B522FD_PUBLIC_KEY_ID_HERE_REREREREFD'],
         always_trust='True',
         output='encrypted_FILE.txt.gpg')
 print 'ok: ', status.ok
 print 'status: ', status.status
 print 'standerd error: ', status.stderr

def main():
 encryptP()

if __name__ == '__main__':
 main()


