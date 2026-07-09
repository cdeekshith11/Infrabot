from datetime import datetime

from app.services.aws_service import aws_service
from app.core.logger import logger


def get_monthly_cost():
    """
    Fetch total AWS cost for the current month.
    """

    logger.info("Fetching AWS monthly cost")

    try:

        today = datetime.utcnow().date()

        start_date = today.replace(day=1)

        end_date = today

        ce = aws_service.ce

        response = ce.get_cost_and_usage(

            TimePeriod={
                "Start": str(start_date),
                "End": str(end_date)
            },

            Granularity="MONTHLY",

            Metrics=[
                "UnblendedCost"
            ]
        )
        print(response)
        amount = response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]

        unit = response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Unit"]

        logger.info(f"Current month AWS cost: {amount} {unit}")

        return {
            "amount": amount,
            "unit": unit,
            "start_date": str(start_date),
            "end_date": str(end_date)
        }

    except Exception:

        logger.exception("Failed to fetch AWS monthly cost")

        raise


def get_cost_by_service():
    """
    Fetch AWS cost by service.
    """

    logger.info("Fetching AWS cost by service")

    try:

        ce = aws_service.ce

        response = ce.get_cost_and_usage()

        cost_by_service = {}

        for group in response["Groups"]:

            service = group["Keys"][0]["Value"]

            cost = group["Metrics"]["UnblendedCost"]["Amount"]

            cost_by_service[service] = cost

        logger.info(f"Cost by service: {cost_by_service}")

        return cost_by_service

    except Exception:

        logger.exception("Failed to fetch AWS cost by service")

        raise