from django.shortcuts import render

# Create your views here.

from django.views import View

# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return render(request=request, template_name='hello_world.html')