# coding: utf-8
import sys
from config import config
from boto3.session import Session

def run(args):
    s3client = Session().client('s3')
    response = s3client.list_objects(
        Bucket=config.BUCKET_NAME,
        Prefix=args.model_output_dir + args.name + '/'
    )
    if "Contents" in response:
        print("S3上に指定のフォルダが既に存在しています。")
        sys.exit(1)