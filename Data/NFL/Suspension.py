import csv

class Suspension(object):
    def __init__(self, mylist = None):
        #Pass the list that was read
        self.mylist = mylist
        self.team_dict = {}
        self.categories_dict = {}
        self.years_dict = {}
        self.parse_list(mylist)


    def __str__(self):
        pass

#name,team,games,category,desc.,year,source

    def parse_list(self, mylist):
        if mylist is None:
            return None
        for row in mylist:
            if row[1] in self.team_dict:
                self.team_dict[row[1]].append([row])

    #Top n teams with suspensions added
    def n_most_suspensions_by_team(self, n=3):
        #check if n is int

    #Top n categories of suspensions 
    def n_categories_of_suspensions(self, n=3):
        #check if n is int
    
    #Top n years of suspensions
    def n_most_years_by_suspension(self, n=3):
        #check if n is int


try:
    with open("nfl-suspensions-data.csv", "rb") as f:
        reader = csv.reader(f)
        mylist = list(reader)

    suspensions = Suspension(mylist[1:])
except Exception as exc:
    print (str(exc))

