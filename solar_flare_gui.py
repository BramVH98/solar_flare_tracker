import requests
import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

API_KEY = "DEMO_KEY"  # Replace with your NASA API key
BASE_URL = "https://api.nasa.gov/DONKI/FLR"

def get_solar_flares(start_date, end_date, output_box):
    try:
        params = {
            "startDate": start_date,
            "endDate": end_date,
            "api_key": API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        output_box.delete(1.0, tk.END)
        if not data:
            output_box.insert(tk.END, "No solar flares found.\n")
        else:
            for flare in data:
                output_box.insert(tk.END, f"Class: {flare['classType']}\n")
                output_box.insert(tk.END, f"Begin: {flare['beginTime']}\n")
                output_box.insert(tk.END, f"Peak: {flare['peakTime']}\n")
                output_box.insert(tk.END, f"Location: {flare.get('sourceLocation', 'N/A')}\n")
                output_box.insert(tk.END, "-" * 40 + "\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_app():
    root = tk.Tk()
    root.title("Solar Flare Tracker")
    root.geometry("600x400")

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(frame, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W)
    start_entry = ttk.Entry(frame)
    start_entry.grid(row=0, column=1, sticky=tk.EW)

    ttk.Label(frame, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, sticky=tk.W)
    end_entry = ttk.Entry(frame)
    end_entry.grid(row=1, column=1, sticky=tk.EW)

    output_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=15)
    output_box.grid(row=3, column=0, columnspan=2, pady=10)

    def fetch_data():
        start_date = start_entry.get()
        end_date = end_entry.get()
        get_solar_flares(start_date, end_date, output_box)

    fetch_button = ttk.Button(frame, text="Fetch Solar Flares", command=fetch_data)
    fetch_button.grid(row=2, column=0, columnspan=2, pady=5)

    frame.columnconfigure(1, weight=1)
    root.mainloop()

create_app()
