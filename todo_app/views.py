from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *

from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import RegisterForm, LoginForm, ProfileForm, PostAdminForm, ContactForm, UserSetting, SettingsForm

User = get_user_model()


def common_data():
    context = {}
    context["title"] = Main_title.objects.last()
    context["menu"] = Menu.objects.all()
    context["icon"] = icon.objects.all()
    return context


def home(request):
    context = {}
    context["title"] = Main_title.objects.last()
    context["menu"] = Menu.objects.all()
    context["main"] = Main.objects.all()
    context["txt"] = TXT.objects.all()
    context["icon"] = icon.objects.all()
    context["article"] = Article.objects.all()
    return render(request, "index.html", context)


def about(request):
    context = common_data()
    context["menu"] = Menu.objects.all()
    context["about_title"] = About_Me.objects.all().last()

    return render(request, "about.html", context)


def contact(request):
    context = common_data()
    context["contact_me"] = Contact_me.objects.all().last()

    context["contact_form"] = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Sorgunuz Ugurla gonderildi!"
            )
            return redirect("contact")
        else:
            context["contact_form"] = ContactForm()

    return render(request, "contact.html", context)


def register(request):
    context = common_data()
    context["register"] = Register_User.objects.all().last()
    context["form"] = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST.get("password"))
            user.save()
            Profil.objects.create(
                user=user,
                profile_image=request.FILES.get("profile_image"),
                background_image=request.FILES.get("background_image"),
                name=user.first_name,
                surname=user.last_name,
            )
            messages.success(
                request, "Qeydiyyat ugurla tamamlandi!"
            )

            return redirect("login-view")
        else:
            context["form"] = form

    return render(request, "register.html", context)


def login_view(request):
    if not request.user.is_authenticated:
        context = common_data()
        context["loginform"] = LoginForm()
        context["login"] = Login_User.objects.all().last()
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)

                if user:
                    if user.is_active:
                        login(request, user)
                        return redirect("home")

                else:
                    messages.error(
                        request, "Username or Password inValid"
                    )
                    return redirect("login-view")
            else:
                return redirect("register-view")
        return render(request, "login.html", context)

    else:
        return redirect("home")


def logout_view(request):
    logout(request)
    return redirect("login-view")


def profile_view(request):
    context = {}
    context["detail"] = Profil.objects.filter(user=request.user)
    context["form"] = ProfileForm
    # print(request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profil)
        if form.is_valid():
            form.save()


        else:
            form = ProfileForm(instance=request.user.profil)
            context["form"] = form
    else:
        context["detail"] = Profil.objects.filter(user=request.user).last()

    return render(request, "profil.html", context)


def post_data(request):
    context = {}
    context = common_data()
    context["post"] = PostPage.objects.all().last()
    context["postform"] = PostAdminForm()
    if request.method == "POST":

        form = PostAdminForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()

            return redirect('home')
        else:
            context["postform"] = PostAdminForm()

    return render(request, "post.html", context)


def detail_user(request, id):
    context = common_data()
    news = Article.objects.filter(id=id).last()
    if news:
        context["text"] = news
        return render(request, "detail.html", context)

    else:
        return redirect("home")


def author_view(request, pk):
    context = common_data()
    objects = Article.objects.filter(user_id=pk)
    fullname = Profil.objects.filter(user_id=pk).last()
    context["fullname"] = fullname
    context["objects"] = objects
    return render(request, "author.html", context)


def dashboard(request):
    context = common_data()
    print(request.user)
    objects = Article.objects.filter(user=request.user)
    context["profil"] = objects
    fullname = Profil.objects.filter(user=request.user).last()
    context["fullname"] = fullname
    context["objects"] = objects

    return render(request, "dashboard.html", context)


def update_view(request, id):
    context = common_data()
    news = Article.objects.filter(id=id).last()
    context["update"] = UpdatePage.objects.all().last()
    if news:
        context["postform"] = PostAdminForm(
            instance=news
        )
        if request.method == "POST":
            form = PostAdminForm(request.POST, request.FILES, instance=news)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Ugurla deyishdi!"
                )
                return redirect("dashboard")
            else:
                context["postform"] = form

    return render(request, "post_edit.html", context)


def deleteview(request, id):
    context = common_data()
    news = Article.objects.filter(id=id).last()
    if news:
        news.delete()
        return redirect("dashboard")


def usersetting(request):
    context = common_data()
    if request.method == "POST":
        form = SettingsForm(request.POST, request.FILES, instance=request.user)
        context["settings"] = form
        if form.is_valid() and request.user.check_password(request.POST.get("password")):
            user = form.save()
            user.profil.about = form.cleaned_data.get("about")
            user.profil.profile_image = request.FILES.get("profile_image")
            user.profil.background_image = request.FILES.get("background_image")
            user.profil.save()
            return redirect("home")
        else:
            context["settings"] = form
    else:
        form = SettingsForm(instance=request.user, initial={
            "about": request.user.profil.about,
            "profile_image": request.user.profil.profile_image,
            "background_image": request.user.profil.background_image,
        })
        context["settings"] = form
    return render(request, "user-settings.html", context)
