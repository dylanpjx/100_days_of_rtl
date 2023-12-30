import os
import sys
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

@cocotb.test()
async def lfsr_test(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))
    dut.reset.value = 1

    await RisingEdge(dut.clk)
    dut.reset.value = 0
    
    await FallingEdge(dut.clk)
    assert dut.lfsr_o.value == 14;
    
    res = "1110"
    for i in range(50):
        await FallingEdge(dut.clk)
        res = res[1:] + str(int(res[0]) ^ int(res[2]))
        assert str(dut.lfsr_o.value) == res


def test_lfsr_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent.parent
    sys.path.append(str(proj_path / "tb"))

    verilog_sources = [proj_path / "rtl" / "lfsr.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="lfsr",
        always=True,
    )

    runner.test(hdl_toplevel="lfsr", test_module="test_lfsr")


if __name__ == "__main__":
    test_lfsr_runner()
