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
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Adicione um título...",
                    "maxlength": "60",
                    "class": "form-control c-title"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Adicione um descrição...",
                    "class": "form-control c-description"
                }
            ),
            "how_help": forms.Textarea(
                attrs={
                    "placeholder": "Como as pessoas podem contribuir...",
                    "rows": "5",
                    "class": "form-control c-how_help"
                }
            ),
            "limit_date": DateTimePickerInput(
                attrs={
                    "class": "form-control c-limit_date"
                },
                options={
                    "locale": "pt-BR",
                    "format": "DD/MM/YYYY"
                }
            )
        }
