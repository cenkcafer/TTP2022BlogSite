import profile
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from .models import Blog
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
#function definition to render the landing page
def base(request):
    return render(request, 'blog/base.html')
#function definition to render the blog section as part of the landing page
def all_blogs(request):
    #blog_count = Blog.objects.count
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
#function to render and reveal the specific blog on a separate page
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
#function definiton for POST request for the contact page
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'blog/index.html')
    form = ContactForm()
    return render(request, 'blog/contact.html', {'form' : form})
#profiles dictionary for group members to be accessed within the about page
profiles = [
    #management
    {'name':'Ege Kacmaz',
     'image':'',
    'gitlink':'https://github.com/iamege',
    'gender':'female'
     },
    {'name':'Syeda Kazmi',
     'image':'',
    'gitlink':'https://github.com/iamege',
    'gender':'female'
     },
    {'name':'Hilal Avci',
     'image':'',
    'gitlink':'https://github.com/hilal212',
    'gender':'female'
     },
    #back-end
    {'name':'Michael Janus',
     'image':'',
    'gitlink':'https://github.com/bluemike61',
     },
    {'name':'Humayun Ahmed',
     'image':'',
    'gitlink':'https://github.com/ahmed-humayun',
     },
    {'name':'Ankit Kafle',
     'image':'',
    'gitlink':'https://github.com/ankitkafle1',
     },
    #front-end
    {'name':'Robert Quartey',
     'image':'',
    'gitlink':'https://github.com/robertquartey7',
     },
    {'name':'Cenk Cafer',
     'image':'',
    'gitlink':'https://github.com/cenkcafer',
     },
    {'name':'Michael Coleman',
     'image':'',
    'gitlink':'https://github.com/mic4x',
     },
    {'name':'Sheikh Ahmed',
     'image':'',
    'gitlink':'https://github.com/SHEIKHIA',
     },
    {'name':'Chistopher Ortega',
     'image':'',
    'gitlink':'https://github.com/chrisortega1928',
     },
    {'name':'Gabriel Tejadaa',
     'image':'',
    'gitlink':'https://github.com/gabrielt1101',
     },
    {'name':'Jeryel Blanco',
     'image':'',
    'gitlink':'',
     },
    {'name':'Lamarana Diallo',
     'image':'',
    'gitlink':'https://github.com/diallolamarana',
     },
    {'name':'Md Redoy',
     'image':'',
    'gitlink':'https://github.com/MdXRedoy',
     },
    {'name':'Nanami Inaba',
     'image':'',
    'gitlink':'https://github.com/mc5rgspider',
    'gender':'female'
     },
]
\
#function defintion to return the about page with the profiles
def about(request):
    return render(request, 'blog/about.html', {'cards':profiles})
