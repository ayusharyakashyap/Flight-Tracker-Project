# ✈ Flight Status Tracker

This project allows you to fetch real-time flight status using the **AviationStack API**. The program retrieves details about a given flight, including departure and arrival information, flight status, and live tracking data (if available).

## 🚀 Features

- Fetches flight details using the **AviationStack API**.
- Displays information in a structured, aesthetic format using **Rich** and **Tabulate**.
- Retrieves **live tracking data** (altitude, speed, latitude, longitude) if available.
- Lists active flights with live tracking data.
- User-friendly input for flight search.

## 📂 Repository Structure

- `Live.py` - Displays a list of currently active flights with live tracking data.
- `Tracker.py` - Fetches and displays detailed flight tracking data.
- `Tracker.ipynb` - Jupyter Notebook containing the implementation and testing.
- `README.md` - Project documentation.

## 🛠 Installation

### 1️⃣ Clone the Repository

```sh
https://github.com/yourusername/flight-status-tracker.git
```

### 2️⃣ Install Dependencies

Make sure you have **Python 3.7+** installed. Install required libraries using:

```sh
pip install requests rich tabulate
```

## 🔑 API Key Setup

The script uses **AviationStack API** to fetch flight data. Replace the placeholder API key in `Live.py` and `Tracker.py` with your own:

```python
API_KEY = "your_api_key_here"
```

## 🚀 Usage

### 1️⃣ Fetch Active Flights

To list currently active flights with live tracking data:

```sh
python Live.py
```

### 2️⃣ Track a Specific Flight

Run the script and enter a **flight number (IATA Code, no spaces)** when prompted:

```sh
python Tracker.py
```

or execute the notebook file in Jupyter.

## 🖥 Example Output

```
🛫 Enter Flight Number (IATA Code): AI302

✈ Flight Information: AI302
----------------------------------
Flight Number      | AI302
Airline           | Air India
Departure Airport | Indira Gandhi International Airport
Arrival Airport   | Sydney Kingsford Smith Airport
Status            | En Route
...

🛰 Live Flight Data
----------------------------------
Altitude    | 10,500 meters
Speed       | 890 km/h
Latitude    | 28.7041
Longitude   | 77.1025
```

## 📝 Notes

- If no flight is found, the program notifies the user.
- If **live tracking** is unavailable, an appropriate message is displayed.
- Ensure your API key is valid and has access to real-time flight data.

## 🔗 API Reference

[AviationStack API](https://aviationstack.com/)

## 📜 License

This project is open-source under the **MIT License**.

---

Feel free to customize the README with your **GitHub repo link** and **your API key details** (if necessary). 🚀
