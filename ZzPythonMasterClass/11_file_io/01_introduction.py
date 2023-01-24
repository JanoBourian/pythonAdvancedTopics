import io

# Abrir el documento
my_file = open('test.txt')
print(my_file)

## FIle is open
print(my_file.read())
my_file.seek(10)
print(my_file.read())

my_file.close()


my_other = open('data.csv')
print(my_other)
print(my_other.readline())
print(my_other.readlines())  # separa por comas
my_other.close()
