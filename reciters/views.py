
from django.http import HttpResponse
from django.shortcuts import render
from .models import RecitersProfile,Surah
from .serializers import ReciterProfileSerializer,RecitersListWithImageSerializer,SurahSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json
from darul_masajid.settings import BASE_DIR
from reciters import serializers

# Create your views here.

class RecitersProfileAPIView(APIView):


    def post(self,request):
        serializer=ReciterProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"new recite profile created....!!"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def get(self,request,pk=None):
        id=pk
        if id is not None:
            
            rec=RecitersProfile.objects.get(id=id)
            serializer=ReciterProfileSerializer(rec)
            return Response({"reciter":serializer.data},status=status.HTTP_200_OK)


        recs=RecitersProfile.objects.all()
        print("recs:",recs)
        n=len(recs) 
        serializer=ReciterProfileSerializer(recs,many=True)
        return Response({"total no of reciters:":n,"reciters":serializer.data},status=status.HTTP_200_OK)



class RecitersListWithImageAPIView(APIView):
    def get(self,request,pk=None):
        ob=RecitersProfile.objects.all()
        serializer=RecitersListWithImageSerializer(ob,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        


class SurahAPIView(ModelViewSet):
    qeryset=Surah.objects.all()
    serializer_class=SurahSerializer

    def retrieve(self,request,pk=None):
        id=pk
        print("id:",id)
        surah=Surah.objects.filter(reciter_id=id)
        print("surah:",surah)
        serializer=SurahSerializer(surah,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




# def fun(request,pk):
#     surahs=Surah.objects.filter(reciter_id=pk)
#     return render(request,"reciters/home.html",{"surahs":surahs})

def saveData(request):
    with open(f"{BASE_DIR}/khalil_al_husary.json") as f:
        data = json.load(f)
        print(data)
        reciter = RecitersProfile.objects.get(id=7)
        for chapter in data:
            surah = Surah.objects.create(chapter_id=chapter["chapter_id"],file_size=chapter["file_size"],duration=chapter["duration"],format=chapter["format"],verse_timings=json.dumps(chapter["verse_timings"]),reciter=reciter)
            surah.save()
            print(chapter,"saved")
        return HttpResponse({"msg":json.dumps(data)})






