#!/usr/bin/env python3
'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions.

- You MUST complete the functions defined below, except the ones that are already defined.
'''


import prettytable

global table
table = prettytable.PrettyTable(['CODE','DESCRIPTION','CATEGORY','COST (Rs)'])
global cost_total
cost_total = 0
table = prettytable.PrettyTable(['CODE','DESCRIPTION','CATEGORY','COST (Rs)'])
table.add_rows([[0,'Tshirt','Apparels',500],
[1,'Trousers','Apparels',600],
[2,'Scarf','Apparels',250],
[3,'Smartphone','Electronics','20,000'],
[4,'iPad','Electronics','30,000'],
[5,'Laptop','Electronics','50,000'],
[6,'Eggs','Eatables',5],
[7,'Chocolates','Eatables',10],
[8,'Juice','Eatables',100],
[9,'Milk','Eatables',45]])



def show_menu():
    '''
    Description: Prints the menu as shown in the PDF

    Parameters: No paramters

    Returns: No return value
    '''
    print('='*50)
    print(' '*15,'MY BAZAAR')
    print('='*50)
    print('Hello! Welcome to my grocery store!\nFollowing are the products available in the shop:\n')

    table = prettytable.PrettyTable(['CODE','DESCRIPTION','CATEGORY','COST (Rs)'])
    table.add_rows([[0,'Tshirt','Apparels',500],
    [1,'Trousers','Apparels',600],
    [2,'Scarf','Apparels',250],
    [3,'Smartphone','Electronics','20,000'],
    [4,'iPad','Electronics','30,000'],
    [5,'Laptop','Electronics','50,000'],
    [6,'Eggs','Eatables',5],
    [7,'Chocolates','Eatables',10],
    [8,'Juice','Eatables',100],
    [9,'Milk','Eatables',45]])

    print(table)

def get_regular_input():
    '''
    Description: Takes space separated item codes (only integers allowed).
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    print('\n\n')
    print('-'*50)
    print('ENTER ITEMS YOU WISH TO BUY')
    print('-'*50)

    items = input('Enter the item codes (space-separated):').split()
    items.sort()
    lizt = []

    for row in table:
                 row.header = False
                 row.border = False
                 code = row.get_string(fields=['CODE']).strip()
                 lizt.append(items.count(code))

    return lizt




def get_bulk_input():
    '''
    Description: Takes inputs (only integers allowed) from a bulk buyer.
    For details, refer PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    print('\n')
    print('-'*50)
    print('ENTER ITEMS AND THEIR QUANTITIES')
    print('-'*50)
    zilt = [0,0,0,0,0,0,0,0,0,0]

    while 2==2:
       l = input('Enter code and quantity (leave blank to stop): ').split()


       if len(l)==0:
           print('Your order has been finalized.')
           break

       if len(l) not in range(2,3):
           print('Invalid quantity. Try again.\n')

       else:
           items = int(l[0])
           quantities = int(l[1])

           if (str(items).isnumeric() == False) or (str(quantities).isnumeric() == False) or (items not in range(0,10)) :
               print('Invalid quantity. Try again.\n')

           else:
               description = table.get_string(fields=['DESCRIPTION'], header=False , border=False , start=items , end=items+1).strip()
               print('You added {} {}\n'.format(quantities,description))
               zilt[items] += quantities


    return zilt


def print_order_details(quantities):
    '''
    Description: Prints the details of the order in a manner similar to the
    sample given in PDF.

    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.

    Returns: No return value
    '''
    print('\n\n')
    print('-'*50)
    print('ORDER DETAILS')
    print('-'*50)
    i = 1

    for x in quantities:

           if x > 0:
               s = quantities.index(x)
               quantities[s] = x*-1
               description = table.get_string(fields=['DESCRIPTION'], header=False , border=False , start=s , end=s+1).strip()
               cost = int(table.get_string(fields=['COST (Rs)'], header=False , border=False , start=s , end=s+1).strip().replace(',',''))
               line = "[{}] {} x {} = Rs {} * {} = Rs {}".format(i,description,x,cost,x,cost*x)
               print(line)
               i += 1
               cost_total += cost*x

    for x in quantities:
           s = quantities.index(x)
           quantities[s] = x*-1


def calculate_category_wise_cost(quantities):
    '''
    Description: Calculates the category wise cost using the quantities
    provided. Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.

    Returns: A 3-tuple of integers in the following format:
    (apparels_cost, electronics_cost, eatables_cost)
    '''
    print('\n\n')
    print('-'*50)
    print('CATEGORY-WISE COST')
    print('-'*50)
    total_a = 0
    total_b = 0
    total_c = 0
    global cost_total

    for x in quantities:
        s = quantities.index(x)
        cost = int(table.get_string(fields=['COST (Rs)'] , header=False , border=False , start=s , end=s+1).strip().replace(',',''))
        category = table.get_string(fields=['CATEGORY'] , header=False , border=False , start=s , end=s+1).strip()
        quantities[s] = x*-1
        if category == 'Apparels':
            total_a += cost*x
        if category == 'Electronics':
            total_b += cost*x
        if category == 'Eatables':
            total_c += cost*x

    if total_a != 0:
        print("Apparels = Rs {}".format(total_a))

    if total_b != 0:
        print("Electronics = Rs {}".format(total_b))

    if total_c != 0:
        print("Eatables = Rs {}".format(total_c))

    return (total_a,total_b,total_c)


def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)




def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the discounted category-wise price, if applicable.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost:     cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost:     cost for the category 'Eatables'

    Returns: A 3-tuple of integers in the following format:
    (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost).
    '''
    print('\n\n')
    print('-'*50)
    print('DISCOUNTS')
    print('-'*50)
    discount = 0.1

    if apparels_cost >= 2000:
        discounted_apparels_cost = apparels_cost - get_discount(apparels_cost, discount)
        print('[APPARELS] Rs {} - Rs {} = Rs {}'.format(apparels_cost,get_discount(apparels_cost, discount),discounted_apparels_cost))
    else:
        discounted_apparels_cost = apparels_cost


    if electronics_cost >= 25000:
        discounted_electronics_cost = electronics_cost - get_discount(electronics_cost, discount)
        print('[ELECTRONICS] Rs {} - Rs {} = Rs {}'.format(electronics_cost,get_discount(electronics_cost, discount),discounted_electronics_cost))
    else:
        discounted_electronics_cost = electronics_cost


    if eatables_cost >= 500:
        discounted_eatables_cost = eatables_cost - get_discount(eatables_cost, discount)
        print('[EATABLES] Rs {} - Rs {} = Rs {}'.format(eatables_cost,get_discount(eatables_cost, discount),discounted_eatables_cost))
    else:
        discounted_eatables_cost = eatables_cost

    total_cost = discounted_apparels_cost + discounted_electronics_cost + discounted_eatables_cost
    total_discount = apparels_cost + electronics_cost + eatables_cost - total_cost

    print('\nTOTAL DISCOUNT = Rs {}'.format(total_discount))
    print('TOTAL COST = Rs {}'.format(total_cost))

    return (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)




