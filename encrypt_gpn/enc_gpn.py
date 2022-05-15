import gnupg
from pprint import pprint
import os

os.system('rm -rf /home/testgpguser/gpghome')
gpg = gnupg.GPG(gnupghome='/home/testgpguser/gpghome')
key_data = open('mykeyfile.asc').read()
import_result = gpg.import_keys(key_data)
pprint(import_result.results)

# gpg = gnupg.GPG(gnupghome='/home/testgpguser/gpghome')
# public_keys = gpg.list_keys()
# private_keys = gpg.list_keys(True)
# print ('public keys:')
# pprint(public_keys)
# print ('private keys:')
# pprint(private_keys)