file = open("forcast.txt", 'r')
forcast = [float(num) for num in file.read().replace('\n', ' ').split()]
print(len(forcast))

file2 = open("actual.txt", 'r')
actual = [float(num) for num in file2.read().replace(' ', '').split(',')]
print(len(actual))