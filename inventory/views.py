from django.shortcuts import render
from django.http import Http404
from inventory.models import Item

def index(request):
	items = Item.objects.exclude(amount=0)
	return render(request, 'inventory/index.html', {
			'items': items,

		})

#Every def in views requires a request parameter.
#The id parameter allows urls to pass id as a param to the web page to use in regex's
#the {}'s at the end of render params allows our templates to access the objects created in the def'
def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')

	return render(request, 'inventory/item_detail.html', {
			'item': item,
		})