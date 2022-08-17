from azure.storage.filedatalake import DataLakeServiceClient

#Config parser parses the config files
from configparser import ConfigParser

#implementation of loggers
import logging

# Create and configure logger
logging.basicConfig(filename="log_file.log", level=logging.INFO)

logger = logging.getLogger()
# logger.setLevel(logging.INFO)

config = ConfigParser()
config.read('config.ini')

storage_account_name = config['cred']['san']
storage_account_key = config['cred']['sak']
logger.info(storage_account_name)
logger.info(storage_account_key)

#Establishing a connection to adls2
def initialize_storage_account(storage_account_name, storage_account_key):
    try:
        global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
        logger.info("connection established successfully")

    except Exception as e:
        logger.info(e)


initialize_storage_account(storage_account_name, storage_account_key)

# #Creation of a container
# def create_file_system():
#     try:
#         global file_system_client
#
#         file_system_client = service_client.create_file_system(file_system="my-file-system")
#         logger.info("file system created")
#     except Exception as e:
#         logger.info(e)
#
# create_file_system()
#
# #Creation of a directory
# def create_directory():
#     try:
#         file_system_client.create_directory("my-directory")
#         logger.info("Directory is created")
#
#     except Exception as e:
#         logger.info(e)

# create_directory()

#Upload a file to a directory
def upload_file_to_directory(encrypted_data,filename):
    try:
        file_system_client = service_client.get_file_system_client(file_system="my-file-system")

        directory_client = file_system_client.get_directory_client("Encrypted_files")
        file_client = directory_client.create_file(filename)
        # logger.info("Created file in ADLS2:"+filename)
        file_client.upload_data(encrypted_data, overwrite=True)
        # file_client.append_data(data=encrypted_data, offset=0, length=len(encrypted_data))

        # file_client.flush_data(len(file_contents))
        # logger.info("Uploaded "+filename)

    except Exception as e:
        logger.info(e)