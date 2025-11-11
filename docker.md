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
- docker image ls --filter "reference=renatobrf/python-k8s-initial"
