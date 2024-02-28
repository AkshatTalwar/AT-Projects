from unittest.mock import patch

import grin
import unittest
import grin.run


class TestProgramState(unittest.TestCase):
    def test_let_statement(self):
        """
        Test Grin parser and executor for 'LET NAME "AKSHAT"'.
        Verifies that the output, after processing, is {'NAME': "AKSHAT"}.
        """
        grin_tokens =  list(grin.parsing.parse(['LET NAME "AKSHAT"' ,'.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'NAME': "AKSHAT"})

    def test_adding_number(self):
        """
        Test adding a number to a variable in Grin.

        Parses and runs Grin code to:
        1. Set A to 10: "LET A 10"
        2. Add 9 to A: "ADD A 9"
        3. Asserts output {'A': 19}.
        """
        grin_tokens = list(grin.parsing.parse(["LET A 10",'ADD A 9', '.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': 19})

    def test_substract_number(self):
        """
        Test case for subtracting a number in Grin: LET A 15, SUB A 3.
        """
        grin_tokens = list(grin.parsing.parse(["LET A 15", 'SUB A 3', '.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': 12})

    def test_adding_variableval(self):
        """
        Test Grin program: LET A=10, LET B=20, ADD A B, ADD B 2, .
        """
        grin_tokens = list(grin.parsing.parse(["LET A 10", "LET B 20", 'ADD A B','ADD B 2', '.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': 30, 'B': 22})

    def test_concatenation(self):
        """
        Test Grin concatenation: LET A "AKSHAT", ADD A " TALWAR".
        """
        grin_tokens = list(grin.parsing.parse(['LET A "AKSHAT"', 'ADD A " TALWAR"', '.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': "AKSHAT TALWAR"})

    def test_multiplication_variableval(self):
        """
        Test multiplication of variable values in Grin.
        """
        grin_tokens = list(grin.parsing.parse(['LET A 10', 'LET B 20', 'MULT A B', '.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': 200, 'B': 20})

    def test_multiplication_string(self):
        """
        Test the multiplication functionality of the GRIN language for string repetition.
        """
        grin_tokens = list(grin.parsing.parse(['LET A "AKSHAT"', 'MULT A 4', '.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': "AKSHATAKSHATAKSHATAKSHAT"})

    def test_division_multiplication(self):
        """
        Test the division and multiplication operations in the Grin language.
        """
        grin_tokens = list(grin.parsing.parse(['LET A 50', 'DIV A 5', 'MULT A 4' '.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': 40})

    def test_arithematic(self):
        """
        Test the arithmetic operations in the Grin language.
        """
        grin_tokens = list(grin.parsing.parse(['LET A 50', 'DIV A 5', 'MULT A 4' '.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': 40})

    def test_gosubtesting(self):
        """
        Test GOSUB functionality in the grin language, ensuring proper program flow and variable handling.
        """
        grin_tokens = list(grin.parsing.parse(['LET A 1', 'GOSUB 4', 'PRINT A','PRINT B','END','LET A 2','LET B 3','RETURN','.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output,)

    def test_labels_and_subroutine(self):
        """
        Test case for Grin language labels and subroutine functionality.
        """
        grin_tokens = list(grin.parsing.parse([
            'LET A 3',
            'PRINT A',
            'GOSUB "CHUNK"',
            'PRINT A',
            'PRINT B',
            'GOTO "FINAL"',
            'CHUNK:  LET A 4',
            'LET B 6',
            'RETURN',
            'FINAL:  PRINT A',
            '.'
        ]))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': 4, 'B': 6})

    def test_goto_new_testing(self):
        """
        Test the behavior of the Grin programming language interpreter when executing a program
        with LET statements, a GOTO conditional jump, and PRINT statements.
        """
        grin_tokens = list(grin.parsing.parse([
            'LET A 3',
            'LET B 5',
            'GOTO 2 IF A < 4',
            'PRINT A',
            'PRINT B',
            '.'
        ]))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': 3, 'B': 5})


    def test_gosubtesting(self):
        """
        Test the behavior of the GOSUB statement in the Grin language interpreter.
        """
        grin_tokens = list(grin.parsing.parse(['LET A 1', 'GOSUB 4', 'PRINT A','PRINT B','END','LET A 2','LET B 3','RETURN','.']))
        with self.assertRaises(SystemExit):
            output = grin.run.Run(grin_tokens).run_all_statements()

    def test_gosub_return_negative_label(self):
        """
        Tests GOSUB and RETURN statements with a negative label in GRIN.
        """
        with patch('grin.run.exit', side_effect=SystemExit) as mock_exit:
            grin_tokens = list(grin.parsing.parse([
                'LET A 1',
                'GOSUB 5',
                'PRINT A',
                'END',
                'LET A 3',
                'RETURN',
                'PRINT A',
                'LET A 2',
                'GOSUB -4',
                'PRINT A',
                'RETURN',
                '.'
            ]))
            with self.assertRaises(SystemExit):
                output = grin.run.Run(grin_tokens).run_all_statements()

            # Optionally, you can check whether exit was called
            self.assertTrue(mock_exit.called)

    def test_goto_multiple_lines(self):
        """
        Test case for evaluating the execution of multiple lines in a Grin program,
        including the use of GOTO statements.
        """
        grin_tokens = list(grin.parsing.parse(['LET A 10', 'GOTO 2', 'LET B 9', 'LET C 5' '.']))
        output = grin.run.Run(grin_tokens).run_all_statements()
        self.assertEqual(output, {'A': 10, 'C': 5})
