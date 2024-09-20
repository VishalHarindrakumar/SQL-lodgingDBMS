import mysql.connector as mc
import datetime
from datetime import date
from datetime import timedelta
import csv
from tabulate import tabulate
conn=mc.connect(host="localhost",user="root",passwd="vish100%",database="lodging")
cur=conn.cursor()
 
def LODGING_MAIN_UI():
    def bookRoom():
        branch=int(input("""
                                    Branch
                                   ---------\n
                               [1]:Anna Nagar
                               [2]:Mogappair
                               [3]:Exit
                               """))
        if branch==3:
            LODGING_MAIN_UI()
        
      
       
        
        if branch==1:
            cur.execute("select room_no,occup_status,tier,tier_desc from roomdb_annanagar;")
            rooms=cur.fetchall()
            
            for i in rooms:
                table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description"])
                print(table)
                print("\n")
            room_no=int(input("Book Room No.[1,2,3,4]: "))
            occ_name=input("Name of occupant: ")
            date_booked_day=int(input("Enter booking day: "))
            date_booked_month=int(input("Enter booking month: "))
            date_booked_year=int(input("Enter booking year: " ))
            date_booked=datetime.date(date_booked_year,date_booked_month,date_booked_day)
            days_booked=int(input("No. of days for stay: "))
            date_checkout=date_booked+datetime.timedelta(days=days_booked)
            current_datetime=date.today()
                    
            

            cur.execute("select*from roomdb_annanagar")
            roomdb_show=cur.fetchall()
            print
            cur.execute(f"select(occup_status)from roomdb_annanagar where room_no={room_no};")
            occup_status_check=cur.fetchall()
            occup_status_check=occup_status_check[0][0]
            if occup_status_check=="staying":
                print("Room already booked")
            
                
            else:
                addtoallbranch=f"insert into bookings_allbranches values({room_no},'{occ_name}','{date_booked}',NULL,{days_booked},'{branch}','staying','{date_checkout}',NULL);"
                cur.execute(addtoallbranch)
                set_current_date=f"update bookings_allbranches set booking_completion='{current_datetime}' where room_no={room_no};"
                cur.execute(set_current_date)
                
                addtospecificbranch=f"insert into bookings_annanagar values({room_no},'{occ_name}','{date_booked}',NULL,{days_booked},'N','staying','N','{date_checkout}',NULL);"
                cur.execute(addtospecificbranch)
                set_current_date_S=f"update bookings_annanagar set booking_completion='{current_datetime}' where room_no={room_no};"
                cur.execute(set_current_date_S)
                
                
                
                update_room=f"update roomdb_annanagar set occup_status='Y',occ_name='{occ_name}',days_occ='{days_booked}'where room_no={room_no};"
                cur.execute(update_room)

                tier_check_query=f"select(tier)from roomdb_annanagar where room_no={room_no}"
                cur.execute(tier_check_query)
                tier_res=cur.fetchall()
                if tier_res[0][0]==1:
                    price=250*days_booked
                elif tier_res[0][0]==2:
                    price=500*days_booked
                elif tier_res[0][0]==3:
                    price=1000*days_booked
                





                print(f"""                                              BILLING:
                        Date:{current_datetime}
                      
                                                    Name:{occ_name}
                                                    Room No:{room_no}
                                                    Booked from:{date_booked}|To:{date_checkout}|For:{days_booked} days

                                                    Price:
                                                    {price}""")


        if branch==2:
            cur.execute("select room_no,occup_status,tier,tier_desc from roomdb_mogappair;")
            rooms=cur.fetchall()
           
            for i in rooms:
                table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description"])
                print(table)
                print("\n")
                
            room_no=int(input("Book Room No.[1,2,3,4]: "))
            occ_name=input("Name of occupant: ")
            date_booked_day=int(input("Enter booking day: "))
            date_booked_month=int(input("Enter booking month: "))
            date_booked_year=int(input("Enter booking year: " ))
            date_booked=datetime.date(date_booked_year,date_booked_month,date_booked_day)
            days_booked=int(input("No. of days for stay: "))
            date_checkout=date_booked+datetime.timedelta(days=days_booked)
            current_datetime=date.today()
            cur.execute(f"select(occup_status)from roomdb_mogappair where room_no={room_no};")
            occup_status_check=cur.fetchall()
            occup_status_check=occup_status_check[0][0]


            if occup_status_check=="staying":
                print("Room already booked")
            else:
                addtoallbranch=addtoallbranch=f"insert into bookings_allbranches values({room_no},'{occ_name}','{date_booked}',NULL,{days_booked},'{branch}','staying','{date_checkout}',NULL);"
                cur.execute(addtoallbranch)
                set_current_date=f"update bookings_allbranches set booking_completion='{current_datetime}' where room_no={room_no};"
                
                cur.execute(set_current_date)
                addtospecificbranch=f"insert into bookings_mogappair values({room_no},'{occ_name}','{date_booked}',NULL,{days_booked},'N','staying','N','{date_checkout}',NULL);"
                cur.execute(addtospecificbranch)
                set_current_date_S=f"update bookings_mogappair set booking_completion='{current_datetime}' where room_no={room_no};"
                cur.execute(set_current_date_S)
                
                update_room=f"update roomdb_mogappair set occup_status='Y',occ_name='{occ_name}',days_occ='{days_booked}'where room_no={room_no};"
                cur.execute(update_room)


                tier_check_query=f"select(tier)from roomdb_annanagar where room_no={room_no}"
                cur.execute(tier_check_query)
                tier_res=cur.fetchall()
                if tier_res[0][0]==1:
                    price=250*days_booked
                elif tier_res[0][0]==2:
                    price=500*days_booked
                elif tier_res[0][0]==3:
                    price=1000*days_booked
                print(f"""                                                      BILLING:
                Date:{current_datetime}
                
                                            Name:{occ_name}
                                            Room No:{room_no}
                                            Booked from:{date_booked} |To:{date_checkout}|For:{days_booked}

                                            Price{price}""")
        
    def checkout():
        branch=int(input("Enter the branch[1]Anna Nagar [2]Mogappair [3]Exit: "))
        

        current_datetime=date.today()
        
        
      

        if branch==1:
            cur.execute("select room_no,occup_status,tier,tier_desc from roomdb_annanagar;")
            rooms=cur.fetchall()
            for i in rooms:
                table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description"])
                print(table)
                print("\n")
            room_no=int(input("Enter room no: "))
            cur.execute(f"select(occup_status)from roomdb_annanagar where room_no={room_no};")
            occup_status_check=cur.fetchall()
            occup_status_check=occup_status_check[0][0]
          
            if occup_status_check=="Y":
                  cur.execute("select(a_date_checkout)from bookings_annanagar;")
                  r=cur.fetchall()
                  r=r[0][0]
     
                  if current_datetime<r:
                      update_checkedoutEARLY=f"update bookings_allbranches set status='Checked Out', date_checkout='{current_datetime}' where room_no={room_no};"
                      cur.execute(update_checkedoutEARLY)
                
                      b_update_checkedoutEARLY=f"update bookings_annanagar set status='Checked Out', early_checkout='Y', date_checkout='{current_datetime}' where room_no={room_no};"
                      cur.execute(b_update_checkedoutEARLY)
                      update_room_checkedoutEARLY=f"update roomdb_annanagar set occup_status='N', occ_name='None',days_occ=0 where room_no={room_no};"
                      cur.execute(update_room_checkedoutEARLY)
                      print("Check Out Complte, Thanks for staying")
                  if current_datetime>r:
                      print("EXTENDED CHECKOUT")
                      update_checkedoutLATE=f"update bookings_allbranches set status='Checked Out',date_checkout='{current_datetime}' where room_no={room_no};"
                      curexecute(update_checkedoutLATE)

                      b_update_checkedoutLATE=f"update bookings_annanagar set status='Checked Out', late_checkout='Y',date_checkout='{current_datetime}' where room_no={room_no};"
                      cur.execute(b_update_checkedoutLATE)
                      
                      update_room_checkedoutLATE=f"update roomdb_annanagar set occup_status='N', occ_name='None',days_occ=0 where room_no={room_no};"
                      cur.execute(update_room_checkedoutLATE)
                      print("Check Out Complte, Thanks for staying")
                      print(f"""                                 EXTENDED CHECKOUT NOTICE
                                                The Client has overstayed/ extended their checkout for|{current_datetime-r} days|
                                                A penalty of{(current_datetime-r)*50} is to be paid""")
                      
                  else:
                       update_checkedout=f"update bookings_allbranches set status='Checked Out',date_checkout='{current_datetime}' where room_no={room_no};"
                       cur.execute(update_checkedout)
                       
                       b_update_checkedout=f"update bookings_annanagar set status='Checked Out',date_checkout='{current_datetime}' where room_no={room_no};"
                       cur.execute(b_update_checkedout)
                       update_room_checkedout=f"update roomdb_annanagar set occup_status='N', occ_name='None',days_occ=0 where room_no={room_no};"
                       cur.execute(update_room_checkedout)
                       print("Check Out Complete, Thanks for staying")
            else:
                print("Room Not Booked")
        if branch==2:
            cur.execute("select room_no,occup_status,tier,tier_desc from roomdb_mogappair;")
            rooms=cur.fetchall()
            for i in rooms:
                table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description"])
                print(table)
                print("\n")
            room_no=int(input("Enter room no: "))
            cur.execute(f"select(occup_status)from roomdb_mogappair where room_no={room_no};")
            occup_status_check=cur.fetchall()
            occup_status_check=occup_status_check[0][0]
          

            if occup_status_check=="Y":
                  cur.execute("select(a_date_checkout)from bookings_mogappair;")
                  r=cur.fetchall()
                  r=r[0][0]

                  if current_datetime<r:
                      update_checkedoutEARLY=f"update bookings_allbranches set status='Checked Out', date_checkout='{current_datetime}' where room_no={room_no};"
                      cur.execute(update_checkedoutEARLY)
                
                      b_update_checkedoutEARLY=f"update bookings_mogappair set status='Checked Out', early_checkout='Y', date_checkout='{current_datetime}' where room_no={room_no};"
                      cur.execute(b_update_checkedoutEARLY)
                      update_room_checkedoutEARLY=f"update roomdb_mogappair set occup_status='N', occ_name='None',days_occ=0 where room_no={room_no};"
                      cur.execute(update_room_checkedoutEARLY)
                      print("Check Out Complte, Thanks for staying")
                  if current_datetime>r:
                      print("EXTENDED CHECKOUT")
                      update_checkedoutLATE=f"update bookings_allbranches set status='Checked Out',date_checkout='{current_datetime}' where room_no={room_no};"
                      curexecute(update_checkedoutLATE)

                      b_update_checkedoutLATE=f"update bookings_mogappair set status='Checked Out', late_checkout='Y',cdate_checkout='{current_datetime}' where room_no={room_no};"
                      cur.execute(b_update_checkedoutLATE)
                      
                      update_room_checkedoutLATE=f"update roomdb_mogappair  set occup_status='N', occ_name='None',days_occ=0 where room_no={room_no};"
                      cur.execute(update_room_checkedoutLATE)
                      print("Check Out Complte, Thanks for staying")
                      print(f"""                                 EXTENDED CHECKOUT NOTICE
                                                The Client has overstayed/ extended their checkout for|{current_datetime-r} days|
                                                A penalty of{(current_datetime-r)*50} is to be paid""")
                  else:
                      update_checkedout=f"update bookings_allbranches set status='Checked Out',date_checkout='{current_datetime}' where room_no={room_no};"
                      cur.execute(update_checkedout)
                       
                      b_update_checkedout=f"update bookings_mogappair set status='Checked Out', date_checkout='{current_datetime}' where room_no={room_no};"
                      cur.execute(b_update_checkedout)
                      update_room_checkedout=f"update roomdb_mogappair  set occup_status='N', occ_name='None',days_occ=0 where room_no={room_no};"
                      cur.execute(update_room_checkedout)
                      print("Check Out Complte, Thanks for staying")
            else:
                print("Room not booked")
                      
     
                
           
        
    def addRoomToBranch():
        
        room_no=int(input("Enter Room No.: "))
        tier=int(input("Entet the Tier: "))
        branch=int(input("Area of the Hotel Branch:[1]Anna Nagar [2]Moggapair "))
        if area==1:
            if tier==1:
                add_query=f"insert into roomdb_annanagar(room_no,1,'Normal') values({room_no});"
                cur.execute(add_query)
                cur.execute("select*from roomdb_annanagar;")
                db=cur.fetchall()
                print("Room Added")
                for i in db:
                    table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description","Occupant Name","Days Occupied","Room Service Status"])
                    print(table)
                    print("\n")
            elif tier==2:
                add_query=f"insert into roomdb_annanagar(room_no,2,'AC') values({room_no});"
                cur.execute(add_query)
                cur.execute("select*from roomdb_annanagar;")
                db=cur.fetchall()
                print("Room Added")
                for i in db:
                    table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description","Occupant Name","Days Occupied","Room Service Status"])
                    print(table)
                
            elif tier==3:
                add_query=f"insert into roomdb_annanagar(room_no,1,'Suite') values({room_no});"
                cur.execute(add_query)
                cur.execute("select*from roomdb_annanagar;")
                db=cur.fetchall()
                print("Room Added")
                for i in db:
                    table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description","Occupant Name","Days Occupied","Room Service Status"])
                    print(table)
        if branch==2:
            if tier==1:
                add_query=f"insert into roomdb_mogappair(room_no,1,'Normal') values({room_no});"
                cur.execute(add_query)
                cur.execute("select*from roomdb_mogappair;")
                db=cur.fetchall()
                print("Room Added")
                for i in db:
                    table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description","Occupant Name","Days Occupied","Room Service Status"])
                    print(table)
            elif tier==2:
                add_query=f"insert into roomdb_mogappair(room_no,2,'AC') values({room_no});"
                cur.execute(add_query)
                cur.execute("select*from roomdb_mogappair;")
                db=cur.fetchall()
                print("Room Added")
                for i in db:
                    table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description","Occupant Name","Days Occupied","Room Service Status"])
                    print(table)
            elif tier==3:
                add_query=f"insert into roomdb_mogappair(room_no,1,'Suite') values({room_no});"
                cur.execute(add_query)
                cur.execute("select*from roomdb_mogappair;")
                db=cur.fetchall()
                print("Room Added")
                for i in db:
                    table=tabulate([i],headers=["Room No","Occupied","Tier","Tier Description","Occupant Name","Days Occupied","Room Service Status"])
                    print(table)
            

        
    def checkRoomOccupancy_RecpAction():

        branch=int(input("Enter branch:[1]Anna nagar [2]Mogappair"))
        
        if branch==1:
            room_no=int(input("Enter Room No:"))
            check_room_occupancy=f"select(status)from bookings_annanagar where room_no={room_no};"
            cur.execute(check_room_occupancy)
            room_status=cur.fetchall()
            room_status=room_status[0][0]
            check_room_occupant=f"select(occ_name)from bookings_annanagar where room_no={room_no};"
            cur.execute(check_room_occupant)
            room_occupant=cur.fetchall()
            room_occupant=room_occupant[0][0]
            print("Room No",room_no,"Status:",room_status,"Name:",room_occupant)
        if branch==2:
            room_no=int(input("Enter Room No:"))
            check_room_occupancy=f"select(status)from bookings_mogappair where room_no={room_no};"
            cur.execute(check_room_occupancy)
            room_status=cur.fetchall()
            room_status=room_status[0][0]
            check_room_occupant=f"select(occ_name)from bookings_mogappair where room_no={room_no};"
            cur.execute(check_room_occupant)
            room_occupant=cur.fetchall()
            room_occupant=room_occupant[0][0]
            print("Room_No:",room_no,"Status:",room_status,"Name:",room_occupant)
        
    def bookingDetails_branch():
        branch=int(input("Enter branch:[1]Anna Nagar [2]Mogappair "))
        if branch==1:
            showDetails=f"select*from bookings_annanagar;"
            cur.execute(showDetails)
            branchBookingDetails=cur.fetchall()
            for i in branchBookingDetails:
                print("Room No:",i[0],"\nOccupant Name:",i[1],"\nDate Booked",i[2],"\nDate checked Out",i[3],"\nDays Booked",i[4],"\nEarly Checkout?:",i[5],"\nStatus:",i[6],"\nLate Checkout:",i[7],"\nChecked Out on:",i[8],"\nDate of booking Completion:",i[9],"\n----------------")
        if branch==2:
            showDetails=f"select*from bookings_mogappair;"
            cur.execute(showDetails)
            branchBookingDetails=cur.fetchall()
            for i in branchBookingDetails:
                print("Room No:",i[0],"\nOccupant Name:",i[1],"\nDate Booked",i[2],"\nDate checked Out",i[3],"\nDays Booked",i[4],"\nEarly Checkout?:",i[5],"\nStatus:",i[6],"\nLate Checkout:",i[7],"\nChecked Out on:",i[8],"\nDate of booking Completion:",i[9],"\n----------------")
                
            

    def bookingDetails_ForPrint(x):
        if x=="Mgmt":
            cur.execute("select*from bookings_allbranches;")
            rs=cur.fetchall()
            with open("BookingsDetails_All.csv","w",newline='')as file:
                writer=csv.writer(file)
                writer.writerow(["Room No","Occ.Name","Check In Date","Checked Out on","Days Booked","Branch","Status","Date to CheckedOut","Booking Completion"])
                writer.writerows(rs)
        else:
            branch=int(input("Enter branch [1]Anna Nagar [2]Mogappair"))
            if branch==1:
                cur.execute("select*from bookings_annanagar;")
                rs=cur.fetchall()
                with open("BookingsDetails_AnnaNagar.csv","w",newline='')as file:
                    writer=csv.writer(file)
                    writer.writerow(["Room No","Occ.Name","Check In Date","Checket out on","Days Booked","Branch","Status","Date to CheckedOut","Booking Completion"])
                    writer.writerows(rs)
                print("CSV File created")
            if branch==2:
                cur.execute("select*from bookings_annanagar;")
                rs=cur.fetchall()
                with open("BookingsDetails_Mogappair.csv","w",newline='')as file:
                    writer=csv.writer(file)
                    writer.writerow(["Room No","Occ.Name","Check In Date","Check Out Date","Days Booked","Branch","Status","Date CheckedOut","Booking Time","Checkout Time","Booking Completion"])
                    writer.writerows(rs)
                print("CSV File created")
                
        
        

    def EmployeePortalFunc():
      
            ch=int(input("""
                        [1]Room Services:
                        [2]Reception:
                        [3]Higher Mgmt:
                        [4]Back"""))
             
            if ch==1:
                branchRoomServ=int(input("Enter branch:[1]Anna nagar [2] Mogappair [3]Back"))
                if branchRoomServ==1:
                    queryServ="select room_no from roomdb_annanagar where room_service_status='Y'"
                    cur.execute(queryServ)
                    ServReq=cur.fetchall()
                    print(ServReq)
                    if len(ServReq)==0:
                        print("None Requiring service at the moment.")
                    print("Requiring Service: ")
                    for i in ServReq:
                        print("Room No: ",i[0])
                    served_q=input("Press Y once served")
                    if served_q.lower()=='y':
                        print("Served")
                        served_query=f"update roomdb_annanagar set room_service_status='N';"
                        cur.execute(served_query)
                    
                if branchRoomServ==2:
                    queryServ="select room_no from roomdb_annanagar where room_service_status='Y'"
                    cur.execute(queryServ)
                    ServReq=cur.fetchall()
                    print(ServReq)
                    if len(ServReq)==0:
                        print("None Requiring service at the moment.")
                    print("Requiring Service: ")
                    for i in ServReq:
                        print("Room No: ",i[0])
                    served_q=input("Press Y once served")
                    if served_q.lower()=='y':
                        print("Served")
                        served_query=f"update roomdb_annagar set room_service_status='N';"
                        cur.execute(served_query)
                if branchRoomServ==3:
                    EmployeePortalFunc()
                    
            if ch==2:
                reception_action=int(input("""
                                              [1]Check room occupancy
                                              [2]Booking Details[Offical Purposes]
                                              [3]Check In
                                              [4]Checkout
                                              [5]Booking Details[For Print][Offical Purposes]
                                              [6]Back"""))
                if reception_action==1:
                    checkRoomOccupancy_RecpAction()
                if reception_action==2:
                    bookingDetails_branch()
                if reception_action==3:
                    bookRoom()
                if reception_action==4:
                    checkout()
                if reception_action==5:
                    bookingDetails_ForPrint("emp")
                if reception_action==6:
                    EmployeePortalFunc()
                    
                    
                                     
            if ch==3:
                mgmt_action=int(input("""
                                         [1] Add new room to branch
                                         [2]Booking Details All branches[For Print]
                                         [3]Back
                                         """))
                if mgmt_action==1:
                     MgmtPassword=input("Enter Password[Mgmt. Access]: ")
                     if MgmtPassword=="test123":
                         addRoomToBranch()
                     else:
                         print("Access Denied")
                if mgmt_action==2:
                    bookingDetails_ForPrint("Mgmt")
                if mgmt_action==3:
                    EmployeePortalFunc()
            if ch==4:
                LODGING_MAIN_UI()
                    
        
        


    option=int(input('''
            -----------------------------
            ||LODGING-MANAGEMENT SYSTEM||
            -----------------------------\n
             [1]Book Room:

             
             [2]Employee Portal[Employee Access]:


             [3]EXIT'''))
    if option==1:
        bookRoom()

    if option==2:
          EmpPassword=input("Enter password[Emp. Access: ")
          if EmpPassword=="emp123":
              EmployeePortalFunc()
    if option==3:
        exit()
       
               
                      

    conn.commit()
    cur.close()
    conn.close()
            
LODGING_MAIN_UI()        

            
            
        




