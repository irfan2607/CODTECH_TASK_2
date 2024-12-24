import csv

def save_results_to_csv(results, filename="scan_results.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "State", "Service", "Version"])
        for result in results:
            writer.writerow(result)
    print(f"Results saved to {filename}")
