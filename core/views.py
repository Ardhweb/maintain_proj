from django.shortcuts import render,redirect,get_object_or_404,HttpResponse

# Create your views here.
from .forms import SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()
def core_engine(request):
    return render(request, "core/home.html")


@login_required
def search_user(request):
    if request.method == "POST":
        query =  request.POST['searched']
        search_results = User.objects.filter(
                    Q(email__icontains=query))
        context = {'search_results':search_results}
        return render(request,"core/search_results.html",context)
    else:
        user_obj = User.objects.all()
    return render(request, 'core/search_results.html', {})