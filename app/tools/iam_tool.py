from app.services.aws_service import aws_service
from app.core.logger import logger

def get_iam_users():
    """Fetch all IAM users"""
    logger.info("Fetching IAM users")
        
    try:

        
        iam = aws_service.iam

        response = iam.list_users()
        
        users = []

        
        for user in response["Users"]:
            users.append({
                "user_name": user["UserName"],
                "created": str(user["CreateDate"])
            })

        logger.info(f"Received {len(users)} IAM users")


        return users
    except Exception:
        logger.exception("Failed to fetch IAM users")
        raise


def get_iam_roles():
    """Fetch all IAM roles"""
    logger.info("Fetching IAM roles")
    try:
        iam = aws_service.iam

        response = iam.list_roles()

        roles = []

        for role in response["Roles"]:
            roles.append({
                "role_name": role["RoleName"],
                "created": str(role["CreateDate"])
            })
        logger.info(f"Received {len(response['Roles'])} IAM roles")

        return roles
    except Exception:
        logger.exception("Failed to fetch IAM roles")
        raise