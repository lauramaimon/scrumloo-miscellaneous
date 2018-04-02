from django.db import models

class Voter(models.Model):
    voter_number = models.IntegerField()
    voter_status = models.CharField(max_length=10)
    date_registered = models.CharField(max_length=10)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    locality = models.CharField(max_length=50)
    precinct = models.CharField(max_length=20)
    precinct_id = models.IntegerField()
    voted = models.BooleanField(default=0)

    def __str__(self):
        return str(self.voter_number) + ", " + self.last_name + ", " + self.first_name
    def change_voted(self, a):
        self.voted = bool(a)
    
