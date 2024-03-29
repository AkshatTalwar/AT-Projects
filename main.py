# project3.py
#
# ICS 33 Spring 2023
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.

import grin

def main() -> None:
    input_lines = []
    while True:D
        current_line = input()
        input_lines.append(current_line)
        if current_line == '.':
            break
    try:
        parsed_tokens = list(grin.parsing.parse(input_lines))
    except Exception as e:
        print(e)
        exit()
    executor_instance = grin.run.Run(parsed_tokens)
    executor_instance.run_all_statements()


if __name__ == '__main__':
    main()
