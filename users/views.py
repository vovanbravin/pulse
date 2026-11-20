from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth import login
from django.urls import reverse_lazy
# Create your views here.


class SignUpView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
    


    


