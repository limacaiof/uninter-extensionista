from django import forms
from .models import Campaign
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ["title", "description",
                  "how_help", "image_path", "limit_date"]
        labels = {
            "title": "Título",
            "description": "Descrição",
            "image_path": "Selecione uma imagem",
            "how_help": "Como ajudar",
            "limit_date": "Data limite para campanha"
        }
        widgets = {
            "limit_date": DateTimePickerInput(
                attrs={
                    "placeholder": "A campanha vai durar até...",
                    "class": "form-control c-limit_date"
                },
                options={
                    "locale": "pt-BR",
                    "format": "DD/MM/YYYY"
                }
            )
        }

    title = forms.CharField(
        label="Título",
        min_length=5,
        max_length=60,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Adicione um título...",
                "maxlength": "60",
                "class": "form-control c-title"
            }
        )
    )
    description = forms.CharField(
        label="Descrição",
        min_length=25,
        max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                "maxlength": "999",
                "placeholder": "Adicione um descrição...",
                "class": "form-control c-description"
            }
        )
    )
    how_help = forms.CharField(
        label="Como ajudar",
        min_length=5,
        max_length=500,
        required=True,
        widget=forms.Textarea(
            attrs={
                "maxlength": "500",
                "placeholder": "Como as pessoas podem contribuir...",
                "rows": "5",
                "class": "form-control c-how_help"
            }
        )
    )
    image_path = forms.ImageField(
        label="Selecione uma imagem",
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "id": "c-image",
                "style": "display: none;",
                "accept": "image/*"
            }
        )
    )
