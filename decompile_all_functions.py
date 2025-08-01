#TODO Decompile functions into C-like code and store them into a text file.
#@author Mount
#@category Custom Scripts
#@keybinding
#@menupath
#@toolbar
# @runtime Jython

from ghidra.program.flatapi import FlatProgramAPI
from ghidra.app.decompiler.flatapi import FlatDecompilerAPI

def getFunctions():
    api = FlatProgramAPI(currentProgram, monitor)
    first = api.getFirstFunction()
    functionObjects =  []
    while first:
        functionObjects.append(first)
        next = api.getFunctionAfter(first)
        first = next
    return api, functionObjects

def decompiledFunctionsToFile(api, functionObjects):
    decomp = FlatDecompilerAPI(api)
    decomp.initialize()
    outFile = r'C:\Users\mount\Desktop\ghidra_scripts\decompiledFunctions.txt'
    with open(outFile, 'w') as f:
        f.write('-' * 100)
        for i, obj in enumerate(functionObjects):
            f.write(decomp.decompile(obj))
            f.write('-' * 100)
            print("Decompiled: {}, {}/{}".format(obj.getName(), i + 1, len(functionObjects)))

if __name__ == "__main__":
    api, functionObjects = getFunctions()
    decompiledFunctionsToFile(api, functionObjects)
