from django.test import TestCase

# Create your tests here.
import csv

with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('a', 'b', 'c'))
    writer.writerow(('1', '2', '3'))




