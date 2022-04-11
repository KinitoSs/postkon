from django.shortcuts import get_object_or_404, render
from .models import User, Post
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'postkon_webapp/index.html')


# def show_all_users(request):
#     users = User.objects.all()
#     return render(request, 'postkon_webapp/all_users.html', context={
#         'users': users
#     })

def search_users(request, search_input):
    search_input = "чины"
    username_filter = User.objects.filter(username__icontains=search_input)
    first_name_filter = User.objects.filter(first_name__icontains=search_input)
    last_name_filter = User.objects.filter(last_name__icontains=search_input)
    result = username_filter.union(first_name_filter).union(last_name_filter)


def users_view(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        users = User.objects.filter(username__icontains=url_parameter)
    else:
        users = User.objects.all()

    ctx["users"] = users
    does_req_accept_json = request.accepts("application/json")
    is_ajax_request = request.headers.get(
        "x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    if is_ajax_request:

        html = render_to_string(
            template_name="postkon_webapp/all_users_search.html", context={"users": users}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "postkon_webapp/all_users.html", context=ctx)


def show_one_user(request, slug_user: str):
    user = get_object_or_404(User, slug=slug_user)
    posts = Post.objects.filter(user=user)
    return render(request, 'postkon_webapp/one_user.html', context={
        'user': user,
        'posts': posts,
    })
