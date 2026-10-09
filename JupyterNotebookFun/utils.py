
def dummy_function():
    print("hello from dummy function (again!!)")

def get_column(table, header, col_name):
   
    #TODO 
    pass
    


def get_frequencies(table, header, col_name):
    # TODO: resolve this using python dictionaries
    col = get_column(table, header, col_name)
    # we want to get the unique values from this column
    unique_col_values = sorted(list(set(col)))
    print(unique_col_values)
    counts = []
    for val in unique_col_values:
        counts.append(col.count(val))

    return unique_col_values, counts

def group_by(table, header, group_by_col_name):
    #TODO
    pass

def compute_slope_intercept(x, y):
    meanx = sum(x) / len(x)
    meany = sum(y) / len(y)

    num = sum([(x[i] - meanx) * (y[i] - meany) for i in range(len(x))])
    den = sum([(x[i] - meanx) ** 2 for i in range(len(x))])
    m = num / den
    # y = mx + b -> y - mx
    b = meany - m * meanx
    return m, b
