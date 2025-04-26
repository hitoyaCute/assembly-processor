types = (
    ("definitions",("define","_","identifier","_","identifier,int")),
    ("operation",("identifier","#","_","ram,int,base,register","*")),
    ("systate",("comment","#","comment","endline","*")),
    ("ram",("lram","_,none","int,identifier,base","_,none","rram")),
    ("register",("reg","_","int,base,identifier"))
) 


class Parser:
    def __init__(self):
        self.tags:dict[str, str] = {}
        self.output:list[str] = []


    def parse(self,tokens:list[list[str]]) -> list[str]:
    
        tags:dict[str,str] = {}

        output:list[str] = []
        temp = ""

        pos = 0
        while True:
            token = tokens[pos]
            for par_type,par in parse:
                if token[0] == par[0]:
                    while True:
                        temp += " " + token[1]
                        pos += 1

