
# MECHATRONICS QUIZ APP
# Created by: Your Name
# Department: Mechatronics Engineering

# This list stores all the quiz questions and answers
questions = [
    {
        "question": "What is Mechatronics?",
        "options": [
            "Study of only mechanical systems",
            "Combination of mechanical, electrical and computer engineering",
            "Study of buildings",
            "Study of chemical substances"
        ],
        "answer": 2
    },
    {
        "question": "What is the function of a sensor?",
        "options": [
            "To detect changes in the environment",
            "To produce electricity",
            "To store information only",
            "To stop every machine"
        ],
        "answer": 1
    },
    {
        "question": "What is an actuator?",
        "options": [
            "A device that measures temperature",
            "A device that converts energy into physical movement",
            "A type of computer screen",
            "A storage device"
        ],
        "answer": 2
    },
    {
        "question": "What does PLC stand for?",
        "options": [
            "Power Logic Control",
            "Programmable Logic Controller",
            "Personal Level Computer",
            "Program Line Connection"
        ],
        "answer": 2
    },
    {
        "question": "Which of these is an input device?",
        "options": [
            "Motor",
            "Lamp",
            "Temperature sensor",
            "Speaker"
        ],
        "answer": 3
    },
    {
        "question": "Which component is commonly used to control a robot?",
        "options": [
            "Controller",
            "Water pump only",
            "Bulb",
            "Fuse only"
        ],
        "answer": 1
    },
    {
        "question": "What is the function of a microcontroller?",
        "options": [
            "To wash machines",
            "To process inputs and control outputs",
            "To produce water",
            "To increase machine weight"
        ],
        "answer": 2
    },
    {
        "question": "Which of these is an output device?",
        "options": [
            "Push button",
            "Temperature sensor",
            "Proximity sensor",
            "Electric motor"
        ],
        "answer": 4
    },
    {
        "question": "What is feedback in a control system?",
        "options": [
            "Information returned from the output for control",
            "Switching off the power supply",
            "Removing all sensors",
            "Increasing machine size"
        ],
        "answer": 1
    },
    {
        "question": "Which system operates without measuring its output?",
        "options": [
            "Closed-loop system",
            "Feedback system",
            "Open-loop system",
            "Automatic feedback system"
        ],
        "answer": 3
    }
]


# Function to calculate the percentage score
def calculate_percentage(score, total):
    return (score / total) * 100


# Function to display and mark each question
def ask_question(question_data, number):

    print("\nQuestion", number)
    print(question_data["question"])

    # Display the answer options
    for i, option in enumerate(question_data["options"], 1):
        print(i, ".", option)

    # Get and validate the student's answer
    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))

            if 1 <= answer <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    # Check the answer
    if answer == question_data["answer"]:
        print("Correct answer!")
        return True
    else:
        print("Wrong answer!")
        return False


# Main program starts here
def main():

    score = 0
    missed_questions = []

    print("===================================")
    print("       MECHATRONICS QUIZ APP")
    print("===================================")
    print("Welcome to the Mechatronics Quiz!")
    print("There are 10 questions.")
    print("Choose the correct option from 1 to 4.")

    # Loop through all the questions
    for number, question in enumerate(questions, 1):

        result = ask_question(question, number)

        if result:
            score += 1
        else:
            missed_questions.append(question)

    # Calculate the final percentage
    total = len(questions)
    percentage = calculate_percentage(score, total)

    print("\n========== QUIZ RESULT ==========")
    print("Your score:", score, "/", total)
    print("Percentage:", round(percentage, 2), "%")

    # Display the student's grade
    if percentage >= 80:
        print("Grade: A")
        print("Excellent performance!")
    elif percentage >= 60:
        print("Grade: B")
        print("Very good performance!")
    elif percentage >= 50:
        print("Grade: C")
        print("Good effort! Keep practising.")
    else:
        print("Grade: F")
        print("You need more practice.")

    # EXTRA FEATURE: Review incorrect answers
    print("\n========== ANSWER REVIEW ==========")

    if len(missed_questions) > 0:
        print("Here are the questions you missed:")

        for question in missed_questions:
            print("\nQuestion:", question["question"])
            correct = question["answer"]
            print("Correct answer:", question["options"][correct - 1])

    else:
        print("Amazing! You answered every question correctly.")

    print("\nThank you for using the Mechatronics Quiz App!")


# Run the main program
if __name__ == "__main__":
    main()
