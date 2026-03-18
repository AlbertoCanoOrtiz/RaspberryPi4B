# NFS Dynamic Provisioner Deployment Guide

## 1. Create the Namespace

First, create the dedicated nfs namespace to isolate these resources.

```Bash

kubectl apply -f nfs-namespace.yaml
```
## 2. Configure RBAC (Permissions)

The provisioner needs specific permissions to watch for PersistentVolumeClaims and create PersistentVolumes automatically. Apply the ServiceAccount, Roles, and Bindings.

```Bash

kubectl apply -f nfs-serviceaccount.yaml
kubectl apply -f nfs-role.yaml
kubectl apply -f nfs-rolebinding.yaml
kubectl apply -f nfs-clusterrole.yaml
kubectl apply -f nfs-clusterrolebinding.yaml
```
## 3. Deploy the NFS Client Provisioner

This deployment runs the actual pod that communicates with your NFS server at /mnt/nfsShare/. It uses the nfs-client-provisioner ServiceAccount created in the previous step.

```Bash

kubectl apply -f nfs-deployment.yaml
```
## 4. Create the Persistent Volume Claim (PVC)

Now that the provisioner is running, you can request storage. This PVC uses the managed-nfs-storage StorageClass to dynamically carve out 1Gi of space.

```Bash

kubectl apply -f nfs-persistentvolumeclaim.yaml
```
## 5. Verify with a Test Pod

To ensure the NFS mounting is working correctly, deploy the test pod. It will attempt to write a file named SUCCESS to the NFS share and then exit.

```Bash

kubectl apply -f nfs-pod.yaml

Check result: kubectl get pods -n nfs (The nfs-pod should show Completed).

Check logs: kubectl logs nfs-pod -n nfs.
```

## 6. (Optional) Configure External Access

If you are running JupyterHub on this cluster, apply the Ingress rule to route traffic from raspberrypi.jupyterhub.com to your internal proxy service.

```Bash

kubectl apply -f nfs-nginx-ingress-jupyterhub.yaml
```




















kubectl patch svc proxy-public -n nfs -p '{"spec": {"type": "LoadBalancer", "externalIPs":["192.168.1.1"]}}'



helm uninstall jupyterhub.v.1 -n nfs




helm upgrade --install jupyterhub.v.1 jupyterhub/jupyterhub --namespace nfs --version= 1.1