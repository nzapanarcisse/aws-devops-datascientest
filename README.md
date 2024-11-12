# Projet de Migration Cloud pour Geniou-Tech

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

  # PROPOSITION SOLUTION
## 1. Provisionnement du Cluster Kubernetes et l'instance Bastion-eks
pour créer l'infrastructure nous allant lancer une instance ec2 et à partir de cette instance nous allons lancer un scripts cloudformation pour provisionner le cluster( le scripte cloud for est disponible dans le lien:https://raw.githubusercontent.com/nzapanarcisse/cursus-devops-stack/refs/heads/master/stack/eks-cloudformation.yaml
   ### provisionnement de instance Bastion-eks
   1. **lancement de l'instance**
   2. **création d'un group de sécurité de l'instance bastion**
   3. **création d'un role iam permettant à l'instance d'accéder aux resources aws**
   4. **connexion au bastion et install aws-cli,kubectl,...**
   5. 
   
