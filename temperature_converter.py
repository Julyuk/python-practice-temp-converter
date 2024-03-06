def temperature_converter(cls):
    if type(cls) == float or type(cls) == int:
        if cls >=-273.5:
            print(round(cls*9/5+32,2))
        else:
            raise ValueError("The entered temperature is below absolute zero (-273.5 °C)")
    else:
        raise AttributeError("The temperature must be a float or an integer")
