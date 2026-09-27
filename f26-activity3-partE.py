# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 3
# Author Name: Zaima Atoshi
# Date: September 27, 2026

# SCENARIO
# A group of friends is planning a road trip and wants to estimate the
# driving time and fuel cost. Use these starting values:
# Distance: 650 km
# Average speed: 100 km/h
# Fuel efficiency: 8 L per 100 km
# Fuel price: $1.55 per litre
# Passengers: 3
# Assume constant average speed and fuel efficiency. Ignore stops,
# traffic, taxes, and other vehicle costs.

# TODO 1: Create five variables to store the trip information above.
# Give each variable a meaningful name.

# distance = input("type the distance")
# speed = input("type speed per hour")
distance = 650
speed = 100
efficiency = 8
price = 1.55
passengers = 3


# TODO 2: Calculate estimated driving time in HOURS.
# Hint: distance / average speed
time = distance / speed

# TODO 3: Calculate the total fuel needed in LITRES.
# Hint: fuel efficiency describes litres used for every 100 km.
totalfuel = float(distance/100)*efficiency

# TODO 4: Calculate the total fuel cost.
cost = totalfuel * price

# TODO 5: Use an if/else statement to check that passengers is greater
# than zero before calculating the fuel cost per passenger.
# If passengers is zero or less, print a helpful message instead.

if passengers > 0:
  result = cost / passengers
  #print ("fuel cost per passanger is: $" + str(result))
else:
  print ("error invalid passanger number")


# TODO 6: Print a readable trip summary showing:
#   - Estimated driving time (hours)
#   - Total fuel needed (litres)
#   - Total fuel cost (CAD)
#   - Fuel cost per passenger (CAD), when it can be calculated

summary = """
Summary :
- Estimated driving time {0}
- Total fuel needed {1}
- Total fuel cost {2:.2f}
- Total cost per passanger {3:.2f}""".format(time, totalfuel, cost, result)
print(summary)

# CHECK YOUR WORK
# With the starting values above, expect:
# Driving time: 6.5 hours
# Fuel needed: 52 litres
# Total fuel cost: $80.60
# Fuel cost per passenger: about $26.87
# Test again with zero passengers. Your program should not divide by zero.