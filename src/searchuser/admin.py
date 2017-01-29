from django.contrib import admin

# Register your models here.
from .models import userSearch, queryReport
from django.utils.html import format_html


class userSearchAdmin(admin.ModelAdmin):
	list_display = ["id","name","email","followers","timestamp","updatedtime","image_tag","publish"]
	search_fields = ["email","timestamp"]
	list_filter =["timestamp"]
	list_editable = ["publish"]
	class Meta:
		model = userSearch

class queryReportAdmin(admin.ModelAdmin):
	list_display =["requested","timestamp"]
	class Meta:
		model = queryReport

admin.site.register(userSearch,userSearchAdmin)
admin.site.register(queryReport,queryReportAdmin)