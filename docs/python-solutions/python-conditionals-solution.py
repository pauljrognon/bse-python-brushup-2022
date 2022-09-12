#
# 1)
# Create a function called "should_work"
# it should take one parameter: "tired"
# which is a boolean.
# if tired is True, should_work should return
# False. If tired is False, should_work should
# return True. (i.e. it returns the opposite)

def should_work(tired):
    return not tired

# 2)
# Create a function called "is_even"
# that takes one parameter: "num"
# which is a number.
# It returns True if the number is even
# and False if the number is odd.
# It should raise an error if not
# given a numer
#

def is_even(num):
    if num is not None:
        return not (num % 2)
    else:
        raise Exception("The parameter doesn't exist!")

# 2)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception.

def car_at_light(light):
    instructions = {"red": "stop", "yellow": "wait", "green": "go"}
    if light == "red":
        return "stop"
    elif light == "yellow":
        return "wait"
    elif light == "green":
        return "go"
    else:
        raise Exception("Incorrect light!")

#
# 3)
# Create a function called "is_cold"
# which takes one parameter: "temperature"
# which is a number.
# If the temperature is above 15 degrees,
# it should return False,
# if it is equal or below 15 degrees,
# it should return True,
# if the temperature is not a number,
# it should raise an exception that
# says "temperature must be a number"
# (hint: you need to raise an exception
# with EXACTLY that message)

def is_cold(temperature):
    try:
        return temperature <= 15
    except:
        raise Exception("temperature must be a number")
#
# 4)
# Create a function called "wear_sweater"
# which takes two parameter: "temperature", "friolera"
# The first is a number, the second a boolean
# (which might sometimes be a None).
# If the temperature is above 15,
# it should return False,
# if it is 15 or below,
# it should return True if friolera
# is True, False if friolera is False,
# and True if friolera is None.
# (In other words, if we don't know whether
# she is a friolera or not, we should act
# cautiously and tell her to wear a sweater)
# (hint: you should use is_cold from above!)

def wear_sweater(temperature, friolera):
    return is_cold(temperature) and (friolera in [True, None])

#
# 5)
# Create a function called "equality"
# which takes three parameters: "x", "y", and "z"
# it should return the following:
# if x, y, and z are all equal --> "all are equal"
# if only x and y are equal --> "x and y are equal"
# if only z and x are equal --> "x and z are equal"
# if only y and z are equal --> "y and z are equal"
# if nothing is equal --> "nothing is equal"

def equality(x, y, z):
    ans = [-1, -1, -1]
    if x == y:
        if x == z:
            ans[0], ans[1], ans[2] = "x", "y", "z"
        else:
            ans[0] = "x"
            ans[1] = "y"
    else:
        if x == z:
            ans[0], ans[1] = "x", "z"
        elif y == z:
            ans[0], ans[1] = "y", "z"
    if ans.count(-1) == 0:
        return "all are equal"
    elif ans.count(-1) == 1:
        return " and ".join([ans[i] for i in range(len(ans)) if ans[i] != -1]) + " are equal"
    else:
        return "nothing is equal"   
     
# 6)
# Write a function for the following situation:
# Sofia can drive manual and automatic cars.
# Diego only knows how to drive automatic.
# Sofia prefers to drive long distances (> 10 km).
# Diego prefers to drive short distances.
#
# The function should be called "driver_seat"
# and should take two parameters: "distance", "is_manual".
# The first should be a number, the second should be a
# boolean. The function should return a string, which is
# the name of the person who should drive, "Diego" or "Sofia".

def driver_seat(distance, is_manual):
    names = ["Sofia", "Diego"]
    return names[int(not is_manual and distance <= 10)]