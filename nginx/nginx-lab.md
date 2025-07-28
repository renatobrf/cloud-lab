# main
gemini: nginx deployment kube
- kubectl get svc
- 10.102.46.77:8080

## reference
https://medium.com/@muppedaanvesh/deploying-nginx-on-kubernetes-a-quick-guide-04d533414967
- kubectl expose pod nginx-pod --type=NodePort --port=80 --name=nginx-service
- kubectl get svc
- minikube service nginx-service --url