def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax:     Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    return int(cost * tax)




def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the total cost including taxes.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost:     cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost:     cost for the category 'Eatables'

    Returns: A 2-tuple of integers in the following format:
    (total_cost_including_tax, total_tax)
    '''
    print('\n\n')
    print('-'*50)
    print('TAX')
    print('-'*50)
    a = 0.1
    b = 0.15
    c = 0.05
    apparels_tax = get_tax(apparels_cost,a)
    electronics_tax = get_tax(electronics_cost,b)
    eatables_tax = get_tax(eatables_cost,c)

    if apparels_cost != 0:
        print('[APPARELS] Rs {} * {} = Rs {}'.format(apparels_cost,a,apparels_tax))

    if electronics_cost != 0:
        print('[ELECTRONICS] Rs {} * {} = Rs {}'.format(electronics_cost,b,electronics_tax))

    if eatables_cost != 0:
        print('[EATABLES] Rs {} * {} = Rs {}'.format(eatables_cost,c,eatables_tax))

    total_cost = apparels_cost + electronics_cost + eatables_cost
    total_tax = apparels_tax + electronics_tax + eatables_tax
    total_cost_including_tax = total_cost + total_tax

    print('\nTOTAL TAX = Rs {}'.format(total_tax))
    print('TOTAL COST = Rs {}'.format(total_cost_including_tax))

    return (total_cost_including_tax, total_tax)




def apply_coupon_code(total_cost):
    '''
    Description: Takes the coupon code from the user as input (case-sensitive).
    For details, refer the PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: The total cost (integer) on which the coupon is to be applied.

    Returns: A 2-tuple of integers:
    (total_cost_after_coupon_discount, total_coupon_discount)
    '''
    print('\n\n')
    print('-'*50)
    print('COUPON CODE')
    print('-'*50)

    while 2==2:
        code = input('Enter coupon code (else leave blank): ')

        if code == "HELLE25" and total_cost >= 25000:
            coupon_discount = 0.25*total_cost

            if coupon_discount > 5000:
                coupon_discount = 5000
            print('[{}] min(5000, Rs {} * 0.25) = Rs {}'.format(code,total_cost,coupon_discount))
            break

        if code == "CHILL50" and total_cost >= 50000:
            coupon_discount = 0.5*total_cost

            if coupon_discount > 10000:
                coupon_discount = 10000
            print('[{}] min(10000, Rs {} * 0.5) = Rs {}'.format(code,total_cost,coupon_discount))
            break

        if len(code) == 0:
            print('No coupon code applied.')
            coupon_discount = 0
            break

        print('Invalid coupon code. Try again.\n')

    print('\nTOTAL COUPON DISCOUNT = Rs {}'.format(coupon_discount))
    print('TOTAL COST = Rs {}'.format(total_cost - coupon_discount))
    return (total_cost - coupon_discount,coupon_discount)






def main():
    '''
    Description: This is the main function. All production level codes usually
    have this function. This function will call the functions you have written
    above to design the logic. You will see how splitting your code into specialised
    functions makes the code easier to read, write and debug. Include appropriate
    print statements to match the output with the screenshots provided in the PDF.

    Parameters: No parameters

    Returns: No return value
    '''
    show_menu()

    while 4*2==8:
        preference = input('\nWould you like to buy in bulk? (y or Y / n or N): ')

        if preference =='y'or preference=='Y':
            a = get_bulk_input()
            print_order_details(a)
            print('\nTOTAL COST = Rs {}'.format(cost_total))
            break

        if preference =='n'or preference =='N':
            a = get_regular_input()
            print_order_details(a)
            break

    b = calculate_category_wise_cost(a)
    c = calculate_discounted_prices(b[0],b[1],b[2])
    d = calculate_tax(c[0],c[1],c[2])
    apply_coupon_code(d[0])
    print('\nTHANK YOU FOR VISITING!!!')










if __name__ == '__main__':
    main()
