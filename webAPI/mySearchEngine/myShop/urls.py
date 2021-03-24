from django.urls import path
from myShop import views

urlpatterns = [
    path("infoproduct/<int:id>/", views.RedirectionInfosProduit.as_view()),
    path("infoproducts/", views.RedirectionInfosProduitListe.as_view()),
    path("putonsale/<int:id>/<str:newprice>/", views.RedirectionMiseEnPromoManuelle.as_view()),
    path("removesale/<int:id>/", views.RedirectionSuppressionPromoManuelle.as_view()),
    path("incrementstock/<int:id>/<int:number>/", views.RedirectionAugmentationStock.as_view()),
    path("decrementstock/<int:id>/<int:number>/", views.RedirectionDiminutionStock.as_view()),
    path("transaction/<int:tigID>/<str:type>/<str:price>/<str:quantity>/", views.RedirectionAjoutTransaction.as_view()),
    path("transaction/getannee/<int:annee>/", views.RedirectionTransactionAnnee.as_view()),
    path("transaction/gettrimestre/<int:annee>/<int:trimestre>/", views.RedirectionTransactionTrimestre.as_view()),
    path("transaction/getmois/<int:annee>/<int:mois>/", views.RedirectionTransactionMois.as_view()),
    path("transaction/getjour/<int:annee>/<int:mois>/<int:jour>/", views.RedirectionTransactionJour.as_view())
]
