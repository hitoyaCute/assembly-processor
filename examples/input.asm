// emulator: CUMPU
// encoding: cumpu_CHARSET
// SIM: ram=256 word_size=8

// comment
/*so do i*/
// include "file.asm" // the emulator is the one will rpovide this
// include "builtin_lib.asm"
define var 34
define var2 18


main_:
  ldi $0 var
  // maybe let var = 4 sounds good
  ldi $1 var2
  ldi $2 add
  jump end
end:halt

