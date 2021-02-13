from django.shortcuts import render
from .models import Valentine
from .forms import Valentineform
import random
# Create your views here.

def home(request):
    if request.method=='POST':
        form =Valentineform(request.POST)

        if form.is_valid():
            valen=form.save(commit=False)
            if valen.name.lower()!='sreedhar':
                print(valen.name)
                valen.score=random.randint(0,100)
                form.save()
            else:
                error='wow you tried typing my name !'

            
    else:
        form=Valentineform()
    valentine_now=Valentine.objects.all()
    return render(request,'valentine_template/valentinespecial.html',{'form':form,'valentines':valentine_now})


