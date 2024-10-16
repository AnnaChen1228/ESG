# 假設 data_name 包含五個子列表
data_name = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [2, 3, 4, 7],
    [3, 4, 8]
]

# 找出共同元素並保持順序
common_elements = [item for item in data_name[0] if all(item in sublist for sublist in data_name[1:])]

# 找出不再共同元素的獨特元素
unique_elements = []
for i, sublist in enumerate(data_name):
    # 找出該子列表中不在共同元素中的獨特元素
    unique = [item for item in sublist if item not in common_elements]
    unique_elements.append((f"List {i + 1}", unique))  # 將結果添加到 unique_elements

# 輸出共同元素和不再共同元素的獨特元素
print("共同元素 (五個皆有):", common_elements)
print("不再共同元素的獨特元素:")
for list_name, unique in unique_elements:
    print(f"{list_name}: {unique}")
