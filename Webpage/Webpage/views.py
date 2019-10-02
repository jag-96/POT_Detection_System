from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from .models import List_data_point

from .forms import NameForm


def List(request):
    latest_data_list = List_data_point.objects.order_by('priority')[:5]
    all_data = List_data_point.objects.order_by('priority')
    context = {'latest_data_list': latest_data_list, 'all_data': all_data}
    return render(request, 'Webpage/List.html', context)

def edit_data_delete(request):
    data = List_data_point.objects.get(pk=request.GET['List_data_point'])
    data.delete()
    return HttpResponseRedirect(reverse('List'))

def edit_data_add(request):
    list_instance = List_data_point.objects.create(longitude=request.POST['longitude'],  latitude=request.POST['latitude'], priority=request.POST['priority'])
    list_instance.save()
    return HttpResponseRedirect(reverse('List'))

def edit_data_update(request):
    data = List_data_point.objects.get(pk=request.GET['List_data_point'])
    data.latitude = round(float(request.GET['List_data_point_lat']), 5)
    data.longitude= round(float(request.GET['List_data_point_long']), 5)
    data.save()
    return HttpResponseRedirect(reverse('List'))








def Map(request):
    latest_data_list = List_data_point.objects.order_by('priority')[:5]
    context = {'latest_data_list': latest_data_list}
    return render(request, 'Webpage/Map.html', context)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    latest_data_list = List_data_point.objects.order_by('priority')[:5]
    context = {
        'latest_data_list': latest_data_list,
        'form': form
        }

    return render(request, 'Webpage/test.html', context)

def edit_data(request):
    all_data = List_data_point.objects.order_by('priority')
    context = {'all_data': all_data}
    return render(request, 'Webpage/edit_data.html', context)
