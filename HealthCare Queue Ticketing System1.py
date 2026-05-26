# =========================================================
# HealthCare TICKETING SYSTEM
# Developed with Python Tkinter
# Features:
# - Automatic Ticket Generation
# - Queue Prioritization
# - Live Waiting Queue
# - Modern Skeuomorphic UI
# - Timestamp Registration
# - Department Selection
# - Priority Customer Handling
# - Stylish Dashboard Layout
# =========================================================

import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox


# =========================================================
# MAIN APPLICATION
# =========================================================

class TicketingSystem:

    def __init__(self, root):

        self.root = root
        self.root.title("HealthCare Queue Ticketing System")
        self.root.geometry("1200x700")
        self.root.configure(bg="#d6d6d6")

        # Queue Data
        self.normal_queue = []
        self.priority_queue = []

        self.ticket_counter = 100

        # =================================================
        # STYLE CONFIGURATION
        # =================================================

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Treeview",
            background="#f2f2f2",
            foreground="black",
            rowheight=35,
            fieldbackground="#f2f2f2",
            font=("Segoe UI", 11)
        )

        self.style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 12, "bold"),
            background="#d9d9d9"
        )

        # =================================================
        # MAIN FRAME
        # =================================================

        main_frame = tk.Frame(
            root,
            bg="#d6d6d6"
        )
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # =================================================
        # LEFT PANEL
        # =================================================

        left_panel = tk.Frame(
            main_frame,
            bg="#e0e0e0",
            bd=2,
            relief="ridge"
        )

        left_panel.place(x=10, y=10, width=400, height=650)

        # Header
        title = tk.Label(
            left_panel,
            text="QUEUE REGISTRATION",
            font=("Segoe UI", 20, "bold"),
            bg="#e0e0e0",
            fg="#222222"
        )

        title.pack(pady=20)

        # =================================================
        # FORM FIELDS
        # =================================================

        # Name
        tk.Label(
            left_panel,
            text="Full Name",
            font=("Segoe UI", 11),
            bg="#e0e0e0"
        ).pack(anchor="w", padx=25)

        self.name_entry = tk.Entry(
            left_panel,
            font=("Segoe UI", 12),
            relief="sunken",
            bd=3
        )

        self.name_entry.pack(fill="x", padx=25, pady=10)

        # Reason
        tk.Label(
            left_panel,
            text="Reason For Visit",
            font=("Segoe UI", 11),
            bg="#e0e0e0"
        ).pack(anchor="w", padx=25)

        self.reason_entry = tk.Entry(
            left_panel,
            font=("Segoe UI", 12),
            relief="sunken",
            bd=3
        )

        self.reason_entry.pack(fill="x", padx=25, pady=10)

        # Department
        tk.Label(
            left_panel,
            text="Department",
            font=("Segoe UI", 11),
            bg="#e0e0e0"
        ).pack(anchor="w", padx=25)

        self.department = ttk.Combobox(
            left_panel,
            values=[
                "Accounts Billing",
                "Emergency Services",
                "Consultation",
                "Surgery",
                "Pharmacy",
                "Patients Records",
                "Radiology",
                "Laboratory",
                "Consultation"
            ],
            font=("Segoe UI", 11)
        )

        self.department.pack(fill="x", padx=25, pady=10)
        self.department.current(0)

        # Priority Checkbox
        self.priority_var = tk.BooleanVar()

        priority_check = tk.Checkbutton(
            left_panel,
            text="Priority Customer",
            variable=self.priority_var,
            font=("Segoe UI", 11),
            bg="#e0e0e0",
            activebackground="#e0e0e0"
        )

        priority_check.pack(anchor="w", padx=25, pady=10)

        # =================================================
        # BUTTONS
        # =================================================

        register_btn = tk.Button(
            left_panel,
            text="GENERATE TICKET",
            font=("Segoe UI", 13, "bold"),
            bg="#4d4d4d",
            fg="white",
            relief="raised",
            bd=5,
            padx=10,
            pady=10,
            cursor="hand2",
            command=self.generate_ticket
        )

        register_btn.pack(fill="x", padx=25, pady=20)

        next_btn = tk.Button(
            left_panel,
            text="CALL NEXT CUSTOMER",
            font=("Segoe UI", 13, "bold"),
            bg="#2f2f2f",
            fg="white",
            relief="raised",
            bd=5,
            padx=10,
            pady=10,
            cursor="hand2",
            command=self.call_next_customer
        )

        next_btn.pack(fill="x", padx=25)

        # =================================================
        # RIGHT PANEL
        # =================================================

        right_panel = tk.Frame(
            main_frame,
            bg="#efefef",
            bd=2,
            relief="ridge"
        )

        right_panel.place(x=430, y=10, width=740, height=650)

        queue_title = tk.Label(
            right_panel,
            text="LIVE WAITING QUEUE",
            font=("Segoe UI", 20, "bold"),
            bg="#efefef"
        )

        queue_title.pack(pady=20)

        # =================================================
        # TREEVIEW TABLE
        # =================================================

        columns = (
            "Ticket",
            "Name",
            "Department",
            "Priority",
            "Time"
        )

        self.tree = ttk.Treeview(
            right_panel,
            columns=columns,
            show="headings",
            height=20
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        # =================================================
        # FOOTER
        # =================================================

        footer = tk.Label(
            root,
            text="Smart AI Queue Management System",
            font=("Segoe UI", 10),
            bg="#d6d6d6",
            fg="#555555"
        )

        footer.pack(side="bottom", pady=5)

    # =====================================================
    # GENERATE TICKET
    # =====================================================

    def generate_ticket(self):

        name = self.name_entry.get()
        reason = self.reason_entry.get()
        department = self.department.get()
        priority = self.priority_var.get()

        if not name or not reason:
            messagebox.showerror(
                "Missing Information",
                "Please complete all fields."
            )
            return

        # Generate Automatic Ticket Number
        self.ticket_counter += 1
        ticket_number = f"T-{self.ticket_counter}"

        # Current Time
        current_time = datetime.now().strftime("%H:%M:%S")

        customer_data = {
            "ticket": ticket_number,
            "name": name,
            "department": department,
            "priority": "YES" if priority else "NO",
            "time": current_time
        }

        # Queue Prioritization Logic
        if priority:
            self.priority_queue.append(customer_data)
        else:
            self.normal_queue.append(customer_data)

        # Insert Into Table
        self.tree.insert(
            "",
            "end",
            values=(
                ticket_number,
                name,
                department,
                customer_data["priority"],
                current_time
            )
        )

        # Ticket Popup
        messagebox.showinfo(
            "Ticket Generated",
            f"""
            Ticket Successfully Generated

            Ticket Number: {ticket_number}
            Customer: {name}
            Department: {department}
            Priority: {customer_data['priority']}
            Time: {current_time}
            """
        )

        # Clear Inputs
        self.name_entry.delete(0, tk.END)
        self.reason_entry.delete(0, tk.END)
        self.priority_var.set(False)

    # =====================================================
    # CALL NEXT CUSTOMER
    # =====================================================

    def call_next_customer(self):

        next_customer = None

        # Priority Queue First
        if self.priority_queue:
            next_customer = self.priority_queue.pop(0)

        elif self.normal_queue:
            next_customer = self.normal_queue.pop(0)

        else:
            messagebox.showinfo(
                "Queue Empty",
                "There are no customers waiting."
            )
            return

        # Display Current Customer
        messagebox.showinfo(
            "Next Customer",
            f"""
            NOW SERVING

            Ticket: {next_customer['ticket']}
            Name: {next_customer['name']}
            Department: {next_customer['department']}
            """
        )

        # Remove from Treeview
        for item in self.tree.get_children():

            values = self.tree.item(item)["values"]

            if values[0] == next_customer["ticket"]:
                self.tree.delete(item)
                break


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = TicketingSystem(root)

    root.mainloop()