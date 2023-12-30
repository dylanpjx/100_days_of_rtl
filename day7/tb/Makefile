TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
    VERILOG_SOURCES = $(PWD)/../rtl/lfsr.sv

TOPLEVEL := lfsr
MODULE   := test_lfsr

include $(shell cocotb-config --makefiles)/Makefile.sim
