def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = """"""
    first_nums = []
    operators = []
    second_nums = []

    for problem in problems:
        first_nums.append(problem.split()[0])
        operators.append(problem.split()[1])
        second_nums.append(problem.split()[2])

    for operator in operators:
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

    for num1, num2 in zip(first_nums, second_nums):
        try:
            int(num1)
            int(num2)
        except ValueError:
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

    for i, (num1, num2) in enumerate(zip(first_nums, second_nums)):
        if len(num1) > len(num2):
            arranged_problems += "  " + num1
        else:
            arranged_problems += (" " * (len(num2) + 2 - len(num1))) + num1

        if i != len(first_nums) - 1:
            arranged_problems += "    "
    
    arranged_problems += "\n"

    for i, (num1, num2) in enumerate(zip(first_nums, second_nums)):
        arranged_problems += operators[i]

        if len(num1) > len(num2):
            arranged_problems += (" " * (len(num1) - len(num2) + 1)) + num2
        else:
            arranged_problems += " " + num2

        if i != len(first_nums) - 1:
            arranged_problems += "    "

    arranged_problems += "\n"

    for i, (num1, num2) in enumerate(zip(first_nums, second_nums)):
        if len(num1) > len(num2):
            arranged_problems += ("-" * (len(num1) + 2))
        else:
            arranged_problems += ("-" * (len(num2) + 2))

        if i != len(first_nums) - 1:
            arranged_problems += "    "

    if display_answers:
        arranged_problems += "\n"

        for i, (num1, num2) in enumerate(zip(first_nums, second_nums)):
            if operators[i] == "+":
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))

            if len(num1) > len(num2):
                arranged_problems += (" " * (len(num1) + 2 - len(answer)))
            else:
                arranged_problems += (" " * (len(num2) + 2 - len(answer)))

            arranged_problems += answer

            if i != len(first_nums) - 1:
                arranged_problems += "    "

    return arranged_problems