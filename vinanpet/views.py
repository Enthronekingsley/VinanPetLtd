from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReportForm
from formtools.preview import FormPreview
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, "home.html")



def report(request):
    if request.method == "POST":
            form = ReportForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                messages.success(request, "Report successfully submitted")
                return redirect("report")
    else:
        form = ReportForm()
    return render(request, "report.html", {"form": form})



def remark(request):
    return render(request, "remark.html")