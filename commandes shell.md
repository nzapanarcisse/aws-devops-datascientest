**création du bucket relase du code de deploiement**

    ```bash
    # Création du bucket S3
    aws s3 mb s3://deployment-code-release-eks --region us-east-1

    # Activation du versionning sur le bucket
    aws s3api put-bucket-versioning --bucket deployment-code-release-eks --versioning-configuration Status=Enabled --region us-east-1
    ```

**linstallation codedeploy agent**

```bash
# Mise à jour de la VM Bastion
sudo yum update -y

# Installation de l'agent Code deploy
sudo yum update -y
sudo yum install ruby -y
sudo yum install epel-release -y
sudo yum install ruby -y


sudo yum install ruby-2.0.0.648-39.el7_9  wget-1.14-18.el7_6.1.x86_64 -y
wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent status
```

**création du docker-secret pour ecr**

```bash
kubectl create secret docker-registry alpinehelloworld-ecr --docker-server=688567275492.dkr.ecr.us-east-1.amazonaws.com --docker-username=AWS --docker-password=$(aws ecr get-login-password --region us-east-1)
```
