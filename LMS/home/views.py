from django.shortcuts import render,redirect,get_object_or_404
from .models import Book,book_issue
from register.models import student_master
from django.db import IntegrityError
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def ahome(request):
    issues = book_issue.objects.all()
    return render(request,"ahome.html",{'issues':issues})

def shome(request):
    name=request.session.get('name')
    issues = book_issue.objects.all()
    return render(request, "shome.html", {'name':name,'issued_books': issues})

def book_management(request):
    if request.method == "POST":
        isbn_no = request.POST.get("isbn_no")
        book_name = request.POST.get("book_name")
        author = request.POST.get("author")

        # Check if the book already exists
        book = Book.objects.filter(isbn_no=isbn_no).first()

        if book:
            # Update existing book details
            book.book_name = book_name
            book.author = author
            book.save()
        else:
            # Add new book
            try:
                Book.objects.create(book_name=book_name, author=author, isbn_no=isbn_no)
            except IntegrityError:
                # Handle the case where the ISBN number is not unique
                return render(request, 'books.html', {
                    'data': Book.objects.all(),
                    'error_message': 'A book with this ISBN number already exists.'
                })

        return redirect('books')
        
    data = Book.objects.all()
    return render(request, 'books.html', {'data': data})

def delete_book(request, isbn_no):
    book = get_object_or_404(Book, pk=isbn_no)
    book.delete()
    return redirect('books')

def books_avail(request):
    Books = Book.objects.all()
    return render(request, 'books_avail.html', {'book': Books})

def issue_book(request):
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        author = request.POST.get("author")
        isbn_no = request.POST.get("isbn_no")

        # Check if the book is available in the Book model
        try:
            book = Book.objects.get(book_name=book_name, author=author, isbn_no=isbn_no)
        except Book.DoesNotExist:
            # Book does not exist
            return render(request, "issue_book.html", {"error": "Book not available for issuance."})

        # If book exists, create a new book issue record
        ob = book_issue.objects.create(book_name=book_name, author=author, isbn_no=isbn_no)
        ob.save()
        
        return render(request, "issue_book.html", {"success": "Book issued successfully!"})
    return render(request, "issue_book.html")

def issue_list(request):
    # Retrieve all book issues from the database
    issues = book_issue.objects.all()

    # Check if the request is POST for approving issues
    if request.method == "POST":
        issue_id = request.POST.get('issue_id')
        action = request.POST.get('action')

        if issue_id and action:
            try:
                issue = book_issue.objects.get(id=issue_id)
                if action == 'approve':
                    issue.approve = 1
                elif action == 'decline':
                    issue.approve = 2
                else:
                    return HttpResponse("Invalid action", status=400)
                
                issue.save()
            except book_issue.DoesNotExist:
                return HttpResponse("Issue not found", status=404)

            return redirect('issue_list')  # Redirect to avoid form resubmission issues

    # Render the issue list template with issues
    return render(request, "book_issue_list.html", {"issues": issues})