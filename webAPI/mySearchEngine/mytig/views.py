import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from mytig.config import baseUrl
from mytig.models import ProduitEnPromotion
from mytig.models import ProduitDisponible
from mytig.serializers import ProduitEnPromotionSerializer
from mytig.serializers import ProduitDisponibleSerializer

from django.http import Http404
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl + 'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class RedirectionPointDeLivraison(APIView):
    def get(self, request, format = None):
        response = requests.get(baseUrl + "shipPoints/")
        jsondata = response.json()
        return Response(jsondata)

class RedirectionDetailProduit(APIView):
    def get_object(self, pk):
        try:
            response = requests.get(baseUrl + 'product/' + str(pk) + '/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404

    def get(self, request, pk, format = None):
        response = requests.get(baseUrl + 'product/' + str(pk) + '/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

class RedirectionDetailPointDeLivraison(APIView):
    def get_object(self, pk):
        try:
            response = requests.get(baseUrl + "shipPoint/" + str(pk) + "/")
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404

    def get(self, request, pk, format = None):
        response = requests.get(baseUrl + "shipPoint/" + str(pk) + "/")
        jsondata = response.json()
        return Response(jsondata)

class PromoList(APIView):
    def get(self, request, format = None):
        res = []
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe = False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class DispoList(APIView):
    def get(self, request, format = None):
        res = []

        for prod in ProduitDisponible.objects.all():
            serializer = ProduitDisponibleSerializer(prod)
            response = requests.get(baseUrl + "product/" + str(serializer.data["tigID"]) + "/")
            jsondata = response.json()
            res.append(jsondata)

        return JsonResponse(res, safe = False)

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk = pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl + 'product/' + str(serializer.data['tigID']) + '/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"

class DispoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitDisponible.objects.get(pk = pk)
        except:
            raise Http404

    def get(self, request, pk, format = None):
        prod = self.get_object(pk)
        serializer = ProduitDisponibleSerializer(prod)
        response = requests.get(baseUrl + "product/" + str(serializer.data["tigID"]) + "/")
        jsondata = response.json()
        return Response(jsondata)

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello World !"}
        return Response(content)
