

print("-------------------------module two start-------------------------")
print(__name__ ) # when the module is run directly the __name__ is __main__


import if_name_is_main as main
print(main.__name__)
print("-------------------------module two end-------------------------")