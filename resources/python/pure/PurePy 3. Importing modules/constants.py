# these constants are available if the module is imported
speed_of_light = 299792458
planck = 6.62607004e-34
electron_charge = -1.6021766208e-19
electron_mass = 9.10938356e-31

if __name__ == '__main__':
    # this code will ONLY be executed if the module
    # is launched independently, not imported.
    print("The speed of light in a vacuum is", speed_of_light, "ms⁻ⁱ")
    print("Planck's constant is", planck, "J·s")
    print("An electron has charge", electron_charge, "C")
    print("An electron has mass", electron_mass, "kg")
