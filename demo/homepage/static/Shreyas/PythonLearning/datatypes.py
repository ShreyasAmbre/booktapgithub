# 7 different datatypes we will learn
data1 = 10  # Number :- It is not change able because it is Immutable
data1_1 = 10.2  # Float :- It is not change able because it is Immutable
data2 = "Ten"  # String :- It is not change able because it is Immutable
data3 = True  # Boolean :- It is not change able because it is Immutable
daat4 = [1, "One", 2, "Two", ]  # List :- it is change able and Mutable, It has index value
data5 = {
    "Key1": "Computer_Data",
    "Key2": "information Technology Data",
    "Key3": "Automobile Data"
}  # Dictionary :- it is change able and Mmutable, it has index value
data6 = ("S", "B", "A")  # Tuple :- is an ordered & unchangeable & it also contain duplicate value &
data7 = {10, 20, 20, "Tiger", "Lion", "Lion", "A", "Z"}  # set datatype does not have index number

# range is use when we want to itirate the values whihc start from 0
data8 = range(10)
print(data6)
print(data7)


# ****************************************Data Types Ended*************************************************************

# type() method is used to see what type of data is present in varibale
# str(), int(), list(), dict(), set(), tuple() this methods are used in conversion datatypes to a specified datatypes

TypeConversionNumberToString = str(data2)
TypeConversionStringToNumbere = int(data1)

print(type(TypeConversionStringToNumbere))
print(type(TypeConversionNumberToString))
