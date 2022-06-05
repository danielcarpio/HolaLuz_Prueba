from tabulate import tabulate

def print_output(data):
    if len(data) == 0:
        print('No suspicious data has been found')
    else:
        print(tabulate(data, headers=['Client', 'Month', 'Suspicious', 'Median'], tablefmt="github"))