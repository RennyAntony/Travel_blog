from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm

# Create your views here.
def create(request):   
    # 'if request.method == 'POST' or the below code
    if request.POST:
        frm = MovieForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save() 
    else:
        frm=MovieForm()
    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})
    #movies is the name of the key in list.html

def edit(request,pk):
    instance_to_be_edited=MovieInfo.objects.get(pk=pk)
    if request.POST:
        # title=request.POST.get('title')
        # year=request.POST.get('year')
        # description=request.POST.get('description')
        # instance_to_be_edited.title=title 
        # instance_to_be_edited.year=year 
        # instance_to_be_edited.description=description
        # instance_to_be_edited.save() 
      frm=MovieForm(request.POST,instance= instance_to_be_edited)
      if frm.is_valid():
        instance_to_be_edited.save()
    else:         
        frm=MovieForm(instance= instance_to_be_edited)
    return render(request,'create.html',{'frm':frm})
    
     
def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})