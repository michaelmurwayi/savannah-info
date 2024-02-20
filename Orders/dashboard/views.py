from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import requests


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class ProductView(TemplateView):
    template_name = 'products.html'

    def get_context_data(self):
        api_url = 'http://127.0.0.1:8000/api/products/'  # Replace with your API endpoint
        try:
            context = {}
            response = requests.get(api_url)
            response.raise_for_status()  # Check for HTTP errors
            context["data"] = response.json()
            print(context)
            return context
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)



class OrdersView(TemplateView):
    template_name = 'orders.html'


    def post(self, request):
        return render(self.template_name)
