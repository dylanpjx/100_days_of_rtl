import os
import sys
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

@cocotb.test()
async def edge_detector_test(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))
    dut.reset.value = 1

    await RisingEdge(dut.clk)
    dut.reset.value = 0

    reg_val = 0
    for i in range(10):
        val = random.randint(0, 1)
        dut.a_i = val
        await FallingEdge(dut.clk)
        reg_val = val
        assert dut.rising_edge_o.value == (val and not reg_val)
        assert dut.falling_edge_o.value == (reg_val and not val)


def test_edge_detector_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent.parent
    sys.path.append(str(proj_path / "tb"))

    verilog_sources = [proj_path / "rtl" / "edge_detector.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="edge_detector",
        always=True,
    )

    runner.test(hdl_toplevel="edge_detector", test_module="test_edge_detector,")


if __name__ == "__main__":
    test_edge_detector_runner()
