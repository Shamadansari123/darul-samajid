from rest_framework import serializers
from .models import RecitersProfile,Surah


class ReciterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecitersProfile
        fields=['id','name','image','about']




class RecitersListWithImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecitersProfile
        fields=['id','name','image']




class SurahSerializer(serializers.ModelSerializer):
    class Meta:
        model=Surah
        fields=['chapter_id','title','surah_meaning','location','file_size','format','audio_url','reciter','duration']