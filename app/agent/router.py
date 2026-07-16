from app.agent.tool_registry import TOOLS

from app.services.bedrock_service import bedrock_service
from app.core.logger import logger


class AgentRouter:

    def route(self, question):

        logger.info(f"Received question: {question}")

        question_lower = question.lower()

        context = {}

        # Execute matching tools
        for tool_name, tool in TOOLS.items():

            if any(
                keyword in question_lower
                for keyword in tool["keywords"]
            ):

                logger.info(f"{tool['name']} Tool selected")

                context[tool_name] = tool["function"]()

        if not context:
            return "Sorry, I don't know how to answer that yet."
        

        # Check if any tool returned "no instances"
        for result in context.values():
          
           if (
              isinstance(result, dict)
                and result.get("status") == "no_instances"
                          ):

             logger.warning("Skipping Bedrock")

             return result["message"]

        logger.info("Sending context to Bedrock")

        answer = bedrock_service.generate_response(
            question,
            context
        )

        logger.info("Received response from Bedrock")

        return answer


agent_router = AgentRouter()