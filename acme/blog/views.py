from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from .mocks import Post

from blog.forms.forms import UsersForms
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


from .models import Post
from .models import Comment

# Create your views here.

#------------------------------------------------liste Articles-----------------------------------------------------------

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'toto' : posts})


#------------------------------------------------details Articles-----------------------------------------------------------

def show(request, id):
    #post = get_object_or_404(Post, pk=id)
    try:
        posts = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404('Sorry, post #{} not found.'.format(id))
    return render(request, 'blog/show.html', {'toto' : posts})

#------------------------------------------------Liste des Commentaires-----------------------------------------------------------

# def index(request):
#     com = Comment.objects.all()
#     return render(request, 'blog/show.html', {'com' : com})

#------------------------------------------------ajouter Commentaires-----------------------------------------------------------



#------------------------------------------------login-----------------------------------------------------------

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            context["error"] = "ce n'est pas valide lol !"
            return render(request, "blog/login.html", context)
    else:
        return render(request, "blog/login.html", context)

#------------------------------------------------logout-----------------------------------------------------------

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))
#------------------------------------------------inscription-----------------------------------------------------------
class UserFormView(View):
    form_class = UsersForms
    template_name = 'blog/registration_form.html'
    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returne User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('blog/index.html')

        return render(request, self.template_name, {'form': form})
