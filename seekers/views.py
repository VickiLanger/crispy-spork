from django.shortcuts import render, get_object_or_404
from .models import Listing  # maybe this helps?


# Create your views here.
def seeker_list(request):
    return render(request, 'seekers/seeker_list.html', {})


def seeker_detail(request):
    return render(request, 'seekers/seeker_detail.html', {})


"""
def seeker_detail(request, pk):
    seekers = get_object_or_404(Listing, pk=pk)
    return render(request, 'seekers/seeker_detail.html', {'listing': listing})


def seeker_list(request, pk):
    seekers = get_object_or_404(Listing, pk=pk)
    return render(request, 'seekers/seeker_list.html', {'listing': listing})
"""
