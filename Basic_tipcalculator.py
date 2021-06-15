# Basic Tip calculator script
# user will input a bill amount example:$10.52
# Suggest 3 standadrd tips 15 percent, 18 percent, 20 percent




bill_amount = (input("What is your bill amount?"))
bill_amount=bill_amount.replace("$","") #allowing user to choose to input dollar or to disregard
bill=float(bill_amount) # allowing for a float input



tip_amount_15 = float(bill * .15) #percent formula for 15%
tip_amount_18 = float(bill * .18) #percent formula for 18%
tip_amount_20 = float(bill * .20) #percent formula for 20%

print(f" You can tip either {tip_amount_15:.2f}(15%), {tip_amount_18:.2f}(18%), or {tip_amount_20:.2f}(20%)!! Thank You!") #This prints the tip amount for 15, 18 and 20 percent.



