from django.db import models

# Create your models here.
H="High"
L="Low"
A="Avarage"
c="Completed"
w="Work in Progress"
n="Not Started"
crik=[(H,"High"),(L,"Low"),(A,"Avarage")]
stat=[(c,"Completed"),(w,"Work in Progress"),(n,"Not Started")]
class todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=300)
    created_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    criticality=models.CharField(max_length=100,choices=crik)
    status=models.CharField(max_length=100,choices=stat)


    def __str__(self):
        return self.title
