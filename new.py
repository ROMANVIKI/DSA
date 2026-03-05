"""
Dictionary Inversion Program
CS 1101-01 - AY2026-T2
Programming Assignment Unit 7

This program inverts a dictionary that maps students to their courses,
creating a new dictionary that maps courses to enrolled students.
"""


def invert_dictionary(original_dict):
    """
    Inverts a dictionary where keys are students and values are lists of courses.

    Parameters:
    original_dict (dict): Dictionary with student names as keys and course lists as values

    Returns:
    dict: Inverted dictionary with courses as keys and student lists as values
    """
    inverted_dict = {}

    # Iterate through each student and their courses
    for student, courses in original_dict.items():
        # Iterate through each course for the current student
        for course in courses:
            # If the course is not yet a key in inverted_dict, create it with empty list
            if course not in inverted_dict:
                inverted_dict[course] = []

            # Append the student to the course's list of students
            inverted_dict[course].append(student)

    return inverted_dict


# Main program execution
if __name__ == "__main__":
    # Original dictionary: students mapped to their courses
    student_courses = {
        "Stud1": ["CS1101", "CS2402", "CS2001"],
        "Stud2": ["CS2402", "CS2001", "CS1102"],
    }

    # Display the original dictionary
    print("Original Dictionary (Students -> Courses):")
    print("-" * 50)
    for student, courses in student_courses.items():
        print(f"{student}: {courses}")

    print("\n")

    # Invert the dictionary
    course_students = invert_dictionary(student_courses)

    # Display the inverted dictionary
    print("Inverted Dictionary (Courses -> Students):")
    print("-" * 50)
    for course, students in sorted(course_students.items()):
        print(f"{course}: {students}")

    print("\n")

    # Additional verification: Display in dictionary format
    print("Inverted Dictionary in Python Format:")
    print("-" * 50)
    print(course_students)
