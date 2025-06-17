# creating env
- install visual studio code
- extension for copilot on vscode

# github-cli
- sudo apt install gh

# github desktop
- ref: https://linux.how2shout.com/install-github-desktop-app-on-ubuntu-22-04-or-20-04-linux/
- sudo apt update && sudo apt upgrade
- wget -qO - https://mirror.mwt.me/shiftkey-desktop/gpgkey | gpg --dearmor | sudo tee /etc/apt/keyrings/mwt-desktop.gpg > /dev/null
- sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/mwt-desktop.gpg] https://mirror.mwt.me/shiftkey-desktop/deb/ any main" > /etc/apt/sources.list.d/mwt-desktop.list'
- sudo apt update
- sudo apt install github-desktop

# docker repo setup
- ref: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
- create file install_docker.sh
- ls -al install_docker.sh
- chmod +x install_docker.sh
- ./install_docker.sh
- sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
- sudo docker run hello-world

# docker desktop
- ref: https://docs.docker.com/desktop/setup/install/linux/ubuntu/
- download manual de install file, go to downloads folder and execute,
- sudo apt-get update
- sudo apt-get install ./docker-desktop-amd64.deb

# credential mng
- ref: https://docs.docker.com/reference/cli/docker/logout/
- docker login -u renatobrf
- ref: https://docs.docker.com/desktop/setup/sign-in/#credentials-management-for-linux-users
- app password on gnome

# mkdocs dependecy
- sudo apt install mkdocs
- https://www.mkdocs.org/user-guide/choosing-your-theme/
- https://www.mkdocs.org/getting-started/#creating-a-new-project

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
