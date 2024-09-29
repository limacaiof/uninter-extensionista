from django.shortcuts import render, redirect
from django.contrib import messages
from campaign.forms import CampaignForm
from django.http import HttpRequest
from .models import Campaign


# Create your views here.
def index(request: HttpRequest):
    query = request.GET.get("q")
    if query:
        result = Campaign.search_by_term(query)
    else:
        result = Campaign.objects.all()

    response = {
        "query": query,
        "campaigns": result
    }

    return render(request, "campaigns.html", response)


def register(request: HttpRequest):
    if request.method != "POST":
        form = CampaignForm()
        return render(request, "register.html", {"form": form})

    form = CampaignForm(request.POST, request.FILES)
    if not form.is_valid():
        for _, errors in form.errors.items():
            for error in errors:
                messages.add_message(request, messages.ERROR, error)
        return redirect("register")

    try:
        form.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Campanha criada com sucesso, faremos o melhor para que essa ação solidária chegue ao maior número de "
            "pessoas possível. Obrigado!"
        )
        return redirect("home")
    except:
        messages.add_message(
            request,
            messages.ERROR,
            "Houve uma falha ao criar a campanha, tente novamente."
        )
        return redirect("register")
