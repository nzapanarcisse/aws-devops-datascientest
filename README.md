# Projet devops aws

## Contexte
Geniou-Tech souhaite moderniser son infrastructure en migrant vers le cloud afin de réduire ses coûts et de tirer parti des nombreux avantages offerts par les services cloud. Pour ce faire, l'entreprise recherche un ingénieur DevOps spécialisé en AWS.

## Objectif
La mission principale consiste à provisionner un cluster Kubernetes sur AWS, qui hébergera l'ensemble des applications de l'entreprise. Ce cluster sera accessible via une machine EC2, désignée comme bastion (bastion-eks), permettant ainsi la communication avec le cluster.

## Tâches Principales

1. **Provisionnement du Cluster Kubernetes :**
   - Configurer un cluster Kubernetes sur AWS pour abriter toutes les applications de Geniou-Tech.

2. **Configuration de l'Accès :**
   - Déployer une instance EC2 (bastion-eks) pour faciliter l'accès sécurisé au cluster Kubernetes.

3. **Mise en Place d'un Pipeline CI/CD :**
   - **Utilisation de CodeBuild :** Créer un pipeline qui compile les applications et construit les images Docker.
   - **Création d'un Registre Privé :** Mettre en place un registre privé pour stocker les images Docker.
   - **Intégration de CodeDeploy :** Déployer les applications sur le cluster Kubernetes à partir du registre privé.
   - **Automatisation avec CodePipeline :** Configurer CodePipeline pour automatiser les étapes de build et de déploiement.

## Résultats Attendus
- Un cluster Kubernetes opérationnel sur AWS, accessible via une machine bastion.
- Un pipeline CI/CD fonctionnel, permettant une intégration continue et un déploiement automatisé des applications.
- Une infrastructure optimisée qui réduit les coûts d'exploitation tout en améliorant la flexibilité et l'évolutivité des applications.

# SOLUTION

## 1. Provisionnement du Cluster Kubernetes et de l'instance Bastion-eks
Pour créer l'infrastructure, nous allons lancer une instance EC2. À partir de cette instance, nous exécuterons un script CloudFormation pour provisionner le cluster. Le script CloudFormation est disponible [ici](https://raw.githubusercontent.com/nzapanarcisse/cursus-devops-stack/refs/heads/master/stack/eks-cloudformation.yaml).

### Provisionnement de l'instance Bastion-eks
1. **Lancement de l'instance :**  
   Démarrer une instance EC2 qui servira de point d’accès (bastion) pour gérer le cluster Kubernetes.
   
