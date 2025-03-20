import re

import numpy as np

# this is a universal assembler that will take a file and covert it to more computer readable format
#



class EncodingError(Exception):
    """when you mess with the the "/" """
    pass


# default definitions
# like operands yes!! i use constant values as operand
default_definition = {"not": "0", "and": "1", "or": "2", "xor": "3", "add": "4", "sub": "5", "mul": "6", "div": "7",}



def assemble(inp:str, default_const: dict[str,str] | None = None) -> tuple[list[str],list[int,int,int],dict[str,str]]:
    """Inputs:
        default_definition: dict[str,str] - the default definition will be used

    returns formatted_code, indesis, settings"""
    # first split the input into lines
    lines = inp.split("\n")
    definitions = {}

    ismulti = False


    # find each marker on each line and list the marker and its starting and ending index
    markers = []
    for y in range(len(lines)):
        if lines[y].startswith("//"):
            continue
        if lines[y].startswith("define"):
            constant, value = lines[y].split(" ")[5:]
            definitions[constant.strip()] = int(value)
            continue
        # surft on each char on each line
        for x in range(len(lines[y])):



    

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
    u = assemble(testinp)

    print(*u,sep="\n")



