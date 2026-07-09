from app.services.aws_service import aws_service
from app.core.logger import logger

def get_s3_buckets():
    """Fetch all S3 buckets"""
    logger.info("Fetching S3 buckets")
    try:
        s3 = aws_service.s3

        response = s3.list_buckets()

        buckets = []

        for bucket in response["Buckets"]:
            buckets.append({
                "name": bucket["Name"],
                "created": str(bucket["CreationDate"])
            })
        logger.info(f"Received {len(buckets)} S3 buckets")

        return buckets
    except Exception:
        logger.exception("Failed to fetch S3 buckets")
        raise


def get_bucket_count():
    """Return total bucket count"""

    buckets = get_s3_buckets()

    return len(buckets)