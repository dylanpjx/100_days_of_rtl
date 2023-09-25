TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
    VERILOG_SOURCES = $(PWD)/../rtl/counter.sv

TOPLEVEL := counter
MODULE   := test_counter

include $(shell cocotb-config --makefiles)/Makefile.sim
