import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from abc import ABC, abstractmethod


# ----------------------------------- Colors -----------------------------------

BG = "#f1f5f9"
SIDEBAR = "#1e293b"
PRIMARY = "#f97316"
GREEN = "#16a34a"
RED = "#dc2626"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
GRAY = "#64748b"
WHITE = "#ffffff"


# ----------------------------------- OOP Classes -----------------------------------

class Vehicle(ABC):

    def __init__(self, vehicle_id, brand, model, rental_price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.__rental_price = rental_price
        self.__is_available = True

    # Getter Method
    def get_rental_price(self):
        return self.__rental_price

    # Getter Method
    def get_is_available(self):
        return self.__is_available

    # Setter Method
    def set_is_available(self, status):
        self.__is_available = status

    # Abstract Method
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def vehicle_type(self):
        pass

    def status_text(self):
        return "Available" if self.get_is_available() else "Rented"


# ----------------------------------- Car Class -----------------------------------

class Car(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price,
                 number_of_seats, fuel_type):

        super().__init__(vehicle_id, brand, model, rental_price)

        self.number_of_seats = number_of_seats
        self.fuel_type = fuel_type

    def vehicle_type(self):
        return "Car"

    def short_details(self):
        return f"{self.number_of_seats} Seats | {self.fuel_type}"

    def display(self):

        return (
            "---- Car Details ----\n\n"
            f"Vehicle ID       : {self.vehicle_id}\n"
            f"Brand            : {self.brand}\n"
            f"Model            : {self.model}\n"
            f"Rental Price     : Rs. {self.get_rental_price():.2f}\n"
            f"Number of Seats  : {self.number_of_seats}\n"
            f"Fuel Type        : {self.fuel_type}\n"
            f"Status           : {self.status_text()}"
        )


# ----------------------------------- Bike Class -----------------------------------

class Bike(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price,
                 bike_type):

        super().__init__(vehicle_id, brand, model, rental_price)

        self.bike_type = bike_type

    def vehicle_type(self):
        return "Bike"

    def short_details(self):
        return f"Type: {self.bike_type}"

    def display(self):

        return (
            "---- Bike Details ----\n\n"
            f"Vehicle ID   : {self.vehicle_id}\n"
            f"Brand        : {self.brand}\n"
            f"Model        : {self.model}\n"
            f"Rental Price : Rs. {self.get_rental_price():.2f}\n"
            f"Bike Type    : {self.bike_type}\n"
            f"Status       : {self.status_text()}"
        )


# ----------------------------------- GUI App -----------------------------------

class VehicleRentalApp(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Vehicle Rental Management System")
        self.geometry("1100x650")
        self.minsize(950, 580)
        self.configure(bg=BG)

        self.vehicles = {}

        self._setup_style()
        self._build_header()
        self._build_sidebar()
        self._build_vehicle_table()
        self._build_details_panel()
        self._build_statusbar()

        self.refresh()


    # ---------- Styling ----------

    def _setup_style(self):

        style = ttk.Style(self)

        style.theme_use("clam")

        style.configure(
            "Treeview",
            rowheight=32,
            font=("Segoe UI", 10),
            background=WHITE,
            fieldbackground=WHITE,
            borderwidth=0
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background=PRIMARY,
            foreground=WHITE,
            relief="flat"
        )

        style.map(
            "Treeview",
            background=[("selected", "#fed7aa")],
            foreground=[("selected", "#000000")]
        )


    # ---------- Header ----------

    def _build_header(self):

        header = tk.Frame(
            self,
            bg=PRIMARY,
            height=70
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="🚗  Vehicle Rental Management System",
            bg=PRIMARY,
            fg=WHITE,
            font=("Segoe UI", 20, "bold")
        ).pack(side="left", padx=25)

        tk.Label(
            header,
            text="Python OOP Project",
            bg=PRIMARY,
            fg="#ffedd5",
            font=("Segoe UI", 11)
        ).pack(side="right", padx=25)


    # ---------- Button ----------

    def _make_button(self, parent, text, color, command):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=WHITE,
            activebackground=color,
            activeforeground=WHITE,
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            anchor="w",
            padx=18,
            pady=10
        )

        button.pack(
            fill="x",
            padx=15,
            pady=6
        )

        return button


    # ---------- Sidebar ----------

    def _build_sidebar(self):

        side = tk.Frame(
            self,
            bg=SIDEBAR,
            width=250
        )

        side.pack(
            side="left",
            fill="y"
        )

        side.pack_propagate(False)

        tk.Label(
            side,
            text="OPERATIONS",
            bg=SIDEBAR,
            fg="#94a3b8",
            font=("Segoe UI", 10, "bold")
        ).pack(pady=(25, 10))


        self._make_button(
            side,
            "🚗  Add Car",
            GREEN,
            lambda: self.add_vehicle("car")
        )

        self._make_button(
            side,
            "🏍️  Add Bike",
            BLUE,
            lambda: self.add_vehicle("bike")
        )

        self._make_button(
            side,
            "🔑  Rent Vehicle",
            PRIMARY,
            self.rent_vehicle
        )

        self._make_button(
            side,
            "↩️  Return Vehicle",
            RED,
            self.return_vehicle
        )

        self._make_button(
            side,
            "📋  Show Details",
            PURPLE,
            self.show_details
        )

        self._make_button(
            side,
            "🚪  Exit",
            GRAY,
            self.on_exit
        )


    # ---------- Vehicle Table ----------

    def _build_vehicle_table(self):

        center = tk.Frame(
            self,
            bg=BG
        )

        center.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(20, 10),
            pady=20
        )

        tk.Label(
            center,
            text="Vehicles",
            bg=BG,
            fg=SIDEBAR,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            pady=(0, 8)
        )


        columns = (
            "id",
            "brand",
            "model",
            "type",
            "price",
            "details",
            "status"
        )

        self.tree = ttk.Treeview(
            center,
            columns=columns,
            show="headings",
            selectmode="browse"
        )


        widths = {
            "id": 70,
            "brand": 100,
            "model": 100,
            "type": 80,
            "price": 90,
            "details": 180,
            "status": 90
        }


        for column in columns:

            self.tree.heading(
                column,
                text=column.title()
            )

            self.tree.column(
                column,
                width=widths[column],
                anchor="center"
            )


        self.tree.tag_configure(
            "available",
            background="#dcfce7"
        )

        self.tree.tag_configure(
            "rented",
            background="#fee2e2"
        )


        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )


        scrollbar = ttk.Scrollbar(
            center,
            orient="vertical",
            command=self.tree.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )


        self.tree.bind(
            "<Double-1>",
            lambda e: self.show_details()
        )


    # ---------- Details Panel ----------

    def _build_details_panel(self):

        right = tk.Frame(
            self,
            bg=WHITE,
            width=280,
            highlightbackground="#e2e8f0",
            highlightthickness=1
        )

        right.pack(
            side="right",
            fill="y",
            padx=(10, 20),
            pady=20
        )

        right.pack_propagate(False)


        tk.Label(
            right,
            text="🚘  Vehicle Details",
            bg=SIDEBAR,
            fg=WHITE,
            font=("Segoe UI", 14, "bold"),
            pady=10
        ).pack(fill="x")


        self.details_box = tk.Text(
            right,
            bg=WHITE,
            fg=SIDEBAR,
            font=("Consolas", 10),
            relief="flat",
            state="disabled",
            padx=12,
            pady=10
        )

        self.details_box.pack(
            fill="both",
            expand=True
        )


        self.total_label = tk.Label(
            right,
            text="Vehicles : 0",
            bg=PRIMARY,
            fg=WHITE,
            font=("Segoe UI", 14, "bold"),
            pady=12
        )

        self.total_label.pack(
            fill="x"
        )


    # ---------- Status Bar ----------

    def _build_statusbar(self):

        self.status = tk.Label(
            self,
            text="Welcome! Add a vehicle to begin.",
            bg=SIDEBAR,
            fg="#e2e8f0",
            anchor="w",
            padx=15,
            font=("Segoe UI", 10)
        )

        self.status.pack(
            side="bottom",
            fill="x"
        )


    # ---------- Helpers ----------

    def set_status(self, message):

        self.status.config(
            text=message
        )


    def refresh(self):

        self.tree.delete(
            *self.tree.get_children()
        )


        for vehicle in self.vehicles.values():

            tag = (
                "available"
                if vehicle.get_is_available()
                else "rented"
            )


            self.tree.insert(
                "",
                "end",
                iid=vehicle.vehicle_id,
                tags=(tag,),
                values=(
                    vehicle.vehicle_id,
                    vehicle.brand,
                    vehicle.model,
                    vehicle.vehicle_type(),
                    f"{vehicle.get_rental_price():.2f}",
                    vehicle.short_details(),
                    vehicle.status_text()
                )
            )


        available = sum(
            1
            for vehicle in self.vehicles.values()
            if vehicle.get_is_available()
        )


        self.total_label.config(
            text=f"Vehicles : {len(self.vehicles)}"
        )


        self.details_box.config(
            state="normal"
        )

        self.details_box.delete(
            "1.0",
            "end"
        )

        self.details_box.insert(
            "end",
            f"Total Vehicles : {len(self.vehicles)}\n"
            f"Available      : {available}\n"
            f"Rented         : {len(self.vehicles) - available}"
        )

        self.details_box.config(
            state="disabled"
        )


    def get_target_vehicle(self, action):

        if not self.vehicles:

            messagebox.showwarning(
                "No Vehicles",
                "No vehicle is added."
            )

            return None


        selection = self.tree.selection()


        vehicle_id = (
            selection[0]
            if selection
            else simpledialog.askstring(
                action,
                f"Enter Vehicle ID to {action.lower()} :",
                parent=self
            )
        )


        if not vehicle_id:

            return None


        vehicle = self.vehicles.get(
            vehicle_id.strip()
        )


        if vehicle is None:

            messagebox.showerror(
                "Not Found",
                "This Vehicle ID does not exist."
            )


        return vehicle


    # ---------- Add Vehicle ----------

    def add_vehicle(self, kind):

        win = tk.Toplevel(self)

        win.title(
            "Add Car"
            if kind == "car"
            else "Add Bike"
        )

        win.configure(
            bg=WHITE
        )

        win.resizable(
            False,
            False
        )

        win.grab_set()


        color = (
            GREEN
            if kind == "car"
            else BLUE
        )


        tk.Label(
            win,
            text="🚗 Car"
            if kind == "car"
            else "🏍️ Bike",
            bg=color,
            fg=WHITE,
            font=("Segoe UI", 14, "bold"),
            pady=10
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew"
        )


        fields = [
            ("Vehicle ID", "id"),
            ("Brand", "brand"),
            ("Model", "model"),
            ("Rental Price", "price")
        ]


        if kind == "car":

            fields += [
                ("Number of Seats", "seats"),
                ("Fuel Type", "fuel")
            ]

        else:

            fields += [
                ("Bike Type", "bike_type")
            ]


        widgets = {}


        for row, (label, key) in enumerate(
            fields,
            start=1
        ):

            tk.Label(
                win,
                text=label,
                bg=WHITE,
                font=("Segoe UI", 10, "bold"),
                anchor="w"
            ).grid(
                row=row,
                column=0,
                padx=20,
                pady=8,
                sticky="w"
            )


            if key == "fuel":

                widget = ttk.Combobox(
                    win,
                    values=[
                        "Petrol",
                        "Diesel",
                        "Electric",
                        "CNG"
                    ],
                    state="readonly",
                    width=23
                )

                widget.set("Petrol")

            elif key == "bike_type":

                widget = ttk.Combobox(
                    win,
                    values=[
                        "Sports",
                        "Cruiser",
                        "Scooter",
                        "Commuter"
                    ],
                    state="readonly",
                    width=23
                )

                widget.set("Commuter")

            else:

                widget = ttk.Entry(
                    win,
                    width=26
                )


            widget.grid(
                row=row,
                column=1,
                padx=20,
                pady=8
            )


            widgets[key] = widget


        def save():

            vehicle_id = widgets["id"].get().strip()
            brand = widgets["brand"].get().strip()
            model = widgets["model"].get().strip()


            if not vehicle_id or not brand or not model:

                messagebox.showerror(
                    "Error",
                    "Vehicle ID, Brand and Model are required.",
                    parent=win
                )

                return


            if vehicle_id in self.vehicles:

                messagebox.showerror(
                    "Error",
                    "This Vehicle ID already exists.",
                    parent=win
                )

                return


            try:

                price = float(
                    widgets["price"].get()
                )

                if price < 0:

                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Enter a valid rental price.",
                    parent=win
                )

                return


            if kind == "car":

                try:

                    seats = int(
                        widgets["seats"].get()
                    )

                    if seats <= 0:

                        raise ValueError

                except ValueError:

                    messagebox.showerror(
                        "Error",
                        "Enter a valid number of seats.",
                        parent=win
                    )

                    return


                vehicle = Car(
                    vehicle_id,
                    brand,
                    model,
                    price,
                    seats,
                    widgets["fuel"].get()
                )

            else:

                vehicle = Bike(
                    vehicle_id,
                    brand,
                    model,
                    price,
                    widgets["bike_type"].get()
                )


            self.vehicles[vehicle_id] = vehicle

            self.refresh()

            self.set_status(
                f"{vehicle.vehicle_type()} created : "
                f"{brand} {model} "
                f"(ID {vehicle_id})"
            )

            win.destroy()


        tk.Button(
            win,
            text="Save Vehicle",
            command=save,
            bg=color,
            fg=WHITE,
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            pady=8
        ).grid(
            row=len(fields) + 1,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=18
        )


    # ---------- Rent Vehicle ----------

    def rent_vehicle(self):

        vehicle = self.get_target_vehicle(
            "Rent"
        )


        if vehicle is None:

            return


        if vehicle.get_is_available():

            vehicle.set_is_available(
                False
            )

            self.refresh()

            self.set_status(
                f"{vehicle.vehicle_type()} "
                f"{vehicle.brand} {vehicle.model} "
                f"has been rented successfully."
            )

        else:

            messagebox.showinfo(
                "Already Rented",
                f"{vehicle.brand} {vehicle.model} "
                f"is already rented."
            )


    # ---------- Return Vehicle ----------

    def return_vehicle(self):

        vehicle = self.get_target_vehicle(
            "Return"
        )


        if vehicle is None:

            return


        if not vehicle.get_is_available():

            vehicle.set_is_available(
                True
            )

            self.refresh()

            self.set_status(
                f"{vehicle.vehicle_type()} "
                f"{vehicle.brand} {vehicle.model} "
                f"returned successfully."
            )

        else:

            messagebox.showinfo(
                "Already Available",
                f"{vehicle.brand} {vehicle.model} "
                f"is already available."
            )


    # ---------- Show Details ----------

    def show_details(self):

        selection = self.tree.selection()


        if not selection:

            messagebox.showinfo(
                "Select Vehicle",
                "Please select a vehicle from the table first."
            )

            return


        vehicle = self.vehicles[
            selection[0]
        ]


        messagebox.showinfo(
            "Vehicle Details",
            vehicle.display()
        )


    # ---------- Exit ----------

    def on_exit(self):

        if messagebox.askyesno(
            "Exit",
            "Exiting the Programme. Goodbye!\n\n"
            "Do you want to exit?"
        ):

            self.destroy()


# ----------------------------------- Main -----------------------------------

if __name__ == "__main__":

    VehicleRentalApp().mainloop()