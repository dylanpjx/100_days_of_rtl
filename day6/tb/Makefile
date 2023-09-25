TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
    VERILOG_SOURCES = $(PWD)/../rtl/shift_register.sv

TOPLEVEL := shift_register
MODULE   := test_shift_register

include $(shell cocotb-config --makefiles)/Makefile.sim
