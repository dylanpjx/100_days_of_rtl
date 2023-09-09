TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
    VERILOG_SOURCES = $(PWD)/../rtl/edge_detector.sv

TOPLEVEL := edge_detector
MODULE   := test_edge_detector

include $(shell cocotb-config --makefiles)/Makefile.sim
