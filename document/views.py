from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from haystack.query import SearchQuerySet
from haystack.inputs import Clean, Exact

from .models import Document
from .inputs import Words


@csrf_exempt
def home(request):
    return JsonResponse({'message': 'Plase hit the appropriate endpoint.'})


@csrf_exempt
def index(request):
    doc_id = request.POST.get('id', '').strip()
    title = request.POST.get('title', '').strip()
    data = request.POST.get('data', '').strip()

    if not all((doc_id, title, data)):
        message = 'Please send all parameters.'
        return JsonResponse({'message': message}, status=422)
    Document.objects.update_or_create(
        id=int(doc_id),
        defaults={"title": title, "data": data},
    )

    return JsonResponse({'message': 'Indexed submitted data.'})


@csrf_exempt
def search(request):
    query = request.GET.get('q', '').strip()

    if query.startswith('"') and query.endswith('"'):
        results = SearchQuerySet().filter(content=Clean(Exact(query)))
    else:
        results = SearchQuerySet().filter(content=Clean(Words(query)))

    data = [{'id': i.pk, 'title': i.title, 'data': i.data}
            for i in results]

    return JsonResponse({'results': data})
