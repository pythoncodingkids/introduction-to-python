print("Please enter your first name?")
first_name = input()
print("Please enter your last name?")
last_name = input()
print("Please enter your age?")
age = int(input())

print("\nName:")
print("----")
print(first_name, last_name)

print("\nVoting eligible:")
print("----")
print(age >= 18)
