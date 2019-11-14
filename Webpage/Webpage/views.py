from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from .models import List_data_point

from .forms import NameForm


def List(request):
    latest_data_list = List_data_point.objects.order_by('priority')
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





#test pages, not part of the webpage

def test(request):
    return render(request, 'Webpage/Test.html')
