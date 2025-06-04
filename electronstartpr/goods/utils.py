from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


from .models import Product

def q_search(query):

    #vector = SearchVector('name', 'description', 'article')
    #query = SearchQuery(query)

    #return Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')
    
    #return Product.objects.filter(article__iexact=query)
    
    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(name__icontains=token)
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(article__icontains=token)

    return Product.objects.filter(q_objects) 
