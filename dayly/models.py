from django.db import models


class techProcess(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('name',)
        def __str__(self):
         return self.name

class tools(models.Model):
        name = models.CharField(max_length=100, db_index=True)
        class Meta :
            ordering = ('name',)
            def __str__(self):
                return self.name

#class dayly_task (models.Model):
   # name = models.CharField(max_length=100, db_index=True)
   # date = models.DateField()
   # N_tech = models.IntegerField()
   # N_worker = models.IntegerField()

   # class Meta:
       # ordering = ('name',)
        #def __str__(self):


