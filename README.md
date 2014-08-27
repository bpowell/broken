Build docker image:
sudo docker build -t broken . 

Run docker image:
 sudo docker run -name broken_instance -p 5000:5000 -i -t broken
