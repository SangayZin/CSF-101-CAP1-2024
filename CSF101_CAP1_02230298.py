# References:

# 1. https://www.w3schools.com/python/python_file_handling.asp
# 2. https://www.geeksforgeeks.org/sorting-algorithms-in-python/
# 3. https://www.geeksforgeeks.org/linear-search-vs-binary-search/
# 4. https://www.w3schools.com/python/python_lists_comprehension.asp
# 5. https://www.geeksforgeeks.org/find-average-list-python/


# file path for the student data
filename = '02230298.txt'

# Step 1: Read the file data

def read_students_data(file_path):
    students_scores = []  # List to store names and scores
    
    # Open the file and read its content line by line
    with open(file_path, 'r') as file:
        # Prase the input to creat a list of (name, score) tuples
        for line in file:
            # Remove extra spaces and split on the last comma to seperate name and score
            name, score = line.strip().rsplit(',', 1)
            # Add the tuple (name, score) to the list
            students_scores.append((name, int(score)))
    
    return students_scores  # Return the data


# Task 1: Sorting Algorithms

# 1: Implementing bubble sort algorithm
# Sorts the students by score in ascending order
def bubble_sort(students_scores):
    n = len(students_scores) # Gets the total number of students

    # Outer Loop to gothrough each student
    for i in range(n):
        # Inner Loop to compare each student with the next one
        for j in range(0, n-i-1):
            #Swap if they are in worng order
            if students_scores[j][1] > students_scores[j+1][1]: #Compare scores
                students_scores[j], students_scores[j+1], students_scores[j]

    # Return the sorted list of students and their scores
    return students_scores

# 2: Implementing Insertion sort algorithm
def insertion_sort(students_scores):
    # Loop through each element starting from the second one
    for i in range(1, len(students_scores)):
        key = students_scores[i]  # The current element (name, score) tuple
        j = i - 1

        # Shift elements of the sorted part to the right if they are larger than the key's score
        while j >= 0 and students_scores[j][1] > key[1]:  # Compare scores
            students_scores[j + 1] = students_scores[j]  # Move the larger element to the right
            j -= 1

        # Place the current element (key) in its correct sorted position
        students_scores[j + 1] = key

    # Return the sorted list of students and their scores
    return students_scores

        
# Task 2: Searching Algorithms
        
 # 1: Applying linear search algorithm
    # Function to search for students with the target score.
def linear_search(students_scores, target_score):
    result = [] # To store students with the target score.
    
    # Loop through each student in the list
    for name, score in students_scores:
        # If the score matches the target score, add the student's name to the result.
        if score == target_score:
            result.append(name)

    # Return the message based on whether any matches were found.
    if result:
        return f"Students with score {target_score}: {', '.join(result)}"
    else:
        return f"No student found with score {target_score}"
    

 # 2: Applying binary search algorithm
  # Function to search for students with the target score
def binary_search(students_scores, target_score):
    # Ensure the list is sorted by score before performing binary search
    students_scores.sort(key=lambda x: x[1])  
    low, high = 0, len(students_scores) - 1  # Set initial boundaries for search
    result = []  # To store students with the target score

    # Perform binary search within the boundaries (low to high)
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        mid_score = students_scores[mid][1]  # Get the score at the middle index

        # If the middle score matches the target score
        if mid_score == target_score:
            result.append(students_scores[mid][0])  # Add the student at mid to result

            # Check left side of mid for any additional matches
            left = mid - 1
            while left >= 0 and students_scores[left][1] == target_score:
                result.append(students_scores[left][0])
                left -= 1

            # Check right side of mid for any additional matches
            right = mid + 1
            while right < len(students_scores) and students_scores[right][1] == target_score:
                result.append(students_scores[right][0])
                right += 1

            break  # Exit once all matches are found

        elif mid_score < target_score:  # If mid score is less than target, move right
            low = mid + 1
        else:  # If mid score is greater, move left
            high = mid - 1

    # Return results if any students were found, otherwise indicate no match
    if result:
        return f"Students with score {target_score}: {', '.join(result)}"
    else:
        return f"No student found with score {target_score}"
    
#Task 3: Calculating average score

 # 1: Function to calculate the average score
def calculate_average_score(students_scores):
    total_score = 0
    for name, score in students_scores:
        total_score += score  # Sum all scores

    if len(students_scores) == 0:
        return 0  # To Avoid division by zero if there are no students

    average_score = total_score / len(students_scores)  # Calculate the average
    return average_score

 # 2:Function to find the students with the lowest and highest score
