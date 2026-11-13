"""List comprehensions are a concise way to create lists in Python. They consist of brackets containing an expression followed by a for clause, and can also include optional if clauses."""
#create new lists from an existing list using list comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names= ["Alice", "Bob", "Charlie", "David", "Eve"]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]




#map
doubled_nums = [num * 2 for num in nums]
str_nums = [str(num) for num in nums]
even_nums = [x for x in nums if x % 2 == 0]

clean_and_lower_names = [name.strip().lower() for name in names]

#Multiple conditions for filtering
even_nums_gt_5 = [x for x in nums if x % 2 == 0 and x > 5]

#if / else in list comprehension mapping values to even or odd

even_odd = ["even" if x % 2 == 0 else "odd" for x in nums]

#flattening a matrix
flattened_matrix = [num for row in matrix for num in row]

squares_set = {x ** 2 for x in nums}        # set comprehension, duplicates will be removed
squared_dict = {x: x ** 2 for x in nums}    # dictionary comprehension
lazy = (x * x for x in nums)                #  generator expression, lazy evaluation, χωρίς λίστα στη μνήμη