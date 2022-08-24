#Program 7-1
#Program to calculate the payable amount for the tent without
#functions
print( "Enter values for the cylindrical part of the tent in meters\n")
h = float(input("Enter height of the cylindrical part: "))
r = float(input("Enter radius: "))
l = float(input("Enter the slant height of the conical part in meters: "))
csa_conical = 3.14*r*l #Area of conical part
csa_cylindrical = 2*3.14*r*h #Area of cylindrical part
# Calculate area of the canvas used for making the tent
canvas_area = csa_conical + csa_cylindrical
print("The area of the canvas is",canvas_area,"m^2")
#Calculate cost of the canvas
unit_price = float(input("Enter the cost of 1 m^2 canvas: "))
total_cost= unit_price * canvas_area
print("The total cost of canvas = ",total_cost)
#Add tax to the total cost to calculate net amount payable by the
#customer
tax = 0.18 * total_cost;
net_price = total_cost + tax
print("Net amount payable = ",net_price)
