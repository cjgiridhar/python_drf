from django.shortcuts import render
from rest_framework import generics, renderers
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
# Create your views here.


class SnippetList(generics.ListCreateAPIView):
    renderer_classes = (JSONRenderer, )
    queryset = Snippet.objects.filter()
    serializer_class = SnippetSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Snippet.objects.filter(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = (JSONRenderer, )
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer