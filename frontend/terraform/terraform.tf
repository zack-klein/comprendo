
terraform {

  backend "s3" {
    bucket = "zacharyjklein-state"
    key    = "state/comprendo.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region  = "us-east-1"
  version = "~> 2.60"
}