students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# Part 1
def print_students(arr):
    for x in range(0, len(arr)):
        print arr[x]['first_name'], arr[x]['last_name']
print_students(students)
# Part 2
def print_users(dict):
    print "Students"
    s = dict['Students']
    sl = len(s)
    for x in range(0, sl):
        length = len(s[x]['first_name']) + len(s[x]['last_name'])
        print x+1, "-", s[x]['first_name'].upper(), s[x]['last_name'].upper(), "-", length
    print "Instructors"
    i = dict['Instructors']
    il = len(i)
    for x in range(0, il):
        length = len(i[x]['first_name']) + len(i[x]['last_name'])
        print x+1, "-", i[x]['first_name'].upper(), i[x]['last_name'].upper(), "-", length
print_users(users)