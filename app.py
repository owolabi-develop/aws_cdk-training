#!/usr/bin/env python3

import aws_cdk as cdk

from real_time_sendashboad.real_time_sendashboad_stack import RealTimeSendashboadStack


app = cdk.App()
RealTimeSendashboadStack(app, "RealTimeSendashboadStack")

app.synth()
