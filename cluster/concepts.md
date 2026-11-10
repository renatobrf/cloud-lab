# Fundamental Kubernetes Concepts
1. Pod - Smallest in Kubernetes, wraps one or more containers with shared network and storage.
2. Node - A worker machine that runs pods and is managed by the Kubernetes control plane.
3. Cluster - A group of nodes working together as a single Kubernetes system.
4. Deployment - Manages the desired state of pods and handles rolling updates.
5. ReplicaSet - Keeps a specific number of identical pods running at all times.
6. Service - Provides stable networking to access a group of pods reliably.
7. Ingress - Manages external HTTP/S access to services using rules and paths.
8. ConfigMap - Stores non sensitive configuration data separately from containers images.
9. Secret - Stores sensitive information like passwords and tokens in a secure way.
10. Namespace - Logical partitoning of cluster resources for isolation and organization.
11. Kubelet - Node agent that makes sure containers described in pods are running.
12. Kubectl - CLI tool to interact with and manage Kubernetes cluster.
13. Control Plane - The set of components that manages the overwall cluster state.
14. Scheduler - Assigns new pods to suitable nodes based on resources needs and policies.
15. Controller Manager - Runs background controllers to maintain cluster state automatically.
16. Etcd - Distributed key value store used to persist all cluster data.
17. Taints & Tolerations - Control wich pods are allowed to run on specific nodes.
18. Labels & Selectors - Used to group and select Kubernetes objects dynamically.
19. Resource Requests & Limits - Define how much CPU and memory a container needs and can use.
20. Helm - Kubernetes package manager for deploying and managing applications.
21. CRD(custom resource definition) - Lets you define your own Kubernetes resource types.
22. Operator - A controller built to automate complex application operations using CRDs.
23. DaemonSet - Runs a pod on every node or specific nodes in the cluster.
24. Logs & Events - Help you debug and track what's happening inside the cluster.
