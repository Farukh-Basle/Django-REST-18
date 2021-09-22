
from petsapp.models import Account
from petsapp.api.serializers import AccountRegisterSerializer
from rest_framework import generics

from rest_framework.parsers import MultiPartParser,FormParser,JSONParser

class AccountRegisterView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRegisterSerializer
    # parser_classes = [JSONParser,MultiPartParser,FormParser]


