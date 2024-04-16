# if name == '___main__': is included in the code to ensure that the code is only run if the script is run directly, and not if it is imported as a module. This is useful if you want to include code that should only run when the script is run directly, but not when it is imported as a module.
# the reason to include the if __name__ == '__main__': statement is to prevent code from being run when the module is imported as a module. This is useful if you want to include code that should only run when the script is run directly, but not when it is imported as a module.
# this also allows modules to be run as standalone scripts, which can be useful for testing and debugging purposes, or combining multiple modules into a single script.




print("-------------------------module one start-------------------------")
print(__name__ ) # when the module is run directly the __name__ is __main__


# import if_name_is_main2 as main2
# print(main2.__name__) # when the module is imported the __name__ is the name of the module

if __name__ == '__main__':
    print("Running module one directly")
else:
    print("Running module one indirectly")
print("-------------------------module one end-------------------------")
