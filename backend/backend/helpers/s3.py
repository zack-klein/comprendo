from aws_cdk import aws_s3, core


def create_downloads_bucket(cls, name):
    downloads_bucket = aws_s3.Bucket(
        cls,
        id=f"{name}-downloads-bucket",
        bucket_name=name,
        removal_policy=core.RemovalPolicy.DESTROY,
    )
    downloads_bucket.add_lifecycle_rule(
        expiration=core.Duration.days(1),
    )
    return downloads_bucket
