# FPGA-dev-tool
Tools for synthesis and running simulations files on Icarus verilog platform. 

run.py script automagically gets all source files (.v, .vh), compiled it and runs simulation tool (GTKWave). 
rebuild.py script just recompile all changes in code. 

Sripts additionaly sets "SIMULATION" flag, therefore all simulation specific code can be ignored in sythesis tool by using preprocessor statements.

NOTE: All source files must be in subdirectory "src"

