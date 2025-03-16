import re

import numpy as np

# this is a universal assembler that will take a file and covert it to more computer readable format
#

class EncodingError(Exception):
    """when you fk the "/" """
    pass


def assemble(inp:str, default_const: dict | None = None) -> tuple[list[str],dict]:
    # first step cut each line
    lines: list[str] = inp.split("\n")
    line_buffer = []
    # well do pattern matching

    multi_line_comment = False
    
    reading = True
    encoding = False

    configs = False
    # surffing on each part of file
    for y in range(len(lines)):
        buffer = ""
        
        # to speed things up
        # we will skip from here
        if lines[y].startswith("//"):
            continue
        else:
            configs = True
        
        if lines[y].strip().statswith("define"): # why tf it gives error
            continue

        # line skipflag
        skip = False
        for x in range(len(lines[y])):
            char = lines[y][x]
            if multi_line_comment: # to basically do nothing if we are inside a multi line comment
                if lines[y][x-1:x] == "*/":
                    multi_line_comment = False
            elif encoding:
               if char ==  "/": # triggers a line skip aka comment
                   skip = True
                   break
               if char == "*":
                   multi_line_comment = True
            elif reading:
                if char == "/": # triggers a encoding
                    encoding = True
                    continue
                elif char == ",":
                    line_buffer.append(buffer)
                    buffer = ""
                else:
                    buffer += char

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


print("start")
outp = assemble(testinp)



if __name__ == "__mai n__":
    with open("./program/test.asm", "r") as file:
        data = file.read()
        data = assemble(data)
        with open("./program/test.casm", "w") as outp:
            print(*data[0], sep="\n")
            print(*data[0], sep="\n",file=outp)



