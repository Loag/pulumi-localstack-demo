import pulumi
from pulumi_aws import s3

bucket = s3.Bucket("new-bucket")

pulumi.export('bucket_name', bucket.id)
