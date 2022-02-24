#we can insert text in string using format

print('This is a string {}'.format("Inserted"))
#the numbering will start from 0

print('Once upon a time,\n there was {2} who used to come late to the school,\n the teacher used to scold him.\n His friend {1} used to save him from getting scolded,\nThey fought with {0} together'.format('Ram','Shayam','Tarun'))
v = "this is a fine line b/w git and me"
print(v)

# alternate way
print('Once upon a time,\n there was {a} who used to come late to the school,\n the teacher used to scold him.\n His friend {b} used to save him from getting scolded,\nThey fought with {c} together'.format(a='Ram',b='Shayam',c='Tarun'))


