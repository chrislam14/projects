#                                           ICS 51, Lab #1
# 
#                                          IMPORTATNT NOTES:
# 
#                       Write your assembly code only in the marked blocks.
# 
#                       DO NOT change anything outside the marked blocks.
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
count_ones_lbl: .asciiz "\nCount Ones \nExpected output:\n20 24 13\nObtained output:\n"
bcd_2_bin_lbl: .asciiz "\nBCD to Binary (Hexadecimal Values)\nExpected output:\n004CC853 00BC614E 00008AE0\nObtained output:\n"
bin_2_bcd_lbl: .asciiz "\nBinary to BCD (Hexadecimal Values) \nExpected output:\n05032019 06636321 00065535\nObtained output:\n"

count_ones_test_data:  .word 0xBABABABA, 0xFEABBAEF, 0x09876543

bcd_2_bin_test_data: .word 0x05032019, 0x12345678, 0x35552

bin_2_bcd_test_data: .word 0x4CC853, 0x654321, 0xFFFF

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
#                            PART 1 (Count Bits)
# 
# You are given a 32-bits integer stored in $t0. Count the number of 1's
#in the given number. For example: 1111 0000 should return 4
count_ones:
move $t0, $a0 
############################ Part 1: your code begins here ###
li $t1, 1 #constant for comparison
li $t2, 0 #temp storage for calculations
li $t3, 0 #holds the final result
li $t4, 32 #run counter
start:
ble $t4, $zero, end #jumps to end if the counter is zero
and $t2, $t1, $t0 #masks all but the least significant bit
bgt $t2, $zero, count #jumps to count if result is 1
addi $t4, $t4, -1 #subtracts one from counter
srl $t0, $t0, 1 #shifts input to the right to analyze the next bit
j start 
count:
addi $t3, $t3, 1 #adds 1 to the final result
addi $t4, $t4, -1 #subtracts 1 form the counter
srl $t0, $t0, 1 #shifts input to the right to analyze the next bit
j start
end:
move $t0, $t3
############################ Part 1: your code ends here ###
move $v0, $t0
jr $ra

###############################################################
###############################################################
###############################################################

###############################################################
###############################################################
###############################################################
#                            PART 2 (BCD to Binary)
# 
# You are given a 32-bits integer stored in $t0. This 32-bits
# present a BCD number. You need to convert it to a binary number.
# For example: 0x7654_3210 should return 0x48FF4EA.
# The result must be stored inside $t0 as well.
bcd2bin:
move $t0, $a0
############################ Part 2: your code begins here ###
li $t1, 15 #for masking all but least significant nibble
li $t2, 0 #temp storage for comparisons
li $t3, 8 #run counter for 8 runs
li $t4, 0 #holds final result
li $t5, 1 #multiplier for 10
li $t6, 10 #ten constant for multiplying result by tenths
start2:
ble $t3, $zero, end2 #end of counter
and $t2, $t1, $t0 #masks all but least signifcant nibble 
mult $t2, $t5 #multiplies by 10eN to add to the final number
mflo $t2 #loads answer into $t2
add $t4 $t4, $t2 #adds $t2 to the final result
mult $t5, $t6 #multiplies by 10 bc of BCD
mflo $t5
srl $t0, $t0, 4 #shifts by 4 to access the next nibble
addi $t3, $t3, -1 #counter goes down 1
j start2
end2:
move $t0, $t4
############################ Part 2: your code ends here ###
move $v0, $t0
jr $ra

###############################################################
###############################################################
###############################################################
#                            PART 3 (Binary to BCD)
# 
# You are given a 32-bits integer stored in $t0. This 32-bits
# present an integer number. You need to convert it to a BCD.
# The result must be stored inside $t0 as well.
bin2bcd:
move $t0, $a0
############################ Part 3: your code begins here ###
li $t1, 0x80000000 #masking variable
li $t2, 32 #run counter
li $t3, 0x00000000 #holds final result
li $t4, 0 #variable for intermediate calculations
start3:
ble $t2, 0, end3
j checkfor4
returnfromcheck:
and $t4, $t1, $t0
sll $t3, $t3, 1
srl $t1, $t1, 1
addi $t2, $t2, -1
bgt, $t4, $zero, shift
j start3
shift:
or $t3, $t3, 1
j start3
checkfor4:
li $t5, 0x0000000F
li $t6, 0x33333333
li $t7, 0x44444444
li $t8, 0 
li $t9, 8
start4:
ble $t9, $zero, returnfromcheck
and $t4, $t5, $t3
and $t8, $t7, $t5
addi $t9, $t9, -1
bgt $t4, $t8, plus3
sll $t5, $t5, 4
j start4
plus3:
and $t8, $t6, $t5
add $t3, $t3, $t8
sll $t5, $t5, 4
j start4
end3:
move $t0, $t3
############################ Part 3: your code ends here ###
move $v0, $t0
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
la $a0, count_ones_lbl
syscall

# Testing part 1
li $s0, 3 # num of test cases
li $s1, 0
la $s2, count_ones_test_data

test_p1:
add $s4, $s2, $s1
# Pass input parameter
lw $a0, 0($s4)
jal count_ones

move $a0, $v0        # $integer to print
li $v0, 1
syscall

li $v0, 4
la $a0, space
syscall

addi $s1, $s1, 4
addi $s0, $s0, -1
bgtz $s0, test_p1

li $v0, 4
la $a0, new_line
syscall
la $a0, bcd_2_bin_lbl
syscall

# Testing part 2
li $s0, 3 # num of test cases
li $s1, 0
la $s2, bcd_2_bin_test_data

test_p2:
add $s4, $s2, $s1
# Pass input parameter
lw $a0, 0($s4)
jal bcd2bin

move $a0, $v0        # hex to print
jal print_hex

li $v0, 4
la $a0, space
syscall

addi $s1, $s1, 4
addi $s0, $s0, -1
bgtz $s0, test_p2

li $v0, 4
la $a0, new_line
syscall
la $a0, bin_2_bcd_lbl
syscall

# Testing part 3
li $s0, 3 # num of test cases
li $s1, 0
la $s2, bin_2_bcd_test_data

test_p3:
add $s4, $s2, $s1
# Pass input parameter
lw $a0, 0($s4)
jal bin2bcd

move $a0, $v0        # hex to print
jal print_hex

li $v0, 4
la $a0, space
syscall

addi $s1, $s1, 4
addi $s0, $s0, -1
bgtz $s0, test_p3

_end:
# end program
li $v0, 10
syscall

