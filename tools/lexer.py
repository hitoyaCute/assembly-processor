# the main main goal of lexer is to identify a patern on a text called lex and give a coresponding
# tag to it then it will give its output to the parser

import re



lex = (
        # comment
        ("comment",r"//.*"),
        ("comment",r"/\*.*?\*/"),
        ("string",r"'.*?'"),
        ("string",r'".*?"'),
        ("label",r"[a-zA-Z_][a-zA-Z0-0_]*:(?!:)"), # labels like tag:
        ("identifier",r"[a-zA-Z_][a-zA-Z0-9_]*"), # anything that starts with char
        
)



# 








