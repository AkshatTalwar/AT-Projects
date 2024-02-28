
class Interpreter:
    def __init__(self, statement_grin : list, variables : dict):
        self._statement_grin = statement_grin
        self._vars = variables

    def let(self) -> dict:
        """Assigns a value to a variable and returns the updated variable environment."""
        variable_name = self._statement_grin[1].value()
        value = self._find_value(self._statement_grin[2])
        self._vars[variable_name] = value
        return self._vars

    def print(self) -> None:
        """
        Print the value associated with the key from the _statement_grin list.
        """
        try:
            key = self._statement_grin[1].value()
            if key in self._vars:
                print(self._vars[key])
            elif self._statement_grin[1].kind().index() == 11:
                print(0)
            else:
                print(key)
        except Exception as e:
            print(e)
            exit()

    def innum(self) -> dict:
        """
        Prompts for user input and assigns the numeric value to a variable in the object's dictionary.
        """
        key = self._statement_grin[1].value()
        try:
            input_val = input()
            if '.' in input_val:
                value = float(input_val)
            else:
                value = int(input_val)
        except Exception as e:
            print(e)
            exit()
        else:
            self._vars[key] = value
            return self._vars

    def instr(self) -> dict:
        """
        Takes user input and stores it in the instance variable _vars using the key
        obtained from the second element of _statement_grin. The user is prompted to
        enter a value, which is then associated with the key in the _vars dictionary.
        """
        key = self._statement_grin[1].value()
        value = input()
        self._vars[key] = value
        return self._vars

    def _find_value(self, token_val):
        """
        Retrieve the value associated with a variable or constant token.
        """
        try:
            key = token_val.value()
            if key in self._vars:
                return self._vars[key]
            else:
                return key
        except Exception as e:
            print(e)
            exit()


    def operation_bool(self, op):
        """
        Performs a boolean operation based on the given operator.
        """
        try:
            val_a = self._find_value(self._statement_grin[3])
            val_b = self._find_value(self._statement_grin[5])
            match op:
                case '>':
                    return val_a > val_b
                case '>=':
                    return val_a >= val_b
                case '<':
                    return val_a < val_b
                case '<=':
                    return val_a <= val_b
                case '=':
                    return val_a == val_b
                case '<>':
                    return val_a != val_b
                case _:
                    print("Error Unknown Operator")
        except Exception as e:
            print(e)
            exit()

    def operation_arithematics(self, op):
        """
        Perform specified arithmetic operation on variables.
        """
        result = None
        try:
            key = self._statement_grin[1].value()
            val_a = self._vars[key]
            val_b = self._find_value(self._statement_grin[2])
            match op:
                case "ADD":
                    result = val_a + val_b
                case "SUB":
                    result = val_a - val_b
                case "MULT":
                    result = val_a * val_b
                case "DIV":
                    if type(val_a) == int and type(val_b) == int:
                        result = val_a // val_b
                    else:
                        result = val_a / val_b
                case _:
                    print("Error")
        except Exception as e:
            print(e)
            exit()
        else:
            self._vars[key] = result
            return self._vars

__all__ = [Interpreter.__name__]
