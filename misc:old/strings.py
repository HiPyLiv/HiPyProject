def numerical_to_written_date(date):
    months = {1: "January",
              2: "February",
              3: "March",
              4: "April",
              5: "May",
              6: "June",
              7: "July",
              8: "August",
              9: "September",
              10: "October",
              11: "November",
              12: "December"}
    if '/' in date:
        date = date.replace('/', '.')
    date = date.split('.')
    return "{} {}, {}".format(months[date[1], int(str(date[0])), date[2])

def feet_to_meters():
    pass

def inches_to_centimeters():
    pass

def gallons_to_liters():
    pass

def quarts_to_liters():
    pass

def meters_to_feet():
    pass

def inches_to_centimeters():
    pass

def celsius_to_farenheit():
    pass

def farenheit_to_celsius():
        
question = input("What do you want to convert?")
