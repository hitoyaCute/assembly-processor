parse = (
    ("definitions", ("define","identifier","identifier,int")),
    ("operation", ("identifier","#" ,"ram,int,base,register","*")),
    ("systate", ("comment","#","comment","endline","*")),
    ("ram", ("lram","lram","int,identifier,base","rram")),
    ("register", ("reg", "int,base,identifier"))
)


class Parser:
    def __init__(self):
        self.tags:dict[str, str] = {}
        self.output:list[str] = []

    def parse_type(self, token):

        pass
    

    def parse(self,tokens:list[list[str]]) -> list[str]:
        is_milti_line = False
        is_meta_data = True
    
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

