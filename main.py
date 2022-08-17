#implementation of loggers
import logging

# Create and configure logger
logging.basicConfig(filename="log_file.log",level=logging.INFO)
logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# import required module
import os

from cryptography.fernet import Fernet

# key generation
from adlsconn import upload_file_to_directory

key = Fernet.generate_key()

# string the key in a file
with open('C://Project_sample//file_key//filekey.key', 'wb') as filekey:
    filekey.write(key)

# opening the key
with open('C://Project_sample//file_key//filekey.key', 'rb') as filekey:
    key = filekey.read()

# using the generated key
fernet = Fernet(key)

# assign directory
dir_path = r'c:\\Project_sample\files_folder'
# list to store files
res = []
filenum=0

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
logger.info(res)

# iterate over files in
# that directory
for filename in res:
    logger.info(filename)
    # opening the original file to encrypt
    with open(dir_path+'/'+filename, 'rb') as file:
        original = file.read()
    # encrypting the file
    encrypted = fernet.encrypt(original)
    # logger.info(encrypted)
    upload_file_to_directory(encrypted,filename)
    # filenum+=1


# # using the key
# fernet = Fernet(key)
#
# # opening the encrypted file
# with open('C://Project_sample//files_folder//encrypt_Testing', 'rb') as enc_file:
#     encrypted = enc_file.read()
#
# # decrypting the file
# decrypted = fernet.decrypt(encrypted)
#
# # opening the file in write mode and
# # writing the decrypted data
# with open('C://Project_sample//files_folder//decrypt_Testing', 'wb') as dec_file:
#     dec_file.write(decrypted)




