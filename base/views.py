from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from .models import List, Task
from django.contrib.auth.decorators import login_required
from .forms import CreateListForm, CreateTaskForm
from django.contrib import messages
from django.contrib.auth.models import User


# Home view


def home(request):
    if request.method == "POST" and 'delete' in request.POST:
        list_id = request.POST.get('item_id')
        item = get_object_or_404(List, id=list_id)
        item_name = item.name  # Optional: Get the name for the success message
        item.delete()
        messages.success(request, f'Item "{
            item_name.title()}" has been deleted successfully!')
        return redirect('home')  # Redirect to avoid resubmission issues
    lists = List.objects.order_by('-name')
    context = {'title': 'home', 'lists': lists}
    return render(request, 'base/home.html', context)

# Tasks view


def tasks(request, qk):
    list = get_object_or_404(List, id=qk)
    tsks = list.task_set

    if request.method == "POST":

        if request.POST.get("save"):
            for task in tsks.all():
                if request.POST.get("c" + str(task.id)) == 'clicked':
                    task.complete = True

                else:
                    task.complete = False

                task.save()

        elif request.POST.get("submit"):
            txt = request.POST.get('newT')

            if len(txt) > 0:
                tsks.create(list=list, title=txt, complete=False)

            else:
                print('invalied')

    context = {'title': 'tasks', 'list': list, 'tasks': tsks.all()}
    return render(request, 'base/tasks.html', context)

# CreateList view


@login_required
def createList(request):
    if request.method == "POST":
        form = CreateListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user  # Assign the user
            new_list.save()
            messages.success(
                request, f'One list has been created => "{new_list.name}"')
            return redirect("home")
    else:
        form = CreateListForm()

    return render(request, 'base/createList.html', {'form': form})


def about(request):
    return render(request, 'base/about.html')
