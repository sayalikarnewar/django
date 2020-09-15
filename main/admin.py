from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	#fields = ["Tutorial_title",
	#"Tutorial_published",
				#"Tutorial_content"]

	fieldsets = [
		("Title/date",{"fields" : ["Tutorial_title", "Tutorial_published"]}),
		("Content", {"fields" : ["Tutorial_content"]})
	]

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }



admin.site.register(Tutorial, TutorialAdmin)

  