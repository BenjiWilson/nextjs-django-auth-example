from django.utils import timezone
from rest_framework import generics, response
from rest_framework.permissions import IsAuthenticated

from django.views.generic import TemplateView

from . import serializers

# class Feed(TemplateView):
#     template_name = 'api/feed.html'
#     def get_context_data(self, **kwargs):
#         current_user = self.request.user
#         print("current_user:")
#         print(current_user)
#         return context    

class Profile(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.User

    def get_object(self):
        return self.request.user


class Ping(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        return response.Response({'now': timezone.now().isoformat()})



class Profile(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.User

    def get_object(self):
        return self.request.user

