'''
Created on Jun 14, 2013

@author: lnunno
'''
from pyparsing import Word,alphas,Group,Optional,delimitedList,nums,oneOf,alphanums,ZeroOrMore, Regex

def hello_parser(text):
    greet = Word( alphas ) + "," + Word( alphas ) + "!" # <-- grammar defined here
    show_parse(greet, text)
    
def show_parse(parser,text):
    print text,'->',parser.parseString(text)
    
def c_function_call(text):
    variable = Word(alphanums+'_')
    show_parse(variable, 't9_a')
    cFunction = Word(alphas)+ "(" + Group( Optional(delimitedList(variable)) ) + ")"
    show_parse(cFunction, text)
    
def decimal_parse_action(s,loc,t):
    if len(t) > 1: num = t[0] + t[1] + t[2]
    else: num = t[0]
    return float(num)

def arithmetic_parser(text):
    number = Word(nums) + Optional('.' + Word(nums))
    number.setParseAction(decimal_parse_action)
    op = oneOf('+ * - / ^')
    expression = number + ZeroOrMore(op + number)
    show_parse(expression, text)
    
def email_address_parser(text):
    emailExpr = Regex(r"(?P<user>[A-Za-z0-9._%+-]+)@(?P<hostname>[A-Za-z0-9.-]+)\.(?P<domain>[A-Za-z]{2,4})")
    print emailExpr.parseString(text).dump()

if __name__ == '__main__':
    hello_parser("Hello, World!")
    c_function_call('function(a_bc,a_variable_name, 52)')
    arithmetic_parser('3.119 + 5.2333 - 100 *90.25')
    email_address_parser('lucas@gmail.com')
    
    