This converts a BrainF*ck code to Python code.

It expects a header to define the array size (eg. `$30` would initialize a 30 blocks wide array). If the header is not found (when the first character isn't `$`), it defaults to 30000.

Recognized caracters: 

+ \> = move pointer 1 block to the right

+ < = move pointer 1 block to the left

+ \+ = increase value stored at the block by 1

+ \- = decrease value stored at the block by 1

+ [ = starts a loop if the block the pointer is in is different than zero

+ ] = jumps back to the last [

+ , = receives a character as input

+ . = prints a character to the console

Every character that isn't listed here, except for the header, is considered a comment, so feel free to decorate your code and leave as much explanations as you need.
