from django.shortcuts import render
from meds.models import Med
from .models import Team
# Create your views here.

def home(request):
    teams = Team.objects.all()
    # meds = Med.objects.all()
    meds = Med.objects.order_by('-created_date').filter(is_featured=True)
    search_fields = Med.objects.values('brand', 'model', 'problem',)

    data = {
        'teams':teams,
        'meds':meds,
        'search_fields':search_fields,
        # 'featured_meds': featured_meds,

    }

    return render(request, 'pages/home.html',  data)
