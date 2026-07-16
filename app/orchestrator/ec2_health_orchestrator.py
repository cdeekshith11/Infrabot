from app.tools.ec2_tool import get_ec2_instances
from app.tools.cloudwatch_tool import get_cpu_utilization
from app.core.logger import logger

class EC2HealthOrchestrator:

    def analyze(self):

        instances = get_ec2_instances()

        health_report = []
        if not instances:
            logger.warning("No EC2 instances found")
            return {
                "status": "no_instances",
                "message": "No EC2 instances found in your AWS account."
            }

        for instance in instances:

            metrics = get_cpu_utilization(
                instance["instance_id"]
            )

            average_cpu = None

            if metrics:

                average_cpu = metrics[-1]["Average"]

            health_report.append({

                "instance_id": instance["instance_id"],

                "instance_type": instance["instance_type"],

                "state": instance["state"],

                "cpu_average": average_cpu
            })

        return health_report


ec2_health_orchestrator = EC2HealthOrchestrator()