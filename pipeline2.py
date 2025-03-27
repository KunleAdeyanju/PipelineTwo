# Exercise: Process store_sales.csv and calculate basic statistics
# Your task is to complete this outline with working code
#
# See ./Notes.md for some more instructions and explanations.
pass

# Import the csv module
# Import any other modules you need (e.g., collections for defaultdict)
import csv
import collections

# Initialize data structures to hold our results
# Hint: Consider using a dictionary with store_id as keys
store_template = {
    "items_sold" : 0,
    "transactions" : 0
}

stores = {

}
# For each store, you'll need to track:
#   - Count of days
#   - Total items sold
#   - Total revenue
#   - Minimum revenue
#   - Maximum revenue


# Open the CSV file for reading
# Remember to use "with" to ensure the file gets closed properly

    # Create a CSV reader

    # Read the header row first

    # Loop through each row in the CSV file
        # Extract values from each row (date, store_id, items_sold, revenue)
        # Convert numerical values to the right data types (int, float)

        # Update the appropriate store's statistics:
        #   - Increment day count
        #   - Add to total items
        #   - Add to total revenue
        #   - Update min revenue if current is lower
        #   - Update max revenue if current is higher

# Calculate averages for each store
# For each store in your data structure:
    # Calculate average items per day (total_items / days)
    # Calculate average revenue per day (total_revenue / days)

# Determine which store had the highest average daily revenue
# Initialize variables to track best store and its revenue
# Loop through stores and compare average revenues

# Print a summary of statistics for each store
# Print which store had the highest average daily revenue

import csv

store_template = {
    "items_sold": 0,
    "transactions": 0,
    "revenue" : 0,
    "Avg items sold per day" : 0
}

stores = {
}


with open('store_sales.csv', 'r', newline='') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    sum_of_items = 0
    sum_of_revenue = 0 
    lines = 0
    for line in csv_reader:
        #print(line)
        if lines == 0:
            lines += 1
            continue
        sum_of_items += int(line[2])
        sum_of_revenue += float(line[3])
        curstore = line[1]
        if stores.get(curstore) == None:
            stores[curstore] = store_template.copy()
        stores[curstore]["items_sold"] += int(line[2])
        stores[curstore]["revenue"] += float(line[3])
        stores[curstore]["revenue"] = round(stores[curstore]["revenue"],2)
        
        # finctions

        lines += 1
        stores[curstore]["transactions"] += 1
        if stores[curstore]["transactions"] > 0:
            stores[curstore]["Avg items sold per day"] = stores[curstore].get('items_sold') // stores[curstore]["transactions"]

        #print(lines, line[0], line[1], line[2], line[3])
    print(f"Total number of items sold: {sum_of_items}")
    print(f"Total number of transactions: {lines-1}")
    print(f"The total revenue: {sum_of_revenue:.2f} ")
    print("\nStores Stats")
    [print(f"{key}: {Value}") for key,Value in stores.items()]
    