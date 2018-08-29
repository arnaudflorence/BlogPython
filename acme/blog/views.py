from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
#from .mocks import Post

from blog.forms.forms import UsersForms, CommentForm
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
    post = get_object_or_404(Post, pk=id)
    try:
        posts = Post.objects.get(pk=id)
    #--------------------afficher un com--------------------
        com = Comment.objects.filter(post=posts.id).order_by('-created_at')
    #--------------------ecrire un com--------------------
        if request.method == 'POST':
            comment_form = CommentForm(request.POST or None)
            if comment_form.is_valid():
                content = request.POST.get('content')
                comment = Comment.objects.create(post=post, user=request.user, content=content)
                comment.save()
                #return HttpResponseRedirect(post.get_absolute_url())
                return HttpResponseRedirect(reverse('blog:index'))



        else:
            comment_form = CommentForm()

        context = {
            "comments":com,
            'toto' : posts,
            "comment_form" : comment_form,
        }

    except Post.DoesNotExist:
        raise Http404('Sorry, post #{} not found.'.format(id))

    return render(request, 'blog/show.html', context)

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
