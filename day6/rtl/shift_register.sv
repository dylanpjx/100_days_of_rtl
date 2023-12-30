module shift_register (
  input  wire       clk,
  input  wire       reset,
  input  wire       x_i,
  output wire [3:0] sr_o

);
  logic [3:0] sr_reg;

  always_ff @(posedge clk) begin
    if (reset) begin
      sr_reg <= 'd0;
    end else begin
      sr_reg <= { sr_reg[2:0], x_i };
    end
  end
  
  assign sr_o = sr_reg;
endmodule
