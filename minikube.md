# minikube install
- ref: https://phoenixnap.com/kb/install-minikube-on-ubuntu
- sudo apt update
- sudo apt install curl apt-transport-https
- curl -O https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
- sudo cp minikube-linux-amd64 /usr/local/bin/minikube
- sudo chmod 755 /usr/local/bin/minikube
- minikube version
- sudo snap install kubectl --classic
- curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
- chmod +x ./kubectl
- sudo mv ./kubectl /usr/local/bin/kubectl

# minikube cmd
- minikube start
- minikube ssh
- minikube status
- minikube addons list
- minikube addons enable [addon_name]
- minikube stop
- minikube delete
- minikube dashboard
- minikube dashboard --url
