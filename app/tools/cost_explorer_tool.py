from datetime import datetime
from pprint import pprint
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
       
        pprint(response)

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

        today= datetime.utcnow().date()

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
            ],

            GroupBy=[
                {
                    "Type": "DIMENSION",
                    "Key": "SERVICE"
                }
            ]
        )

        pprint(response)

        services = []

        groups=response["ResultsByTime"][0]["Groups"]

        for group in groups:

            service = group["Keys"][0]

            cost = group["Metrics"]["UnblendedCost"]["Amount"]

            unit = group["Metrics"]["UnblendedCost"]["Unit"]

            services.append({
                "service": service,
                "amount": cost,
                "unit": unit
            }
            )

        logger.info(f"Cost by service: {services}")

        return services 

    except Exception:

        logger.exception("Failed to fetch AWS cost by service")

        raise



def get_last_month_cost():
 
    """
    Fetch total AWS cost for the last month.
    """

    logger.info("Fetching AWS last month cost")

    try:

        today = datetime.utcnow().date()

        first_day_of_current_month = today.replace(day=1)

        last_day_of_last_month = first_day_of_current_month - timedelta(days=1)

        start_date = last_day_of_last_month.replace(day=1)

        end_date = last_day_of_last_month

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

        pprint(response)

        amount = response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]

        unit = response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Unit"]

        logger.info(f"Last month AWS cost: {amount} {unit}")

        return {
            "amount": amount,
            "unit": unit,
            "start_date": str(start_date),
            "end_date": str(end_date)
        }

    except Exception:

        logger.exception("Failed to fetch AWS last month cost")

        raise


def get_daily_cost_trend():

    """
    Fetch AWS daily cost trend.
    """

    logger.info("Fetching AWS daily cost trend")

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

            Granularity="DAILY",

            Metrics=[
                "UnblendedCost"
            ]
        )

        daily_costs=[]

        for day in response["ResultsByTime"]:
         date=day["TimePeriod"]["Start"]
         amount=day["Total"]["UnblendedCost"]["Amount"]
         unit=day["Total"]["UnblendedCost"]["Unit"]
            
         daily_costs.append({
                    "date":date,
                    "amount":amount,
                    "unit":unit
         })
        

        return daily_costs

    except Exception:

        logger.exception("Failed to fetch AWS daily cost trend")

        raise