import csv
def mainmenu():
  print("------welcome to dating system------")
  while True:
    print ("""

    *********MAIN MENU**********
    FIND THE LOVE OF YOUR LIFE
    1. Register
    2. Login
    3. Search
    4. Matchmake
    5. Quit
    

    """)
    
    x=input("Enter choice:")
    if int(x)==1:
      register()
      break
    elif int(x)==2:
      login()
      break
    elif int(x)==3:
      search()
      break
    elif int(x)==4:
      matchmake()
      break
    elif int(x)==5:
      print("Goodbye!!")
      break


def register():
  print("---Register---")
  print("Sign up and tell us a little about you!")
    
  with open("dating.txt","a") as fo:
    writer=csv.writer(fo)
        
    firstname=input("Enter first name")
    lastname=input("Enter last name")
    username=firstname+lastname[0]+"-member"
    print("Your generated username is:",username)
    password=input("Enter password:")
    gender=input("Enter Gender [M/F/Other]: ")
    email=input("Enter email:")
    dob=input("Enter date of birth: dd/mm/yy:")
    beliefs=input("Enter your religion:")
    #what are your strengths.
    strengthslist=["patience","frankeness","efficiency","sensitivity","leadership","timekeeping","laidback","enthusiastic"]
    print(strengthslist)
    strengths=input("Enter your top strength [select from the list]:")
        
    writer.writerow([username,password,firstname,lastname,
              gender,email,dob,beliefs,strengths])
    print("Thank you! you have successfully registered!")
        

def login():
  print("---Login---")
  notloggedin = True
  while notloggedin==True:
    with open("dating.txt","r") as f:
      username=input("Enter username:")
      password=input("Enter password:")
      reader=csv.reader(f)
      for row in reader:
        for field in row:
          if field==username and row[1]==password:
            notloggedin=False
          else:
            break
      if notloggedin==True:
        print("Try again:")
      else:
        print("Access granted! let the dating begin!")
        
def search():
  print("---SEARCH MENU---")
  print("""
  1. Search by gender
  2. Search by keyword
  3. Return to mainmenu
  """)
    
  choice=input("What would you like to do?")
  if int(choice)==1:
    gender()
  elif int(choice)==2:
    keyword()
  elif int(choice)==3:
    mainmenu()
        
def keyword():
  print("----KEYWORD SEARCH---")
  wordfound=False
  while wordfound==False:
    with open("dating.txt","r") as f:
      keyword=input("Enter keyword:")
      reader=csv.reader(f)
      for row in reader:
        for field in row:
          if field==keyword:
            print(row)
            wordfound=True
                        
def matchmake():
  print("---MATCHMAKING MAGIC---")
  wordfound=False
  while wordfound==False:
    with open("dating.txt","r") as f:
      keystrength=input("Enter one of your key strengths:")
      print()
      print()
      print("Potential --true love-- matches:")
      reader=csv.reader(f)
      for row in reader:
        if row[8] != keystrength:
          print(row)

def gender():
  print("---Search by gender---")
  print("Narrow down the search")
  with open("dating.txt","r") as f:
    gender=input("Enter the gender you are looking for:")
    reader=csv.reader(f)
    for row in reader:
      for field in row:
        if field==gender:
          print(row)
                    
mainmenu()

    
        


    
        


    
        
