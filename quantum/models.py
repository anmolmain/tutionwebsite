from django.db import models

class LowerSchoolStudent(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    CLASS_CHOICES = [
        ('nursery', 'Nursery'),
        ('preK', 'Pre-K'),
        ('firstGrade', 'First Grade'),
        ('secondGrade', 'Second Grade'),
        ('thirdGrade', 'Third Grade'),
    ]

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    currentClass = models.CharField(max_length=20, choices=CLASS_CHOICES)
    parentName = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    emergencyContact = models.CharField(max_length=15)
    subjectsRequired = models.TextField()
    interests = models.TextField(blank=True, null=True)
    expectations = models.TextField(blank=True, null=True)

class MiddleSchoolStudent(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    CLASS_CHOICES = [
        ('fourthGrade', 'Fourth Grade'),
        ('fifthGrade', 'Fifth Grade'),
        ('sixthGrade', 'Sixth Grade'),
        ('seventhGrade', 'Seventh Grade'),
        ('eighthGrade', 'Eighth Grade'),
    ]

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    currentClass = models.CharField(max_length=20, choices=CLASS_CHOICES)
    parentName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    emergencyContact = models.CharField(max_length=15)
    subjectsRequired = models.TextField()
    academicGoals = models.TextField()
    interests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class HighSchoolStudent(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    CLASS_CHOICES = [
        ('ninthGrade', 'Ninth Grade'),
        ('tenthGrade', 'Tenth Grade'),
        ('eleventhGrade', '10+1 Grade'),
        ('twelfthGrade', '10+2 Grade'),
        ('spokenEnglish', 'Spoken English'),
    ]

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    currentClass = models.CharField(max_length=20, choices=CLASS_CHOICES)
    parentName = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    emergencyContact = models.CharField(max_length=15)
    subjectsRequired = models.TextField()
    interests = models.TextField(blank=True, null=True)
    expectations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class HomePageContact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name    
