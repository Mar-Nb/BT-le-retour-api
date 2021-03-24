from rest_framework.serializers import ModelSerializer
from mytig.models import ProduitEnPromotion
from mytig.models import ProduitDisponible

class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID', "discount")

class ProduitDisponibleSerializer(ModelSerializer):
    class Meta:
        model = ProduitDisponible
        fields = ('id', 'tigID')
