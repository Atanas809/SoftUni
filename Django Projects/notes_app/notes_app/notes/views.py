from django.shortcuts import render, redirect

from notes_app.notes.forms import NoteCreateForm, NoteEditForm, NoteDeleteForm
from notes_app.notes.models import Note


# Create your views here.

def add_note(request):
    if request.method == 'GET':
        form = NoteCreateForm()
    else:
        form = NoteCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'notes/note-create.html', context)


def edit_note(request, note_id):
    note = Note.objects.filter(pk=note_id).get()

    if request.method == 'GET':
        form = NoteEditForm(instance=note)
    else:
        form = NoteEditForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note_id': note_id,
    }

    return render(request, 'notes/note-edit.html', context)


def delete_note(request, note_id):
    note = Note.objects.filter(pk=note_id).get()

    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)
    else:
        form = NoteDeleteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note_id': note_id,
    }

    return render(request, 'notes/note-delete.html', context)


def details_note(request, note_id):
    note = Note.objects.filter(pk=note_id).get()

    context = {
        'note': note,
    }

    return render(request, 'notes/note-details.html', context)
