#!/usr/bin/python
import gnupg
from pprint import pprint
#
#IMPORT NEW KEY to TALK to NEW SERVERS IE. YOUR FRIENDS DUH
#
def importK():
 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 key_data = open('/PATH/TO/NEW/PUBKEY_USER/pub.key').read()
 import_result = gpg.import_keys(key_data)
 pprint(import_result.results)
def main():
 importK()
if __name__ == '__main__':
 main()
