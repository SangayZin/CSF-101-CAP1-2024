# References:
# 1. "Python File Handling" - W3Schools: https://www.w3schools.com/python/python_file_handling.asp
# 2. "Python Sorting Algorithms" - GeeksforGeeks: https://www.geeksforgeeks.org/sorting-algorithms-python/
# 3. "Python Linear Search and Binary Search" - Programiz: https://www.programiz.com/python-programming/searching-algorithms
# 4. "Python List Comprehensions" - Real Python: https://realpython.com/list-comprehensions-python/
# 5. "How to Calculate Average in Python" - GeeksforGeeks: https://www.geeksforgeeks.org/python-program-to-calculate-average-of-numbers-in-a-given-list/


# file path
filename = '02230298.txt'

# Step 1:Read the file data
def read_students_data(file_path):
    students_scores = []
    with open(file_path, 'r') as file:
        students = file.readlines()  # Reads all lines in the file

    # Parse the input to create a list of (name, score) tuples
    for student in students:
        name, score = student.strip().rsplit(',', 1)  # Split on the last comma
        students_scores.append((name, int(score)))     # Append tuple (name, score)

    return students_scores

# Task 1: Sorting Algorithms

# Step 1: Implementing bubble sort algorithm
    # Sorts the student by score.
def bubble_sort(students_scores):
    n = len(students_scores)

    for i in range(n):
        for j in range(0, n-i-1):
            if students_scores[j][1] > students_scores[j+1][1]:  # Compare scores
                # Swap if the curreent score is greater than the next
                students_scores[j], students_scores[j+1] = students_scores[j+1], students_scores[j]
    return students_scores

# Step 2: Implementing insertion sort algorithm
def insertion_sort(students_scores):
    # Loop through each element starting from the second one
    for i in range(1, len(students_scores)):
        key = students_scores[i]  # Current element (name, score) tuple
        j = i - 1

        # Shift element of the sorted part if they are larger than the key's score, one position ahead
        while j >= 0 and students_scores[j][1] > key[1]:  # Compare scores
            students_scores[j + 1] = students_scores[j]    # Shift larger element to the right
            j -= 1

        students_scores[j + 1] = key  # Insert key in its correct position

    return students_scores

# Task 2: Searching Algorithms

# Step 1: Applying linear search algorithm
def linear_search(students_scores, target_score):
    result = []
    for name, score in students_scores:
        if score == target_score:
            result.append(name)
    
    if result:
        return f"Students with score {target_score}: {', '.join(result)}"
    else:
        return f"No student found with score {target_score}"

# Step 2: Applying binary search algorithm
def binary_search(students_scores, target_score):
    students_scores.sort(key=lambda x: x[1])  # Ensure the list is sorted by score
    low, high = 0, len(students_scores) - 1
    result = []

    while low <= high:
        mid = (low + high) // 2
        mid_score = students_scores[mid][1]

        if mid_score == target_score:
            result.append(students_scores[mid][0])
            left = mid - 1
            while left >= 0 and students_scores[left][1] == target_score:
                result.append(students_scores[left][0])
                left -= 1
            right = mid + 1
            while right < len(students_scores) and students_scores[right][1] == target_score:
                result.append(students_scores[right][0])
                right += 1
            break
        elif mid_score < target_score:
            low = mid + 1
        else:
            high = mid - 1

    if result:
        return f"Students with score {target_score}: {', '.join(result)}"
    else:
        return f"No student found with score {target_score}"

# Task 3: Calculating average score

# Step 1: Function to calculate the average score
def calculate_average_score(students_scores):
    total_score = 0
    for name, score in students_scores:
        total_score += score  # Sum all scores

    if len(students_scores) == 0:
        return 0  # To Avoid division by zero if there are no students

    average_score = total_score / len(students_scores)  # Calculate the average
    return average_score

# Step 2: Function to find the student(s) with the lowest and highest score
def find_lowest_highest(students_scores):
    students_scores.sort(key=lambda x: x[1])  # Sort by score
    lowest_score_students = [students_scores[0][0]]  # List to store students with the lowest score
    highest_score_students = [students_scores[-1][0]]  # List to store students with the highest score

    # Check for other students with the same lowest score
    lowest_score = students_scores[0][1]
    for name, score in students_scores[1:]:
        if score == lowest_score:
            lowest_score_students.append(name)
        else:
            break

    # Check for other students with the same highest score
    highest_score = students_scores[-1][1]
    for name, score in reversed(students_scores[:-1]):
        if score == highest_score:
            highest_score_students.append(name)
        else:
            break

    return (lowest_score_students, highest_score_students)

# Step 3: Function to write the output to a file
def write_output_to_file(bubble_sorted, insertion_sorted, average_score, linear_search_result, binary_search_result, output_file):
    lowest_students, highest_students = find_lowest_highest(bubble_sorted)

    with open(output_file, 'w') as file:
        # Write the average score
        file.write(f"Average score of students: {average_score:.2f}\n\n")
        
        # Write a separator for clarity
        file.write("-" * 50 + "\n\n")

        # Write the sorted list from Bubble Sort as a table
        file.write("Sorted list of students (Bubble Sort):\n")
        file.write(f"{'Name':<20} {'Score':<10}\n")  # Header
        file.write("-" * 30 + "\n")  # Separator
        for name, score in bubble_sorted:
            file.write(f"{name:<20} {score:<10}\n")  # Row format

        file.write("\n")

        # Write the sorted list from Insertion Sort as a table
        file.write("Sorted list of students (Insertion Sort):\n")
        file.write(f"{'Name':<20} {'Score':<10}\n")  # Header
        file.write("-" * 30 + "\n")  # Separator
        for name, score in insertion_sorted:
            file.write(f"{name:<20} {score:<10}\n")  # Row format

        file.write("\n")

        # Write the search results
        file.write("Search Results:\n")
        file.write(f"Linear Search Result: {linear_search_result}\n")
        file.write(f"Binary Search Result: {binary_search_result}\n")
        
        file.write("\n" + "-" * 50 + "\n\n")  # Separator

        # Write the students with the lowest score
        file.write(f"Students with the lowest score ({bubble_sorted[0][1]}): {', '.join(lowest_students)}\n")

        # Write the students with the highest score
        file.write(f"Students with the highest score ({bubble_sorted[-1][1]}): {', '.join(highest_students)}\n")

    print(f"\nOutput written to {output_file}")


# Usage

# Read the input data from the file
students_scores = read_students_data(filename)

# Task 1: Sorting Algorithms
bubble_sorted = bubble_sort(students_scores.copy())  # Sort the data using bubble sort
insertion_sorted = insertion_sort(students_scores.copy())  # Sort the data using insertion sort

# Task 3: Calculate the average score of all students
average_score = calculate_average_score(students_scores)

# Task 2: Searching Algorithms
# Ask the user for the target score
try:
    target_score = int(input("\nEnter the score to search for: "))  # Get input from the user
except ValueError:
    print("Please enter a valid integer score.")
    exit()

# Apply linear search
linear_search_result = linear_search(students_scores, target_score)

# Apply binary search
binary_search_result = binary_search(students_scores, target_score)

# Task 5: Write sorted list, average score, search results, and lowest/highest scores to output file
output_filename = 'output.txt'
write_output_to_file(bubble_sorted, insertion_sorted, average_score, linear_search_result, binary_search_result, output_filename)
