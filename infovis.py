import matplotlib.pyplot as plt
import os

# Function to create a bar chart from the sales data
def visualize_sales(summary):
    # Ensure the summary data is valid
    validate_summary_data(summary)

    item_names = [item["name"] for item in summary["items"]]
    item_prices = [float(item["price"]) for item in summary["items"]]

    if not item_names or not item_prices:
        raise ValueError("Items or prices list is empty. Unable to generate graph.")

        Set up the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(item_names, item_prices, color='blue')
    plt.xlabel('Items')
    plt.ylabel('Prices (Currency)')
    plt.title('Sales Summary')

    Adjust item labels to avoid overlap
    plt.xticks(rotation=45, ha="right")

    # Save the graph to a file
    graph_folder = os.path.join(os.path.dirname(os.path.abspath(file)), "visualization")
    os.makedirs(graph_folder, exist_ok=True)
    plt.savefig(os.path.join(graph_folder, "sales_summary.png"))
    plt.show()