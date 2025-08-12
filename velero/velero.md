# main
- ref: https://tellesnobrega.github.io/velero-demo/
- https://velero.io/docs/v0.10.0/get-started/

## requirements
- install docker
- install minikube
- install kubectl
 
## run minio
- docker pull minio/minio
- docker run -p 9000:9000 --name minio -e "MINIO_ACCESS_KEY=minio" -e "MINIO_SECRET_KEY=minio123" -v /mnt/data:/data minio/minio server /data

Install velero by wget
- velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.0.0 --bucket backups --secret-file ./aws-iam-creds --backup-location-config region=us-east-2 --snapshot-location-config region=us-east-2 --use-restic

## operation
By default, Velero backs up all resources in all namespaces. If you want to back up only specific namespaces, use the --include-namespaces flag.
- velero backup create renato-minikube-lab1-bkp1
