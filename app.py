#!/usr/bin/env python3
import os
from aws_cdk import core as cdk

from custom_resources.custom_ec2 import WebserverStack
# from expert_fortnight.expert_fortnight_stack import ExpertFortnightStack
# env = cdk.Environment( region= "us-east-1", account= "275239396717")

app = cdk.App()
ec2_Stack = WebserverStack(app, "WebServer-Stack", env=cdk.Environment(account='275239396717', region='us-west-2'))

app.synth()
