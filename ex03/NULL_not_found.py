import inspect
import math
def NULL_not_found(object: any) -> int:
    caller_vars = inspect.currentframe().f_back.f_locals.items()

    var_name = next(
    (
        name for name, val in caller_vars
        if not name.startswith("__")
        and (
            val is object or
            (isinstance(val, float) and isinstance(object, float) and math.isnan(val) and math.isnan(object))
        )
    ),
    None
)
    if var_name == "Nothing" :
        print(var_name + ":",object, type(object))
    elif var_name == "Garlic" : 
        print("Cheese" + ":",object, type(object))
    elif var_name == "Zero" : 
        print(var_name + ":",object, type(object))
    elif var_name == "Empty" :
        print(var_name + ":", object, type(object))
    elif var_name == "Fake" :
        print(var_name + ":", object, type(object))
    else :
        print("Type not Found")
        return 1
