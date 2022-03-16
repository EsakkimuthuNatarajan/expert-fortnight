from aws_cdk import (
    core as cdk,
    aws_ec2 as _ec2
)


class TestVpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc_configs =  self.node.try_get_context('vpc_configs')

        self.vpc = _ec2.Vpc(self,
            "CustomVpc",
            cidr= vpc_configs['vpc_cidr'],
            max_azs= 2,
            nat_gateways= 1,
            subnet_configuration= [
                _ec2.SubnetConfiguration(
                    name = "PublicSubnet",
                    cidr_mask= vpc_configs['cidr_mask'],
                    subnet_type= _ec2.SubnetType.PUBLIC
                ),
                _ec2.SubnetConfiguration(
                    name = "PrivateSubnet",
                    cidr_mask= vpc_configs['cidr_mask'],
                    subnet_type= _ec2.SubnetType.PRIVATE
                ),
                _ec2.SubnetConfiguration(
                    name = "DBSubnet",
                    cidr_mask= vpc_configs['cidr_mask'],
                    subnet_type= _ec2.SubnetType.ISOLATED
                )
            ]
            )

        tag = cdk.Tags.of(self.vpc).add("Note", "Please Delete After Using")

        Output = cdk.CfnOutput(self,
        "CustomVpcId",
        value= self.vpc.vpc_id,
        export_name= "CustomTestVpc"
        )
        
        
        
        
        