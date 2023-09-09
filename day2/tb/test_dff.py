import os
import sys
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge
from cocotb.triggers import Timer
from cocotb.types import LogicArray


@cocotb.test()
async def dff_test(dut):
    """Test that d propagates to q"""

    # Assert initial output is unknown
    assert LogicArray(dut.q_norst_o.value) == LogicArray("X")
    # Set initial input value to prevent it from floating
    dut.d_i.value = 0

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    dut.reset.value = 0
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    # Synchronize with the clock. This will regisiter the initial `d` value
    await RisingEdge(dut.clk)
    expected_val = 0  # Matches initial input value
    for i in range(10):
        val = random.randint(0, 1)
        dut.d_i.value = val  # Assign the random value val to the input port d
        await RisingEdge(dut.clk)
        assert dut.q_norst_o.value == expected_val, f"output q was incorrect on the {i}th cycle"
        expected_val = val  # Save random value for next RisingEdge

    # Check the final input on the next clock
    await RisingEdge(dut.clk)
    assert dut.q_norst_o.value == expected_val, "output q was incorrect on the last cycle"
    # Check for rst functionality

    dut.d_i.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 1

    await RisingEdge(dut.clk)
    assert dut.q_norst_o.value == 1, f"output q was incorrect on reset"
    assert dut.q_asyncrst_o.value == 0, f"async q was incorrect on reset"
    assert dut.q_syncrst_o.value == 1, f"sync q resetting incorrectly"

    await FallingEdge(dut.clk)
    assert dut.q_norst_o.value == 1, f"output q was incorrect on reset"
    assert dut.q_asyncrst_o.value == 0, f"async q was incorrect on reset"
    assert dut.q_syncrst_o.value == 0, f"sync q was incorrect on reset"


def test_simple_dff_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent.parent
    sys.path.append(str(proj_path / "tb"))

    verilog_sources = [proj_path / "rtl" / "dff.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="dff",
        always=True,
    )

    runner.test(hdl_toplevel="dff", test_module="test_dff,")


if __name__ == "__main__":
    test_simple_dff_runner()
