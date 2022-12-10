## First way
year = 2016
event = "Referendum"
print(f"Results of the {year} {event}")

## str.format()
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print("{:9} YES votes {:2.2%}".format(yes_votes, percentage))

## str() or repr() statement
animals = "eels"
print(f"My hovercraft is full of {animals}")
print(f"My hovercraft is full of {animals!r}")

bugs = "roaches"
count = 13
area = "living room"
print(f"Debugging {bugs=} {count=} {area=}")

## string format
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))