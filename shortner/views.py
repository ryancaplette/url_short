from django.shortcuts import render, redirect
from .models import UrlMapping
from .forms import UrlForm
from .utils.path_generator import ShortPath
from django.http import Http404

def shortner(request):
    form = UrlForm(request.POST)
    short_path = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            short_path = ShortPath().gen_path()
            NewUrl.short_path = short_path
            NewUrl.save()
        else:
            form = UrlForm()
            q = UrlMapping.objects.get(original_url=request.POST.get('original_url'))
            short_path = q.short_path

    return render(request, 'shortner/index.html', {'form': form, 'short_path': short_path})


def goto(request, short_path):
    try:
        print('short_path')
        print(short_path)
        goto = UrlMapping.objects.get(short_path=short_path)
        return redirect(goto.original_url)
    except:
        raise Http404("Short URL Not Found.")

    