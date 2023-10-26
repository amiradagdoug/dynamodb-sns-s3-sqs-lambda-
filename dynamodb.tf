resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "basic-dynamodb-table"
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "Id"

  attribute {
    name = "Id"
    type = "S"
  }



}


