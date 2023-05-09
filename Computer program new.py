
#usernames allowed-
    #1. sales1@abcmall.com (password= sales1)
    #2. sales2@abcmall.com (password= sales2)
    #3. sales3@abcmall.com (password= sales3)

#admin-
    #username= admin@abcmall.com
    #passwrod= admin123

#-------------------------------------------------------------------------#

#Variables section

usernames={'sales1@abcmall.com':'sales1','sales2@abcmall.com':'sales2','sales3@abcmall.com':'sales3'}
admin_username={'admin@abcmall.com':'admin123'}
wish=True

#--------------------------------------------------------------------------#

#Importing modules

import csv
import pickle
#-------------------------------------------------------------------#

# Functions

def csv_reader():

    f=open('customers.csv','r')
    reader=csv.DictReader(f)
    count=0
    key_list=[]

    for i in reader:
        key=int(i['id'])
        key_list.append(key)
        count+=1 

    if (count==0):  #for checking if the file is empty or not
        last_key=100

    else:
        last_key=key
        pass

    f.close()

    return count,key_list,last_key


def bin_reader(b):

    g=open(b,'rb')
    reader2=[]

    try:
        while True:
            a=pickle.load(g)
            reader2.append(a)
    except:
        g.close()

    return reader2

#-----------------------------------------------------------------------#

                            #Main Program

print("**--------PARAMAK Mall Sales-cum-Database Management Software--------**")
print('\n \n',end='')

