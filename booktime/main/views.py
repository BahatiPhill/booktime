from django.shortcuts import render
from django.views.generic.edit import FormView
from main import forms
# Create your views here.

class ContactUsView(FormView):

    template_name =  'contact_us.html'
    form_class = forms.ContactForm
    success_url = '/'

    def form_valid(self, form):
        print('Am i working')
        form.send_mail()
        return super().form_valid(form)

'''
def contact_us(request):

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            return HttpResponseRedirect('/')

    else:
        form = forms.ContactForm()

    return render(request, 'contact_us.html', {'form':form})
'''