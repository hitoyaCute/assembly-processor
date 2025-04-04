




class Parser:
    def __init__(self):
        self.tags:dict[str, str] = {}
        self.output:list[str] = []

    def parse_type(self, token):

        
    

    def parse(tokens:list[list[str]]) -> list[str]:
        is_milti_line = False
        is_meta_data = True
    
        tags:dict[str,str] = {}

        output:list[str] = []
        temp = ""

        pos = 0
        while True:
            token = tokens[pos]
            if token[0] == "tag":
                tags[token[0]] = str(pos)
            if token[0] == "identifier":
                name = tokens[0]
                if name in tags:
                    temp += f" {tags[name]}"
                else:
                    raise ValueError(f"identifier '{name}' couldn't find")
            if token[0] == "define":
                name = tokens[pos+1]
                if name[0] != "identifier":
                    raise ValueError(f"")
                value = self.
