
# Metrics Generator Service

Metrics-enerator service is a service wrriten with Python which listen to HTTP requests and expose metrics about them


## Build

To build new service's image run:

* Make sure you logged in to ishais123 docker hub registry, Use 'docker login' command.
```bash
bash scripts/build.sh <app-version>
```
    
## Deployment

To deploy this service run 

```bash
bash scripts/deploy.sh <app-version>
```


## Monitoring Setup

Deploy kube-prometheus-stuck helm chart 

```bash
 helm upgrade -install kube-prometheus-stack \
  prometheus-community/kube-prometheus-stack \
  --set kubeStateMetrics.enabled=false \
  --set alertmanager.enabled=false \
  --set nodeExporter.enabled=false \
  --create-namespace \
  -nmonitoring
```
* If you want to expose grafana outside the cluster, consider to set grafana service type to LoadBalancer or use ingress (make sure you configured all related external LoadBalancer configuration base on your cloud provider)
Expose Grafana UI locally

```bash
 kubectl port-forward svc/kube-prometheus-stack-grafana <your-local-port>:80 -nprometheus
```

Get Grafana UI credentials

```bash
  kubectl get secret \
  kube-prometheus-stack-grafana  \
  -nmonitoring \
  -o jsonpath="{.data.admin-user}" | base64 -d

  kubectl get secret \
  kube-prometheus-stack-grafana \
  -nmonitoring \
  -o jsonpath="{.data.admin-password}" | base64 -d
```
