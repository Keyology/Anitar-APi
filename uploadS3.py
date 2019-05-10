import boto3
import os
from dotenv import load_dotenv
load_dotenv()
 
def upload_files(path):
    try:
        session = boto3.Session(
            aws_access_key_id=os.getenv("aws_access_key_id"),
            aws_secret_access_key=os.getenv("aws_secret_access_key"),
            region_name=os.getenv("region_name")
        )
        s3 = session.resource('s3')
        bucket = s3.Bucket('anitar-images')
    
        for subdir, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(subdir, file)
                with open(full_path, 'rb') as data:
                    bucket.put_object(Key=full_path[len(path)+1:], Body=data)
    except:
        print("ERROR Uploading files")

def get_file_url():

    session = boto3.Session(
        aws_access_key_id=os.getenv("aws_access_key_id"),
        aws_secret_access_key=os.getenv("aws_secret_access_key"),
        region_name=os.getenv("region_name")
        )
    s3 = session.resource('s3')
    bucket = s3.Bucket('anitar-images')
    bucket_location = boto3.client(
    's3',
    aws_access_key_id=os.getenv("aws_access_key_id"),
    aws_secret_access_key=os.getenv("aws_secret_access_key")
    ).get_bucket_location(Bucket="anitar-images")
    urls = []
    for file in bucket.objects.all():
        # params = {'Bucket': 'anitar-images', 'Key': file.key}
        # url = s3_client.generate_presigned_url('get_object', params)
        # urls.append(url)
        # print("BUCKET URL", urls)
        object_url = f"https://s3-{bucket_location['LocationConstraint']}.amazonaws.com/anitar-images/{file.key}"
        urls.append(object_url)
    return urls
        



if __name__ == "__main__":
    #upload_files('/home/key/Dev/anitar-api/image_download')
    get_file_url()