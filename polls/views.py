from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Question

# Create your views here.
class IndexView(TemplateView)
    def index(request):
        latest_question_list =  Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)

class DetailView(TemplateView)
    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        context = {'question': question}
        return render(request, 'polls/detail.html', context)
