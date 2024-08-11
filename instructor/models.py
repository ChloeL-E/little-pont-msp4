from django.db import models

# Create your models here.
class Instructor(models.Model):
    """ 
    Instructor model to manage information about the different team members.
    Used as FK within the course model
    """

    instructor_name = models.CharField(max_length=50)
    bio_description = models.TextField()
    experience = models.TextField()
    speciality_age_group = models.CharField(max_length=50)

    def __str__(self):
        """
        Return the instructors name as its string representation.
        """
        return self.instructor_name
