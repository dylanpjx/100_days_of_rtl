import os
import sys
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import Timer

@cocotb.test()
async def bin_2_gray_test(dut):
    for i in range(10):
        val = random.randint(0, 15)
        dut.bin_i.value = val

        await Timer(2, units ="ns")
        gray = (val >> 1) ^ val
        assert dut.gray_o.value == gray, "Randomized test failed with: {val}".format(val=val)

def test_bin_2_gray_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    proj_path = Path(__file__).resolve().parent.parent
    sys.path.append(str(proj_path / "tb"))

    verilog_sources = [proj_path / "rtl" / "bin_2_gray.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="bin_2_gray",
        always=True,
    )

    runner.test(hdl_toplevel="bin_2_gray", test_module="test_bin_2_gray,")


if __name__ == "__main__":
    test_bin_2_gray_runner()
