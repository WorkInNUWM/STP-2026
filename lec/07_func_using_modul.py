# using function with customs moduls

# import func_param_copy

# print(f"sumN(2,3,4) => {func_param_copy.sumN(2,3,4)}")
# print(f"suma parnih => {func_param_copy.suma_number_flag(True,2,3,4,5,6)}")

# from func_param_copy import sumN,suma_number_flag
# print(f"sumN(2,3,4) => {sumN(2,3,4)}")
# print(f"suma parnih => {suma_number_flag(True,2,3,4,5,6)}")



# from func_param_copy import *
# import mypackage.mymodule
# print(f"sumN(2,3,4) => {sumN(2,3,4)}")
# print(f"suma parnih => {suma_number_flag(True,2,3,4,5,6)}")
# runtask()

# import mypackage
# mypackage.mymodule.hello_by_name("Tetiana")

# import mypackage.mymodule  as mymod
# mymod.suma(3,4)

# from mypackage.mymodule import *
# suma(3,4)

from mypackage import mymodule
mymodule.suma(3,4)
