from django.shortcuts import render
from meds.models import Med
from .models import Team
# Create your views here.

def home(request):
    teams = Team.objects.all()
    # meds = Med.objects.all()
    meds = Med.objects.order_by('-created_date').filter(is_featured=True)
    # search_fields = Med.objects.values('brand', 'model', 'problem',)
    model_search = Med.objects.values_list('model', flat=True).distinct()
    brand_search = Med.objects.values_list('brand', flat=True).distinct()
    data = {
        'teams':teams,
        'meds':meds,
        # 'search_fields':search_fields,
        'model_search':model_search,
        'brand_search':brand_search,

    }

    return render(request, 'pages/home.html',  data)
