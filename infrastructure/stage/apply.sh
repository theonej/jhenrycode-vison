export TF_VAR_tag=$(git rev-parse HEAD)

cd $PWD/infrastructure/stage

terraform init
terraform plan

./push_images_to_stage.sh

terraform apply -auto-approve