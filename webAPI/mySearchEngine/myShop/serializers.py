from rest_framework.serializers import ModelSerializer
from myShop.models import InfosProduit, TransactionProduit

class InfosProduitSerializer(ModelSerializer):
    class Meta:
        model = InfosProduit
        fields = ("id","tigID", "name", "category", "price", "unit", "availability",
                  "sale", "discount", "comments", "owner", "quantityInStock")

class TransactionProduitSerializer(ModelSerializer):
    class Meta:
        model = TransactionProduit
        fields = ("id", "tigID", "price", "quantity", "type", "date")
