import json

def exprCheck(expr):
    stack = []
    for char in expr:
        if (char == "(" ):
            stack.append(char)
        elif((char == ")")and stack):
            stack.pop()
    if stack:
        return False
    else:
        return True

def bracketRemover(expr):
    for i in range(len(expr)-2):
        if(expr[i] == '(' and expr[i+1] == '('):
            expr = expr[i+1:]
        if(expr[i] == ')' and expr[i+1] == ')'):
            expr = expr[:i+1]
    return expr
    
def evalExpr(expr,index):
    item = {}
    title = ""
    list = []
    while index < len(expr):
        if (expr[index] == '('):
            temp,index= evalExpr(expr,index+1)
            list.append(temp)
        elif(expr[index] == '&'):
            title = 'and'
        elif(expr[index] == '|'):
            title = 'or'
        elif(expr[index] == '='):
            item[expr[index-1]] = expr[index+1]
        elif(((expr[index] == ')'))and( title != "")):
            list.append({title:item})
            return list,index
        index+=1
    return {title : list},index 
    
    
if __name__ == '__main__':
    expr = input("Enter Expression: ")
    is_valid = exprCheck(expr)
    if(is_valid):
        expr = bracketRemover(expr)
        result,temp = evalExpr(expr,0)
        result = dict(query=result) 
        json_object = json.dumps(result, indent = 4)
        print("Expression in JSON Format: ")
        print(json_object)
    else: 
        print("Syntax invalid")
