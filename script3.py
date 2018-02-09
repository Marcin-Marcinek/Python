#!/usr/bin/env python3
while True:
    password = input("Please enter password:")
    if password != "hellothere":
        print("Invalid Password")
        continue
    print("Access granted")
    break
print("All the data that you wanted!")