# Alinura Sultanova
# 08.18.2023

def compare_sum_with_10():
    # Get two inputs from the user
    input1 = float(input("Enter the first input: "))
    input2 = float(input("Enter the second input: "))
    
    # Calculate the sum of the inputs
    sum_inputs = input1 + input2
    
    # Compare the sum with 10 and print the result
    if sum_inputs > 10:
        print("The sum is greater than 10.")
    elif sum_inputs < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")

# Call the function to compare the sum with 10
compare_sum_with_10()
