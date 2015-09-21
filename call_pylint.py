#encoding=utf-8

import commands
from pylint import epylint

if __name__ == '__main__':
	(pylint_stdout,pylint_stderr) = epylint.py_run('just_for_test.py',return_std=True)
	#(pylint_stdout,pylint_stderr) = epylint.py_run('test.py',return_std=True)
	print pylint_stdout.read()
	print pylint_stderr.read()
	#print epylint.py_run('test.py')
	#print epylint.py_run('just_for_test.py')

	#status,output = commands.getstatusoutput('pylint test.py')
	#print status
	#print output

