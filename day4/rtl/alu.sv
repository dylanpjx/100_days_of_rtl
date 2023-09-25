typedef enum {
  ADD,
  SUB,
  SLL,
  LSR,
  AND,
  OR,
  XOR,
  EQL
} opcode;

module alu (
  input  logic [7:0]   a_i,
  input  logic [7:0]   b_i,
  input  logic [2:0]   op_i,

  output logic [7:0]   alu_o
);

  always_comb begin
    case (op_i)
      ADD: alu_o = a_i + b_i;
      SUB: alu_o = a_i - b_i;
      SLL: alu_o = a_i << b_i[2:0];
      LSR: alu_o = a_i >> b_i[2:0];
      AND: alu_o = a_i & b_i;
      OR:  alu_o = a_i | b_i;
      XOR: alu_o = a_i ^ b_i;
      EQL: alu_o = (a_i == b_i);
    endcase
  end

endmodule

