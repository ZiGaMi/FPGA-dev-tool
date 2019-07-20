import os
import sys
import string

# Verilog project
class Project():

	def __init__(self):
	
		# Get directory
		#os.system("cd")
		#self.dir = sys.argv[0]
		self.dir = os.getcwd()
		self.dir = string.replace(self.dir, "rebuild.py", "")
		
		# Search for source file in src subfolder
		self.dir += "\\src"
		
		name = ""
		
		# Parse folder name
		for char in self.dir[:len(self.dir)-1]:
			if (char == "\\"):
				name = ""
			else:	
				name += char
		
		# Parse obj name
		self.obj_name = name
		
		# Clear cmd
		os.system("cls")

	# Get data for compiling
	def get_source(self):
	
		# List of source files
		src = []
		
		# Collecting
		print "Collecting..."
		
		# Parse source files
		for file in os.listdir(self.dir):		
			if not (file == "objdir" or file == "run.py" or file == "rebuild.py"):
				if file[-2:] == ".v":
					src.append(file)
		
		return src
		
	# Compile RTL code
	def compile(self):
	
		# Get source files
		src = self.get_source()
		
		# Objdir directory
		self.objdir = os.path.join(self.dir, "objdir/")
		
		# Make objdump directory
		try:
			# Objdir does not exsist
			if not os.path.exists(self.objdir):
				os.makedirs(self.objdir)
			# Clear objdir	
			else:
				for file in os.listdir(self.objdir):
					os.remove(os.path.join(self.objdir, file))
				
		except OSError as e:
		
			print "Error:" + str(e)
			
		#Compiler flags
		# Wall 		- All Warnings
		# -g2012 	- 2012 generation, including SystemVerilog
		# SIMULATION	- Macro definition 
		flags = "-Wall -g2012 -DSIMULATION"
		
		# Compile command
		#compile_cmd = "iverilog -Wall -o " + self.objdir + self.obj_name + " "
		compile_cmd = "iverilog " + flags + " -o " + self.objdir + self.obj_name + " "
		
		for s in src:
			compile_cmd += s + " "
		
		print "Compiling..." 
		os.system(compile_cmd)
		#print "\n"
		
	# Execute obj code
	def execute(self):
		
		obj = []
		
		# Go to objdir directory
		os.chdir(self.objdir)
		
		# Get compiled file
		for file in os.listdir(self.objdir):
		
			obj.append(file)
		
		# Execute
		execute_cmd = "vvp " + obj[0]
		print "Executing...\n"
		os.system(execute_cmd)
	
		
if __name__ == "__main__":
	
	project = Project()

	print "Rebuilding project..."
	
	project.compile()	
	project.execute()
	
	print "\nProject successfully rebuild..."
	
	# Prevent from closing
	raw_input()
	