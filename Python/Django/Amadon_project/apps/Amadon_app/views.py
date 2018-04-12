from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'quantity' not in request.session:
        request.session['quantity'] = 0
    return render(request,"Amadon_app/amadon.html")

def purchase(request):
    product_id=request.POST['id']
    quantity = request.POST['quantity']
    for product in request.session['products']:
        if product['id'] == product_id:
            request.session['quantity'] += int(request.POST['quantity'])
            request.session['price'] = product['price']
            request.session['sum'] = float(request.session['quantity'])*float(request.session['price'])
            request.session['total'] += request.session['sum']
    return redirect ('/checkout')

def checkout(request):
    return render(request,"Amadon_app/checkout.html")











    # request.session['products'] = []
    # f={
    #     'id' : '1',
    #     'item' : 'Dojo Shirt',
    #     'price' : '19.99',
    # }
    # s={
    #     'id' : '2',
    #     'item' : 'Dojo Sweater',
    #     'price' : '29.99',
    # }
    # t={
    #     'id' : '3',
    #     'item' : 'Dojo Cup',
    #     'price' : '4.99',
    # }
    # y={
    #     'id' : '4',
    #     'item' : 'Algorithm Book',
    #     'price' : '49.99',
    # }
    # request.session['products'].append(f)
    # request.session['products'].append(s)
    # request.session['products'].append(t)
    # request.session['products'].append(y)
    # request.session.modified= True
    # print request.session['products']