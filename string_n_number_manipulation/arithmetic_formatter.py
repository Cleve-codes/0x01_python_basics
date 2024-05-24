def arithmetic_arranger(problems, show_answers = False):
    # Check length of problems
    if len(problems) > 5:
        return "Error! Too many problems"

    top_line = ''
    bottom_line = ''
    dash_line = ''
    answer_line = ''

    for problem in problems:
        # Split problem into portions
        operand1 , operator , operand2 = problem.split()

        # Check if the operands are digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error! Operands must only be digits"

        # Check if operator is valid
        if operator not in ['-', '+']:
            return 'Error! Operator must be "-" or "+"'

        #Check if length of operands is more than 4
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error! Numbers should be less than 4 digits"

        # Find the maximum length of the operand for aligning
        max_length = max(len(operand1), len(operand2)) + 2

        # Add space for padding
        top_line = operand1.rjust(max_length) + "  "
        bottom_line = operator + " " + operand2.rjust(max_length - 2) + "  "
        dash_line = "-" + max_length + "  "

        # If show_answer is true, show answer
        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            answer_line += result.rjust(max_length) + "  "

        # remove the extra space at the end
        arranged_problems = top_line.rstrip() + '\n' + bottom_line.rstrip() + '\n' + dash_line.rstrip()

        # If show answers is true add the answer line
        if show_answers:
            arranged_problems += '\n' +answer_line.rstrip()

        return arranged_problems




print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')