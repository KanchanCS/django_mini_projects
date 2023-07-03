import django_filters
from django import forms
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import IndustrySummary

# Create your views here.


def likelihood(request):
    data = {
        "data": [],
        "lable1": [],
        "lable2": [],
    }
    summaries = IndustrySummary.objects.all()[:200]
    for summary in summaries:
        if summary.country or summary.region:
            data["data"].append(summary.likelihood)
            data["lable1"].append(summary.country)
            data["lable2"].append(summary.region)
    context = {
        "data": data,
        "title": "Likelihood",
        "limits": 15,
        "type1": "bar",
        "type2": "line",
    }
    return render(
        request,
        "chart-bar.html",
        context,
    )


def intensity(request):
    data = {
        "data": [],
        "lable1": [],
        "lable2": [],
    }
    summaries = IndustrySummary.objects.all()[:200]
    for summary in summaries:
        if summary.country or summary.region:
            data["data"].append(summary.intensity)
            data["lable1"].append(summary.country)
            data["lable2"].append(summary.region)
    context = {
        "data": data,
        "title": "Intensity",
        "limits": 100,
        "type1": "bar",
        "type2": "line",
    }
    return render(
        request,
        "chart-bar.html",
        context,
    )


def relevance(request):
    data = {
        "data": [],
        "lable1": [],
        "lable2": [],
    }
    summaries = IndustrySummary.objects.all()[:200]
    for summary in summaries:
        if summary.country or summary.region:
            data["data"].append(summary.relevance)
            data["lable1"].append(summary.country)
            data["lable2"].append(summary.region)
    context = {
        "data": data,
        "title": "Revelance",
        "limits": 15,
        "type1": "bar",
        "type2": "line",
    }
    return render(
        request,
        "chart-bar.html",
        context,
    )


def home(request):
    return render(
        request,
        "home.html",
    )


class IndustrySummaryFilter(django_filters.FilterSet):
    end_year = django_filters.DateFilter(
        field_name="end_year",
        lookup_expr="lte",
        widget=forms.DateInput(attrs={"class": "form-control"}),
    )
    topic = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    sector = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    region = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    pestle = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    sources = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    country = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = IndustrySummary
        fields = [
            "end_year",
            "topic",
            "sector",
            "region",
            "pestle",
            "sources",
            "country",
        ]


def industry_summary_list(request):
    filter_data = IndustrySummaryFilter(
        request.GET, queryset=IndustrySummary.objects.all()
    )
    paginator = Paginator(filter_data.qs, 25)  # Show 10 results per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "filter-list.html",
        {"filter": filter_data, "page_obj": page_obj},
    )
