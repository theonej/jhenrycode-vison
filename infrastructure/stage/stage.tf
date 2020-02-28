variable "tag" {}

data "terraform_remote_state" "jhenrycode-vision" {
    backend = "s3"
    config = {
        region = "us-east-1"
        bucket = "jhenrycode-vision"
        key = "stage_inf.tfstate"
    }
}

provider "aws" {
    shared_credentials_file = "$HOME/.aws/credentials"
    profile = "default"
    region = "us-east-1"
}

terraform {
    backend "s3" {
        bucket = "jhenrycode-vision"
        key = "stage_service_inf.tfstate"
        region = "us-east-1"
    }
}

module "vision-predictions" {
    source = "git@github.com:theonej/jhenrycode-infrastructure.git//module/ecs"

    security_group_id = data.terraform_remote_state.jhenrycode-vision.outputs.security_group_id
    subnet_ids = data.terraform_remote_state.jhenrycode-vision.outputs.subnet_ids
    target_group_arn = data.terraform_remote_state.jhenrycode-vision.outputs.target_group_arn
    ecs_cluster_id = data.terraform_remote_state.jhenrycode-vision.outputs.ecs_cluster_id
    
    tag = "${var.tag}"
}