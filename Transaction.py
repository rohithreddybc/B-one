import requests

flag=0
pin=1234

balance=20000
def goto(linenum):
    global line
    line = linenum

line = 0
while True:  
  if line == 0:
    amount=int(input("Enter amount:"))
    goto(3)
  elif line ==3:
    PIN=int(input("Enter PIN:"))
    goto(1)
  elif line == 1:
    if(amount<=10000):
      if(PIN==pin):
        balance=balance-amount
        flag=1
        break
      else:
        print("Incorrect PIN")
        use1=str(input("Do u want to Re enter PIN - y or n:"))
        if(use1=='y') :
          goto(3)
        else :
          break;
    else : 
      goto(2)
  elif line == 2:
    if(PIN==pin):
      if(amount>10000):
        if(amount<=balance):
          request = requests.get('https://2factor.in/API/V1/4ad183d9-07a2-11ea-9fa5-0200cd936042/SMS/8296432455/AUTOGEN')
          print("otp sent")
          goto(4)
        elif(amount>balance):
          print("Insufficient Balance")
          use2=str(input("Do u want to continue - y or n:"))
          if(use2=='y') :
           goto(0)
          else :
           break;
    else:
      print("Incorrect PIN")
      use3=str(input("Do u want to Re enter PIN - y or n:"))
      if(use3=='y') :
        goto(3)
      else :
        break;
  elif line == 4 :
    use=str(input("Enter OTP:"))
    data=request.json()
    request2 = requests.get('https://2factor.in/API/V1/4ad183d9-07a2-11ea-9fa5-0200cd936042/SMS/VERIFY/'+data["Details"]+'/'+use)      
    if(request2.status_code==200): 
      balance=balance-amount
      flag=1
      break
    else:
      print("Incorect otp")
      use4=str(input("Do u want to Re enter OTP - y or n"))
      if(use4=='y') :
        goto(4)
      else :
        break;   
if(flag==1):
  print('Balance:',balance)
  print("Transaction Successful")
else:
  print("Transaction Failed")