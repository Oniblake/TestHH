class Calculator:
    def __init__(self):
        self.vars = {"x": None}
        self.operations = ["*", "+", "-", "/", "**", "(", ")", "()", "."]

    def calculate(self, equation):
        try:
            equation = equation.replace("x", str(self.vars["x"]))
            if equation.lower() == 'off':
                return "off"
            else:
                for char in equation:
                    if not (char.isnumeric() or char in self.operations):
                        if char == '!=':
                            pass
                        return Exception("Has to be an equation.")

                answer = eval(equation)
                return answer
        except Exception as Err:
            print('Invalid equation')
            return Err


c = Calculator()
while not False:
    out = c.calculate(input("$ "))
    if out == 'off':
        break
    if out != None: print(out)
