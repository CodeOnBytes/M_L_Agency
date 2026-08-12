from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def services(request):
    return render(request, 'core/services.html')


# def elements(request):
#     return render(request, 'core/elements.html')


# def blog(request):
#     return render(request, 'core/blog.html')


# def blog_details(request):
#     return render(request, 'core/blog_details.html')


def contact(request):
    if request.method == 'POST':
        # TODO: validate request.POST, send email / save to DB
        messages.success(request, "Thanks! We'll be in touch soon.")
        return redirect('contact')
    return render(request, 'core/contact.html')

def apply(request):
    if request.method == 'POST':
        # TODO: validate request.POST + request.FILES['cv'], save application
        messages.success(request, "Application received — we'll review it shortly.")
        return redirect('apply')
    return render(request, 'core/apply.html')