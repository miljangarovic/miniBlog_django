from .models import Profile
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def paginationProfiles(request,profiles,results):
    page = request.GET.get('page')  # trenutna stranica
    result = results  # na koliko stanica zelimo da podijelimo citav set
    paginator = Paginator(profiles, result)
    try:  # try except koristimo jer u pocetku nam se trazi br. stranice
        profiles = paginator.page(page)
    except PageNotAnInteger:  # prvi put kad udjes u projects neka se otvori prva stranica
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    return custom_range,profiles


def searchProfiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')



    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query))
   #distinct() omogucavaju da se ne ponavljaju isti objekti
    return profiles, search_query