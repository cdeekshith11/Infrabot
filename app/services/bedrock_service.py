import json

from app.services.aws_service import aws_service


class BedrockService:

    def __init__(self):
        self.client = aws_service.bedrock

    def generate_response(self, question, aws_data):

        prompt = f"""
You are InfraBot, an AI CloudOps Assistant.

User Question:
{question}

AWS Data:
{json.dumps(aws_data, indent=2)}

Provide a clear and concise answer.
"""

        response = self.client.invoke_model(
            modelId="amazon.nova-lite-v1:0",
            body=json.dumps({
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            })
        )

        result = json.loads(
            response["body"].read()
        )

        answer = result["output"]["message"]["content"][0]["text"]

        return answer


bedrock_service = BedrockService()