from users.models import image_db
def insert():
    for i in range(0,248):
        q = image_db(content = "test",title = str(i)+'.jpg')
        q.save()
def delete():
    image_db.objects.all().delete()
