from django.urls import path
from myShop import views

urlpatterns = [
    path("infoproduct/<int:id>/", views.RedirectionInfosProduit.as_view()),
    path("infoproducts/", views.RedirectionInfosProduitListe.as_view()),
    path("putonsale/<int:id>/<str:newprice>/", views.RedirectionMiseEnPromoManuelle.as_view()),
    path("removesale/<int:id>/", views.RedirectionSuppressionPromoManuelle.as_view()),
    path("incrementstock/<int:id>/<int:number>/", views.RedirectionAugmentationStock.as_view()),
    path("decrementstock/<int:id>/<int:number>/", views.RedirectionDiminutionStock.as_view()),
    path("transaction/<int:tigID>/<str:type>/<str:price>/<str:quantity>/", views.RedirectionAjoutTransaction.as_view())
]