def find_lowest_highest(students_scores):
    students_scores.sort(key=lambda x: x[1])  # Sort by score
    lowest_score_students = [students_scores[0][0]]  # List to store students with the lowest score
    highest_score_students = [students_scores[-1][0]]  # List to store students with the highest score

    # Check for other students with the same lowest score
    lowest_score = students_scores[0][1]  # Get the lowest score from the first student
    for name, score in students_scores[1:]:  # Loop through remaining students
        if score == lowest_score:
            lowest_score_students.append(name)  # Add student with the same lowest score
        else:
            break  # Stop if a different score is found

    # Check for other students with the same highest score
    highest_score = students_scores[-1][1]  # Get the highest score from the last student
    for name, score in reversed(students_scores[:-1]):  # Loop through students in reverse order
        if score == highest_score:
            highest_score_students.append(name)  # Add student with the same highest score
        else:
            break  # Stop if a different score is found

    # Return both the lowest and highest scoring students
    return (lowest_score_students, highest_score_students)

# Task 4 : Storing Search Result.

 # Function to write the results to an output file
def write_output_to_file(bubble_sorted, insertion_sorted, average_score, linear_search_result, binary_search_result, output_file):
    # Finds the students with the lowest and highest scores
    lowest_students, highest_students = find_lowest_highest(bubble_sorted)

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Write the average score, formatted to two decimal places
        file.write("The average score of all students is: {:.2f}\n\n".format(average_score))

        
        # Write a separator for clarity
        file.write("-" * 50 + "\n\n")

        # Write the sorted list from Bubble Sort as a formatted table
         # header for the Bubble Sort results
        file.write("Bubble Sort Results for Students:\n")
        # Format the header for the table of names and scores
        file.write("{:<20} {:<10}\n".format("Student Name", "Score"))  
        # Insert a line to clearly distinguish sections
        file.write("-" * 30 + "\n")  


        for name, score in bubble_sorted:
            file.write(f"{name:<20} {score:<10}\n")  # Write each student and score

        file.write("\n")  # Blank line for separation

        # Write the sorted list from Insertion Sort as a formatted table
        file.write("Sorted list of students (Insertion Sort):\n")
        file.write(f"{'Name':<20} {'Score':<10}\n")  # Table header
        file.write("-" * 30 + "\n")  # Separator line
        for name, score in insertion_sorted:
            file.write(f"{name:<20} {score:<10}\n")  # Write each student and score

        file.write("\n")  # Blank line for separation

        # Write the search results
        file.write("Search Results:\n")
        # Output the result from the linear search
        file.write("Result from Linear Search: {}\n".format(linear_search_result))  
        # Output the result from the binary search
        file.write("Result from Binary Search: {}\n".format(binary_search_result))  

        
        # Add a separator for readability
        file.write("\n" + "-" * 50 + "\n\n")

        # Write the names of students with the lowest score to the file
        lowest_score = bubble_sorted[0][1]  # Get the lowest score
        # Record the names of students who achieved the lowest score in the file
        file.write("Students with the minimum score ({}): {}\n".format(lowest_score, ', '.join(lowest_students)))

        # Write the names of students with the highest score to the file
        highest_score = bubble_sorted[-1][1]  # Get the highest score
        file.write("Students achieving the highest score ({}): {}\n".format(highest_score, ', '.join(highest_students)))

        
    # Print confirmation that the output was successfully written to the file
    print(f"\nOutput written to {output_file}")


# Usage
    
 # Read input data from the file
students_scores = read_students_data(filename)

 # Task 1: Sorting
bubble_sorted = bubble_sort(students_scores.copy())  # Bubble sort
insertion_sorted = insertion_sort(students_scores.copy())  # Insertion sort

 # Task 3: Calculate average score
average_score = calculate_average_score(students_scores)

 # Task 2: Search algorithms
try:
    target_score = int(input("Enter a score to search: "))  # Get user input
except ValueError:
    print("Invalid input, please enter a number.")
    exit()

 # Perform searches
linear_search_result = linear_search(students_scores, target_score)
binary_search_result = binary_search(students_scores, target_score)

 # Task 5: Write results to output file
output_filename = 'output.txt'
write_output_to_file(bubble_sorted, insertion_sorted, average_score, linear_search_result, binary_search_result, output_filename)








