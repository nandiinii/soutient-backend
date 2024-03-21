from rest_framework import generics,mixins,viewsets,status
from .models import MetamaskUser
from .serializers import MetamaskUserSerializer
from rest_framework.response import Response
# Create your views here.
class MetamaskUserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    serializer_class = MetamaskUserSerializer
    queryset = MetamaskUser.objects.all()

    def create(self, request, *args, **kwargs):
        metamask_id = request.data.get('metamask_id')
        date_time = request.data.get('date_time')
        existing_user = MetamaskUser.objects.filter(metamask_id=metamask_id).first()
        if existing_user:
            existing_user.date_time = date_time
            existing_user.save()
            serializer = self.get_serializer(existing_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)