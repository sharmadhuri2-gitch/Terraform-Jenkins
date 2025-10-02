provider "aws" {
region "us-east-1"
}
resource "aws instance" "foo" {
ami = "ami-0e3c2921641a4a215" # us-east-1
instance_type="t2.micro"
tags = {
  Name = "TF-Instance"
}
}
