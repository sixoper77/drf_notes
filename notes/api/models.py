from django.db import models


class Note(models.Model):
    name=models.CharField(max_length=255,blank=False,null=False)
    subtask=models.CharField(max_length=255,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Заметка'
        verbose_name_plural='Заметки'
        ordering=['-created_at']
         
    def __str__(self):
        return f'{self.name[:50]}-{self.created_at}'