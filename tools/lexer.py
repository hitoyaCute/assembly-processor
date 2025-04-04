#!/home/hitoya/Downloads/programs/.venv/bin/activate python3
# the main main goal of lexer is to identify a patern on a text called lex and give a coresp   

import re


patterns = (
        # but not here
        ("comment",   r"\/\/.*"),
        # ("comment2",  r"/\*.*?\*/"),
        ("lcomment",  r"/\*"),
        ("rcomment",  r"\*/"),
        ("string",    r"'.*?'"),
        ("string",    r'".*?"'),
        # ("label",     r"[a-zA-Z_]+[a-zA-Z0-0_]*:(?!:)"), # labels like tag:
        ("collon",    r":"),
        ("identifier",r"\.[a-zA-Z_][a-zA-Z0-9_]*"), # anything that starts with char
        ("endline",   r"\n"),
        ("reg",       r"\$"),# $reg
        ("lbracket",  r"\b\["),# ram is just the value
        ("rbracket",  r"\]"),
        ("base",      r"0[a-z0-9][a-z0-9]*"), # to detect 0xff like or 033
        ("whitespace",r"\s+"),
        ("int",       r"[0-9]*"),
        ("opcode",    r"[a-zA-Z_][a-zA-Z0-9_]"),
        ("define",    r"\bdefine\b")
)

def tokenize(assembly:str) -> list[list[str]]:
    pos = 0
    tokens:list[list[str]] = []
    initializing = True
    while pos < len(assembly):
        match = None
        for name, pattern in patterns:
            match = re.match(pattern, assembly[pos:])
                
            if match:
                value = match.group(0)
                pos += match.end()
                if name == "whitespace":
                    break
                tokens.append([name,value])
                break
        if not match:
            raise ValueError(f"bro wtf are you doing {assembly[pos:pos+5],pos} {initializing}")
    return tokens



if __name__ == "__main__":
    # dont bash me cus this suck i know
    test = """// stuff
// bruh
// fck
// me

//comment
define sui 0xff



stuff1:
    meh $1 2 $3 0xf3[0o5]
    /* meh
    */sus .stuff1 sui
//hope this works
"""


    outp = tokenize(test)
    print(*outp,sep="\n")




















