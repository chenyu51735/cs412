from django.db import models

# Create your models here.
class Voter(models.Model):

    # personal informations
    last_name = models.TextField()
    first_name = models.TextField()

    # information for residence address
    street_number = models.IntegerField()
    street_name = models.TextField()
    apartment_number = models.TextField(blank=True)
    zip_code = models.IntegerField()

    # date 
    dob = models.DateField()
    date_of_registration = models.DateField()

    party_affiliation = models.TextField()
    precinct_number = models.TextField()

    # These fields indicate whether or not a given voter participated in several recent elections
    v20state = models.TextField()
    v21town = models.TextField()
    v21primary = models.TextField()
    v22general = models.TextField()
    v23town = models.TextField()

    # how many of the past 5 elections the voter participated in
    voter_score = models.IntegerField()

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f'{self.first_name} {self.last_name} ({self.dob})'
    

def load_data():
    '''Function to load data records from CSV file into Django model instances.'''
    # delete existing records to prevent duplicates:
    Voter.objects.all().delete()
    
    filename = '/Users/chicchili/Desktop/newton_voters.csv'
    f = open(filename)
    f.readline()
    for line in f:
        fields = line.split(',')
       
        try:
            # create a new instance of Voter object with this record from CSV
            voter = Voter(last_name = fields[1],
                            first_name = fields[2],
                            street_number = fields[3],
                            street_name = fields[4],
                            apartment_number = fields[5],
                            zip_code = fields[6],
                            dob = fields[7],
                            date_of_registration = fields[8],
                            party_affiliation = fields[9],
                            precinct_number = fields[10],
                        
                            v20state = fields[11],
                            v21town = fields[12],
                            v21primary = fields[13],
                            v22general = fields[14],
                            v23town = fields[15],
                            voter_score = fields[16],
                        )
            voter.save() # commit to database
            print(f'Created voter: {voter}')
            
        except:
            print(f"Skipped: {fields}")
    
    print(f'Done. Created {len(Voter.objects.all())} Voters.')