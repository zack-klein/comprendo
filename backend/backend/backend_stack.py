import os

from dotenv import load_dotenv

from aws_cdk import core, aws_lambda, aws_iam

from backend.helpers.lambdas import create_lambda
from backend.helpers.apigateway import create_post_api

load_dotenv()


class BackendStack(core.Stack):
    def __init__(
        self, scope: core.Construct, construct_id: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        canonical_name = construct_id

        # The code that defines your stack goes here
        ecr_image = aws_lambda.EcrImageCode.from_asset_image(
            directory=os.path.join(os.getcwd(), "backend/lambdas")
        )
        copier_lambda = create_lambda(
            self,
            canonical_name,
            ecr_image,
            env={
                "TWITTER_API_KEY": os.getenv("TWITTER_API_KEY"),
                "TWITTER_API_SECRET_KEY": os.getenv("TWITTER_API_SECRET_KEY"),
            },
            duration_sec=90,
        )
        copier_lambda.add_to_role_policy(
            statement=aws_iam.PolicyStatement(
                actions=["comprehend:*"],
                resources=["*"]
            )
        )

        create_post_api(self, canonical_name, copier_lambda)
