	.data
keyboard: .space 4     	# direccion de memoria donde tenemos el teclado
seven_seg: .word 64	# direccion de memoria del display
	.text
main:
	la	$s0, keyboard
loop01:
	addi 	$s1, $0, 1
	lw	    $t0, 0($s0)
	beq 	$t0, $s0, loop01
loop02:
	beq 	$t0, $s1, display
	sll	    $s1, $s1, 1
	andi	$t1, $s1, 1023
	beq 	$t1, $0, loop01 
	j	loop02
display:
	andi 	$t1, $s1, 1
	beq 	$t1, $0, compara2
	addi	$t0, $0, 6
	j	write_data

compara2:
	andi	$t1, $s1, 2
	beq 	$t1, 0, compara3
	addi	$t0, 0, 6
	j 	write_data

compara3:
	andi	$t1, $s1, 4
	beq 	$t1, 0, compara4
	addi	$t0, 0, 91
	j 	write_data
compara4:
	andi	$t1, $s1, 8
	beq 	$t1, 0, compara5
	addi	$t0, 0, 79
	j 	write_data 

compara5:
	andi	$t1, $s1, 16
	beq 	$t1, 0, compara6
	addi	$t0, 0, 102
	j 	write_data

compara6:
	andi	$t1, $s1, 32
	beq 	$t1, 0, compara7
	addi	$t0, 0, 109
	j 	write_data

compara7:
	andi	$t1, $s1, 64
	beq 	$t1, 0, compara8
	addi	$t0, 0, 125
	j 	write_data

compara8:
	andi	$t1, $s1, 128
	beq 	$t1, 0, compara9
	addi	$t0, 0, 7
	j 	write_data

compara9:
	andi	$t1, $s1, 256
	beq 	$t1, 0, compara10
	addi	$t0, 0, 127
	j 	write_data

compara10:
	andi	$t1, $s1, 512
	beq 	$t1, 0, compara11
	addi	$t0, 0, 111
	j 	write_data
compara11:
	j loop01
write_data:
	la	    $s2, seven_seg
	sw      $t0, 0($s2)
	.end
### Numeros

0 = 63
1 = 6
2 = 91
3 = 79
4 = 102
5 = 109
6 = 125
7 = 7
8 = 127
9 = 111
