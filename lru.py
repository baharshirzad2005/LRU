def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    print("LRU Page Replacement Algorithm")
    print("--------------------------------")

    for page in pages:
        if page not in memory:
            page_faults += 1

            if len(memory) == capacity:
                memory.pop(0)

            memory.append(page)
            result = "Page Fault"
        else:
            memory.remove(page)
            memory.append(page)
            result = "Page Hit"

        print(f"Page: {page} | Memory: {memory} | {result}")

    print("--------------------------------")
    print("Total Page Faults:", page_faults)


pages = [1, 2, 3, 1, 4, 5, 2, 1, 2, 3, 4, 5]
capacity = 3

lru_page_replacement(pages, capacity)
