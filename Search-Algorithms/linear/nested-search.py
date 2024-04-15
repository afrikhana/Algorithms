def nested_search(values, name, points):
    v = len(values)
    for i in range(v):
        if name and points == values[i]:
            return values[i]
    return 'Name nor point dont exist'
values = [
            ['Brian',13],
            ['Titus',15],
            ['sherry',15],
            ['Peter',18],
            ['Gerald',20],
            ['Mary',19]
            ]
name = input('Enter name:')
points = input('Enter Points:')
result = nested_search(values,name,points)
print(f'')    