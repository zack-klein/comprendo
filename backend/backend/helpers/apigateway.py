from aws_cdk import aws_apigateway


def create_post_api(cls, name, lambda_function):
    api = aws_apigateway.RestApi(
        cls,
        id=f"{name}-post-api",
        rest_api_name=name,
    )
    entity = api.root.add_resource(name)
    lambda_integration = aws_apigateway.LambdaIntegration(
        lambda_function,
        proxy=False,
        integration_responses=[
            {
                "statusCode": "200",
                "responseParameters": {
                    "method.response.header.Access-Control-Allow-Origin": "'*'",  # noqa:E501
                },
            }
        ],
    )
    entity.add_method(
        "POST",
        lambda_integration,
        method_responses=[
            {
                "statusCode": "200",
                "responseParameters": {
                    "method.response.header.Access-Control-Allow-Origin": True,  # noqa:E501
                },
            }
        ],
    )
    # Add CORS
    entity.add_method(
        "OPTIONS",
        aws_apigateway.MockIntegration(
            integration_responses=[
                {
                    "statusCode": "200",
                    "responseParameters": {
                        "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",  # noqa:E501
                        "method.response.header.Access-Control-Allow-Origin": "'*'",  # noqa:E501
                        "method.response.header.Access-Control-Allow-Methods": "'GET,OPTIONS'",  # noqa:E501
                    },
                }
            ],
            passthrough_behavior=aws_apigateway.PassthroughBehavior.WHEN_NO_MATCH,  # noqa:E501
            request_templates={"application/json": '{"statusCode":200}'},
        ),
        method_responses=[
            {
                "statusCode": "200",
                "responseParameters": {
                    "method.response.header.Access-Control-Allow-Headers": True,  # noqa:E501
                    "method.response.header.Access-Control-Allow-Methods": True,  # noqa:E501
                    "method.response.header.Access-Control-Allow-Origin": True,  # noqa:E501
                },
            }
        ],
    )
