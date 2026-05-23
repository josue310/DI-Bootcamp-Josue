# Daily Challenge : Pagination

import math


# Custom Exception
class PageOutOfRangeError(ValueError):
    def __init__(self, page_num, total_pages):
        super().__init__(
            f"Page {page_num} does not exist. "
            f"Valid range is 1 to {total_pages}."
        )


# Pagination Class
class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # Step 3: Get visible items on current page
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Step 4: Navigation methods
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise PageOutOfRangeError(page_num, self.total_pages)
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Step 5 (Bonus): __str__ magic method
    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())



# Step 6: Tests

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print("--- get_visible_items() → page 1 ---")
print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

print("\n--- next_page() → page 2 ---")
p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

print("\n--- last_page() ---")
p.last_page()
print(p.get_visible_items())
# ['y', 'z']

print("\n--- go_to_page(10) → ValueError ---")
try:
    p.go_to_page(10)
except PageOutOfRangeError as e:
    print(e)

print("\n--- go_to_page(0) → ValueError ---")
try:
    p.go_to_page(0)
except PageOutOfRangeError as e:
    print(e)

print("\n--- Bonus: __str__ ---")
p.first_page()
print(str(p))

print("\n--- Bonus: Method chaining ---")
p.first_page()
print(p.next_page().next_page().next_page().get_visible_items())
# ['m', 'n', 'o', 'p']