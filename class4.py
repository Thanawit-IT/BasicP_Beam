# def Grade (score) :
#     if score >= 80 :
#         print("Grade A")
#     elif score >= 70 :
#         print("Grade B")
#     elif score >= 60 :
#         print("Grade C")

# for i in range(3) :
#     input_score = int(input("กรอกคะเเนน : "))

#     Grade(input_score)    

# def my_sum (a,b) :
#     return a+b

# result = my_sum(5,5)
# print(result)

# def Menu () :

#     Choice = int(input("[1]. เลือกคำนวณราคาสินค้า , [2]. ออก : "))
#     return Choice

# def Calculate(num,Price) :

#     sum = 0
#     for i in range(num) :
#         sum += Price
#     vat = (sum * 7) / 100
#     return sum + vat


# while True :
#     Choice_Result = Menu()

#     if Choice_Result == 1 :

#         input_range = int(input("กรอกจำนวนสินค้า : "))
#         input_price = int(input("กรอกราคาสินค้า : "))
#         Result = Calculate(input_range,input_price)
#         print("Result : ",Result)

#     if Choice_Result == 2 :

#         print("ออกเเล้ว")
#         break

# my_List = [1, 2 , "BEAmE"]

# for i in my_List:
#     print(i)

# Dict = {

#     "Thailand" : "Bangkok"

# }

# Dict["France"] = "Paris"
# Dict["Thailand"] = "Osaka"
# print(Dict)

students = [

    {"Name" : "Beam" ,"ID" : 1 ,"Age" : 18},
    {"Name" : "Fourcuz" ,"ID" : 2 ,"Age" : 18},
    {"Name" : "Pond" ,"ID" : 3 ,"Age" : 18}

]

for student in students :
    print("Name:" + student["Name"],"ID: " + str(student["ID"]),"Age: " + str(student["Age"]))