# Part 1 - Main Version
def predict_progression(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits

    if not isinstance(pass_credits, int) or not isinstance(defer_credits, int) or not isinstance(fail_credits, int):
        return "Integer required"
    elif pass_credits not in [0, 20, 40, 60, 80, 100, 120] or \
            defer_credits not in [0, 20, 40, 60, 80, 100, 120] or \
            fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
        return "Out of range"
    elif total_credits != 120:
        return "Total incorrect"
    else:
        if pass_credits == 120:
            return "Progress"
        elif pass_credits == 100 and defer_credits == 0:
            return "Progress (module trailer)"
        elif pass_credits == 100 and defer_credits == 20:
            return "Progress (module trailer)"
        elif pass_credits == 80 and defer_credits == 40:
            return "Do not Progress – module retriever"
        elif pass_credits == 80 and defer_credits == 20 and fail_credits == 20:
            return "Do not Progress – module retriever"
        elif pass_credits == 80 and defer_credits == 0 and fail_credits == 40:
            return "Do not Progress – module retriever"
        elif pass_credits == 60 and defer_credits == 60:
            return "Do not progress – module retriever"
        elif pass_credits == 60 and defer_credits == 40 and fail_credits == 20:
            return "Do not progress – module retriever"
        elif pass_credits == 60 and defer_credits == 20 and fail_credits == 40:
            return "Do not progress – module retriever"
        elif pass_credits == 60 and defer_credits == 0 and fail_credits == 60:
            return "Do not progress – module retriever"
        elif pass_credits == 40 and defer_credits == 80:
            return "Do not progress – module retriever"
        elif pass_credits == 40 and defer_credits == 60 and fail_credits == 20:
            return "Do not progress – module retriever"
        elif pass_credits == 40 and defer_credits == 40 and fail_credits == 40:
            return "Do not progress – module retriever"
        elif pass_credits == 40 and defer_credits == 20 and fail_credits == 60:
            return "Do not progress – module retriever"
        elif pass_credits == 40 and defer_credits == 0 and fail_credits == 80:
            return "Exclude"
        elif pass_credits == 20 and defer_credits == 100:
            return "Do not progress – module retriever"
        elif pass_credits == 20 and defer_credits == 80 and fail_credits == 20:
            return "Do not progress – module retriever"
        elif pass_credits == 20 and defer_credits == 60 and fail_credits == 40:
            return "Do not progress – module retriever"
        elif pass_credits == 20 and defer_credits == 40 and fail_credits == 60:
            return "Exclude"
        elif pass_credits == 20 and defer_credits == 20 and fail_credits == 80:
            return "Exclude"
        elif pass_credits == 20 and defer_credits == 0 and fail_credits == 100:
            return "Exclude"
        elif pass_credits == 0 and defer_credits == 120:
            return "Exclude"
        elif pass_credits == 0 and defer_credits == 100 and fail_credits == 20:
            return "Exclude"
        elif pass_credits == 0 and defer_credits == 80 and fail_credits == 40:
            return "Exclude"
        elif pass_credits == 0 and defer_credits == 60 and fail_credits == 60:
            return "Exclude"
        elif pass_credits == 0 and defer_credits == 40 and fail_credits == 80:
            return "Exclude"
        elif pass_credits == 0 and defer_credits == 20 and fail_credits == 100:
            return "Exclude"
        else:
            return "Total incorrect"


# Part 2 - List (extension)
def display_data_list(student_records):
    print("\nPart 2:")
    for progression_data in student_records:
        outcome = predict_progression(*progression_data)
        print(f"{outcome} - {', '.join(str(credit) for credit in progression_data)}")


# Part 3 - Text File (extension)
def save_data_to_file(student_records, file_name):
    with open(file_name, "w") as file:
        for progression_data in student_records:
            outcome = predict_progression(*progression_data)
            data_string = f"{outcome} - {', '.join(str(credit) for credit in progression_data)}\n"
            file.write(data_string)


def read_data_from_file(file_name):
    student_records = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            progression_data = [int(credit) for credit in line.strip().split("-")[1].split(",")]
            student_records.append(progression_data)
    return student_records


# Part 4 - Dictionary (separate program)
def display_data_dictionary(student_records):
    print("\nPart 4:")
    for student_id, progression_data in student_records.items():
        outcome = predict_progression(*progression_data)
        print(f"{student_id} : {outcome} - {', '.join(str(credit) for credit in progression_data)}")


def main():
    student_records = []

    while True:
        pass_credits = input("Enter your total PASS credits: ")
        if not pass_credits.isdigit():
            print("Integer required")
            continue

        defer_credits = input("Enter your total DEFER credits: ")
        if not defer_credits.isdigit():
            print("Integer required")
            continue

        fail_credits = input("Enter your total FAIL credits: ")
        if not fail_credits.isdigit():
            print("Integer required")
            continue

        pass_credits = int(pass_credits)
        defer_credits = int(defer_credits)
        fail_credits = int(fail_credits)

        if pass_credits not in [0, 20, 40, 60, 80, 100, 120] or \
           defer_credits not in [0, 20, 40, 60, 80, 100, 120] or \
           fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range")
            continue

        outcome = predict_progression(pass_credits, defer_credits, fail_credits)
        if outcome == "Total incorrect":
            print(outcome)
            continue

        student_records.append((pass_credits, defer_credits, fail_credits))

        choice = input("Would you like to enter another set of data? (Enter 'y' for yes or 'q' to quit): ")
        if choice.lower() == "q":
            break

    # Part 2 - List (extension)
    display_data_list(student_records)

    # Part 3 - Text File (extension)
    file_name = "student_records.txt"
    save_data_to_file(student_records, file_name)
    stored_records = read_data_from_file(file_name)
    print("\nPart 3:")
    display_data_list(stored_records)

    # Part 4 - Dictionary (separate program)
    student_ids = ["w1234567", "w1234566", "w1234565", "w1234564", "w1234563"]
    student_records_dict = {student_id: progression_data for student_id, progression_data in zip(student_ids, student_records)}
    print("\nPart 4:")
    display_data_dictionary(student_records_dict)


if __name__ == "__main__":
    main()
