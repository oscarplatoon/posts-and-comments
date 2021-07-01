## polls/views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Question, Choice

def get_question(question_id):
  # this is a helper method we've created since we need to find the question in detail(), results(), and vote()
  return Question.objects.get(id=question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    data = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    question = get_question(question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    question = get_question(question_id)
    try: # try to do this
        selected_choice = question.choices.get(pk=request.POST['choice']) # find the choice that the user submitted in the form
    except (KeyError, Choice.DoesNotExist): # couldn't find the selected_choice above will raise an error. using "except" will catch that error from blowing up the app
        return render(request, 'polls/detail.html', { # re-display the question voting form
            'question': question,
            'error_message': "You didn't select a choice.", # these two are local variables that the view needs. this "error_message" is specifically for that
            # {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %} line of code
        })
    else:
        selected_choice.votes += 1 # add 1 to the number of votes for that selected choice
        selected_choice.save() # save it to the database
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

def results(request, question_id):
    question = get_question(question_id)
    return render(request, 'polls/results.html', {'question': question})
