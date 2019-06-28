from todo.models import Task


def add_variable_to_context(request):

	if request.user.is_authenticated:
		if request.user.is_superuser:
			all_tasks = Task.objects.all().count()
			all_tasks_completed = Task.objects.filter(completed=1).count()

			try:
				all_tasks_percentage = (all_tasks_completed * 100) / all_tasks
			except ZeroDivisionError:
				all_tasks_percentage = 0

			return {
				'all_tasks': all_tasks,
				'all_tasks_completed': all_tasks_completed,
				'all_tasks_percentage': all_tasks_percentage,
			}
		else:
			all_tasks = Task.objects.filter(assigned_to=request.user).count()
			all_tasks_completed = Task.objects.filter(assigned_to=request.user, completed=1).count()

			try:
				all_tasks_percentage = (all_tasks_completed * 100) / all_tasks
			except ZeroDivisionError:
				all_tasks_percentage = 0

			return {
				'all_tasks': all_tasks,
				'all_tasks_completed': all_tasks_completed,
				'all_tasks_percentage': all_tasks_percentage,
			}
	else:
		return {
			'': ''
		}
