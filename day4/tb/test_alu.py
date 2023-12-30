import os
import random
import sys
from pathlib import Path

import cocotb
from cocotb.binary import BinaryValue
from cocotb.runner import get_runner
from cocotb.triggers import Timer

if cocotb.simulator.is_running():
    from alu_model import alu_model

@cocotb.test()
async def alu_randomized_test(dut):
    for i in range(10):
        for op_i in range(8):
            a_i = random.randint(0, 1<<8-1)
            b_i = random.randint(0, 1<<8-1)

            dut.a_i.value = a_i
            dut.b_i.value = b_i
            dut.op_i.value = op_i

            await Timer(2, units="ns")
            
            assert dut.alu_o.value == alu_model(
                a_i, b_i, op_i
                ), "Randomised test failed with: {op_i}: {a_i}, {b_i} -> {alu_o}".format(
                op_i=dut.op_i.value, a_i=dut.a_i.value, b_i=dut.b_i.value, alu_o=dut.alu_o.value
            )


def test_alu_runner():
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")

    # setting PYTHONPATH
    proj_path = Path(__file__).resolve().parent.parent
    sys.path.append(str(proj_path / "tb"))

    verilog_sources = [proj_path / "rtl" / "alu.sv"]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="alu",
        always=True,
    )
    runner.test(hdl_toplevel="alu", test_module="test_alu")

if __name__ == "__main__":
    test_alu_runner()
