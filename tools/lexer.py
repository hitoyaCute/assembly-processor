#!/home/hitoya/Downloads/programs/.venv/bin/python3.12
# the main main goal of lexer is to identify a patern on a text called lex and give a coresp   
import re

patterns = (
        ("comment",   r"\/\/.*"),
        ("lcomment",  r"(?s)\/\*.*?\*\/"),
        ("string",    r"(['\"]).*?\1"),
        ("label",     r"[a-zA-Z_][a-zA-Z0-9_]*:"), # labels like tag:
        ("identifier",r"[a-zA-Z_][a-zA-Z0-9_]*"), # anything that starts with char
        ("endline",   r"\n"),
        ("terminator",r"[\s\t\f\v]*\n"),
        ("reg",       r"\$w*"),# $reg q
        ("ram",       r"\[.*?\]"),
        ("base",      r"0[a-z0-9][a-z0-9]*"), # to detect 0xff like or 033
        ("int",       r"\d+"),
        ("define",    r"define .*"),
        ("whitespace",r"[\s\t]+"),
        ("invalid",   r".*") # match all pattern that didnt matched of previus patterns
)
class LexError(ValueError):
    """This error will be raised whenever theres a error while tokenizing"""
    pass

def tokenize(assembly:str) -> list[list[str]]:
    pos = 0
    lpos = 0
    line = 0
    tokens:list[list[str]] = []
    com =  True # is finding settings
    while pos < len(assembly):
        match = None
        name = value = ""


        for name, pattern in patterns:
            match = re.match(pattern, assembly[pos:])            
            if match:
                
                value = match.group(0)
                lpos += len(value)
                pos += match.end()
                
                if name == "invalid":
                    break
                if name in ["whitespace","endline"]:
                    break
                if com and name == "terminator":
                    com = False
                    tokens.append(["terminator","",*"000"])

                elif name == "lcomment" or name == "terminator":
                    break
                else:
                    tokens.append([name,value,str(lpos-len(value)),str(lpos-1),str(line)])
                break
        if not match or name == "invalid":
            raise LexError(f"unknow pattern found started at {line}:{lpos} >> '{value}'")
    return tokens

if __name__ == "__main__":
    # dont bash me cus this suck i know
    test = """// stuff
// bruh
// fck
// me

//comment
define sui 0xff
/*meh*/ 

"string" 'cus why not'

stuff1:
    sus $0x64
    meh $1234 22342 $3 0xf3[0o5]
    /* meh
    */sus stuff1 sui

//hope this works
"""


    outp = tokenize(test)
    print(*outp,sep="\n")
