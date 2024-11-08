import boto3
import datetime
import time

# Paramètres à configurer
region = 'us-east-1'  # Région AWS
instance_type = 't2.micro'  # Type d'instance Spot que vous souhaitez
price_threshold = 0.02  # Seuil de prix pour acheter des instances Spot (en USD)
max_instances = 5  # Nombre d'instances à acheter
product_description = 'Linux/UNIX'  # Type de produit

# Fonction pour récupérer les prix des instances Spot
def get_spot_prices(region, instance_type, price_threshold):
    # Créer un client EC2 pour la région spécifiée
    ec2_client = boto3.client('ec2', region_name=region)

    try:
        # Récupérer les prix Spot des instances EC2
        start_time = datetime.datetime.utcnow() - datetime.timedelta(hours=1)  # Heure de début (dernière heure)
        response = ec2_client.describe_spot_price_history(
            InstanceTypes=[instance_type],
            StartTime=start_time,
            ProductDescriptions=[product_description],
            MaxResults=10  # Limiter le nombre de résultats à 10
        )

        # Extraire les prix Spot des instances
        spot_prices = response['SpotPriceHistory']
        return spot_prices

    except Exception as e:
        print(f"Erreur lors de la récupération des prix Spot: {e}")
        return []

# Fonction pour acheter des instances Spot
def purchase_spot_instances(region, instance_type, price_threshold, max_instances):
    ec2_client = boto3.client('ec2', region_name=region)

    # Récupérer les prix Spot en temps réel
    spot_prices = get_spot_prices(region, instance_type, price_threshold)

    # Vérifier les prix et acheter si un prix dépasse le seuil
    for price_info in spot_prices:
        spot_price = float(price_info['SpotPrice'])
        availability_zone = price_info['AvailabilityZone']
        print(f"Prix actuel pour {instance_type} dans {availability_zone}: {spot_price} USD")

        # Si le prix dépasse le seuil, acheter des instances Spot
        if spot_price <= price_threshold:
            print(f"Le prix {spot_price} est inférieur ou égal au seuil de {price_threshold}. Achat des instances Spot.")
            
            # Lancer la demande pour 5 instances Spot
            try:
                response = ec2_client.request_spot_instances(
                    InstanceCount=max_instances,
                    Type='one-time',
                    LaunchSpecification={
                        'InstanceType': instance_type,
                        'AvailabilityZone': availability_zone,
                        'ImageId': 'ami-0abcdef1234567890',  # Remplacez par l'AMI que vous souhaitez utiliser
                        'KeyName': 'your-key-name',  # Remplacez par le nom de votre clé SSH
                    }
                )
                
                # Afficher les IDs des instances Spot demandées
                spot_instance_requests = response['SpotInstanceRequests']
                for request in spot_instance_requests:
                    print(f"Demande d'instance Spot lancée avec ID: {request['SpotInstanceRequestId']}")

            except Exception as e:
                print(f"Erreur lors de la demande d'instances Spot: {e}")
                continue

# Fonction principale
def main():
    print("Vérification des prix des instances Spot...")
    purchase_spot_instances(region, instance_type, price_threshold, max_instances)

if __name__ == "__main__":
    main()
