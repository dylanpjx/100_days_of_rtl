module counter (
  input  wire       clk,
  input  wire       reset,
  input  wire       load_i,
  input  wire [3:0] load_val_i,
  
  output wire [3:0] count_o
);

  logic [3:0] count_reg;
  
  always_ff @(posedge clk) begin
    if (reset) begin
      count_reg <= 'd0;
    end else begin
      count_reg <= (load_i) ? load_val_i : count_reg + 'd1;
    end
  end

  assign count_o = count_reg;
endmodule
