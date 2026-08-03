import json

from app.services.aws_service import aws_service


class BedrockService:

    def __init__(self):
        self.client = aws_service.bedrock

    def generate_response(self, question, aws_data):

        prompt = f"""

User Question:
{question}

AWS Data:
{json.dumps(aws_data, indent=2)}

"""

        response = self.client.converse(
            modelId="amazon.nova-lite-v1:0",

            system=[
                {
                    "text":"You are InfraBot, an AI CloudOps Assistant. Answer clearly and concisely."
                }
            ],

            messages=[{
                "role":"user",
                "content":[
                    {
                        "text":prompt
                    }
                ]
            }]
            
        )


        answer = response["output"]["message"]["content"][0]["text"]

        return answer


bedrock_service = BedrockService()