from django.core.management.base import BaseCommand
from myShop.models import InfosProduit
from myShop.serializers import InfosProduitSerializer
from mytig.config import baseUrl
import requests
import time

class Command(BaseCommand):
    help = "Refresh the list of products from TIG server."

    def handle(self, *args, **options):
        self.stdout.write("[" + time.ctime() + "] Refreshing data...")
        response = requests.get(baseUrl + "products/")
        jsondata = response.json()
        InfosProduit.objects.all().delete()

        for produit in jsondata:
            data = {
                "tigID": str(produit["id"]),
                "name": str(produit["name"]),
                "category": str(produit["category"]),
                "price": str(produit["price"]),
                "unit": str(produit["unit"]),
                "availability": str(produit["availability"]),
                "sale": str(produit["sale"]),
                "discount": str(produit["discount"]),
                "comments": str(produit["comments"]),
                "owner": str(produit["owner"]),
                "quantityInStock": "0"
            }
            serializer = InfosProduitSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(
                    "[" + time.ctime() + "] Successfully added product id='%s'" % produit["id"]))
                self.stdout.write(
                    "[" + time.ctime() + "] Data refresh terminated.")
