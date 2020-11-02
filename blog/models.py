from django.db import models


# Create your models here.

class BlogPost(models.Model) :

    title = models.CharField(max_length = 75, null = False)
    description = models.CharField(max_length = 200) 
    content = models.TextField()
    date_posted = models.DateField(auto_now = True) 


    def __str__(self) : 
        return self.title  + '| posted in : ' + str(self.date_posted)

    


