from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import requests
from django.core.paginator import Paginator
from .models import Item
from .forms import ItemSearchForm


def home(request):
	context = {'page_title':"Hacker News"}
	items = Item.objects.topstories()
	########### PAGINATION ###############################
	paginator = Paginator(items, 5)  # Display 5 items per page
	page_number = request.GET.get('page')
	page_items = paginator.get_page(page_number)
	context['items'] = page_items
	return render(request,'items/home.html',context)


def new(request):
	context = {'page_title':"Latest "}
	items = Item.objects.new_items()
	########### PAGINATION ###############################
	paginator = Paginator(items, 5)  # Display 5 items per page
	page_number = request.GET.get('page')
	page_items = paginator.get_page(page_number)
	context['items'] = page_items
	return render(request,'items/new.html',context)


def past(request):
	context = {'page_title':"Hacker news V2.0"}
	items = Item.objects.past_items()
	########### PAGINATION ###############################
	paginator = Paginator(items, 5)  # Display 5 items per page
	page_number = request.GET.get('page')
	page_items = paginator.get_page(page_number)
	context['items'] = page_items
	return render(request,'items/past.html',context)


def comments(request):
	context = {'page_title':"Hacker news V2.0"}
	items = Item.objects.comments()
	########### PAGINATION ###############################
	paginator = Paginator(items, 5)  # Display 5 items per page
	page_number = request.GET.get('page')
	page_items = paginator.get_page(page_number)
	context['items'] = page_items
	return render(request,'items/comments.html',context)


def ask(request):
	context = {'page_title':"Hacker news V2.0"}
	items = Item.objects.askstories()
	########### PAGINATION ###############################
	paginator = Paginator(items, 5)  # Display 5 items per page
	page_number = request.GET.get('page')
	page_items = paginator.get_page(page_number)
	context['items'] = page_items
	return render(request,'items/ask.html',context)


def show(request):
	context = {'page_title':"Hacker news V2.0"}
	items = Item.objects.showstories()
	########### PAGINATION ###############################
	paginator = Paginator(items, 5)  # Display 5 items per page
	page_number = request.GET.get('page')
	page_items = paginator.get_page(page_number)
	context['items'] = page_items
	return render(request,'items/show.html',context)


def jobs(request):
	context = {'page_title':"Hacker news V2.0"}
	items = Item.objects.jobstories()
	########### PAGINATION ###############################
	paginator = Paginator(items, 5)  # Display 5 items per page
	page_number = request.GET.get('page')
	page_items = paginator.get_page(page_number)
	context['items'] = page_items
	return render(request,'items/jobs.html',context)


def search_items(request):
	context = {'page_title':'Search'}
	form = ItemSearchForm(request.GET)
	results = []

	if form.is_valid():
		query = form.cleaned_data['query']
		category = form.cleaned_data['category']
		search_in_creator = form.cleaned_data['search_in_creator']
		search_in_score = form.cleaned_data['search_in_score']

		#If search query in title
		query_args = Q(title__icontains=query)

		# Or if its in creator
		if search_in_creator:
			query_args |= Q(item_creator__icontains=query)

		# Or if its in score
		if search_in_score:
			query_args |= Q(score__icontains=query)

		if category:  # Only filter by category if a category is selected
			query_args &= Q(item_type=category)

		items = Item.objects.filter(query_args)
	########### PAGINATION ###############################
	paginator = Paginator(items, 5)  # Display 5 items per page
	page_number = request.GET.get('page')
	page_items = paginator.get_page(page_number)
	context['items'] = page_items
	context['form'] = form
	return render(request, 'items/search_results.html', context)


def item_detail(request,item_id):
	context = {'page_title':"Hacker news V2.0"}
	item = get_object_or_404(Item,id=item_id)
	comments = Item.objects.filter(parent_item=item)
	context['item'] = item
	context['comments'] = comments
	return render(request,'items/item_detail.html',context)


###################### LOGIN USERS #####################################
########################################################################
########################################################################

@login_required
def threads(request):
	context = {'page_title':"Hacker news V2.0"}
	return render(request,'items/threads.html',context)


@login_required
def submit(request):
	context = {'page_title':"Hacker news V2.0"}
	return render(request,'items/submit.html',context)








########## SIMPLE SEARCH 
# def search_items(request):
# 	form = ItemSearchForm(request.GET)
# 	results = []

# 	if form.is_valid():
# 		query = form.cleaned_data['query']
# 		results = Item.objects.filter(title__icontains=query)

# 	return render(request, 'items/search_results.html', {'form': form, 'results': results})

# def search_items(request):
# 	form = ItemSearchForm(request.GET)
# 	results = []

# 	if form.is_valid():
# 		query = form.cleaned_data['query']
# 		category = form.cleaned_data['category']

# 		query_args = {
# 			'title__icontains': query,
# 		}

# 		if category:  # Only filter by category if a category is selected
# 			query_args['item_type'] = category

# 		results = Item.objects.filter(**query_args)

# 	return render(request, 'items/search_results.html', 
# 		{'form': form, 'results': results})




