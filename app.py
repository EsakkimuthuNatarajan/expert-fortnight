#!/usr/bin/env python3
import os
from aws_cdk import core as cdk

from custom_resources.custom_ec2 import WebserverStack
from custom_resources.custom_vpc import TestVpcStack
# from expert_fortnight.expert_fortnight_stack import ExpertFortnightStack
# env = cdk.Environment( region= "us-west-2", account= "275239396717")

app = cdk.App()
vpc_Stack = TestVpcStack(app, "Vpc-Stack", env=cdk.Environment(account='275239396717', region='us-west-2'))
ec2_Stack = WebserverStack(app, "WebServer-Stack", env=cdk.Environment(account='275239396717', region='us-west-2'))

app.synth()
