from django.contrib import admin

from .models import IndustrySummary


class IndustrySummaryAdmin(admin.ModelAdmin):
    list_display = (
        "topic",
        "sector",
        "country",
        "add_date",
        "publish_date",
    )
    search_fields = (
        "title",
        "topic",
        "region",
        "sector",
        "country",
        "pestle",
        "impact",
        "insight",
    )
    list_filter = ("country", "sector", "region")
    date_hierarchy = "publish_date"


admin.site.register(IndustrySummary, IndustrySummaryAdmin)
