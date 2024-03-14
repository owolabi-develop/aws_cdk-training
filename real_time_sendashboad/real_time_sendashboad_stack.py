from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
    
)
from . hitcounter import HitCounter
from cdk_dynamo_table_view import TableViewer


class RealTimeSendashboadStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        my_lambda = _lambda.Function(self,"helloHandler",
                                     runtime=_lambda.Runtime.PYTHON_3_12,
                                     code=_lambda.Code.from_asset('lambda'),
                                     handler='hello.handler',
                                     )
        hello_with_count = HitCounter(
            self,"helloCounter",
            downstream=my_lambda,
        )
        
        apigw.LambdaRestApi(
            self,"Endpoint",
            handler = hello_with_count.handler,
        )
        
        TableViewer(
            self,
            'ViewHitCounter',
            title='Hello Hits',
            table=hello_with_count.table
        )
        

       
