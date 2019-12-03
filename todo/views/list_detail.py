import bleach
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from todo.forms import AddEditTaskForm
from todo.models import Task, TaskList
from todo.utils import send_notify_mail, staff_check

from django.core.paginator import Paginator


@login_required
@user_passes_test(staff_check)
def list_detail(request, list_id=None, list_slug=None, view_completed=False) -> HttpResponse:
    """Display and manage tasks in a todo list.
    """

    # Defaults
    task_list = None
    form = None

    # Which tasks to show on this list view?
    if list_slug == "mine":
        pagination_tasks = Task.objects.filter(assigned_to=request.user)
        paginator = Paginator(pagination_tasks, 6)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    else:
        # Show a specific list, ensuring permissions.
        task_list = get_object_or_404(TaskList, id=list_id)
        if task_list.group not in request.user.groups.all() and not request.user.is_superuser:
            raise PermissionDenied
        pagination_tasks = Task.objects.filter(task_list=task_list.id)
        paginator = Paginator(pagination_tasks, 6)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    # Additional filtering
    if view_completed:
        pagination_tasks = pagination_tasks.filter(completed=True)
        paginator = Paginator(pagination_tasks, 6)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    else:
        pagination_tasks = pagination_tasks.filter(completed=False)
        paginator = Paginator(pagination_tasks, 6)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    # ######################
    #  Add New Task Form
    # ######################

    if request.POST.getlist("add_edit_task"):
        form = AddEditTaskForm(
            request.user,
            request.POST,
            initial={"assigned_to": request.user.id, "priority": 999, "task_list": task_list},
        )

        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.created_date = timezone.now()
            new_task.note = bleach.clean(form.cleaned_data["note"], strip=True)
            form.save()

            # Send email alert only if Notify checkbox is checked AND assignee is not same as the submitter
            if (
                "notify" in request.POST
                and new_task.assigned_to
                and new_task.assigned_to != request.user
            ):
                send_notify_mail(new_task)

            messages.success(request, 'New task "{t}" has been added.'.format(t=new_task.title))
            return redirect(request.path)
    else:
        # Don't allow adding new tasks on some views
        if list_slug not in ["mine", "recent-add", "recent-complete"]:
            form = AddEditTaskForm(
                request.user,
                initial={"assigned_to": request.user.id, "priority": 999, "task_list": task_list},
            )

    context = {
        "list_id": list_id,
        "list_slug": list_slug,
        "task_list": task_list,
        "form": form,
        "tasks": tasks,
        "view_completed": view_completed,
    }

    return render(request, "todo/list_detail.html", context)
