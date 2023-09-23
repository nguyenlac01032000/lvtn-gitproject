from django.shortcuts import render, get_object_or_404
from .models import Med

# Create your views here.

def home(request):
    teams = Team.objects.all()
    # featured_meds = Med.objects.order_by('-created_date').filter(is_featured=True)


    data = {
        'teams':teams,
        # 'featured_meds': featured_meds,
        'search_fields':search_fields,
    }

    return render(request, 'pages/home.html', data)

def meds(request):
    return render(request, 'meds/meds.html')

def med_detail(request, id):
    single_med = get_object_or_404(Med, pk=id)

    data = {
        'single_med': single_med,
    }
    return render(request, 'meds/med_detail.html', data)

def search(request):
    meds = Med.objects.order_by('-created_date')
    # search_fields = Med.objects.values('brand', 'model', 'problem',)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            meds = meds.filter(problem__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            meds = meds.filter(model__iexact=model)

    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            meds = meds.filter(brand__iexact=brand)

    data = {
        'meds': meds,
        # 'search_fields':search_fields,
    }
    return render(request, 'meds/search.html', data)
