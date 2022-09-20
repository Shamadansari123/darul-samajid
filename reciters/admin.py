from django.contrib import admin
from reciters.models import RecitersProfile,Surah
# Register your models here.

@admin.register(RecitersProfile)
class ReciterAdmin(admin.ModelAdmin):
    list_display=['id','name','image','about']




@admin.register(Surah)
class SurahAdmin(admin.ModelAdmin):
    list_display=['chapter_id','title','surah_meaning','location','file_size','format','audio_url','reciter','duration','verse_timings']

