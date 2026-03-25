import pandas as pd
import time

history = {}

# LOAD DATA
def load_data():
    file = input("Enter CSV file name: ")

    print("Loading...")
    start = time.time()

    try:
        df = pd.read_csv(file)
        df = df.fillna(0)

        # create total sales
        if "quantity" in df.columns and "unit_price" in df.columns:
            df["sales"] = df["quantity"] * df["unit_price"]

        end = time.time()

        print("Loaded!")
        print("Time:", round(end - start, 2))
        print("Rows:", len(df))
        print("Columns:", list(df.columns))

        return df

    except:
        print("Error loading file")
        return None


# EXPORT (extra req 1)
def export_result(result):
    choice = input("Export to Excel? (y/n): ").lower()

    if choice == "y":
        name = input("File name: ")

        if name == "":
            print("Invalid name")
            return

        if not name.endswith(".xlsx"):
            name += ".xlsx"

        try:
            result.to_excel(name)
            print("Saved!")
        except:
            print("Error saving file")


# SAVE HISTORY (extra req 10)
def save_result(name, result):
    history[name] = result


def show_history():
    if len(history) == 0:
        print("No saved analytics")
    else:
        print("\nSaved analytics:")
        for name in history:
            print("\n" + name)
            print(history[name])


def show_done():
    print("\nCompleted:")
    if len(history) == 0:
        print("None")
    else:
        for name in history:
            print("-", name)


# ANALYTICS

def show_first(df):
    total = len(df)

    print("Enter rows (1 to", total, ") or 'all'")
    choice = input("Your choice: ").lower()

    if choice == "":
        print("Skipped")
        return

    if choice == "all":
        result = df
    elif choice.isdigit():
        n = int(choice)
        if n < 1 or n > total:
            print("Invalid number")
            return
        result = df.head(n)
    else:
        print("Invalid input")
        return

    print(result)
    save_result("Preview", result)
    export_result(result)


def total_sales(df):
    if "sales" not in df.columns:
        print("Missing data")
        return

    table = pd.pivot_table(
        df,
        values="sales",
        index="sales_region",
        columns="order_type",
        aggfunc="sum",
        fill_value=0
    )

    print(table)
    save_result("Total Sales", table)
    export_result(table)


def avg_sales(df):
    table = pd.pivot_table(
        df,
        values="sales",
        index="sales_region",
        columns=["customer_state", "order_type"],
        aggfunc="mean",
        fill_value=0
    )

    print(table)
    save_result("Average Sales", table)
    export_result(table)


def sales_customer(df):
    table = pd.pivot_table(
        df,
        values="sales",
        index=["customer_state", "customer_type"],
        columns="order_type",
        aggfunc="sum",
        fill_value=0
    )

    print(table)
    save_result("Sales Customer", table)
    export_result(table)


def sales_product(df):
    table = pd.pivot_table(
        df,
        values=["quantity", "sales"],
        index=["sales_region", "produce_name"],
        aggfunc="sum",
        fill_value=0
    )

    print(table)
    save_result("Sales Product", table)
    export_result(table)


def sales_customer_type(df):
    table = pd.pivot_table(
        df,
        values=["quantity", "sales"],
        index=["customer_type", "order_type"],
        aggfunc="sum",
        fill_value=0
    )

    print(table)
    save_result("Sales Customer Type", table)
    export_result(table)


def max_min(df):
    table = pd.pivot_table(
        df,
        values="sales",
        index="product_category",
        aggfunc=["max", "min"],
        fill_value=0
    )

    print(table)
    save_result("Max Min", table)
    export_result(table)


def unique_emp(df):
    table = pd.pivot_table(
        df,
        values="employee_name",
        index="sales_region",
        aggfunc="nunique",
        fill_value=0
    )

    print(table)
    save_result("Employees", table)
    export_result(table)


# CUSTOM PIVOT (simplified)
def custom(df):
    print("\nCustom Pivot")

    rows = input("Row: ")
    cols = input("Column (or blank): ")
    vals = input("Value: ")
    agg = input("Agg (sum/mean/count): ")

    try:
        if cols == "":
            table = pd.pivot_table(df, values=vals, index=rows, aggfunc=agg)
        else:
            table = pd.pivot_table(df, values=vals, index=rows, columns=cols, aggfunc=agg)

        print(table)
        save_result("Custom", table)
        export_result(table)

    except:
        print("Error")


# MENU (tuple still there for requirement)
def main():
    df = load_data()
    if df is None:
        return

    menu = (
        ("Show first rows", show_first),
        ("Total sales", total_sales),
        ("Average sales", avg_sales),
        ("Sales by customer", sales_customer),
        ("Sales by product", sales_product),
        ("Sales by customer type", sales_customer_type),
        ("Max min sales", max_min),
        ("Unique employees", unique_emp),
        ("Custom pivot", custom),
        ("Show saved", show_history),
        ("Exit", None)
    )

    while True:
        show_done()

        print("\n--- Dashboard ---")
        for i in range(len(menu)):
            print(i+1, ".", menu[i][0])

        choice = input("Choose: ")

        if not choice.isdigit():
            print("Invalid")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(menu):
            print("Invalid")
            continue

        if menu[choice-1][0] == "Exit":
            print("Bye")
            break

        func = menu[choice-1][1]

        if func == show_history:
            func()
        else:
            func(df)


main()