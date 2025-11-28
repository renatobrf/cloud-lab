# env
$ podman --version
$ podman images
$ podman machine list
$ podman machine init
$ sudo apt install qemu-kvm
$ podman machine start

## lab1
from https://podman.io/docs
$ podman pull docker.io/library/httpd
$ podman images
$ podman run -dt -p 8080:80/tcp docker.io/library/httpd
$ podman ps
$ curl http://localhost:8080
$ podman top -l
$ podman stop -l
