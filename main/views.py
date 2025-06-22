from django.shortcuts import render
from django.views import generic
from .models import Weather
from datetime import date
import random

# Create your views here.

class home(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actualDate = date.today()

        weatherToday = Weather.objects.filter(dia=actualDate.day, mes=actualDate.month, agno=actualDate.year).first()
        weatherTomorrow = Weather.objects.filter(dia=(actualDate.day + 1), mes=actualDate.month, agno=actualDate.year).first()
        recommendationSunny = ["llevar gafas de sol y protector solar.", "mantenerte bien hidratado durante el día.", "evitar la exposición prolongada al sol en horas pico."]
        recommendationRainy = ["llevar paraguas y ropa impermeable.", "evitar actividades al aire libre si la lluvia es intensa.", "considerar usar calzado adecuado para el agua."]

        if weatherToday.probabilidad >= 50:
            recommendation = random.choice(recommendationRainy) 
        else:
            recommendation = random.choice(recommendationSunny)

        if weatherTomorrow.probabilidad >= 50:
            recommendationTomorrow = random.choice(recommendationRainy) 
        else:
            recommendationTomorrow = random.choice(recommendationSunny)

        context['weatherToday'] = weatherToday
        context['weatherTomorrow'] = weatherTomorrow
    
        context['recommendation'] = recommendation
        context['recommendationTomorrow'] = recommendationTomorrow

        context['actualDate'] = actualDate
        return context