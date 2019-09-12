import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Name")
parser.add_argument("Birth")
args = parser.parse_args()

a=args.Birth.split('.')
age = 2019 - int(a[2])
if (int(a[1])>9):
    age -=1
if (int(a[1])==9 and a[0]>12):
    age -= 1


print('hello, '+ args.Name +' '+str(age))