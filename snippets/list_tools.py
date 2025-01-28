a = [
    {
        "id": 1,
        "fileName": "file1.txt",
        "file_size": 1000,
        "last_modified": "2023-01-01",
    },
    {
        "id": 2,
        "fileName": "file2.txt",
        "file_size": 2000,
        "last_modified": "2023-01-02",
    },
    {
        "id": 3,
        "fileName": "file3.txt",
        "file_size": 3000,
        "last_modified": "2023-01-03",
    },
]

b = [
    {"fileName": "file2.txt", "file_size": 2000, "last_modified": "2023-01-02"},
    {"fileName": "file3.txt", "file_size": 3000, "last_modified": "2023-01-03"},
]

# Using list comprehension to find elements in `a` but not in `b`
result = [
    item_a
    for item_a in a
    if not any(
        item_a["fileName"] == item_b["fileName"]
        and item_a["file_size"] == item_b["file_size"]
        for item_b in b
    )
]

print(result)
