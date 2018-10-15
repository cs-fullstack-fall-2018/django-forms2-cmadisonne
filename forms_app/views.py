from django.shortcuts import render, redirect, get_object_or_404
from forms_app import forms
from .forms import Form
from django.utils import timezone
from .models import FormModel


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)

def form_name_view(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.name = form.cleaned_data['name']
            recipe.recipe = form.cleaned_data['recipe']
            recipe.timeCook = form.cleaned_data['timeCook']
            recipe.dateCreated = timezone.now()
            recipe.save()
            return redirect('index', pk=recipe.pk)
    else:
        form = Form()
    return render(request,'forms_app/formPage.html', {'form': form})

def recipe_edit(request, pk):
    form = get_object_or_404(FormModel, pk=pk)
    if request.method == "GET":
        form = Form(request.GET)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = form.cleaned_data['name']
            form.recipe = form.cleaned_data['recipe']
            form.timeCook = form.cleaned_data['timeCook']
            form.dateCreated = timezone.now()
            form.save()
            return redirect('index', pk=form.pk)
    else:
        form = Form()
    return render(request,'forms_app/formPage.html', {'form': form})

