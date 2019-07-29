from rest_framework.viewsets import ModelViewSet
from .serializers import CoworkingSerializer
from core.models import Coworking
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


class CoworkingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    serializer_class = CoworkingSerializer

    # def get_queryset(self):
    #     user_id = self.request.auth.user_id
    #     return Coworking.objects.filter(cliente=user_id)

    def get_queryset(self):
        return Coworking.objects.all()

