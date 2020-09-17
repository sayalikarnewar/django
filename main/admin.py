from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	#fields = ["Tutorial_title",
	#"Tutorial_published",
				#"Tutorial_content"]

	fieldsets = [
		("Title/date",{"fields" : ["tutorial_title", "tutorial_published"]}),
		("Series", {"fields": ["tutorial_series"]}),
		("Content", {"fields" : ["tutorial_content"]}),
	]

	formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)

  