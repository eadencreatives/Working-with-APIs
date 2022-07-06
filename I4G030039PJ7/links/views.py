from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer


# Create your views here.

class PostListSet(viewsets.ModelListSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateSet(viewsets.ModelCreateSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateSet(viewsets.ModelUpdateSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteSet(viewsets.ModelDeleteSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer