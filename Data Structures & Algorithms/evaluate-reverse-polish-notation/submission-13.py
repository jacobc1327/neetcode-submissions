class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        answer = 0
        operators = {"+", "-", "*", "/"}
        stack = []

        for token in tokens:
            if token in operators:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if token == "+":
                    stack.append(operand1+operand2)
                elif token == "-":
                    stack.append(operand1-operand2)
                elif token == "*":
                    stack.append(operand1*operand2)
                elif token == "/":
                    stack.append(int(operand1/operand2))
                continue
            stack.append(token)

        return int(stack[-1])