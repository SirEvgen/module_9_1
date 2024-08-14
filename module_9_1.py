def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
        result = i(int_list)
        results[i.__name__] = result
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

def calculate_stats(list_of_values):
    result = {}
    avg = sum(list_of_values) / len(list_of_values)
    min_value = min(list_of_values)
    max_value = max(list_of_values)

    result['avg'] = avg
    result['min'] = min_value
    result['max'] = max_value

    return result


numbers = [1, 2, 3, 4, 5]
stats = calculate_stats(numbers)
print(stats)
