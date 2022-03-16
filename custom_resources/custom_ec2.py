from aws_cdk import (
    core as cdk,
    aws_ec2 as _ec2
)


class WebserverStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        try:
            with open("bootstrap_scripts\https.sh", mode = "r") as file:
                user_data = file.read()
        except OSError:
            print("Unable to find the user data file")

        # vpc = _ec2.Vpc.from_lookup(self, "ImportedVPC", vpc_id= "vpc-6c654b14")

        server = _ec2.Instance(self,
        "webserver",
        instance_type = _ec2.InstanceType(instance_type_identifier="t2.micro"),
        instance_name = "TestInstance",
        machine_image= _ec2.MachineImage.generic_linux({"us-west-2": "ami-0359b3157f016ae46"}),
        vpc= vpc,
        vpc_subnets=_ec2.SubnetSelection(subnet_type=_ec2.SubnetType.PUBLIC),
        key_name = "chrisgrey",
        user_data= _ec2.UserData.custom(user_data)  
        )

        server.connections.allow_to_any_ipv4(
            _ec2.Port.tcp(80), description= "Allow web traffic in 80"
        )

        Output = cdk.CfnOutput(self,
        "WebserverPublicIp",
        description= "Webserver IP Address",
        value= f"http://{server.instance_public_ip}"
        )
