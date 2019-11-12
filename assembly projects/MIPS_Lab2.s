jal main
#                                           ICS 51, Lab #2
# 
#                                          IMPORTATNT NOTES:
# 
#                       Write your assembly code only in the marked blocks.
# 
#                     DO NOT change anything outside the marked blocks.
# 
#                      Remember to fill in your name, student ID in the designated sections.
# 
#
j main
###############################################################
#                           Data Section
.data
# 
# Fill in your name, student ID in the designated sections.
# 
student_name: .asciiz "Christopher Lam"
student_id: .asciiz "29545944"

new_line: .asciiz "\n"
space: .asciiz " "
gets: .asciiz " -> "
testing_label: .asciiz "\nTesting "
unsigned_addition_label: .asciiz "64-bit Unsigned Addition \n"
fibonacci_label: .asciiz "Fibonacci \n"
file_label: .asciiz "File read \n"
file:
	.asciiz	"lab2_data.dat"	# File name
	.word	0
fib_array: 
	.space	48
buffer:
	.space	300			# Place to store character

num_tests: .word 3
addition_test_data_A:	.word 0xeee94560, 0x0154a8d0, 0x09876543, 0x000ABABA, 0xFEABBAEF, 0x00a9b8c7
addition_test_data_B:	.word 0x18002e00, 0x0000102a, 0x12349876, 0xBABA0000, 0x93742816, 0x0000d6e5

unsigned_add_64bit_lbl: .asciiz "Expected output:\n0154B8FB06E97360 BAC4BABA1BBBFDB9 00AA8FAD921FE305\nObtained output:\n"
fibonacci_lbl: 	.asciiz "Expected output:\n5 13 55\nObtained output:\n"
file_read_lbl1: .asciiz "Expected output:\n6\nI love ics51...\nI am so glad that i am taking ics 51...\n"
file_read_lbl2:	.asciiz	"AND i love assembly language.\nEVEN more than i love java or c or pyhton\n"
file_read_lbl3: .asciiz "BECAUSE it is such fun\nTHIS was a success.\nObtained output:\n"

hex_digits: .byte '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'

###############################################################
#                           Text Section
.text
# Utility function to print hexadecimal numbers
print_hex:
move $t0, $a0
li $t1, 8 # digits
lui $t2, 0xf000 # mask
mask_and_print:
# print last hex digit
and $t4, $t0, $t2 
srl $t4, $t4, 28
la    $t3, hex_digits  
add   $t3, $t3, $t4 
lb    $a0, 0($t3)            
li    $v0, 11                
syscall 
# shift 4 times
sll $t0, $t0, 4
addi $t1, $t1, -1
bgtz $t1, mask_and_print
exit:
jr $ra
###############################################################
###############################################################
###############################################################
#                           PART 1 (Unsigned Addition)
# You are given two 64-bit numbers A,B located in 4 registers
# $t0 and $t1 for lower and upper 32-bits of A and $t2 and $t3
# for lower and upper 32-bits of B, You need to store the result
# of the unsigned addition in $t4 and $t5 for lower and upper 32-bits.
#
unsigned_add_64bit:
move $t0, $a0
move $t1, $a1
move $t2, $a2
move $t3, $a3
############################## Part 1: your code begins here ###
addu $t4, $t0, $t2
sltu $t5, $t4, $t2
addu $t5, $t5, $t1
addu $t5, $t5, $t3
############################## Part 1: your code ends here   ###
move $v0, $t4
move $v1, $t5
jr $ra
###############################################################
###############################################################
###############################################################

###############################################################
###############################################################
###############################################################
#                            PART 2 (Fibonacci)
#
# 	The Fibonacci Sequence is the series of numbers:
#
#		0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

#	The next number is found by adding up the two numbers before it.
	
#	The 2 is found by adding the two numbers before it (1+1)
#	The 3 is found by adding the two numbers before it (1+2),
#	And the 5 is (2+3),
#	and so on!
#
# You should first compute the twelve elements of fibonacci and put
# in array. The base address of this array is in $a0.
# Then print fib(5), fib(7), fib(10) in one line.
# 
fibonacci:
la $a0, fib_array
############################## Part 2: your code begins here ###
li $t0, 0
li $t1, 0
li $t2, 1
li $t4, 3
li $t5, 0
sw $t1, ($a0)
addi $a0, $a0, 4
sw $t2 ($a0)
fib_store:
bgt $t4, 13, fib_store_end
addi $a0, $a0, 4
add $t5, $t2, $t1
move $t1, $t2
move $t2, $t5
sw $t5, ($a0)
addi $t4, $t4, 1
j fib_store
fib_store_end:
la $t7, fib_array
lw $t6, 20($t7)
move $a0, $t6
li $v0, 1
syscall
la $a0, space
li $v0, 4
syscall
lw $t6, 28($t7)
move $a0, $t6
li $v0, 1
syscall
la $a0, space
li $v0, 4
syscall
lw $t6, 40($t7)
move $a0, $t6
li $v0, 1
syscall
############################## Part 2: your code ends here   ###
jr $ra
###############################################################
###############################################################
###############################################################

