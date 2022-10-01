from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.views import generic
from functools import reduce
from operator import and_
from searchKunn.models import Book


# # Create your views here.
class IndexView(generic.ListView):
    model = Book
    template_name = 'searchKunn/index.html'

    """ オーバーライド """

    def get_queryset(self):
        queryset = Book.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')

        if keyword:
            exclusion = set([' ', '　'])
            q_list = ''

            for i in keyword:
                if i in exclusion:
                    pass
                else:
                    q_list += i

            query = reduce(
                and_, [Q(Title__icontains=q) | Q(Author__icontains=q) | Q(Category__icontains=q) for q in q_list]
            )
            queryset = queryset.filter(query)
            messages.success(self.request, '「{}」の検索結果'.format(keyword))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        keyword = self.request.GET.get('keyword')
        context["keyword"] = keyword
        context["count"] = self.get_queryset().count()
        return context


def kensaku_kunn(request):
    book = Book.objects.order_by('-id')
    return render(request, 'searchKunn/KensakuKunn.html', {
        'book_list': book,
    })


def kekka(request):
    return render(request, 'searchKunn/kekka.html', {
    })
