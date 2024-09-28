from django.shortcuts import render, redirect
from django.contrib import messages
from campaign.forms import CampaignForm
from django.http import HttpRequest, HttpResponse

MOCK_CAMPAIGNS = [
    {
        "id": 1,
        "titulo": "Alimente uma Vida",
        "descricao": 'A campanha "Alimente uma Vida" busca arrecadar alimentos não perecíveis para famílias carentes da Zona Leste de São Paulo, onde a fome afeta milhares de pessoas diariamente. Estamos aceitando doações de arroz, feijão, óleo e outros itens básicos.',
        "localizacao": "São Paulo - Zona Leste",
        "como_ajudar": "Você pode ajudar doando alimentos não perecíveis nos pontos de coleta espalhados pela Zona Leste ou através de doações em dinheiro no site oficial da campanha. Além disso, ajude a divulgar nas redes sociais usando a hashtag #AlimenteUmaVida."
    },
    {
        "id": 2,
        "titulo": "Juntos Contra a Fome",
        "descricao": 'A iniciativa "Juntos Contra a Fome" tem como objetivo distribuir cestas básicas e refeições prontas para comunidades em situação de vulnerabilidade na cidade de Campinas. Além das doações, também incentivamos o voluntariado para a preparação e distribuição dos alimentos.',
        "localizacao": "Campinas - SP",
        "como_ajudar": "Contribua doando cestas básicas nos pontos de coleta ou através de parcerias locais. Se preferir, você pode voluntariar-se para preparar e distribuir refeições. Outra forma de ajudar é compartilhar nossa campanha e arrecadações por meio de eventos solidários."
    },
    {
        "id": 3,
        "titulo": "Solidariedade em Ação",
        "descricao": 'A campanha "Solidariedade em Ação" visa atender famílias em situação de pobreza extrema na região de Sorocaba, por meio de doações de alimentos, roupas e produtos de higiene. A ação também inclui palestras sobre nutrição e saúde alimentar.',
        "localizacao": "Sorocaba - SP",
        "como_ajudar": "Ajude doando alimentos, roupas e produtos de higiene nos centros de arrecadação. Você também pode organizar palestras ou eventos para conscientização sobre saúde alimentar. Divulgar a campanha entre amigos e familiares também faz uma grande diferença."
    },
    {
        "id": 4,
        "titulo": "Fome Zero no Vale",
        "descricao": 'A campanha "Fome Zero no Vale" foi criada para combater a fome na região do Vale do Paraíba. Estamos focados em arrecadar alimentos e direcionar cestas básicas para famílias que perderam renda devido à pandemia, além de promover hortas comunitárias.',
        "localizacao": "Vale do Paraíba - SP",
        "como_ajudar": "Contribua doando alimentos ou materiais para plantio nas hortas comunitárias. Você também pode se voluntariar para organizar e distribuir as cestas básicas. Ajude divulgando a campanha em suas redes sociais ou através de parcerias locais."
    },
    {
        "id": 5,
        "titulo": "São José Sem Fome",
        "descricao": 'A campanha "São José Sem Fome" busca fornecer refeições diárias para moradores de rua e pessoas em situação de vulnerabilidade no município de São José dos Campos. Contamos com a ajuda de voluntários para preparar e distribuir as refeições em abrigos e nas ruas.',
        "localizacao": "São José dos Campos - SP",
        "como_ajudar": "Você pode se voluntariar para cozinhar ou distribuir refeições nos pontos de apoio. Além disso, pode doar ingredientes para as refeições, como arroz, feijão e verduras. Também é possível divulgar a campanha para empresas e organizações que possam contribuir."
    }
]


# Create your views here.
def index(request: HttpRequest):
    query = request.GET.get("q")
    if query:
        result = list(filter(lambda c: any(query.lower() in str(value).lower()
                      for value in c.values()), MOCK_CAMPAIGNS))
    else:
        result = MOCK_CAMPAIGNS

    response = {
        "query": query,
        "campaigns": result
    }

    return render(request, "campaigns.html", response)


def register(request: HttpRequest):
    if request.method == "POST":
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
                "Campanha criada com sucesso, faremos o possível para que essa ação solidária chegue ao maior número de pessoas possível. Obrigado!"
            )
            return redirect("home")
        except:
            messages.add_message(request, messages.ERROR, "Houve uma falha ao criar a campanha, tente novamente.")


    form = CampaignForm()
    return render(request, "register.html", {"form": form})
