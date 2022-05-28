while True:
    print("Enter 'q' to quit.")
    num_1 =input("Please enter the first number: ")
    if num_1 == 'q':
        break
    num_2 =input("Please enter the second number: ")
    if num_2 == 'q':
        break

    try:
        answer = float(num_1) + float(num_2) 

    except ValueError:
        print("The operation can not be done using a string")
        

    else:
        print(f"{num_1} + {num_2} = {answer}")
