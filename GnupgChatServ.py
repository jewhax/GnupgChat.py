#!/usr/bin/python
                    
import socket
import select
import gnupg
import os,sys,time
gpg = gnupg.GPG(gnupghome='/PATH/TO/GPG/FOLDER')
red = '\033[31m'
end = '\033[0m'

class ChatServer:

  def __init__( self, port ):
    self.port = port;
    self.srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    self.srvsock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    self.srvsock.bind( ("", port) )
    self.srvsock.listen( 3 )
    self.descriptors = [self.srvsock]
    print 'GnupgChatServ started on port %s' % port

  def run( self ):
   while 1:
    #EVENT__
    (sread, swrite, sexc) = select.select( self.descriptors, [], [] )
    #READ RECPT___
    for sock in sread:
      #Received Connection___
      if sock == self.srvsock:
        self.accept_new_connection()
      else:

        #DATA ON SOCK____
        str = sock.recv(1024)
        ##################################################
	#GPG Decryption of Message
	#	
	chatLog = open('/tmp/CHAT', 'w')
	chatLog.write(str)
	
	with open('/tmp/CHAT', 'rb') as f:
         status = gpg.decrypt_file(f, passphrase='YOUR_PASSWORD_THE_REALLY_LONG_ONE', output='/tmp/CHAT.log')
  	
	if status.ok == False:
         print "\nClear Text:"

   	elif status.ok == True:        
       # print 'ok: ', status.ok
       # print 'status: ', status.status
       # print 'stderr: ', status.stderr 	 
	 time.sleep(5)
	 print red + "Decrypted Data: " 
         os.system('cat /tmp/CHAT.log' + "\n") 
         print "\n" , end
       #fix=open('/tmp/CHAT.log', 'r')#
       #fix.readline()  		#
       #fix.close()			 #
       ##################################################
        #SOCK CK
        if str == '':
          host,port = sock.getpeername()
          str = 'Client left %s:%s\r\n' % (host, port)
          self.broadcast_string( str, sock )
          sock.close
          self.descriptors.remove(sock)
        else:
          host,port = sock.getpeername()
          newstr = '[%s:%s] %s' % (host, port, str)
          self.broadcast_string( newstr, sock )


  def broadcast_string( self, str, omit_sock ):
   for sock in self.descriptors:
    if sock != self.srvsock and sock != omit_sock:
      sock.send(str)
   print str,

  def accept_new_connection( self ):
   newsock, (remhost, remport) = self.srvsock.accept()
   self.descriptors.append( newsock )
   newsock.send("Python-Gnupg chatserver BETA 0.1\r\nAll Data is sent clear Text.\r\nSo Watch it.\r\n")
   str = 'Client joined %s:%s\r\n' % (remhost, remport)
   self.broadcast_string( str, newsock )


Server = ChatServer( 4443 ).run()

