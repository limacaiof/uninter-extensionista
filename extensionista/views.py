from django.shortcuts import render
from django.http import HttpRequest


def home(request: HttpRequest):
    from campaign.forms import CampaignForm
    form = CampaignForm()
    return render(request, 'home.html', {'form': form})


def about(request: HttpRequest):
    return render(request, 'about.html')
