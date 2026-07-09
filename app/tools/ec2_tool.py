from app.services.aws_service import aws_service
from app.core.logger import logger


def get_ec2_instances():
    """Fetch all EC2 instances with their details"""

    logger.info("Fetching EC2 instances from AWS")

    try:
        ec2 = aws_service.ec2

        response = ec2.describe_instances()

        instances = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append({
                    "instance_id": instance["InstanceId"],
                    "instance_type": instance["InstanceType"],
                    "state": instance["State"]["Name"],
                    "launch_time": str(instance["LaunchTime"]),
                    "public_ip": instance.get("PublicIpAddress", "N/A"),
                    "private_ip": instance.get("PrivateIpAddress", "N/A"),
                    "tags": instance.get("Tags", [])
                })

        logger.info(f"Retrieved {len(instances)} EC2 instances")

        return instances

    except Exception:
        logger.exception("Failed to fetch EC2 instances")
        raise


def get_running_instances():
    """Return only running EC2 instances"""

    logger.info("Filtering running EC2 instances")

    all_instances = get_ec2_instances()

    running_instances = [
        instance
        for instance in all_instances
        if instance["state"] == "running"
    ]

    logger.info(f"Found {len(running_instances)} running EC2 instances")

    return running_instances


def get_stopped_instances():
    """Return only stopped EC2 instances"""

    logger.info("Filtering stopped EC2 instances")

    all_instances = get_ec2_instances()

    stopped_instances = [
        instance
        for instance in all_instances
        if instance["state"] == "stopped"
    ]

    logger.info(f"Found {len(stopped_instances)} stopped EC2 instances")

    return stopped_instances


def get_instance_count():
    """Return count of EC2 instances grouped by state"""

    logger.info("Calculating EC2 instance counts")

    all_instances = get_ec2_instances()

    counts = {}

    for instance in all_instances:
        state = instance["state"]
        counts[state] = counts.get(state, 0) + 1

    logger.info(f"Instance counts: {counts}")

    return counts