![image](https://github.com/user-attachments/assets/0f93b074-8dca-482c-99fe-17f77ee52a37)
![image](https://github.com/user-attachments/assets/de5a341b-cef7-42e3-a8b5-a381d15d069a)
![image](https://github.com/user-attachments/assets/3de64602-12e5-47bc-8f79-31d19fa5104c)
![image](https://github.com/user-attachments/assets/eac39e57-40c2-4b0c-80b8-7042d09593c0)
![image](https://github.com/user-attachments/assets/5961ef24-f658-4f7f-afa8-6efd74ba99fc)



Configurer un groupe de sécurité pour contrôler l'accès à l'instance bastion, en autorisant uniquement le trafic nécessaire (par exemple, SSH).

![image](https://github.com/user-attachments/assets/ed445044-2cb1-4289-8d0e-a00a7b964dc0)
![image](https://github.com/user-attachments/assets/381646dd-69d1-43b9-830b-b68a1443ed54)


4. **Création d'un rôle IAM :**
   Créer un rôle IAM qui permettra à l'instance bastion d'accéder aux ressources AWS, notamment pour interagir avec le cluster Kubernetes. rechercher le service IAM et Roles
   
   ![image](https://github.com/user-attachments/assets/2c596423-a231-4ec7-972f-14fef9f0337c)
![image](https://github.com/user-attachments/assets/675de433-1cb6-4851-b197-7fc38da5af11)
![image](https://github.com/user-attachments/assets/afbc6453-e3c1-478c-a4a5-87dfbeb32ea1)
![image](https://github.com/user-attachments/assets/7a6c80af-de49-458a-a6fa-b1f089c66fb6)
![image](https://github.com/user-attachments/assets/fe04c697-9d06-4971-aa07-735fca7abaa4)
![image](https://github.com/user-attachments/assets/0c4ba6e9-c7c8-4b7c-a214-e9ddafc67655)
![image](https://github.com/user-attachments/assets/8c319658-a8b3-4631-bcc0-964f26f975d8)
![image](https://github.com/user-attachments/assets/3d31e021-9991-4967-8c7f-9b52a2ff79bd)
![image](https://github.com/user-attachments/assets/5fc8bfc8-319a-4aa5-a331-fa3942eace9b)

rechercher le role et modifier pour ajouter 
{
	"Statement": [
		{
			"Action": "*",
			"Resource": "*",
			"Effect": "Allow"
		}
	]
}


Maintenant, nous allons attacher notre rôle créé à l'instance bastion. Pour cela, depuis le menu des services EC2, recherchez l'instance bastion, puis allez dans Actions et sélectionnez sécurité, modifier le role IAM.

![image](https://github.com/user-attachments/assets/90080385-b1dd-475d-9674-5632d450aa97)
![image](https://github.com/user-attachments/assets/661a3cb9-3c24-4543-b575-aca6d856cf76)




6. **Connexion au bastion et installation des outils :**  
   Se connecter à l'instance bastion via SSH et installer les outils nécessaires, tels que AWS CLI et kubectl, puis lancer le script CloudFormation.
Depuis le service EC2, sélectionnez l'instance bastion, utilisez EC2 Instance Connect pour établir la connexion.

   ![image](https://github.com/user-attachments/assets/48e5bb69-df5e-4987-a3bb-0e47549e2819)
   
![image](https://github.com/user-attachments/assets/d96a0a9a-9f18-4282-9ac9-ba591e08664c)



### Provisionnement du Cluster

Utiliser le script CloudFormation pour provisionner le cluster Kubernetes sur AWS. Ce processus inclut la création de la VPC, des sous-réseaux, des groupes de sécurité, et du rôle IAM pour l'EKS.

***Install aws cli**

Cette commande télécharge le package d'installation d'AWS CLI, l'extrait et l'installe sur l'instance.

```bash
          curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
          yum install -y unzip
          unzip awscliv2.zip
          ./aws/install
```
***Install aws-iam-authenticator** 

Cette commande télécharge l'authentificateur IAM pour EKS, lui donne les permissions d'exécution et le déplace vers /usr/bin pour un accès global.

```bash
curl -o aws-iam-authenticator https://amazon-eks.s3.us-west-2.amazonaws.com/1.18.9/2020-11-02/bin/linux/amd64/aws-iam-authenticator
chmod +x aws-iam-authenticator
mv aws-iam-authenticator /usr/bin/
```
***Install kubectl**  
```bash
curl -LO "https://dl.k8s.io/release/v1.29.7/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin
``` 
***Install kubectl auto-completion***

Ces commandes installent le support de l'auto-complétion pour kubectl, améliorant ainsi l'expérience de ligne de commande.
```bash
yum install -y bash-completion
echo 'source <(kubectl completion bash)' >>~/.bashrc
kubectl completion bash >> /etc/bash_completion.d/kubectl
``` 
***Set aws-cli region***

Cette commande crée un répertoire de configuration pour AWS CLI et définit la région par défaut sur us-east-1.
```bash
mkdir ~/.aws
echo -e "[default] \nregion = us-east-1" > ~/.aws/config
```
***Deploy eks stack***

Ces commandes téléchargent le fichier de modèle CloudFormation pour EKS et créent la stack en spécifiant les paramètres requis, notamment les zones de disponibilité et le nom de la clé SSH.

```bash
curl -o eks.yaml https://raw.githubusercontent.com/nzapanarcisse/cursus-devops-stack/refs/heads/master/stack/eks-cloudformation.yaml
aws cloudformation create-stack --stack-name EKS \
           --template-body file://eks.yaml \
           --parameters ParameterKey=AvailabilityZonePublicSubnet01,ParameterValue="us-east-1a" \
           ParameterKey=AvailabilityZonePublicSubnet02,ParameterValue="us-east-1b" \
           ParameterKey=EKSKeyPair,ParameterValue="aws-eks" \
           --capabilities CAPABILITY_NAMED_IAM
```
```bash
aws eks --region us-east-1 update-kubeconfig --name EKS
```
Verification progression script cloudformation
```bash
aws cloudformation describe-stacks --region us-east-1 --stack-name EKS --query "Stacks[*].StackStatus" --output text
```
**sortie**
![image](https://github.com/user-attachments/assets/fa62318a-0503-43ca-9c62-417dcaea8c7b)
après quelque minutes 
![image](https://github.com/user-attachments/assets/b8444a3d-9f3a-46a8-91b0-57ad98e7e4d9)


**découverte du cluster**

Dans le service EKS, nous pouvons observer notre cluster en cours d'exécution. Vous pouvez également voir les nœuds depuis le service EC2 d'AWS. La commande kubectl get nodes exécutée depuis l'instance bastion nous permet également d'afficher les nœuds du cluster.

![image](https://github.com/user-attachments/assets/761af2eb-2d3f-4d34-bc53-b081cbf63b8e)
```bash
kubectl get nodes
```
![image](https://github.com/user-attachments/assets/ef08bde8-20f1-494d-97b6-4af92196f4fd)
depuis le service EC2 

![image](https://github.com/user-attachments/assets/0a163a56-d346-41c8-8b0d-a3cd58b0bce6)

Bravo !!! 🎉

Bravo !!! 🎉
Bravo !!! 🎉 

## 2. CodeBuild
Configurer AWS CodeBuild pour automatiser la construction des images Docker à partir des applications. Cela inclut la définition d'un projet CodeBuild qui récupérera le code source et construira les images.

## 3. CodeDeploy
Mettre en place AWS CodeDeploy pour déployer les applications sur le cluster Kubernetes. Ce service facilitera le déploiement automatique des images Docker sur les nœuds de travail du cluster.

## 4. CodePipeline
Configurer AWS CodePipeline pour orchestrer l'ensemble du flux CI/CD. Cela inclura l'intégration de CodeBuild et CodeDeploy, automatisant ainsi les étapes de construction et de déploiement des applications au sein du cluster Kubernetes.

   
