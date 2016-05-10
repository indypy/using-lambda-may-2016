from __future__ import print_function

import os
import urllib
import boto3

from PIL import Image

print('Loading function')

s3_client = boto3.client('s3')

size = 128, 128


def lambda_handler(event, context):
    # Get the object from the event and create a thumbnail
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
    path, filename = os.path.split(key)
    image_name, ext = os.path.splitext(filename)
    thumb_name = image_name + "_thumb" + ext

    try:
        s3_client.download_file(bucket, key, '/tmp/'+filename)
        im = Image.open('/tmp/'+filename)
        im.thumbnail(size)
        im.save('/tmp/'+thumb_name, "JPEG")
        s3_client.upload_file('/tmp/'+thumb_name, bucket, 'thumbs/'+thumb_name)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist \
              and your bucket is in the same region as this function.'.format(
            key, bucket)
        )
        raise e
