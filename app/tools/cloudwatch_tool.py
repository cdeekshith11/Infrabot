from datetime import datetime , timedelta, UTC

from app.services.aws_service import aws_service
from app.core.logger import logger


def get_cpu_utilization(instance_id):
    """
    Get average CPU utilization for an EC2 instance
    """

    logger.info(
    f"Fetching CPU utilization for instance {instance_id}")  

    try:
        end_time = datetime.now(UTC)

        start_time = end_time - timedelta(days=1)


        cloudwatch = aws_service.cloudwatch

        response = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName = "CPUUtilization",
        Dimensions =[
            {
                "Name": "InstanceId",
                    "Value":instance_id
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=["Average"]
        )

        datapoints=response["Datapoints"]
        

        if not datapoints:
            logger.warning(f"No CPU metrics found for instance {instance_id}")

            return None

        logger.info(
        f"Retrieved {len(datapoints)} CPU datapoints"
        )

        return datapoints
    
    except Exception:
        logger.exception(
        f"Failed to fetch CPU utilization for instance {instance_id}"
        )
        raise
        
         
       
    