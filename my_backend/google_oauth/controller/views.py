from urllib import parse
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from google_oauth.serializer.google_oauth_url_serializer import GoogleOauthUrlSerializer
from google_oauth.service.google_oauth_service_impl import GoogleOauthServiceImpl
class GoogleOauthView(viewsets.ViewSet):
    googleOauthService = GoogleOauthServiceImpl.getInstance()
    def googleOauthURI(self, request):
        url = self.googleOauthService.googleLoginAddress()
        print(f"url:", url)
        serializer = GoogleOauthUrlSerializer(data={ 'url': url })
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data)
