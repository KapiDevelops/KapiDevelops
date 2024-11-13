import sys

class MiniLanguage:
    def __init__(self):
        self.variables = {}

    def execute(self, command):
        if command.startswith("//"):
            return

        parts = command.split(" ", 1)
        if len(parts) < 2:
            return

        cmd = parts[0]
        if cmd == "say":
            print(self.evaluate_expression(parts[1]))
        elif cmd == "define":
            var_name, var_value = parts[1].split(" = ")
            self.variables[var_name.strip()] = self.evaluate_expression(var_value)
        else:
            print(f"Unknown command: {cmd}")

    def evaluate_expression(self, expression):
        expression = expression.strip()
        try:
            return eval(expression, {}, self.variables)
        except:
            return expression

    def run_all(self, commands):
        for command in commands:
            self.execute(command)


def main():
    file_path = sys.argv[1]  # Get the file path from the command line arguments

    with open(file_path, 'r') as file:
        commands = file.readlines()

    mini_lang = MiniLanguage()
    mini_lang.run_all(commands)

if __name__ == "__main__":
    main()
