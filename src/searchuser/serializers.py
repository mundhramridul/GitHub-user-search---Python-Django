from rest_framework import serializers
from .models import userSearch, queryReport

class DataSerializer(serializers.ModelSerializer):
    class Meta:
    	model = userSearch
    	fields = '__all__'

    def update(self, instance ,validated_data):
        #instance.login = validated_data.get('login', instance.login)
        instance.avatar_url = validated_data.get('avatar_url', instance.avatar_url)
        instance.name = validated_data.get('name', instance.name)
        #instance.email = validated_data.get('email',instance.email)
        instance.public_repos = validated_data.get('public_repos',instance.public_repos)
        instance.followers = validated_data.get('followers', instance.followers)
        instance.following = validated_data.get('following',instance.following)
        instance.save()
        return instance

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
    	model = queryReport
    	fields = '__all__'