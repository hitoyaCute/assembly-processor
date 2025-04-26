__settings__
__SIM 
ram=256
word_size=8
SIM__

__definitions__
var 34
var2 18
__start__
ldi $0 var    // 0
ldi $1 var2   // 1
ldi $2 add    // 2
jump 4        // 3
halt          // 4
