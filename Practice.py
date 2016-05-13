"""
A company has four salespeople (1 to 4)
who sell five different products (1 to 5) each with their different cost. Once a day, each salesperson passes in a slip for each differ-
ent type of product sold. Each slip contains:
a) The salesperson number.
b) The product number.
c) The number of that product sold that day.

For the product data given below, calculate the total sales for this day

#RULE
Each salesperson enters all his information at a go and on one line, with each data separated by a space
	e.g 1 4 100

	'1 4 100'
"""

products = {
	1: 100, 2:200, 3:50, 4:129, 5:100
}

salesReport = "Please insert the following separated by a space"
condA = " (a) Your number"
condB = " (b) The sold product number"
condC = " (c) The number of times the product was sold \n       Thank You"

print salesReport
print condA
print condB
print condC

salesRep1 = raw_input("Sales Rep 1 : ")
salesRep2 = raw_input("Sales Rep 2 : ")
salesRep3 = raw_input("Sales Rep 3 : ")
salesRep4 = raw_input("Sales Rep 4 : ")

t1 = salesRep1.split()
t2 = salesRep2.split()
t3 = salesRep3.split()
t4 = salesRep4.split()


a = int(t1[2]) * products[int(t1[2])]
b = int(t2[2]) * products[int(t2[2])]
c = int(t3[1]) * products[int(t3[2])]
d = int(t4[1]) * products[int(t4[2])]

totalSales = (a + b + c + d)

print "Your total sales for today is: \n     %i" %totalSales





