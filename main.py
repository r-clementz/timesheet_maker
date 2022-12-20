from datetime import datetime 
from helper import export_hours,get_duration,edit_data
import getpass 

today=datetime.now()
month=today.month 
month_letter=today.strftime('%B')
year=today.year 

#Main menu 
menu="""*****TIME SHEET MAKER*****\n
0. Report new hours 
1. Edit hours 
x. Quit
choose number and press Enter:)
********************************
"""
ask_if_continue="\nWould you like add more?'\n0. Yes\n1. No\n"

hours=[]
total_hours=[]
month_total=0

main_continuation=True



while main_continuation==True: #Always back to main menu
    #Main menu 
    menu_choice=getpass.getpass(f"{menu}")
    name=input("Please enter your name")
    name=name.capitalize()
    continuation=True

    while continuation==True:
        if menu_choice == "0": #B
            #def input_data():
            day=int(input(f"Date:{year}-{month}-"))
            date=datetime(year,month,day)
            yobi=(date.strftime('%a'))
            
            st=input("Start time(00:00): ")        
            et=input("End time(00:00): ")
            
            info={ "Date": f"{year}-{month}-{day}",
                        "Yobi":yobi,
                        "Start time": st,
                        "End time": et,
                        "Duration": get_duration(st,et)
                    }
            

            hours.append(info)
            total_hours.append(info['Duration'])
            month_total=sum(total_hours)

            #def choose_to_continue
            choice=getpass.getpass(f"{ask_if_continue}")
            if choice =="0": #Continue adding 
                continuation=True
                menu_choice="0"
            
            elif choice =="1":#Quit adding 
                export_hours(hours,month_total,name,today)
                #Show all input 
                print(f"*******\nTotal hours in {month_letter}: {month_total}\n")

                for i in range(len(hours)):
                    print(f"{hours[i]['Date']}({hours[i]['Yobi']}) {hours[i]['Start time']}-{hours[i]['End time']}") 
                #Check if all input is collect     
                choice=getpass.getpass("*******\n0. All correct & exit\n1. Edit\n")
                
                if choice == "0":
                    continuation=False
                    main_continuation=False
                    print("Bye now!")
                    #Exit from Application
                
                elif choice == "1": 
                    continuation=True 
                    menu_choice="1"        
                    #Keep inputing, go to #C             
            else:
                print("Invalid choice, application finished")
                continuation=False
                main_continuation=False 
                #Exit from Application         

        elif menu_choice=="1":#ç
            if len(hours)==0:
                print("You have nothing to edit")
                continuation=False

            else:
                edit_continuation=True
                while edit_continuation==True:
                    edit_data(hours,total_hours,month_total,name,today,year,month)
                    choice=getpass.getpass('Would you like to edit more?\n0.Yes\n1.No\n')
                
                    if choice=="0":
                        edit_continuation=True
                    elif choice=="1":
                        edit_continuation=False 
                        todo_next=getpass.getpass("\n0.Menu 1.Exit")
                        if todo_next=="0":
                            continuation=False
                        elif todo_next=="1":
                            quit()
                        else: 
                            quit()        
                        #Go back to #A 

        elif menu_choice=="x":
            print('Bye for now!')
            quit()                
        
        else:
            continuation=False 

