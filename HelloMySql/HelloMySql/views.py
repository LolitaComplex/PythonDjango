from django.http import HttpResponse
from django.db import connection

def index(request):
    cursor = connection.cursor()
    try:
        cursor.execute("select * from user")
        # rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        print(cursor.description)
        print(cursor.fetchone())
        print(cursor.fetchmany(1))
        for x in range(cursor.rowcount):
            print(cursor.fetchone())

    finally:
        cursor.close()
    
    
    return HttpResponse("MySql练习的主页")