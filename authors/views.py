
from .models import Author

from django.views import generic
from .forms import AuthorForm


class HomeView(generic.ListView):
    model = Author
    template_name = 'authors/home.html'
    context_object_name = 'authors'

    def get_queryset(self):
        fields = {'full_name': 'full_name__icontains'}
        kwargs = {fields[name]: value for name, value in self.request.GET.items() if name in fields and value}
        return self.model.objects.filter(**kwargs) if kwargs else self.model.objects.all()


class CreateView(generic.CreateView):
    form_class = AuthorForm
    template_name = 'authors/create.html'
