from app.tools.ec2_tool import get_ec2_instances
from app.tools.s3_tool import get_s3_buckets
from app.tools.iam_tool import get_iam_users
from app.tools.cost_explorer_tool import get_monthly_cost 
from app.tools.cost_explorer_tool import get_daily_cost_trend
from app.orchestrator.ec2_health_orchestrator import (
    ec2_health_orchestrator
)


TOOLS = {
    "ec2_health": {
    "name": "EC2 Health",
    "description": "Analyze EC2 CPU utilization",
    "keywords": [
        "underutilized",
        "cpu",
        "utilization",
        "health"
    ],
    "function": ec2_health_orchestrator.analyze
},

    "ec2": {
        "name": "EC2",
        "description": "Fetch EC2 instance details",
        "keywords": [
            "ec2",
            "instance"
        ],
        "function": get_ec2_instances
    },

    "s3": {
        "name": "S3",
        "description": "Fetch S3 bucket details",
        "keywords": [
            "bucket",
            "s3"
        ],
        "function": get_s3_buckets
    },

    "iam": {
        "name": "IAM",
        "description": "Fetch IAM users",
        "keywords": [
            "iam",
            "user"
        ],
        "function": get_iam_users
    },

    "cost": {
    "name": "Cost Explorer",
    "description": "Fetch AWS monthly cost",
    "keywords": [
        "cost",
        "spend",
        "billing",
        "price"
    ],
    "function": get_daily_cost_trend
}


}