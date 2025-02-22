import requests
from tabulate import tabulate
from rich.console import Console
from rich.table import Table

# Initialize console for rich output
console = Console()

# Your AviationStack API key
API_KEY = "a676f8f7e90b93f762b96569c3569e64"

# Function to fetch and display flight status
def get_flight_status(flight_iata):
    url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&flight_iata={flight_iata}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        if not data.get("data"):  # Ensure 'data' key exists and is not empty
            console.print("[bold red]⚠ No active flight found for the given flight number.[/bold red]")
            return

        flight = data["data"][0]  # Taking the first match

        # Displaying flight information in a table
        table = Table(title=f"✈ Flight Information: {flight_iata}", style="cyan")

        table.add_column("Field", style="bold yellow")
        table.add_column("Details", style="bold white")

        table.add_row("Flight Number", flight.get('flight', {}).get('iata', 'N/A'))
        table.add_row("Airline", flight.get('airline', {}).get('name', 'N/A'))
        table.add_row("Departure Airport", flight.get('departure', {}).get('airport', 'N/A'))
        table.add_row("Departure IATA", flight.get('departure', {}).get('iata', 'N/A'))
        table.add_row("Arrival Airport", flight.get('arrival', {}).get('airport', 'N/A'))
        table.add_row("Arrival IATA", flight.get('arrival', {}).get('iata', 'N/A'))
        table.add_row("Status", flight.get('flight_status', 'N/A'))
        table.add_row("Scheduled Departure", flight.get('departure', {}).get('scheduled', 'N/A'))
        table.add_row("Scheduled Arrival", flight.get('arrival', {}).get('scheduled', 'N/A'))

        # Print flight details
        console.print(table)

        # Check if 'live' data is available
        live_data = flight.get('live')
        if live_data:
            live_table = Table(title="🛰 Live Flight Data", style="magenta")

            live_table.add_column("Field", style="bold green")
            live_table.add_column("Value", style="bold white")

            live_table.add_row("Altitude", f"{live_data.get('altitude', 'N/A')} meters")
            live_table.add_row("Speed", f"{live_data.get('speed_horizontal', 'N/A')} km/h")
            live_table.add_row("Latitude", str(live_data.get('latitude', 'N/A')))
            live_table.add_row("Longitude", str(live_data.get('longitude', 'N/A')))

            # Print live tracking details
            console.print(live_table)
        else:
            console.print("[bold red]🚫 Live tracking data is not available for this flight.[/bold red]")

    else:
        console.print(f"[bold red]❌ Error fetching flight data: {response.status_code}[/bold red]")

# Take flight number as input from the user
flight_number = input("🛫 Enter Flight Number (IATA Code): ").strip().upper()
get_flight_status(flight_number)