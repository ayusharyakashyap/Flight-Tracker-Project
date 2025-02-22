import requests
from rich.console import Console
from rich.table import Table

# Initialize console for rich output
console = Console()

# Your AviationStack API key
API_KEY = "a676f8f7e90b93f762b96569c3569e64"

# Function to fetch flights with live data
def get_flights_with_live_data():
    url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&flight_status=active"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        if not data.get("data"):  # Ensure 'data' key exists and is not empty
            console.print("[bold red]⚠ No active flights with live data found.[/bold red]")
            return

        # Displaying flights with live data in a table
        table = Table(title="✈ Active Flights with Live Data", style="cyan")

        table.add_column("Flight Number", style="bold yellow")
        table.add_column("Airline", style="bold white")
        table.add_column("Departure", style="bold white")
        table.add_column("Arrival", style="bold white")
        table.add_column("Status", style="bold white")

        for flight in data["data"]:
            live_data = flight.get('live')
            if live_data:
                table.add_row(
                    flight.get('flight', {}).get('iata', 'N/A'),
                    flight.get('airline', {}).get('name', 'N/A'),
                    flight.get('departure', {}).get('airport', 'N/A'),
                    flight.get('arrival', {}).get('airport', 'N/A'),
                    flight.get('flight_status', 'N/A')
                )

        console.print(table)

    else:
        console.print(f"[bold red]❌ Error fetching flight data: {response.status_code}[/bold red]")

# Fetch and display flights with live data
get_flights_with_live_data()