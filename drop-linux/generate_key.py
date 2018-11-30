# author: https://github.com/ddesmond/clarisse-drop
# this file generates youre personal encryption key.
# after you loose it you loose acces to your online repository, so be careful and
# BACKUP THE GENERATED KEY FILE.
import os
from cryptography.fernet import Fernet



if os.path.isfile('keyfile.key'):
	print "-------------------------------------------------------"
	print "keyfile exists, please delete the old keyfile to reset."
	f = open('keyfile.key', 'r')
	print f.readline()
	print "-------------------------------------------------------"
else:
	print "-------------------------------------------------------"
	print "creating new keyfile"
	key = Fernet.generate_key()
	f = open('keyfile.key', 'w')
	f.write(key)
	f.close()
	print "Keyfile written", key
	print "-------------------------------------------------------"