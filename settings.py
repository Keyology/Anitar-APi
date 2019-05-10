from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

os.environ.get("SECRET_KEY")
aws_access_key_id=os.environ.get("aws_access_key_id")
aws_secret_access_key=os.environ.get("aws_secret_access_key")
region_name=os.environ.get("region_name")