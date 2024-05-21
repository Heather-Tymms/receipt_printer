store_name = "Nathan's Grocery"

receipt_width = 30

prices = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.6,
    "pear": 0.4,
    "grape": 0.7,
    "watermelon": 1.0,
}

tax_rate = 0.13

def calculate_price(item, count):
    items_price = prices[item] * count
    return f"${items_price}"

def center_text(text):
    print("|" + text.center(receipt_width) + "|")


def count_items(items):
    dict_of_items = {}
    for item in items:
        if item in dict_of_items:
            dict_of_items[item] += 1
        else:
            dict_of_items[item] = 1
    return dict_of_items


def print_spacer(label, value):
    print("|" + f" {label} ".ljust(receipt_width - len(value) - 1) + f"{value} |")


def print_taxes(title, value):
    print_spacer(title, f"${value}")


def print_receipt(items):
    items_count = count_items(items)
    print("+" + "-" * receipt_width + "+")
    print("|" + " " * receipt_width + "|")
    center_text(store_name)
    print("|" + " " * receipt_width + "|")
    for item in items_count.keys():
        item_name = item
        item_count = items_count[item]
        item_price = calculate_price(item, item_count)
        print_spacer(f"{item_name} x{item_count}", item_price)
    print("|" + "-" * receipt_width + "|")
    subtotal = sum([prices[item] * items_count[item] for item in items_count])
    tax = subtotal * tax_rate
    total = subtotal + tax
    print_taxes("Subtotal", subtotal)
    print_taxes("Tax", tax)
    print_taxes("Total", total)
    print("|" + " " * receipt_width + "|")
    print("+" + "-" * receipt_width + "+")

basket = [
    "banana",
    "pear",
    "pear",
    "grape",
    "orange",
    "grape",
    "pear",
    "apple",
    "grape",
    "watermelon",
]
print_receipt(basket)