# PythonAssignment

# Module1.py defines the function hostblacklist that takes a hostname
# The function reads the Windows hosts file at C:\Windows\System32\drivers\etc\hosts
# If the hostname is already in the file, the function asks the user if they want to continue to blacklist the hostname
# If the user selects n for no, the function exits
# If the user selects y for yes, the function appends a line to the hosts file to redirect the hostname to 0.0.0.0
# If the hostname does not exist in the file, the function appends a line to the hosts file to redirect the hostname to 0.0.0.0

# Module2.py imports hostblacklist from Module1.py and creates an argument to be passed when calling Module2.py from a command-line interface
# The argument is called hostname, type string, and will be taken and passed directly to the function hostblacklist
