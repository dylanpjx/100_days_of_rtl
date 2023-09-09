import random
import os
import sys
from pathlib import Path

import cocotb
from cocotb.runner import get_runner
from cocotb.triggers import Timer

if cocotb.simulator.is_running():
    from mux_model import mux_model 

@cocotb.test()
async def test_mux(dut):
    for i in range(10):
        a_i = random.randint(0, 1<<8-1)
        b_i = random.randint(0, 1<<8-1)
        sel_i = bool(random.getrandbits(1))
        
        dut.a_i = a_i
        dut.b_i = b_i
        dut.sel_i = sel_i

        await Timer(2, units="ns")
        
        assert dut.y_o == mux_model(
                a_i, b_i, sel_i
        ), "Randomized test failed with: ({sel_i}, {a_i}, {b_i}".format(
        sel_i=dut.sel_i, a_i=dut.a_i, b_i = dut.b_i
        )



def test_mux_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    # setting PYTHONPATH
    proj_path = Path(__file__).resolve().parent.parent
    sys.path.append(str(proj_path / "tb"))

    verilog_sources = [proj_path / "rtl" / "mux.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="mux",
        always=True,
    )
    runner.test(hdl_toplevel="mux", test_module="test_mux")

if __name__ == "__main__":
    test_mux_runner()
