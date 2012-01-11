#!/usr/bin/python
import gnupg
from pprint import pprint

def listK():
 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 public_keys = gpg.list_keys()
 private_keys = gpg.list_keys(True)
 print 'public keys:'
 pprint(public_keys)
 print 'private keys:'
 pprint(private_keys)
def main():
 listK()
if __name__ == '__main__':
 main()
