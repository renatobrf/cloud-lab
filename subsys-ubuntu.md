# main steps
- install docker
- sudo apt install docker.io
- docker --version
- systemctl status docker
- whoami
- sudo usermod -aG docker renato

# start the daemon
- sudo systemctl start docker
- docker pull renatobrf/python-k8s-initial:0.1
- sudo apt install wsl
- sudo systemctl status
- sudo -e /etc/wsl.conf

# persistent volume
- kubectl apply -f pv.yaml
