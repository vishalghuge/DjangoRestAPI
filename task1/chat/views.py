from .models import Users
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http.response import JsonResponse


def createUser(request):
    try:
        userName = request.GET['username']
        userEmail = request.GET['email']
        userPass = request.GET['password']
        if(len(userName) < 3 or len(userEmail) < 3 or len(userPass) < 3):
            return JsonResponse({'status': False, "error": "Please enter Name , Email and password with more than 3 characters"})
        else:
            user = Users()
            user.name = userName
            user.email = userEmail
            user.password = userPass
            user.save()

            return JsonResponse({'status': True})
    except Exception as e:
        print(e)
        return JsonResponse({'status': False})


def showUser(request):
    try:
        users = Users.objects.all().values()
        return JsonResponse(list(users), safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'status': False})


def showUserPagination(request):
    try:
        data = Users.objects.all().values()
        users = Paginator(data, 2)
        print(users.page(2).object_list)
        return JsonResponse(list(users.page(1).object_list), safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'status': False})


def UserPaginationHTML(request):
    try:
        limit = 3
        status = True
        pusers = []

        try:
            current = int(request.GET['currentPage'])
        except:
            current = int(1)

        data = Users.objects.all().values()
        users = Paginator(data, limit)

        users_range = users.page_range
        if users_range.start <= current < users_range.stop:
            pusers = users.page(current).object_list
        else:
            status = False

        return render(request, 'index.html', {'status': status, 'data': list(pusers), 'page_range': users_range, 'current': current})
    except Exception as e:
        print(e)
        return JsonResponse({'status': False})


def updateUser(request):
    try:
        id = request.GET['id']
        username = request.GET['username']
        if(len(username) < 3):
            return JsonResponse({'status': False, "error": "Please enter Name with more than 3 characters"})
        else:
            Users.objects.filter(
                id=id).update(name=username)
            return JsonResponse({'status': True})

    except Exception as e:
        print(e)
        return JsonResponse({'status': False})


def deleteUser(request):
    try:
        id = request.GET['id']
        Users.objects.filter(id=id).delete()
        return JsonResponse({'status': True})

    except Exception as e:
        print(e)
        return JsonResponse({'status': False})


def loginUser(request):
    try:
        userEmail = request.GET['email']
        userPass = request.GET['password']
        exist = False
        exist = Users.objects.filter(
            email=userEmail).filter(password=userPass)
        if(exist):
            temp = True
        return JsonResponse({'exist': temp})
    except:
        return JsonResponse({'exist': False})
