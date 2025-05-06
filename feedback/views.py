from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import FeedBack
from .forms import FormFeedBack
# Create your views here.


def feedback_list(request):
    feedback = FeedBack.objects.all()
    return render(request, 'feedback/feedback_list.html', {'feedback': feedback})


@login_required
def feedback_add(request):
    if request.method == 'POST':
        form = FormFeedBack(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback:feedback_list')

    else:
        form = FormFeedBack()
    return render(request, 'feedback/feedback_add.html', {'form': form})