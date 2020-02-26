cd ~/code/jhenrycode-vision/data/validation/plant_maturity/juvenile
curl -i -X POST -H 'Content-Type:multipart/form-data' -F 'image-data=@000002.png' http://0.0.0.0:9001/prediction/plant_maturity