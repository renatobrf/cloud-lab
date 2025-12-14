# def
K3s é uma distribuição Kubernetes leve, certificada pela CNCF, criada pela Rancher, focada em ambientes com recursos limitados, como IoT (Internet das Coisas), Edge Computing e desenvolvimento local, sendo compilada em um único binário pequeno (<100MB) e rodando com poucos recursos (512MB RAM, 1 CPU), mantendo as funcionalidades principais do Kubernetes.

## k3s Vs minikube
Minikube is great for learning and local dev, running a single-node cluster in a VM/container with rich addons but higher resource use; k3s is a lightweight CNCF-certified distribution for edge/IoT/dev, offering a lean, fast single-binary install, built-in features (Traefik, Flannel), and easy multi-node setup via tools like k3d, making it more production-ready and efficient for resource-constrained environments.

## setup
prompt: k3s quick install - single node.
https://docs.k3s.io/quick-start
