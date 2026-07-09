from app.services.bedrock_service import bedrock_service

sample_data = {
    "users": [
        "carprice",
        "infrabot-user"
    ]
}

response = bedrock_service.generate_response(
    "Show IAM users",
    sample_data
)

print(response)