docker build -t 319304591743.dkr.ecr.us-east-1.amazonaws.com/vision-predictions:${TF_VAR_tag} ../../.

eval $(aws ecr get-login --no-include-email --region us-east-1 | sed 's|https://||')

docker push 319304591743.dkr.ecr.us-east-1.amazonaws.com/vision-predictions:${TF_VAR_tag}