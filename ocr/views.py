from django.shortcuts import render
from django.views import generic
from django.db.models import Q, Prefetch
import shlex

from .models import OcrDocument, OcrPage

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'ocr/index.html'
    model = OcrDocument
    paginate_by = 30

    def get_queryset(self):
        if not self.request.GET.get('q',):
            return OcrDocument.objects.all()
        q = self.request.GET.get('q',)
        words = shlex.split(q)
        q_parent = Q()
        q_child = Q()
        for word in words:
            if word.startswith('-'):
                word = word[1:]
                q_parent &= ~Q(ocrpage__text__icontains=word)
                q_child &= ~Q(text__icontains=word)
            else:
                q_parent &= Q(ocrpage__text__icontains=word)
                q_child &= Q(text__icontains=word)
        return OcrDocument.objects.filter(q_parent).distinct().prefetch_related(
            Prefetch(
                'ocrpage_set',
                queryset=OcrPage.objects.filter(q_child),
                to_attr='prefetched_pages'
            )
        )


class DocView(generic.DetailView):
    model = OcrDocument
