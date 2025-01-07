# گرفتن ورودی از کاربر
number = input("یک عدد صحیح وارد کنید: ")
# بررسی و پردازش هر رقم
for digit in number:
    if digit.isdigit():  # بررسی اینکه کاراکتر وارد شده یک عدد است
        print(digit * int(digit))
    else:
        print(f"'{digit}' یک عدد نیست و رد می‌شود.")

        #عدد چاپ کن

# # گرفتن ورودی از کاربر
# number = input("یک عدد صحیح وارد کنید: ")

# # پردازش هر رقم با استفاده از ایندکس
# for i in range(len(number)):
#     if number[i].isdigit():  # بررسی اینکه کاراکتر عدد است
#         print(number[i] * int(number[i]))
#     else:
#         print(f"'{number[i]}' یک عدد نیست و رد می‌شود.")
