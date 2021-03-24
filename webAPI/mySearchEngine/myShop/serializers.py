from rest_framework.serializers import ModelSerializer, DateTimeField
from myShop.models import InfosProduit, TransactionProduit

class InfosProduitSerializer(ModelSerializer):
    class Meta:
        model = InfosProduit
        fields = ("id", "tigID", "name", "category", "price", "unit", "availability",
                  "sale", "discount", "comments", "owner", "quantityInStock")

class TransactionProduitSerializer(ModelSerializer):
    # Nécessaire pour les valeurs de tests, lorsque les valeurs ne sont pas
    # les DateTime d'origine
    date = DateTimeField()

    class Meta:
        model = TransactionProduit
        fields = ("id", "tigID", "price", "quantity", "type", "date")
