import boto3
import datetime

# Paramètres à configurer
region = 'us-east-1'  # Région AWS
instance_type = 't2.micro'  # Type d'instance Spot que vous souhaitez
price_threshold = 0.02  # Seuil de prix pour vérifier les prix Spot (en USD)
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

        # Vérifier les prix et afficher les régions/zones qui vérifient le seuil
        for price_info in spot_prices:
            spot_price = float(price_info['SpotPrice'])
            availability_zone = price_info['AvailabilityZone']
            print(f"Prix actuel pour {instance_type} dans {availability_zone}: {spot_price} USD")

            # Si le prix est inférieur ou égal au seuil, afficher la région et la zone de disponibilité
            if spot_price <= price_threshold:
                print(f"[INFO] Le prix {spot_price} est inférieur ou égal au seuil de {price_threshold} dans la zone {availability_zone}.")

    except Exception as e:
        print(f"Erreur lors de la récupération des prix Spot: {e}")

# Fonction principale
def main():
    print("Vérification des prix des instances Spot...")
    get_spot_prices(region, instance_type, price_threshold)

if __name__ == "__main__":
    main()
