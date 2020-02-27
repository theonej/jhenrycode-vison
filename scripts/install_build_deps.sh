apt-get clean
apt-get update
apt-get install python-pip -y
pip install awscli
apt-get install jq sudo unzip git curl wget -y

sudo apt-get install software-properties-common -y
sudo apt-get update
     
apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
apt update
apt-cache policy docker-ce
apt install docker-ce -y