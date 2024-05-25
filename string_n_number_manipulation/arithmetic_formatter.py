def arithmetic_arranger(problems, show_answers = False):
    # Check if the number of problems is more than 5
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = ''
    bottom_line = ''
    dash_line = ''
    answer_line = ''

    for problem in problems:
        #  Split the problem into its components
        operand1 , operator , operand2 = problem.split()

        # Check if the operands are numbers
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the operator is either '+' or '-'
        if operator not in ['-', '+']:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are more than 4 digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Check the length of the operands and add the necessary spaces
        max_length = max(len(operand1), len(operand2)) + 2

        # Check the length of the top line and add the necessary spaces
        top_line += operand1.rjust(max_length) + "    "
        bottom_line += operator + " " + operand2.rjust(max_length - 2) + "    "
        dash_line += "-" * max_length + "    "

        # Check if the answer should be displayed
        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            answer_line += result.rjust(max_length) + "    "

    # Remove the trailing spaces
    arranged_problems = top_line.rstrip() + '\n' + bottom_line.rstrip() + '\n' + dash_line.rstrip()

    # Add the answer line if show_answers is True
    if show_answers:
        arranged_problems += '\n' + answer_line.rstrip()

    return arranged_problems




print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')