###############################################################
###############################################################
###############################################################
#                           PART 3 (ReadFile)
#
# You will read characters (bytes) from a file (lab2_data.dat) and print them. Valid characters are defined to be
# alphanumeric characters (a-z, A-Z, 0-9),
# " " (space),
# "_" (underscore) character,
# "." (period),
# "!" (exclamation point),
# and "?" (question mark).
# All punctuation marks should be converted to "." (period).
# First word of a line should be written with Uppercase letters and the rest with lowercase letters.
# Invalid characters should be discarded.
# You should print number of lines read from the file and then echo string of each line after modification based on the rules above.
# $a1 : address of the input buffer
#
file_read:

# Open File

	li	$v0, 13			# 13=open file
	la	$a0, file		# $a2 = name of file to read
	add	$a1, $0, $0		# $a1=flags=O_RDONLY=0
	add	$a2, $0, $0		# $a2=mode=0
	syscall				# Open FIle, $v0<-file descriptor (fd)
	add	$s0, $v0, $0	# store fd in $s0
	
# Read file and store it in the buffer

	li	$v0, 14			# 14=read from  file
	add	$a0, $s0, $0	# $s0 contains fd
	la	$a1, buffer		# buffer to hold string
	li	$a2, 300		# Read 300 characters
	syscall

############################### Part 3: your code begins here ##
li $t0, 0
lb $t2, new_line
num_lines: 
lbu $t1, ($a1)
addi $a1, $a1, 1
beq $t1, $zero, start_print
beq $t1, $t2, line_count
j num_lines
line_count: #counts the numbers of line
addi $t0, $t0, 1
j num_lines
start_print: #starts to print
li $t5, 1
move $a0, $t0
li $v0, 1
syscall
move $a0, $t2
li $v0, 11
syscall
la $a1, buffer
print_loop: #starts the print loop
lbu $t4, ($a1)
addi $a1, $a1 1
beq $t4, $zero, endprint
beq $t4, 0x20, print_space
beq $t4, $t2, print_new_line
beq $t4, 0x2E, print_period
beq $t4, 0x21, print_period
beq $t4, 0x3F, print_period
bge $t4, 0x41, capsalpha
bge $t4, 0x30, print_num
j print_loop
capsalpha:
bgt $t4, 0x5A, capslower
beq $t5, 0, print_lower
j print_charc
capslower:
blt $t4, 0x60, print_loop
bgt $t4, 0x7A, print_loop
beq $t5, 1, print_caps
move $a0, $t4
li $v0, 11
syscall
j print_loop
print_space:
li $t5, 0
move $a0, $t4
li $v0, 11
syscall
j print_loop
print_new_line:
li $t5, 1
j print_charc
print_period:
li $a0, 0x2E
li $v0, 11
syscall
j print_loop
print_caps:
addi $t4, $t4, -32
j print_charc
print_lower:
addi $t4, $t4, 32
j print_charc
print_charc:
move $a0, $t4
li $v0, 11
syscall
j print_loop
print_num:
bge $t4 0x39, print_loop
j print_charc
endprint:
############################### Part 3: your code ends here   ##
# Close File

done:
	li	$v0, 16			# 16=close file
	add	$a0, $s0, $0	# $s0 contains fd
	syscall				# close file

jr $ra
###############################################################
###############################################################
###############################################################

#                          Main Function
.globl main
main:

li $v0, 4
la $a0, student_name
syscall
la $a0, new_line
syscall  
la $a0, student_id
syscall 
la $a0, new_line
syscall
##############################################
##############################################
test_64bit_Add_Unsigned:
lw $s0, num_tests
li $s1, 0
la $s2, addition_test_data_A
la $s3, addition_test_data_B
li $v0, 4
la $a0, testing_label
syscall
la $a0, unsigned_addition_label
syscall
la $a0, unsigned_add_64bit_lbl
syscall
##############################################
test_add:
add $s4, $s2, $s1
add $s5, $s3, $s1
# Pass input parameter
lw $a0, 0($s4)
lw $a1, 4($s4)
lw $a2, 0($s5)
lw $a3, 4($s5)
jal unsigned_add_64bit

move $s6, $v0
move $a0, $v1
jal print_hex
move $a0, $s6
jal print_hex

li $v0, 4
la $a0, space
syscall

addi $s1, $s1, 8
addi $s0, $s0, -1
bgtz $s0, test_add
##############################################
##############################################
test_fibonacci:
li $v0, 4
la $a0, new_line
syscall
li $v0, 4
la $a0, testing_label
syscall
la $a0, fibonacci_label
syscall
la $a0, fibonacci_lbl
syscall
jal fibonacci
##############################################
##############################################
test_file_read:
li $v0, 4
la $a0, new_line
syscall
li $s0, 0
li $v0, 4
la $a0, testing_label
syscall
la $a0, file_label
syscall
la $a0, file_read_lbl1
syscall
la $a0, file_read_lbl2
syscall
la $a0, file_read_lbl3
syscall
jal file_read
end:
# end program
li $v0, 10
syscall
