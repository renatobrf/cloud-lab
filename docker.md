# main steps
- install docker
- sudo apt install docker.io
- docker --version
- systemctl status docker
- whoami
- sudo usermod -aG docker renato

## baby steps
- docker images
- docker ps
- docker volume ls

# start the daemon
- sudo systemctl start docker
- sudo apt install wsl
- sudo systemctl status
- sudo -e /etc/wsl.conf

# images mng
- docker pull renatobrf/python-k8s-initial
- docker rmi 36e50cb9ef57
- docker image ls --filter reference=renatobrf/*
- docker image ls --filter reference=gcr.io/k8s-minikube/*

# running
- docker image ls --filter reference=renatobrf/*
- docker run id-img
- docker run -p 8080:8080 id-img
- curl ifconfig.me
