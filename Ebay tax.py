#Calculate how much you'll receive from
#an Ebay sell
# (C) Gil Costa 2019

x = float(input("Received: "))

Ebay_tax = x*10/100
print("Ebay tax:","{0:.2f}".format(Ebay_tax))

VAT = Ebay_tax * 23/100
print("Imposto português, VAT:","{0:.2f}".format(VAT))

Paypal_tax = x * 4.4/100 +0.30
print ("Paypal tax:", "{0:.2f}".format(Paypal_tax))

totalfees = Paypal_tax + Ebay_tax + VAT
print("total fees (Ebay + VAT + Paypal):", "{0:.2f}".format(Ebay_tax),
      "+", "{0:.2f}".format(VAT), "+", "{0:.2f}".format(Paypal_tax))

print("Will receive:","{0:.2f}".format( x - totalfees))
 
print ("Total percentage paid","-","{0:.2f}".format(totalfees/x *100),"%")
 
