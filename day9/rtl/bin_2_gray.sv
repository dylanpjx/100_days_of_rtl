module bin_2_gray #(
  parameter VEC_W = 4
)(
  input  wire [VEC_W-1:0] bin_i,
  output wire [VEC_W-1:0] gray_o
);

  assign gray_o = (bin_i >> 1) ^ bin_i;

endmodule
