# aws-boto3-price-optimization
# AWS Price Optimization with CloudFormation and Boto3

## Description

Ce projet permet d'optimiser les coûts sur le cloud AWS en utilisant **CloudFormation** pour déployer des ressources et **Boto3** pour interagir avec les services AWS. L'objectif est de créer une solution automatisée qui ajuste dynamiquement les ressources AWS en fonction des besoins, réduisant ainsi les coûts tout en maintenant les performances.

## Fonctionnalités

- Déploiement d'infrastructures AWS optimisées avec **CloudFormation**.
- Utilisation de **Boto3** pour interagir avec les services AWS, notamment EC2, S3 et RDS.
- Analyse des coûts en temps réel et ajustement des ressources en fonction des besoins.
- Automatisation de la gestion des instances EC2 (arrêt, démarrage, modification de type d'instance).
- Optimisation des coûts S3 en utilisant des stratégies de cycle de vie des objets.

## Prérequis

- Python 3.x
- AWS CLI configuré avec des accès appropriés
- **Boto3** installé via pip : `pip install boto3`
- **CloudFormation** (AWS Management Console ou CLI)
- Accès à un compte AWS avec des permissions appropriées pour créer et gérer des ressources CloudFormation et Boto3.

## Installation

### 1. Clonez ce dépôt

```bash
git clone https://github.com/username/aws-price-optimizer.git
cd aws-price-optimizer
