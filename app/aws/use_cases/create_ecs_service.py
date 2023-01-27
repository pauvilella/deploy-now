import boto3


def create_ecs_service(
    service_name,
    cluster_name,
) -> bool:

    client = boto3.client()

    response = client.create_task_set(
        service=service_name,
        cluster=cluster_name,
        externalId="string",
        taskDefinition="string",
        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets": [
                    "string",
                ],
                "securityGroups": [
                    "string",
                ],
                "assignPublicIp": "ENABLED" | "DISABLED",
            }
        },
        loadBalancers=[
            {"targetGroupArn": "string", "loadBalancerName": "string", "containerName": "string", "containerPort": 123},
        ],
        serviceRegistries=[
            {"registryArn": "string", "port": 123, "containerName": "string", "containerPort": 123},
        ],
        launchType="EC2" | "FARGATE" | "EXTERNAL",
        capacityProviderStrategy=[
            {"capacityProvider": "string", "weight": 123, "base": 123},
        ],
        platformVersion="string",
        scale={"value": 123.0, "unit": "PERCENT"},
        clientToken="string",
        tags=[
            {"key": "string", "value": "string"},
        ],
    )
    return True
