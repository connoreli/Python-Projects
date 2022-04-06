

# parent class
class Team:
    league = 'NBA'
    name = 'Unknown'
    number_of_players = 15
    coach = 'Unknown'
    record = 'Unknown'

    def information(self):
        msg = '\nLeague: {}\nName: {}\nNumber of Players: {}\nCoach: {}\nRecord: {}'
        return msg
    
# child class no.1
class Mavs:
    name = 'Dallas Mavericks'
    coach = 'Jason Kidd'
    record = '50-30'

    def summary(self):
        msg = '\nThe Mavs are having a great year and are looking to enter the playoffs in the No.3 seed in the Western Conference!'
        return msg

#child class no.2
class Lakers:
    name = 'Los Angeles Lakers'
    coach = 'Frank Vogel'
    record = '36-44'

    def sad_summary(self):
        msg = '\nThe Lakers had an awful year and did not qualify for the NBA playoffs.'
        return msg


if __name__ == '__main__':
    mavs = Mavs()
    print(mavs.summary())
    
    lakers = Lakers()
    print(lakers.sad_summary())