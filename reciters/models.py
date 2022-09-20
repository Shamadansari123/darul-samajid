from django.db import models



class RecitersProfile(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="reciters/",null=True)
    about=models.TextField()

    def __str__(self):
        return self.name




class Surah(models.Model):
    chapter_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=220,default="")
    surah_meaning=models.TextField(default="")
    location=models.CharField(max_length=200,null=True,blank=True)
    file_size=models.DecimalField(max_digits=19, decimal_places=1)
    format=models.CharField(max_length=100)
    audio_url=models.FileField(upload_to="surah/",null=True)
    reciter=models.ForeignKey(RecitersProfile,on_delete=models.CASCADE,related_name="surah")
    duration=models.IntegerField()
    verse_timings=models.CharField(max_length=300000000,blank=True)


    def __str__(self):
        return str(self.title)