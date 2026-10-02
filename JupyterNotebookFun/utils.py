
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

