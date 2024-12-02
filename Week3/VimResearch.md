vi( select everything in the braces the cursor is on
viw selects a word and you can paste over it. viW all text until whitespace.
Vy copy the whole line
Vyp visually yank paragraph
:r !date paste the output of date command in file
di{ delete everything in the {}
di( delete everything in the ()
de delete until end of word

1. Movement/editing/writing Hotkeys:
w	jump by start of words (punctuation considered words)
W	jump by words (spaces separate words)
e	jump to end of words (punctuation considered words)
E	jump to end of words (no punctuation)
b	jump backward by words (punctuation considered words)
B	jump backward by words (no punctuation)
0	(zero) start of line
^	first non-blank character of line
$	end of line
G	Go To command (prefix with number
i	start insert mode at cursor
I	insert at the beginning of the line
a	append after the cursor
A	append at the end of the line
o	open (append) blank line below current line 
O	open blank line above current line
ea	append at end of word
r	replace a single character (does not use insert mode)
J	join line below to the current one
cc	change (replace) an entire line
cw	change (replace) to the end of word
c$	change (replace) to the end of line
s	delete character at cursor and subsitute text
S	delete line at cursor and substitute text (same as cc)
yy	yank (copy) a line
2yy	yank 2 lines
yw	yank word
y$	yank to end of line
p	put (paste) the clipboard after cursor
P	put (paste) before cursor
dd	delete (cut) a line
dw	delete (cut) the current word
x	delete (cut) current character
:w	write (save) the file, but don't exit
:wq	write (save) and quit
:q	quit (fails if anything has changed)
:q!	quit and throw away changes

2. File/window hotkeys:
/pattern	search for pattern
?pattern	search backward for pattern
n		repeat search in same direction
N		repeat search in opposite direction
:e filename	Edit a file in a new buffer
:bnext (or :bn)	go to next buffer
:bprev (of :bp)	go to previous buffer
:bd		delete a buffer (close a file)
:sp filename	Open a file in a new buffer and split window
ctrl+ws		Split windows
ctrl+ww		switch between windows
ctrl+wq		Quit a window
ctrl+wv		Split windows vertically
