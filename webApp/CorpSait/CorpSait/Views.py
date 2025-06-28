from django.http import HttpResponse, JsonResponse
from .models import Employee, Team
from django.shortcuts import render, redirect
from .forms import ClientForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied

def aboba(request):
    return HttpResponse("""<img src = './notOurServers.jpg'> <h1>Это не сервера нашей компании</h1>""")


def employee_info(request):
    return HttpResponse("""<h1>*полезная информация для сотрудников...*</h1>""")


# def employee_detail(request, employee_id):
#     res = f'<h1>employe id: {employee_id}</h1>' #ЗДЕСЬ ПРОДОЛЖИТЬ
#     return HttpResponse(res)


def get_employes(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(name__icontains=query)
    else:
        employees = Employee.objects.all()
    return render(request, 'employeeList.html', {'employees': employees})


def search_Employees(request):
    query = request.GET.get('q', "")
    team_filter = request.GET.get('team', "")
    print(request.GET)
    employees = Employee.objects.all()
    if query:
        employees = Employee.objects.filter(name__icontains=query)
    if team_filter:
        employees = employees.filter(team__id=team_filter)
    teams = Team.objects.all()
    return render(request, "employeeList.html", {'employees': employees, 'teams': teams, 'selected_team': team_filter})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aboba')
    else:
        form = ClientForm()
        return render(request, 'formClient.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("aboba")
    return render(request, 'Login.html')


@login_required
@permission_required(perm="CorpSait.Views.permission_denied" ,raise_exception=True)
def employee_detail(request, employee_id):
    # res = f'<h1>employe id: {employee_id}</h1>'
    
    employee = Employee.objects.get(id=employee_id)
    raise PermissionDenied("test na prava")
    return render(request, "index.html", {'employee':employee})
#ЗДЕСЬ ПРОДОЛЖИТЬ


def permission_denied(request, exception):
    return render(request, '403.html', status=403)


def user_logout(request):
    logout(request)
    return redirect("login")
    # employees = Employee.objects.all()
    # data = {}
    # for emp in employees:
    #     data["name"] = emp.name
    #     data["age"] = emp.age
    #     data["zarplata"] = emp.zarplata
    #     data["position"] = emp.position
    # return JsonResponse(data, json_dumps_params={"ensure_ascii":False})
