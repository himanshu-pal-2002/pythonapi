from rest_framework import serializers

from app.models import Flipkart_Api


# Serializer Represents for Login Api
class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField
    password = serializers.CharField()
    
# Serializer Represents The API Representation.
class Flipkart_ApiSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Flipkart_Api
        fields="__all__"