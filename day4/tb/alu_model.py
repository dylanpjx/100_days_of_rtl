from enum import IntEnum

class Opcode(IntEnum):
    ADD = 0
    SUB = 1
    SLL = 2
    LSR = 3
    AND = 4
    OR  = 5
    XOR = 6
    EQL = 7

def alu_model(a_i: int, b_i: int, op_i: int) -> int:
    if (op_i == Opcode.ADD):
        res = a_i + b_i
    elif (op_i == Opcode.SUB):
        res = a_i - b_i
    elif (op_i == Opcode.SLL):
        res = a_i << (b_i & 0b00000111)
    elif (op_i == Opcode.LSR):
        res = a_i >> (b_i & 0b00000111)
    elif (op_i == Opcode.AND):
        res = a_i & b_i
    elif (op_i == Opcode.OR):
        res = a_i | b_i
    elif (op_i == Opcode.XOR):
        res = a_i ^ b_i
    else:
        return 1 if a_i == b_i else 0
    return res & 0xff
