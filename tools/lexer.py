#!/home/hitoya/Downloads/programs/.venv/bin/activate python3
# the main main goal of lexer is to identify a patern on a text called lex and give a coresp   

import re
import time


patterns = (
        # but not here
        ("comment",   r"\/\/.*"),
        # ("comment2",  r"/\*.*?\*/"),
        # ("lcomment",  r"/\*"),
        # ("rcomment",  r"\*/"),
        ("lcomment",  r"\/\*.*?\*\/"),
        ("string",    r"'.*?'"),
        ("string",    r'".*?"'),
        ("label",     r"[a-zA-Z_][a-zA-Z0-9_]*:"), # labels like tag:
        # ("collon",    r":"), 
        ("identifier",r"[a-zA-Z_][a-zA-Z0-9_]*"), # anything that starts with char
        ("endline",   r"\n"),
        ("reg",       r"\$"),# $reg q
        ("lram",      r"\["),# ram is just the value
        ("rram",      r"\]"),
        ("base",      r"0[a-z0-9][a-z0-9]*"), # to detect 0xff like or 033
        ("whitespace",r"\s+"),
        ("tab",       r"\t+"),
        ("int",       r"\d+"),
        ("define",    r"define\b"),
        # ("opcode",    r"[a-zA-Z_][a-zA-Z0-9_]*")
)

class LexError(ValueError):
    """This error will be called whenever thers a error while tokenizing"""
    pass

def tokenize(assembly:str) -> list[list[str]]:
    pos = 0
    lpos = 0
    line = 0
    tokens:list[list[str]] = []
    initializing = True
    while pos < len(assembly):
        match = None
        for name, pattern in patterns:
            if name == "lcomment":
                match = re.match(pattern, assembly[pos:], re.DOTALL)
            else:
                match = re.match(pattern, assembly[pos:])

            if match:
                
                value = match.group(0)
                lpos += len(value)
                pos += match.end()
                
                if name in ["tab","whitespace"]:
                    name = "_"
                    value = ""

                    break
                elif name == "endline":
                    lpos = 0
                    line += 1
                    tokens.append([name,"","0","0",str(line-1)])
                else:
                    tokens.append([name,value,str(lpos-len(value)),str(lpos-1),str(line)])
                break
        if not match:
            raise LexError(f"unknow pattern found started at {line}:{lpos} >> {repr(re.match(r'^(?![\w_]+$)(.+)',assembly[pos:]).group(0))}")
    return tokens

if __name__ == "__main__":
    # dont bash me cus this suck i know
    test = """// stuff
// bruh
// fck
// me

//comment
define sui 0xff
/*meh*/ dasda*sdad sas



stuff1:
    sus $0x64
    meh $1234 22342 $3 0xf3[0o5]
    /* meh
    */sus stuff1 sui

//hope this works
"""


    outp = tokenize(test)
    print(*outp,sep="\n")
