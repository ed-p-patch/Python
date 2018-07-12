d = {'Name': 'Patrick', 'Age': 28, 'Country': 'United States', 'Prog_pref': 'JavaScript'}

def introduction(dict):
    print "My name is", dict['Name']
    print "My age is", dict['Age']
    print "My country of origin is", dict['Country']
    print "My favorite language", dict['Prog_pref']
    
introduction(d)