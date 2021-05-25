def process_file(filepath):
    with open(filepath, "r") as f:
        filelines = [line.split(", ") for line in f]
    columns = {header: [filelines[y][x] for y in range(1, len(filelines))]
               for x, header in enumerate(filelines[0])}
    return filelines[0], columns
'''
def determine_column_widths(table):
    widths = {}
    for field in table:
        longestentry = max(table[field], key=lambda x: len(str(x)))
        widths[field] = len(longestentry) + 2
    return widths
    '''
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

def build_line(entries):
"|{:^30}| ${:,.2f>6}M |{:,^9}|"

def build_pretty_table(headers, table):
    titles = {header: header.capitalize() for header in headers}


        
headers, table = process_file("topmovies.csv")
table['gross'] = [cash/10**6 for cash in table['gross']]
table['date'] = [numerical_to_written_date(date) for date in table['date']]
widths = determine_column_widths(table)
print(widths)
    

