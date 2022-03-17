# Writing a Simple Recursive Descent Parser
# 2.19.1

expr ::= expr + term
     |   expr - term
     |   term

term ::= term * factor
     |   term / factor
     |   factor

factor ::= ( expr )
       |   NUM 


expr ::= term { (+|-) term}*

term ::= factor { (*|/) factor }*

factor ::= ( expr )
       |    NUM 


# 2.19.2
NUM + NUM * NUM 

# 2.19.3
expr ::= term { (+|-) term }*
expr ::= factor { (*|/) factor }* { (+|-) term }*
expr ::= NUM { (*|/) factor }* { (+|-) term }*
expr ::= NUM { (+|-) term }*
expr ::= NUM + term { (+|-) term }*
expr ::= NUM + factor { (*|/) factor }* { (+|-) term }*
expr ::= NUM + NUM { (*|/) factor}* { (+|-) term }*
expr ::= NUM + NUM * factor { (*|/) factor }* { (+|-) term }*
expr ::= NUM + NUM * NUM { (*|/) factor }* { (+|-) term }*
expr ::= NUM + NUM * NUM { (+|-) term }*
expr ::= NUM + NUM * NUM

# 2.19.4
import re
import collections

NUM    = r'(?P<NUM>\d+)'
PLUS   = r'(?P<PLUS>\+)'
MINUS  = r'(?P<MINUS>-)'
TIMES  = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS     = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))

Token = collections.namedtuple('Token', ['type','value'])

def generate_tokens(text):
     scanner = master_pat.scanner(text)
     for m in iter(scanner.match, None):
          tok = Token(m.lastgroup, m.group())
          if tok.type != 'WS':
               yield tok

# Parser
class ExpressionEvaluator:
     def parse(self,text):
          self.tokens = generate.tokens(text)
          self.tok = None
          self.nexttok = None
          self._advance()
          return self.expr()

     def _advance(self):
          'Advance one token ahead'
          self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

     def _accept(self, toktype):
          'Test and consume the next token if it matches toktype'
          if self.nexttok and self.nexttok.type == toktype:
               self._advance()
               return True
          else:
               return False

     def _expect(self, toktype):
          'Consume next token if it matches toktype or raise syntaxerror'
          if not self._accept(toktype):
               raise SyntaxError('Expected ' + toktype)

     def expr(self):
          "expression ::= term { ('+'|'-') term }*"
          exprval = self.term()
          while self._accept('PLUS') or self._accept('MINUS'):
               op = self.tok.type 
               right = self.term() 
               if op == 'PLUS':
                    exprval += right 
               elif op == 'MINUS':
                    exprval -= right 
                    return exprval
     def term(self):
          "term ::= factor { ('*'|'/') factor }*"
          termval = self.factor()
          while self._accept('TIMES') or self._accept('DIVIDE'):
               op = self.tok.type 
               right = self.factor() 
               if op == 'TIMES':
                    termval *= right 
               elif op == 'DIVIDE': 
                    termval /= right
                    return termval 
     def factor(self):
          "factor ::= NUM | ( expr )"
          if self._accept('NUM'):
               return int(self.tok.value)
          elif self._accept('LPAREN'): 
               exprval = self.expr() 
               self._expect('RPAREN') 
               return exprval
          else:
               raise SyntaxError('Expected NUMBER or LPAREN')