from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from .models import Blog
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.




def base(request):
    return render(request, 'blog/base.html')



def all_blogs(request):
    #blog_count = Blog.objects.count
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

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

