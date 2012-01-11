#!/usr/bin/python
import gnupg

def delK():
 gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
 key_id = 'ERTRVEOEKROE2324335434232342424' ## EXAMPLE ID 
 str(gpg.delete_keys(key_id))
 
def main():
 delK()

if __name__ == '__main__':
 main()
