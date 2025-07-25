#!/bin/bash

# Update PATH
PATH=$PATH:/usr/local/bin
namespace=$(grep -r "namespace" /root/deployment/kustomization.yaml | cut -f2 -d' ')
sleep 60
url=$(kubectl get svc alpinehelloworld-service  --kubeconfig /root/.kube/config -n $namespace -o jsonpath="{.status.loadBalancer.ingress[*].hostname}")
sleep 60
curl http://$url | grep -q "Proven-FR"
