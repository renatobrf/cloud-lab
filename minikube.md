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
- minikube start --force
- minikube ssh
- minikube status
- minikube addons list
- minikube addons enable [addon_name]
- minikube stop
- minikube delete
- minikube dashboard
- minikube dashboard --url
- http://127.0.0.1:40461/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/workloads?namespace=default

# dashboard (not mandatory)
- https://minikube.sigs.k8s.io/docs/handbook/dashboard/
- https://github.com/kubernetes/dashboard
- Add kubernetes-dashboard repository
- helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
- helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
