from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM semsite_author")
    row = cursor.fetchall()

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM semsite_author")
    row = cursor.fetchall()
    print(row)
    cursor.execute("UPDATE semsite_author SET slug = %s WHERE first_name = %s AND last_name = %s", ['b', 'Aaoeu', 'aoeiaoueao'])
    cursor.execute("SELECT * FROM semsite_author")
    row = cursor.fetchall()
    print(row)

