module edge_detector (
  input clk,
  input reset,
  input a_i,

  output rising_edge_o,
  output falling_edge_o
);

  logic a_r;

  always_ff @(posedge clk) begin
    if (reset) begin
      a_r <= 1'b0;
    end else begin
      a_r <= a_i;
    end
  end

  assign rising_edge_o = a_i && ~a_r;
  assign falling_edge_o = ~a_i && a_r;

endmodule
