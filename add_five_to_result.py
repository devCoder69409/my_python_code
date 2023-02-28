def add_five(num):
    print(f"I have received {num}")
    num_after_adding = num + 5
    print(f"I have calculated {num} + 5 = {num_after_adding}")
    return num_after_adding

result_1 = add_five(23)
result_2 = add_five(result_1)
result_3 = add_five(result_2)
print(result_3)