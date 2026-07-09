from app.agent.router import agent_router

print(agent_router.route("Show my IAM users"))

print("--------------------------------")

print(agent_router.route("List my S3 buckets"))

print("--------------------------------")

print(agent_router.route("Show EC2 instances"))