print("\nWelcome to the Pattern Genrator and Number Analyzer\n")
print("Select an option:")
print("1.Generate a Pattern")
print("2.Analyze a Range of Numbers")
print("3.Exit")
choice_number=int(input("Enter your choice:"))
if choice_number==1:
    pattern_number=int(input("Enter your Choice for the pattern:"))
    for i in range(1,pattern_number+1):
        print("*"*i)
elif choice_number==2:
    start_number=int(input("Enter the start of range:"))
    end_number=int(input("Enter the end of range:"))
    total_sum=0
    for i in range(start_number,end_number+1):
        if i%2==0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")
        total_sum+=i
    print(f"The sum of numbers from {start_number} to {end_number} is:{total_sum}")
elif choice_number==3:
    print("Exiting the program. Goodbye!")
    
else:
    print("please enter correct option.")


 