#!/usr/bin/python
import gnupg, time 
import os,sys,socket
#
#Change IP of course if you(127.0.0.1) are not the SERVER 
#NUB 2.0 ----1.0 of this .PY DOESNT HAVE "recipients & always_trust"(just had my email cause I was testing localy 
#
def chat():
  gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
  unencrypted_string = raw_input('Enter txt to encrypt:')
  encrypted_data = gpg.encrypt(unencrypted_string, 
			       recipients=['B522FD_PUBLIC_KEY_ID_HERE_REREREREFD'],
                               always_trust='True')
  encrypted_string = str(encrypted_data)
  def so():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect(('127.0.0.1', 4443))
   da=s.recv(1024)
   print da
   #  print 'ok: ', encrypted_data.ok
   #  print 'status: ', encrypted_data.status
   #  print 'stderr: ', encrypted_data.stderr
   #  print 'unencrypted_string: ', unencrypted_string
   #  print 'encrypted_string: ', encrypted_string
   s.send(encrypted_string)
   time.sleep(5)
   s.close()
  so()   
def main():
 chat()
 
if __name__ == '__main__':
 try:
  while True:
   main()
 except: 
  print "CTL-C Caught Exiting." 
  sys.exit()  
 
