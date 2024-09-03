from django.db import models

# Create your models here.
class Instructor(models.Model):
    """ 
    Instructor model to manage information about the different team members.
    Used as FK within the course model
    """
    instructor_name = models.CharField(max_length=5, null=False, blank=False)
    bio_description = models.TextField(null=False, blank=False)
    experience = models.TextField(null=False, blank=False)
    speciality_age_group = models.CharField(max_length=50, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Return the instructors name as its string representation.
        """
        return f"{self.instructor_name}"
