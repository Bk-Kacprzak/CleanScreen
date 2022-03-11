from ApplicationServices import AXIsProcessTrusted, AXAPIEnabled

# TODO: Connect it to the application
def checkAccessibility() : 
    if AXAPIEnabled():
        return True
    if AXIsProcessTrusted(): 
        return True
    return False

print(checkAccessibility())