# from book.models import Book
from book.models import Book
# all data
# all_data=Book.objects.all()
# print(all_data)

#to run python file in django shell 
# exec(open('C:\\Users\\Tousif\\Desktop\\pythhon\\Django\\library\\book\\dbShell.py').read())
#execute above command in django shell


# for book in all_data:
#     print("details for ID ",book.id)
#     print("Book name ",book.name)
#     print("Book author",book.author)
#     print("Book price ",book.price)
#     print('Book quantity',book.qty)

# #do changes in all books
# for book in all_data:
#     book.qty=10
#     book.save()

# for i in all_data:
#     print(i.__dict__)


# to get specific values like only id,name etc
# all_data=Book.objects.all().values("id","name","qty")
# print(list(all_data))
# for i in all_data:
#     print(i)

#output
'''
{'id': 1, 'name': 'Alchemist', 'qty': 10}
{'id': 2, 'name': 'wings of fire', 'qty': 10}
{'id': 3, 'name': 'Zahir', 'qty': 10}
{'id': 4, 'name': 'IRON MAN', 'qty': 10}
'''


# to get data in list of tuples
# all_data= .values_list()
# for i in all_data:
#     print(i)
 #output
'''(1, 'Alchemist', 'paulo', 10, 500)
(2, 'wings of fire', 'APJ Abdul Kalam', 10, 400)
(3, 'Zahir', 'paulo', 10, 800)
(4, 'IRON MAN', 'Tony Stark', 10, 100)
'''
#__gt  greater than 
#__gte greater than or equal to
#__lt lower than 
#__lte lower than or equal to

# book1=Book.objects.filter(id__gt=2)
# for i in book1:
#     print(i)

# start with ...
#startswith
#endswith
# book1=Book.objects.filter(name__startswith='Z').values("id","name") #CASE SENSITIVE
# book1=Book.objects.filter(name__istartswith='z').values("id","name") #no case sensitive
# for i in book1:
#     print(i)

#order by
# b=Book.objects.all().order_by("name") # asseending
# b=Book.objects.all().order_by("-name") # dessending
# print(b)

#count
# b1=Book.objects.all().count()
# print(b1)
# output 4

#specific data accourding tfo count
# b=Book.objects.all()[3]
# print(b)
# b1=Book.objects.all().count()
# b=Book.objects.all()[b1]
#to fetch last value in database use count opearation
# print(b)
# b=Book.objects.all()[0:2] # renge of data
# print(b)

# when we have list of ID's
# I=[i for i in range(1,4)]
# b2=Book.objects.filter(id__in=I)
# print(b2)
# bulk create

# b1=Book.objects.bulk_create([Book(name="Spider man",author="parker",qty=7,price=1345),
# Book(name="captain america",author="Stive",qty=8,price=134),
# Book(name="HULK",author="prof.Banner",qty=10,price=1378)
# ])

