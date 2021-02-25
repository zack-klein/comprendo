from aws_cdk import (
    core,
    aws_lambda,
)


def create_lambda(
    cls,
    name,
    image,
    env=None,
    description=None,
    memory=128,
    concurrency=10,
    duration_sec=10,
    destroy=True
):
    return aws_lambda.Function(
        cls,
        id=f"{name}-lambda-function",
        description=description,
        code=image,
        handler=aws_lambda.Handler.FROM_IMAGE,
        runtime=aws_lambda.Runtime.FROM_IMAGE,
        environment=env or {},
        function_name=name,
        memory_size=memory,
        reserved_concurrent_executions=concurrency,
        timeout=core.Duration.seconds(duration_sec),
    )
