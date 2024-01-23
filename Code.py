"""
                                                Bill Calculator - Catalog and Discount

This Python program implements a discount calculator for a catalog with three products: Product A, Product B, and Product C.
The code applies various discount rules based on the total cart value and individual product quantities, calculating discounts, fees, and the final total.
The program adheres to certain specifications like, accepting user input for product quantities and gift wrapping preferences.
It provides a command-line interface for interaction and has been developed without the use of external frameworks or libraries.
Follow the instructions in the README to run the program and view the detailed bill.
"""

#Price of products
A=20
B=40
C=50

def shipping_cost():
    shipping_cost = ((q_total - 1) // 10 + 1)*5
    return shipping_cost

def discount_info(subtotal):
    select_discount=["None","flat_10_discount","bulk_5_discount","bulk_10_discount","tiered_50_discount"]
    final_discount=[0.0]

    if subtotal>200:
        flat_10_discount=10
        final_discount.append(flat_10_discount)

    if qA>10 or qB>10 or qC>10:
        bulk_5_discount=0
        if qA>10:
            disc_A=qA*A*0.05
            bulk_5_discount+=disc_A
        
        if qB>10:
            disc_B=qB*B*0.05
            bulk_5_discount+=disc_B
        
        if qC>10:
            disc_C=qC*C*0.05
            bulk_5_discount+=disc_C
        final_discount.append(bulk_5_discount)

    if q_total>20:
        bulk_10_discount=subtotal*0.10
        final_discount.append(bulk_10_discount)

    if q_total> 30 and (qA > 15 or qB > 15 or qC > 15):
        discount_A=A*max(qA - 15, 0) 
        discount_B=B*max(qB - 15, 0)
        discount_C=C*max(qC - 15, 0)
        
        tiered_50_discount=0.5*(discount_A+discount_B+discount_C)
        final_discount.append(tiered_50_discount)

    Damount=max(final_discount)
    Dindex=final_discount.index(Damount)
    Dname=select_discount[Dindex]
    return Dname,Damount

#Main
print("*****Enter following details to generate your bill*****:")

qA=int(input("Product A Quantity:"))
qB=int(input("Product B Quantity:"))
qC=int(input("Product C Quantity:"))

if qA<0 or qB<0 or qC<0:
    print("Wrong Input.......Program Terminated....")
    exit(0)

gift=input("Do you need these items to be wrapped as a gift?(Y/N)\n").upper()
q_total=qA+qB+qC
gift_cost=q_total*1
subtotal=(qA*A)+(qB*B)+(qC*C)

A_info = ['A', qA, qA * A]
B_info = ['B', qB, qB * B]
C_info = ['C', qC, qC * C]

Dname,Damount=discount_info(subtotal)

ship_cost=shipping_cost()

if gift=='Y' or gift=='YES':
    cart_cost=subtotal-Damount+ship_cost+gift_cost

else: 
    cart_cost=subtotal-Damount+ship_cost
    gift_cost=0

#Output
print('''\n***** BILL GENERATED SUCCESSFULLY *****\n
Product, Quantity, Amount''')
for info in [A_info,B_info,C_info]:
    print(info[0],"\t",info[1],"\t",info[2])

print(f'''
Subtotal: ${subtotal}
Discount Name: {Dname}
Discount Applied: ${Damount}
Shipping Fee: ${ship_cost}
Gift Fee: ${gift_cost}
Grand Total: ${cart_cost}
\nThanks for shopping with us :)''')
