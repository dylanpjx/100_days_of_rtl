module dff (
  input clk,
  input reset,

  input d_i,
  
  output logic q_norst_o,
  output logic q_syncrst_o,
  output logic q_asyncrst_o
);

  // no rst
  always_ff @(posedge clk) begin
    q_norst_o <= d_i;
  end

  // sync rst
  always_ff @(posedge clk) begin
    if (reset) begin
      q_syncrst_o <= 1'b0;
    end else begin
      q_syncrst_o <= d_i;
    end
  end

  // async rst
  always_ff @(posedge clk or posedge reset) begin
    if (reset) begin
      q_asyncrst_o <= 1'b0;
    end else begin
      q_asyncrst_o <= d_i;
    end
  end
endmodule
