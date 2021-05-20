from django.shortcuts import render,redirect
from django.http import HttpResponse

from book.models import Book

# Create your views here.
def homepage(request):  # view - function based View(FBV)   # request -- http request   # user defined func
    all_books = Book.objects.all()
    # print(all_books)
    return render(request, template_name='home.html', context={"books": all_books})

def save_book(request):
    print("in save book")
    if request.POST.get("id"):
        book_obj=Book.objects.get(id=request.POST.get("id"))
        b_name=request.POST.get("name")
        b_author=request.POST.get("Author")
        b_price=request.POST.get("Quantity")
        b_qty=request.POST.get("Price")
        b_publish=request.POST.get("Publish")
        book_obj.name=b_name
        book_obj.Author=b_author
        book_obj.Quantity=b_price
        book_obj.Price=b_qty
        if b_publish=="on":
            flag=True
        else:
            flag=False
        book_obj.is_published=flag
        book_obj.save()
        return redirect('welcome')
        
    else:    
        print(request.POST) #POST /save-book/
        b_name=request.POST.get("name")
        b_author=request.POST.get("Author")
        b_price=request.POST.get("Quantity")
        b_qty=request.POST.get("Price")
        b_publish=request.POST.get("Publish")

    # print(b_name,b_author,b_price,b_qty,b_publish)
        if b_publish=="on":
            flag=True
        else:
            flag=False

    
        b=Book(name=b_name,author=b_author,qty=b_price,price=b_qty,is_published=flag)
        b.save()
        return redirect('welcome')

def edit_book(request, id):   # pk -- primary key
    try:
        print("in edi")
        book_obj = Book.objects.get(id=id)
        
    except Exception:
        msg=f"NO BOOK FOUND FOR ID:{id}"
        return HttpResponse(msg)   
    all_books = Book.objects.all()
    return render(request, template_name='home.html', context={"book": book_obj, "books": all_books})

def delete_book(request, pk):
    print("in delete")
    book_obj = Book.objects.get(id=pk)
    book_obj.delete()
    return redirect('welcome')

