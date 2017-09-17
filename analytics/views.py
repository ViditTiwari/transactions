from django.shortcuts import render
from .utils import get_analytics


# Create your views here.

def analytics_index_view(request):
	context = get_analytics()
	return render(request, 'index.html', context)