while wish:

    #login part starts--------------------------------------------
    print("*----------------------Main Menu----------------------*")
    print("Enter 1 to login for salesperson section.")
    print("Enter 2 to login for admin section.")
    print("Enter 3 to exit.")
    print('\n',end='')
    choice=input("Enter your choice:")

    if (choice=='1' or choice=='2' ):
 
        for i in range(0,3): #Username part
            username=input("Enter your username(Max. 3 tries):")

            if ((username in usernames and choice=='1') or (username in admin_username and choice=='2')):
                break
            
            else:
                print("Wrong username!")
                continue

        else:  #this part will execute only if loop ends normally or all tries are over

            print('\n',end='')
            print("Your tries are over.")
            ask=input("Do you want to again continue the main program(y/n)?")

            if(ask in ['y','Y','yes']):
                wish=True
                print('\n',end='')
                continue
            else:
                wish=False
                print("Exiting....")
                break
            

        for i in range(0,3): #password part

            print('\n',end='')
            password=input("Enter your password(Max. 3 tries):")

            if (choice=='1' and (username in usernames) and password==usernames[username]):
                break
            
            elif (choice=='2' and (password==admin_username['admin@abcmall.com']) and username=='admin@abcmall.com'):
                break
            
            else:
                print("Wrong password!")
                continue

        else:  #this part will execute only if loop ends normally or all tries are over

            print('\n',end='')
            print("Your tries are over.")
            ask=input("Do you want to again continue the main program(y/n)?")

            if(ask in ['y','Y','yes']):
                wish=True
                print('\n',end='')
                continue
            else:
                wish=False
                print("Exiting....")
                break

    elif(choice=='3'):
        print("Exiting....")
        print('-------------------------------*------------------------------------')
        break
    
    else:
        print('\n',end='')
        print("You have entered wrong option.")

        print('\n',end='')
        ask=input("Do you want to again continue the main program(y/n)?")

        if(ask in ['y','Y','yes']):
            wish=True
            print('\n',end='')
            continue
        else:
            wish=False
            print("Exiting....")
            break

        

    #login part over---------------------------------------#

    #salesperson section-----------------------------------#

    if(username in usernames):

        print('\n',end='')
        print('-------------------------------*------------------------------------')
        print("Welcome Salesperson.")

        #checking for last key so as to continue from there
        #also making a list of all keys

        count_key,key_list,key=csv_reader()
        
        #last key checking over

        f=open('customers.csv','a+')
        writer=csv.DictWriter(f,fieldnames=['id','name','number','email'],lineterminator='\n')

        ask_new=input("Enter customer id(if any) or else enter 0:")

        if(ask_new.isdigit()):

            ask_new=int(ask_new)
            
            if(ask_new==0):

                key=key+1

                print('\n',end='')
                name=input("Enter name:")

                for i in range(0,3):
                    number=input("Enter contact number(Max. 3 tries):")

                    if(number.isdigit() and len(number)==10):
                        break
                    else:
                        print("Invalid number!")
                        continue

                else: #this part will execute only if loop ends normally or all tries are over

                    print('\n',end='')
                    print("Your tries are over.")
                    print('\n',end='')
                    ask=input("Do you want to again continue the main program(y/n)?")

                    if(ask in ['y','Y','yes']):
                        wish=True
                        continue
                    else:
                        wish=False
                        break

                email=input("Enter email id:")


                writer.writerow({'id':key,'name':name,'number':number,'email':email})

                f.close()

            elif( ask_new in key_list):

                key=ask_new
                print("Key is valid.Moving to billing section.")

            else:
                print('\n',end='')
                print("Entered id is not valid.")

                print('\n',end='')
                ask=input("Do you want to again continue the main program(y/n)?")

                if(ask in ['y','Y','yes']):
                    wish=True
                    continue
                else:
                    wish=False
                    break

        else:
            print('\n',end='')
            print("Invalid input")

            print('\n',end='')
            ask=input("Do you want to again continue the main program(y/n)?")

            if(ask in ['y','Y','yes']):
                wish=True
                continue
            else:
                wish=False
                break
            
            
            #customer details section over-----------
            
            #customer items section start---------------------------
            

        f=open("items.bin",'ab')
        cart=True #for items adding
        item={}
        price=[] #list containing quantity,cost per piece and total price per product
        print('\n')
        print('-------------------------------*------------------------------------')
        print("Billing starts.")
        
        while cart:

            print('\n',end='')
            product=input("Enter product name:")
            cost=float(input("Enter product price (per item or per (kg or L)):"))
            quantity=float(input("Enter number of pieces (or kg or L):"))
            print('\n')

            #checking for cost=0----------------

            if (cost<=0):
                print("Product price cannot be less than or equal to 0. Try again....")
                print('\n',end='')
                continue

            # checking over-------------

            # checking for same product given again--------------

            if (product in item):
                print("This item is already listed once.")
                print("If you continue this new value will overwrite the previous one.")
                print('\n',end='')
                ask_product=input("Do you want to continue(y/n):")
                print('\n',end='')

                if (ask_product in ['y','Y','yes']):
                    pass
                else:
                    print("Reiterating....")
                    print('\n',end='')
                    continue

            #checking over--------------------
            
            price=[quantity,cost,(quantity*cost)]
            
            item[product]=price 

            print('\n',end='')
            ask_item=input("Do you want to add 1 more item(y/n)?")

            if(ask_item=='y'):
                cart=True
                continue
            else:
                cart=False
                break

            
        #correcting records if entered wrong------------------
        wish_correction=True

        print('\n',end='')
        ask_correction=input("Do you wish to delete or modify any item(y/n)?")

        while wish_correction:

            if (ask_correction in ['y','Y','yes'] and len(item)!=0):
                print('\n',end='')
                print("Enter 1 to modify a product.")
                print("Enter 2 to delete a product.")
                print("Enter 3 to exit.")

                choice_correction=input("Enter your choice:")
                print('\n',end='')

                if (choice_correction=='1'):
                    item_name=input("Enter product name:")

                    for i in item:
                        if (i==item_name):
                            print('\n',end='')
                            product=input("Enter new product name:")
                            cost=float(input("Enter product price (per item or per (kg or L)):"))
                            quantity=float(input("Enter number of pieces (or Kg or L):"))
                            print('\n',end='')
                            
                            #checking for cost=0----------------

                            if (cost<=0):
                                print("Product price cannot be less than or equal to 0. Try again....")
                                print('\n',end='')
                                break

                            # checking over-------------
                            
                            del item[i] #storing return value of pop function

                            # checking for same product given again--------------

                            if (product in item):
                                print("This item is already listed once.")
                                print("If you continue this new value will overwrite the previous one.")
                                print('\n',end='')
                                ask_product=input("Do you want to continue(y/n):")
                                print('\n',end='')

                                if (ask_product in ['y','Y','yes']):
                                    pass
                                else:
                                    print("Reiterating....")
                                    print('\n',end='')
                                    break

                            #checking over--------------------

                            price=[quantity,cost,(quantity*cost)]    
                            item[product]=price
                            print("Updation successful.")
                            break
                    else:
                        print('\n',end='')
                        print("Product not found.")
                        
                elif (choice_correction=='2'):
                    item_name=input("Enter product name:")

                    for i in item:
                        if (i==item_name):
                            del item[i]
                            print("Deletion successful.")
                            break
                    else:
                        print('\n',end='')
                        print("Product not found.")

                elif (choice_correction=='3'):
                    print("Exiting menu....")
                    break

                else:
                    print('\n',end='')
                    print("Invalid option.")

                print('\n',end='')
                ask_again=input("Do you wish to again continue this menu(y/n)?")

                if (ask_again in ['y','Y','yes']):
                    wish_correction=True
                    continue
                else:
                    break

            elif (len(item)==0):
                print('Cart is empty. Exiting menu....')
                break

            else:
                break
                            
        #records correction over-----------------------------------
        amt=0
        
        for i in item:

            amt=amt+item[i][2]

        sales=username

        #Checking if no item is bought------------

        if (len(item)==0):
            item='No product bought.'

        #checking for empty item dictionary---------------

        dict1={'id':key,'item':item,'amt':amt,'sales':sales}
        pickle.dump(dict1,f)
        

        #printing of bill
        print('\n')
        print('\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/')
        print("Customer ID is-",key)
        print('\n',end='')
        print("The bill is as follows:")
        print('\n')

        if (item=='No product bought.'): #checking if no item bought
            print(item)
            print('\n',end='')

        else:
            for i in item:
                print("Product-",i,"; Quantity-",item[i][0])
                print("Cost/piece- Rs",item[i][1],"; Total cost- Rs",item[i][2])
                print('\n',end='')

            print("Total bill amount is:- Rs",amt)
            print('\n')
            
        print("THANKS FOR SHOPPING WITH US!!")
        print("HAVE A NICE DAY.... :-) ")
        print('\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/')
        print('\n')
        print('-------------------------------*------------------------------------')
        
        f.close()

        #bill part over
        #salesperson part over


        #admin part starts

    elif(username in admin_username):

        wish2=True

        while wish2:
            print('\n')
            print('-------------------------------*------------------------------------')
            print("Welcome Admin!")

            print("Enter 1 to see customer details.")
            print("Enter 2 to see items bought by a customer.")
            print("Enter 3 to see the sales amount and number of orders per salesperson.")
            print("Enter 4 to see total revenue.")
            print("Enter 5 to see average money spent by a customer.")
            print("Enter 6 to see the total number of orders.")
            print("Enter 7 to see the total number of customers.")
            print("Enter 8 to modify or delete customer details.")
            print("Enter 9 to see the billings made by a salesperson.")
            print("Enter 10 to exit.")

            print('\n',end='')
            choice_admin=input("Enter your choice:")
            print('\n',end='')

            #making a list of all keys

            count_key,key_list,last_key=csv_reader() 
            
            #key checking over and pointer goes to the end
            #so we close and open the file again

            #opening customers file
            f=open('customers.csv','r')
            reader=csv.DictReader(f)
            #opening over

            #opening items file and storing all values in reader2
            try: # using 'try' to check if item file is there or not
                b="items.bin"
                reader2=bin_reader(b)
            except:

                if(choice_admin=='10'): # exiting if user gives exit command
                    print('\n',end='')
                    print("Exiting menu.")
                    print('-------------------------------*------------------------------------')
                    break
                else:
                    print("No data available.")
                    print("Reiterating menu.")
                    continue
                
            #opening and storing over for items file

            if(count_key==0):
                if (choice_admin=='10'):
                    print('\n',end='')
                    print("Exiting menu.")
                    print('-------------------------------*------------------------------------')
                    break
                else:
                    print("FILES ARE EMPTY.")


            elif(choice_admin=='1'):

                print("Enter 1 to view details of a customer.")
                print("Enter 2 to view details of all customers.")
                print("Enter 3 to exit.")
                
                print('\n',end='')
                choice_details=input("Enter your choice:")
                print('\n',end='')

                if(choice_details=='1'):

                    key=int(input("Enter customer key:"))

                    if(key in key_list):

                        print('\n',end='')
                        print("The customer details are as follows:-")

                        for i in reader:

                            if(int(i['id'])==key):

                                print('Name-',i['name'],'; Id-',i['id'])
                                print('number-',i['number'],'; Email-',i['email'])
                                print('\n',end='')

                    else:
                        print('\n',end='')
                        print("Entered key doesn't exist in database.")


                elif(choice_details=='2'):

                    for i in reader:

                        print('Name-',i['name'],'; Id-',i['id'])
                        print('number-',i['number'],'; Email-',i['email'])
                        print('\n',end='')

                elif (choice_details=='3'):
                    print("Exiting menu.")
                    pass

                else:
                    print("You have entered a wrong operator.")
    



            elif(choice_admin=='2'):

                key=int(input("Enter customer key:"))

                if(key in key_list):

                    count_orders=1  #counts the numbers of orders made by the person
                    
                    for i in reader2:

                        if (i['id']==key):

                            print('\n',end='')
                            print('\n',end='')
                            print("This is order number-",count_orders)
                            print('\n',end='')
                            print("The billing was done by:",i['sales'])
                            print('\n',end='')
                            print("The items are as follows:")
                            print('\n')
                            dic=i['item']

                            if (dic=='No product bought.'):
                                print(dic)
                                print('\n',end='')

                            else:
                                for j in dic:
                                    print("Product name-",j,'; Quantity-',dic[j][0])
                                    print("Cost/piece- Rs",dic[j][1],'; Total cost- Rs',dic[j][2])
                                    print('\n',end='')

                                print("Total bill amount- Rs",i['amt'])
                            count_orders+=1

                else:
                    print('\n',end='')
                    print("Entered key is not in database.")


            elif(choice_admin=='3'):

                dic={} #temporary dictionary for storing salesperson's number of order and revenue

                for i in reader2:

                    b=i['sales']
                    count2=0
                    amount=0

                    if (b not in dic):
                        for j in reader2:
                            if (j['sales']==b and j['amt']!=0): #checking if customer bought something or not
                                count2+=1
                                amount+=j['amt']

                        dic[b]=[count2,amount] #storing info in a dic with list values


                for k in dic:
                    print('Salespersons is -',k)
                    print("               Total number of orders are:",dic[k][0])
                    print("               Total sales amount is:",dic[k][1])
                    print('\n',end='')


            elif(choice_admin=='4'):

                revenue=0

                for i in reader2:

                    revenue+=i['amt']

                print("The total revenue is- Rs",revenue)

            elif(choice_admin=='5'):
                
                revenue=0 #first finding total revenue

                for i in reader2:

                    revenue+=i['amt']

                #finding total number of orders
                orders=0
                for j in reader2:
                    orders+=1

                average=revenue/orders

                print("The average spend per customer is: Rs",average)

            elif(choice_admin=='6'):

                orders=0
                for i in reader2:

                    if (i['amt']!=0): #checking for customers who bought nothing
                        orders+=1
                    
                print("Total number of orders till now are:",orders)

            elif(choice_admin=='7'):

                customers_number=0

                for i in reader:
                    customers_number+=1

                print("Total number of customers till now are:",customers_number)

            elif(choice_admin=='8'):

                print('\n')
                key=int(input("Enter key of the customer that need to be modified:"))

                if (key in key_list):

                    print('\n',end='')
                    print("Enter 1 to change name.")
                    print("Enter 2 to change phone number.")
                    print("Enter 3 to change email address.")
                    print("Enter 4 to delete customer records.")
                    print("Enter 5 to exit.")

                    print('\n',end='')
                    choice_modify=input("Enter your choice:")
                    master_list=[] # list for storing all records to be inserted into the csv file
                    marker=0 #for telling if file was updated or not
                    h=open('customers2.csv','w')
                    writer=csv.DictWriter(h,fieldnames=['id','name','number','email'],lineterminator='\n')
                    writer.writeheader()
                    count=0 # for checking if all tries are over or not in number updation
                    print('\n')
                    
                    if (choice_modify=='1'):
                        name=input("Enter new name:")
                        
                        for i in reader:

                            if (int(i['id'])==key):
                                record=i # this is a dictionary that we receive from the csv file
                                record['name']=name # changing name in record
                                master_list.append(record)
                            else:
                                master_list.append(i)
                                

                        writer.writerows(master_list) # writing all the records into the csv file
                        print("Name updated successfully.")
                        h.close()

                    elif (choice_modify=='2'):

                        
                        for i in range(0,3): # inputing new number
                            number=input("Enter new contact number(Max. 3 tries):")

                            if(number.isdigit() and len(number)==10):
                                break
                            else:
                                print("Invalid number!")
                                count=count+1
                                continue

                        if (count==3): # skipping rest part if all tries over and going to the end
                            pass
                        else:
                            for i in reader:

                                if (int(i['id'])==key):
                                    record=i # this is a dictionary that we receive from the csv file
                                    record['number']=number # changing name in record
                                    master_list.append(record)
                                else:
                                    master_list.append(i)
                                

                            writer.writerows(master_list) # writing all the records into the csv file
                            print("Number updated successfully.")
                            h.close()

                    elif (choice_modify=='3'):
                        email=input("Enter new email address:")
                        
                        for i in reader:

                            if (int(i['id'])==key):
                                record=i # this is a dictionary that we receive from the csv file
                                record['email']=email # changing name in record
                                master_list.append(record)
                            else:
                                master_list.append(i)
                                

                        writer.writerows(master_list) # writing all the records into the csv file
                        print("Email updated successfully.")
                        h.close()

                    elif (choice_modify=='4'):
                        for i in reader: #for deletion of record in csv file
                            if (int(i['id'])==key):
                                pass
                            else:
                                master_list.append(i)

                        writer.writerows(master_list)
                        h.close()
                        
                        marker=2 #for deletion of record in binary file

                    elif (choice_modify=='5'):
                        marker=1
                        h.close() #recent change
                        pass

                    else:
                        print("Invalid input.")
                        h.close()
                        marker=1


                    if ((marker==0 or marker==2) and count!=3): # copying data from customers2 only if updation took place
                        h=open('customers2.csv','r') # opening file again so that pointer starts from the bginning 
                        p=open('customers.csv','w')
                        writer2=csv.DictWriter(p,fieldnames=['id','name','number','email'],lineterminator='\n')
                        writer2.writeheader()
                        
                        reader3=csv.DictReader(h)

                        for j in reader3: # transferring records
                            writer2.writerow(j)

                        
                        p.close()
                        h.close()

                    if (marker==2): #for deletion of records purposes

                        q=open('items2.bin','wb')

                        for k in reader2:
                            if (k['id']==key):
                                pass
                            else:
                                pickle.dump(k,q)

                        q.close() #closing file because pointer is at the end

                        q=open('items2.bin','rb') #opening file again to read
                        reader3=bin_reader('items2.bin')

                        r=open('items.bin','wb')

                        for m in reader3:
                            pickle.dump(m,r)

                        print("Deletion successful.")
                        
                        r.close()
                        q.close()
                        

                else:
                    print("Invalid key.")

            elif (choice_admin=='9'):

                person=input("Enter username of salesperson:")

                if (person in usernames):

                    count_orders=1
                    
                    for i in reader2:
                        if (i['sales']==person):

                            print('\n',end='')
                            print('\n',end='')
                            print("This is billing number-",count_orders)
                            print('\n',end='')
                            print("The billing was done for customer with ID:",i['id'])
                            print('\n',end='')
                            print("The items are as follows:")
                            print('\n')
                            dic=i['item']

                            if (dic=='No product bought.'):
                                print(dic)
                                print('\n',end='')

                            else:
                                for j in dic:
                                    print("Product name-",j,'; Quantity-',dic[j][0])
                                    print("Cost/piece- Rs",dic[j][1],'; Total cost- Rs',dic[j][2])
                                    print('\n',end='')

                                print("Total bill amount- Rs",i['amt'])
                            count_orders+=1

                else:
                    print("Invalid username.")
                    print('\n',end='')
                            
            elif (choice_admin=='10'):
                print("Exiting...")
                break

            else:

                print("You entered an invalid option!")
                
            #Closing all files at the end

            f.close()
        
        
            #asking if u want to use this menu again
            print('\n \n',end='')
            ask_admin=input("Do you wish to continue this menu(y/n)?")

            if(ask_admin=='y'):
                wish2=True
                continue
            else:
                wish2=False
                print("Exiting....")
                print('-------------------------------*------------------------------------')
                break


        
    print('\n \n',end='')
    ask=input("Do you want to continue the main program again(y/n)?")

    if(ask in ['y','Y','yes']):
        wish=True
        print('\n',end='')
    else:
        wish=False
        print("Exiting....")
        print('-------------------------------*------------------------------------')
        break
