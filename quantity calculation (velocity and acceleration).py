distance = float(input("Enter distance travelled:"))
time = float(input("enter time taken:"))
quantity= input("enter quantity,acceleration(A) or velocity(V):")

velocity = distance / time
acceleration = velocity / time
if quantity == "A":
    unit = "M/S^2"
    answer = acceleration
elif quantity == "V":
    unit = "M/S"
    answer = velocity
else:
   print("please enter either A or V")
print(f"your answer is:{round(answer, 2)}{unit}")