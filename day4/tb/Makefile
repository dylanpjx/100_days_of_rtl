TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
    VERILOG_SOURCES = $(PWD)/../rtl/alu.sv

TOPLEVEL := alu
MODULE   := test_alu

include $(shell cocotb-config --makefiles)/Makefile.sim
