module lfsr (
  input  wire       clk,
  input  wire       reset,
  output wire [3:0] lfsr_o

);
  logic [3:0] lfsr_reg;

  always_ff @(posedge clk) begin
    if (reset) begin
      lfsr_reg <= 'hE;
    end else begin
      lfsr_reg <= { lfsr_reg[2:0], lfsr_reg[3] ^ lfsr_reg[1] };
    end
  end
  
  assign lfsr_o = lfsr_reg;
endmodule
