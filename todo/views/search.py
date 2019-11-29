from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Task
from todo.utils import staff_check

from django.core.paginator import Paginator


@login_required
@user_passes_test(staff_check)
def search(request) -> HttpResponse:
    """Search for tasks user has permission to see.
    """

    query_string = ""

    if request.GET:

        found_tasks = None
        if ("q" in request.GET) and request.GET["q"].strip():
            query_string = request.GET["q"]

            found_tasks2 = Task.objects.filter(
                Q(title__icontains=query_string) | Q(note__icontains=query_string)
            )
            paginator = Paginator(found_tasks2, 6)
            page = request.GET.get('page')
            found_tasks = paginator.get_page(page)
        else:
            # What if they selected the "completed" toggle but didn't enter a query string?
            # We still need found_tasks in a queryset so it can be "excluded" below.
            found_tasks2 = Task.objects.all()
            paginator = Paginator(found_tasks2, 6)
            page = request.GET.get('page')
            found_tasks = paginator.get_page(page)

        if "inc_complete" in request.GET:
            found_tasks = found_tasks.exclude(completed=True)

    else:
        found_tasks = None

    # Only include tasks that are in groups of which this user is a member:
    if not request.user.is_superuser:
        found_tasks = found_tasks.filter(task_list__group__in=request.user.groups.all())

    context = {"query_string": query_string, "found_tasks": found_tasks}
    return render(request, "todo/search_results.html", context)
