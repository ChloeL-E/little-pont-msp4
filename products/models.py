from django.db import models


class Course(models.Model):
    """
    Course model for managing information about the various courses.
    Includes the age-group and instructor.
    """
    AGE_GROUP = (
        ('Babies', 'Babies'),
        ('Toddler', 'Toddler'),
        ('Preschool', 'Preschool'),
        ('Early Years', 'Early Years'),
    )

    instructor = models.ForeignKey('instructor.Instructor', on_delete=models.CASCADE, related_name='courses', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    age_group = models.CharField(max_length=11, choices=AGE_GROUP)
    

    def __str__(self):
        """
        Return the course name as its string representation.
        """
        return f"{self.name} ({self.age_group})"
