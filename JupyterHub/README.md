## JupyterHub on Kubernetes (K8s) Deployment

This repository contains the configuration files and Docker specifications required to deploy a customized, multi-user JupyterHub instance on a Kubernetes cluster.

## Architecture Overview

The deployment uses a hub-and-spoke model where the Hub manages user authentication and spawns individual Single-User Notebook pods within a dedicated namespace.

Custom Hub Image: Based on the official JupyterHub repository, modified to include specific dependencies (e.g., gcsfuse or cloud-specific drivers).

Role-Based Access Control (RBAC): Configured via YAML to allow the Hub to manage pods and services within the cluster.

Persistence: Uses PersistentVolumeClaims (PVCs) to ensure user data survives pod restarts.

## File Structure & Component Descriptions

File	Description
Docker	Contains the Dockerfile for the custom JupyterHub image. Cloned from the official source to add custom system-level packages.
config.yaml	The primary configuration file for Helm or the Hub process, defining authentication, resource limits, and image tags.
jupyterhub-namespace.yaml	Defines the isolated logical boundary in the cluster where all JupyterHub resources reside.
jupyterhub-role.yaml	Specifies the permissions (get, list, watch, create) required for the Hub to manage user pods.
jupyterhub-rolebinding.yaml	Links the defined Roles to the JupyterHub ServiceAccount.

## Deployment Instructions

### 1. Prepare the Namespace

```Bash

kubectl apply -f jupyterhub-namespace.yaml
```

### 2. Configure Permissions

Apply the RBAC settings to ensure the Hub can communicate with the Kubernetes API:

```Bash

kubectl apply -f jupyterhub-role.yaml
kubectl apply -f jupyterhub-rolebinding.yaml
```

### 3. Build the Custom Image

If you have modified the Docker directory, build and push your image to your preferred registry (GCR, DockerHub, or ECR)

```Bash

docker build -t your-registry/custom-jupyterhub:latest ./Docker
docker push your-registry/custom-jupyterhub:latest
```

### 4. Launch the Hub

Ensure your config.yaml points to the correct custom image and apply your deployment (typically via Helm or a standard Deployment manifest).

## Troubleshooting

Pending Pods / PVC Issues:

If you encounter the error pod has unbound immediate PersistentVolumeClaims, ensure that:

A StorageClass is defined and available in your cluster.

The PV provisioner has enough quota to create the requested volumes.

The PVC size requested in config.yaml matches the capabilities of your cloud provider.