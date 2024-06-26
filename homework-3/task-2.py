import json


def read_stores_sales_from_file(file_path: str = "input.txt") -> dict:
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Input file not found.")
    except json.JSONDecodeError:
        print("Error happened while parsing the file.")
    return {}


def write_products_info_to_file(products_info: dict, file_path: str = "output.txt") -> None:
    try:
        with open(file_path, "w") as f:
            json.dump(products_info, f, indent=4)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")


def create_products_info_from_file() -> None:
    store_sales = read_stores_sales_from_file()
    products_info = {}
    for store, products in store_sales.items():
        for product, sold in products.items():
            products_info[product] = products_info.get(product, 0) + sold

    write_products_info_to_file(products_info)


def main():
    create_products_info_from_file()


if __name__ == '__main__':
    main()
