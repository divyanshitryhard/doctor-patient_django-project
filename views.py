from django.shortcuts import render
import mysql.connector as sql

fn = ''
ln = ''
s = ''
em = ''
pwd = ''
occ=''


# Create your views here.
def signup(request):
    global fn, ln, s, em, pwd,occ
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Disha@12", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                s = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
            if key == "occupation":
                occ = value

        c = "insert into users Values('{}','{}','{}','{}','{}','{}')".format(fn, ln, s, em, pwd, occ)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_page.html')
