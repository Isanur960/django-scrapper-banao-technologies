from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import ProductDB
from .scrapper import scrape
import json

# Create your views here.


def dlt():
    ProductDB.objects.all().delete()


class Index(View):
    def get(self, request):
        items = ProductDB.objects.all().order_by('rating').reverse()[:5]
        return render(request, "index.html", {'items': items})

    def post(self, request):
        req = request.POST.get('name')
        if req == None or req == "" or req == " " :
            return redirect('/')
        item = ProductDB.objects.filter(
            name__icontains=str(req)).order_by('rating').reverse()
        print(len(item))
        if len(item)==0:
            return render(request, "index.html")
        else:
            return render(request, "index.html", {'items': item})


class Detail(View):
    def get(self, request):
        id = request.GET.get('id')
        item = ProductDB.objects.get(id=id)
        data = str(item.detail)
        data = eval(data)
        return render(request, 'detail.html', {'item': item})


class Scrape_req(View):
    def get(self, request):
        dlt()
        datas = scrape()
        for data in datas:
            name = data['name']
            link = data['link']
            img = data['img']
            price = data['price']
            features = data['features']
            rating = data['rating']

            if True:
                product = ProductDB(name=name, link=link,
                                    img=img, price=price, detail=str(features), rating= rating)
                messages.add_message(request, messages.INFO,
                                     'Successfully scrapped')
                product.save()
            else:
                messages.add_message(
                    request, messages.ERROR, 'Scrapping Failed')
                pass
        return redirect('/')
