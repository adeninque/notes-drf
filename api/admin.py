from django.contrib import admin


from .models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
  list_display = ("id", "title",)
  list_display_links = ("id", )

admin.site.register(Note, NoteAdmin)