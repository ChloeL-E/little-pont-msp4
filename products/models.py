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

    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    age_group = models.CharField(max_length=11, choices=AGE_GROUP)
    # instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Return the course name as its string representation.
        """
        return self.name
