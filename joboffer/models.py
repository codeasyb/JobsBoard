from django.db import models

class JobOffer(models.Model):
    
    company_name = models.CharField(max_length=60)
    # company_email = models.CharField(max_length=60)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=60)
    # job_description = models.CharField(max_length=120)
    job_description = models.TextField()
    # salary = models.FloatField()
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        # return f"{self.company_name} {self.job_title}"
        return self.company_name