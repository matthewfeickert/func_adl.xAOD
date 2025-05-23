from typing import List


def get_lines_of_code_qv(qv) -> List[str]:
    "Return all lines of code"

    class dummy_emitter:
        def __init__(self):
            self.Lines = []
            self._indent_level = 0

        def add_line(self, ln):
            if ln == "}":
                self._indent_level -= 1

            self.Lines += [f"{'  ' * self._indent_level}{ln}"]

            if ln == "{":
                self._indent_level += 1

        def process(self, func):
            func(self)
            return self

    d = dummy_emitter()
    qv.emit_query(d)
    return d.Lines


def get_lines_of_code(executor) -> List[str]:
    return get_lines_of_code_qv(executor.QueryVisitor)


def print_lines(lines):
    for ln in lines:
        print(ln)
