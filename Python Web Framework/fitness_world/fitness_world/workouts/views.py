from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from fitness_world.common.forms import CommentCreateForm
from fitness_world.common.views import page_not_found
from fitness_world.core.core_utils import user_permissions
from fitness_world.core.photo_utils import photo_likes_count, photo_is_liked_by_user
from fitness_world.workouts.forms import WorkoutCreateForm, WorkoutEditForm, DeleteWorkoutForm
from fitness_world.workouts.models import Workout

UserModel = get_user_model()


class CreateWorkoutView(LoginRequiredMixin, generic.CreateView):
    template_name = 'workouts/workout-add-page.html'
    form_class = WorkoutCreateForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.user = self.request.user

        return super().form_valid(form)


class EditWorkoutView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'workouts/workout-edit-page.html'
    model = Workout
    form_class = WorkoutEditForm

    def get_success_url(self):
        return reverse_lazy('details workout', kwargs={
            'username': self.object.user.username,
            'slug': self.object.slug,
        })


class DetailsWorkoutView(LoginRequiredMixin, generic.DetailView):
    template_name = 'workouts/workout-details-page.html'
    model = Workout

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        workout_photos = [photo_likes_count(photo) for photo in self.object.photo_set.all()]
        workout_photos = [photo_is_liked_by_user(self.request, photo) for photo in workout_photos]

        context['is_owner'] = self.request.user == self.object.user
        context['workout_photos'] = workout_photos
        context['workout_tags_count'] = self.object.photo_set.count()
        context['user'] = self.request.user
        context['comment_form'] = CommentCreateForm()

        return context


@login_required
def delete_workout(request, username, slug):
    workout = Workout.objects.filter(user__username=username, slug=slug).get()

    if not user_permissions(request, workout.user):
        return page_not_found(request)

    if request.method == 'GET':
        form = DeleteWorkoutForm(instance=workout)
    else:
        form = DeleteWorkoutForm(request.POST, instance=workout)

        if form.is_valid():
            form.save()
            return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
        'username': username,
        'slug': slug,
    }

    return render(request, 'workouts/workout-delete-page.html', context)
