from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, bridegroom
from users.models import User
from django.contrib.auth.decorators import login_required
from .forms import RawSearch
from django.http import Http404
from django.db.models import Q

@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def search(request):
    if request.method == 'POST':
        # searched = request.POST['searched']
        age = request.POST['age_filter']
        gender = request.POST['gender']
        caste  = request.POST['caste']
        # search the bride and groom by age, gender, height, weight, education, job, annual income, marital status, religion, caste, state, country
        try:
            
            bridegrooms = bridegroom.objects.filter(  Q(gender__icontains=gender) & Q(caste__icontains=caste) & Q(age__icontains=age) )
        except bridegroom.DoesNotExist:
            raise Http404("Bride or Groom does not exist")
        
        return render(request, 'blog/search.html', {'searched': caste, 'bridegroom': bridegrooms})
    else:
        return render(request, 'blog/search.html', {})
    
    
    
    
def updateprofile(request):
    status = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        education = request.POST.get('education')
        job =   request.POST.get('job')
        annual_income = request.POST.get('annual_income')
        marital_status = request.POST.get('marital_status')
        religion = request.POST.get('religion')
        caste =   request.POST.get('caste')
        state = request.POST.get('state')
        country = request.POST.get('country')
        up = bridegroom(name=name,age=age,gender=gender,height=height,weight=weight,education=education,job=job,annual_income=annual_income,marital_status=marital_status,religion=religion,caste=caste,state=state,country=country)
        up.save()
        status = 'Profile Updated Successfully'
    return render(request, 'blog/updateprofile.html',{'status':status})
    