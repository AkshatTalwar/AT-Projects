import grin.parsing
import grin.token
import grin.script_interpreter


class Run:
    def __init__(self, grin_tokens):
        self.tokens = grin_tokens
        self.n = len(grin_tokens)
        self.curr_line = 0
        self._vars = {}
        self._labels = {}
        self.store_labels()
        self._return = []

    def store_labels(self):
        """
        Extracts and stores labels from tokens, associating them with line numbers.
        """
        for token in self.tokens:
            print(token)
            try:
                if token[1].kind().index() == 2:
                    line_number = token[1].location().line() - 1
                    self._labels[token[0].value()] = line_number
                    self.tokens[line_number] = self.tokens[line_number][2:]
            except:
                pass

    def run_statement(self, line_tokens):
        """
        Executes a statement based on the given line_tokens in a simple scripting language.
        """
        line_kind = line_tokens[0].kind().index()
        curr_statement = grin.script_interpreter.Interpreter(line_tokens, self._vars)
        match line_kind:
            # add/subtract/multiply/divide
            case 1 | 25 | 21 | 3:
                operation_kind = line_tokens[0].value()
                self._vars = curr_statement.operation_arithematics(operation_kind)

            # goto/gosub
            case 7 | 8:
                condition = False
                unconditional = False
                if len(line_tokens) >= 3 and line_tokens[2].kind().index() == 12:
                    operation_kind = line_tokens[4].text()
                    condition = curr_statement.operation_bool(operation_kind)
                else:
                    unconditional = True
                if condition or unconditional:
                    if line_kind == 7:
                        self._return.append(self.curr_line)
                    if line_tokens[1].kind().index() == 20:
                        try:
                            self.curr_line = self._labels[line_tokens[1].value()] - 1
                        except Exception as e:
                            print(e)
                            exit()
                    else:
                        self.curr_line += int(line_tokens[1].value()) - 1
                    if self.curr_line < 0 or self.curr_line > self.n:
                        print('ERROR')
                        exit()
            case 13: # innum
                self._vars = curr_statement.innum()
            case 14: # instr
                self._vars = curr_statement.instr()
            case 17:
                self._vars = curr_statement.let()
            case 23: # print
                curr_statement.print()
            case 24: # return statement
                try:
                    self.curr_line = self._return[-1]
                    self._return = self._return[:-1]
                except:
                    print('ERROR: Return error')
                    exit()

            case 5:
                exit()
            case _:
                print("Error")
                exit()

    def run_all_statements(self):
        """
        Executes all statements in the script until the last line is reached.
        """
        while self.curr_line < self.n:
            line_tokens = self.tokens[self.curr_line]
            self.run_statement(line_tokens)
            self.curr_line += 1
        return self._vars


__all__ = [Run.__name__]
