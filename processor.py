#!/home/hitoya/Downloads/programs/.venv/bin/python3.12

import re

import numpy as np
# this is a universal assembler that will take a file and covert it to more computer readable format

class EncodingError(Exception):
    """when you mess with the the "/" """
    pass

def assemble(inp:str, default_const: dict[str,str] | None = None) -> tuple[list[str],list[int],dict[str,str]]:
    """Inputs:
        default_definition: dict[str,str] - the default definition will be used

    returns formatted_code, indesis, settings"""
    # first split the input into lines

    reseting = True
    settings = []
    lines:list[str] = inp.split("\n")
    definitions = {}

    encoding = False

    # is multi line comment
    ismulti = False

    # if writing
    reading = True

    buffer:list[str] = []

    output_buffer:list[str] = [] 

    def save_buffer():
        output_buffer.append("".join(buffer).strip())
        buffer.clear()


    # find each marker on each line and list the marker and its starting and ending index
    for y in range(len(lines)):
        if lines[y].startswith("//") and reseting:
            settings.append(lines[y][2:].strip())
            continue
        else:
            reseting = 0
        if lines[y].startswith("define"):
            # print(",",lines[y][6:].strip(),",")
            constant, value = lines[y][6:].strip().split(" ")
            definitions[constant.strip()] = int(value)
            continue
        # surft on each char on each line
        for x in range(len(lines[y])):
            
            if lines[y][x-1:x] == "*/":
                if not ismulti:
                    raise EncodingError("fuck you dont fuck with my syntax")
                ismulti = False
            elif lines[y][x-1:x] == "//": # inline comment
                if "".join(buffer).strip()
                    save_buffer()
                break
            elif lines[y][x-1:x] == "/*":
                ismulti = True
                save_buffer()
            elif lines[y][x] == "/":
                pass

            else:
                if not reading and not lines[y][x]:
                    reading = True
                elif lines[y][x] == ",":
                    save_buffer()
                elif reading:
                    buffer.append(lines[y][x])
        save_buffer()
    if ismulti:
        raise EncodingError("wtf are you doing,did just put '*/' without '/*' ahead?")

    return output_buffer,[0],{"a":"0"}
# am tired.......
# im doomscrolling while coding lmao



#=target================state#
# definition            done
# initiazation          
# tags                  
# operation_split       
# display_index         
# comment               done
# inline_comment        done
# multi_line_comment    WIP


# input
testinp = """// emulator: CUMPU
// stuff
// defines a constant
define constA 123

// default variables
define zero 0
define largerthan 1
define lessthan 2
define equals 3
define overflow 4

// if we define a const twice it willtrow error


tag:
// indent is just nothing
  addim @0 @12 @constA // just a comment
  flag @0 @2 /*muli line comment
  cus whynot
  */
  // ',' is used to end the argument
  addim @0 12 constA, subim @0 12 constA
 

  /*random comment*/bif tag zero
"""
# output format
## ("operand operands"), (line,row_start,row_end), ("settings")
"""
(addim @0 @12 @123,
flag @0 @2,
addim @0 @2 @123,
subim @0 @12 @123,
beef 0 zero)
"""
"""
((18,1,20),
 (19,1,16),
 (20,1,19),
 (20,21,39),
 (23,19,25))
"""
"""
{"emulator":"cumpu"}
"""




if __name__ == "__main__":
    print("start")
    u = assemble(testinp)[0]

    print(*u,sep="\n")



