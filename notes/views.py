from .models import Note

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def editor(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = Note.objects.all()

    if request.method == 'POST':
        noteid = int(request.POST.get('noteid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', 0)

        if noteid > 0:
            note = Note.objects.get(pk=noteid)
            note.title = title
            note.content = content
            # request.user.userNote.add(note)
            note.save()

            return redirect(f'editor/?noteid={noteid}')
        else:
            note = Note.objects.create(title=title, content=content)
            request.user.userNote.add(note)

            return redirect(f'editor/?noteid={note.id}')

    if noteid > 0:
        note = Note.objects.get(pk=noteid)
    else:
        note = ''
    context = {
        'noteid': noteid,
        'notes': notes,
        'note': note
    }
    if noteid > 0:
        if note in request.user.userNote.all():
            return render(request, 'editor.html', context)
        else:
            return render(request, 'notes/dashboard.html')
    else:
        return render(request, 'editor.html', context)

@login_required()
def delete_note(request, noteid):
    note = Note.objects.get(pk=noteid)
    note.delete()
    return redirect('/editor/?noteid=0')


def dashboard(request):
    return render(request, "notes/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "notes/register.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
