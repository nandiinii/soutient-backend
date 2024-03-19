from rest_framework import generics,mixins,viewsets,status
from .models import MetamaskUser
from .serializers import MetamaskUserSerializer

# Create your views here.
class MetamaskUserViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    serializer_class = MetamaskUserSerializer
    queryset = MetamaskUser.objects.all()