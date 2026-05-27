<img width="1475" height="853" alt="image" src="https://github.com/user-attachments/assets/2236af1d-0685-4967-9965-08ed06908d4b" />

This Python program is a graphical healthcare queue ticketing system built using the Tkinter library. It is designed to help hospitals or clinics manage customer queues efficiently through an automated ticketing process.

The system follows an object-oriented structure through the TicketingSystem class, where all interface components and queue operations are managed. The application window is configured with a modern skeuomorphic-style dashboard layout consisting of two main sections:

A left panel for patient registration
A right panel for displaying the live waiting queue

Key features of the system include:
Automatic Ticket Generation
Each patient receives a unique ticket number generated sequentially (T-101, T-102, etc.). The system also records the registration timestamp using Python’s datetime module.
Department Selection
Patients can choose hospital departments such as Consultation, Surgery, Pharmacy, Radiology, and Laboratory through a dropdown combobox widget.

Priority Queue Management
The code implements two separate queues:
priority_queue
Priority customers are always served first before regular customers, demonstrating queue prioritization logic similar to real healthcare triage systems.

Live Queue Display

A Treeview table from Tkinter’s ttk module dynamically displays all waiting patients, including ticket number, name, department, priority status, and time of registration.
Next Customer Processing
The call_next_customer() method removes and serves the next patient from the queue. It first checks the priority queue before moving to the normal queue, ensuring fair and organized queue handling.
