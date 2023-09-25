import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

@cocotb.test()
async def counter_test(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))
    dut.reset.value = 1

    await RisingEdge(dut.clk)
    dut.reset.value = 0
    
    await FallingEdge(dut.clk)
    assert dut.cnt_o.value == 1;

    for cnt in range(3, 512, 2):
        await FallingEdge(dut.clk)
        assert dut.cnt_o.value == cnt % 256


def test_counter_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent.parent
    sys.path.append(str(proj_path / "tb"))

    verilog_sources = [proj_path / "rtl" / "counter.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="counter",
        always=True,
    )

    runner.test(hdl_toplevel="counter", test_module="test_counter,")


if __name__ == "__main__":
    test_counter_runner()
