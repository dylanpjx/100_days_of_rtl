import os
import sys
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

@cocotb.test()
async def shift_register_test(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))
    dut.reset.value = 1

    await RisingEdge(dut.clk)
    dut.reset.value = 0
    
    await FallingEdge(dut.clk)
    assert dut.sr_o.value == 0;
    
    res = "0000"
    for i in range(50):
        x_i = random.randint(0, 1)
        dut.x_i.value = x_i
        await FallingEdge(dut.clk)
        res = res[1:] + str(x_i)
        assert str(dut.sr_o.value) == res


def test_shift_register_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent.parent
    sys.path.append(str(proj_path / "tb"))

    verilog_sources = [proj_path / "rtl" / "shift_register.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="shift_register",
        always=True,
    )

    runner.test(hdl_toplevel="shift_register", test_module="test_shift_register")


if __name__ == "__main__":
    test_shift_register_runner()
