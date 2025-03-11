import pandas as pd

class CSVHandler:

    @staticmethod
    def get_data_from_csv(csv_path):
        return pd.read_csv(csv_path)


if __name__ == '__main__':
    #file_path = r"C:\2025-project\data\circuits.csv"
    file_path = r"C:\2025-project\data\constructor_results.csv"
    # file_path = r"C:\2025-project\data\constructor_standings.csv"
    # file_path = r"C:\2025-project\data\constructors.csv"
    # file_path = r"C:\2025-project\data\driver_standings.csv"
    # file_path = r"C:\2025-project\data\drivers.csv"
    # file_path = r"C:\2025-project\data\lap_times.csv"
    # file_path = r"C:\2025-project\data\pit_stops.csv"
    # file_path = r"C:\2025-project\data\qualifying.csv"
    # file_path = r"C:\2025-project\data\races.csv"
    # file_path = r"C:\2025-project\data\results.csv"
    # file_path = r"C:\2025-project\data\seasons.csv"
    # file_path = r"C:\2025-project\data\sprint_results.csv"
    # file_path = r"C:\2025-project\data\status.csv"

    data = CSVHandler.get_data_from_csv(file_path)

    print(data.head(3))