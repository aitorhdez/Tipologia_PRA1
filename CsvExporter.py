import csv
from pathlib import Path

class CsvExporter:
    
    def ToCsv(routesList, path):
        """        
        Export routes to a 
        """
        
        Path("csv/").mkdir(parents=True, exist_ok=True)
        file_name = path
        with open(file_name, mode='w', encoding="utf-8", newline='\n') as write_file:
            csv_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["Route_name", "Activity", "Starting_Point", "Distance", "Elevation_gain", "Rank1", "Rank2", "Description"])
            row = []
            for route in routesList:
                row.append(route.name)
                row.append(route.activity)
                row.append(route.start)
                row.append(route.distance)
                row.append(route.elevation)
                row.append(route.rank1)
                row.append(route.rank2)
                row.append(route.description)
                csv_writer.writerow(row)
                row = []





