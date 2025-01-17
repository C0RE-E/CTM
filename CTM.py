import tkinter as tk
from tkinter import ttk
import webbrowser 
from OsURL import openSearchURL

def get_customer_data():
    if use_tab_values.get():
        customer_data = customer_data_entry.get().strip().split('\t')
        return customer_data[:3] if len(customer_data) == 3 else ('', '', '')
    else:
        return (
            customer_id_entry.get().strip(),
            node_pod_entry.get().strip(),
            domain_entry.get().strip()
        )

def get_affected_user_data():
    if use_tab_values.get():
        user_data = affected_user_entry.get().strip().split('\t')
        return user_data[:5] if len(user_data) == 5 else ('', '', '', '', '')
    else:
        return (
            name_entry.get().strip(),
            email_entry.get().strip(),
            serviceId_entry.get().strip(),
            lastBackupDate_entry.get().strip(),
            sizeInGb_entry.get().strip()
        )

def insert_and_format():
    # Get values from the entry widgets and dropdowns
    selected_var = selected_variable.get()
    failure_type = failure_type_variable.get()

    # Format failure message based on the selected failure type
    if failure_type == "Full":
        failure_message = "full failure"
    elif failure_type == "Partial":
        failure_message = "partial failure"
    else:
        failure_message = "unknown failure"

    # Create variable message
    variable_message = f"{selected_var} is failing backups {failure_message}"

    customer_data = customer_data_entry.get().strip().split('\t')

    if len(customer_data) == 3:
        customer_id, node_pod, domain = customer_data
    else:
        customer_id, node_pod, domain = '', '', ''

    # Populate the input fields
    customer_id_entry.delete(0, tk.END)
    customer_id_entry.insert(0, customer_id)

    node_pod_entry.delete(0, tk.END)
    node_pod_entry.insert(0, node_pod)

    domain_entry.delete(0, tk.END)
    domain_entry.insert(0, domain)

    user_data = affected_user_entry.get().strip().split('\t')

    Name = user_data[0] if len(user_data) > 0 and user_data[0] else "null"
    email = user_data[1] if len(user_data) > 1 and user_data[1] else "null"
    serviceId = user_data[2] if len(user_data) > 2 and user_data[2] else "null"
    lastBackupDate = user_data[3] if len(user_data) > 3 and user_data[3] else "null"
    sizeInGb = user_data[4] if len(user_data) > 4 and user_data[4] else "null"


    # Populate the input fields
    affected_user_entry.delete(0, tk.END)
    affected_user_entry.insert(0, Name)

    email_entry.delete(0, tk.END)
    email_entry.insert(0, email)

    serviceId_entry.delete(0, tk.END)
    serviceId_entry.insert(0, serviceId)

    lastBackupDate_entry.delete(0, tk.END)
    lastBackupDate_entry.insert(0, lastBackupDate)

    sizeInGb_entry.delete(0, tk.END)
    sizeInGb_entry.insert(0, sizeInGb)    
    summary_data = summary_entry.get().strip()

    # Combine all messages
    result_message = (f"Issue:\n{variable_message}\n\n"
                      f"Customer ID: {customer_id}\nNode/Pod: {node_pod}\nDomain: {domain}\n\n"
                      f"Summary: \n{summary_data}\n\n"
                      f"troubleshooting: \n\n"
                      f"Name: {Name}\nEmail: {email}\nService ID: {serviceId}\n"
                      f"Last Backup Date: {lastBackupDate}\nSize in GB: {sizeInGb}\n\n"
                      f"Log: \n\n"
                      f"Similar Ticket: \n\n"
                      f"Conclusion: \n"
                      f"Action: \n")

    # Clear the text area
    format_text.delete(1.0, tk.END)

    # Insert the combined result into the format box
    format_text.insert(tk.END, result_message)

def call_openSearchURL():
    customer_id = customer_id_entry.get().strip()
    serviceId = serviceId_entry.get().strip()
    openSearchURL(customer_id, serviceId)


# # def toggle_dark_mode():  **** depreciated ****
#     current_theme = root.option_get('theme', 'light')  # Get the current theme

#     if current_theme == 'light':
#         # Dark mode is currently off, so enable dark mode
#         root.configure(bg='#333333')
#         dark_mode_button.configure(bg='#555555', fg='#ffffff', activebackground='#777777')
#         format_text.configure(bg='#333333', fg='#ffffff')

#         # Configure tab_checkbox using ttk.Style
#         style = ttk.Style()
#         style.configure("Dark.TCheckbutton", background='#333333', foreground='#ffffff', indicatorbackground='#333333')
#         tab_checkbox.configure(style="Dark.TCheckbutton")

#         # Configure other entry widgets
#         for entry in (customer_data_entry, customer_id_entry, node_pod_entry, domain_entry,
#                       summary_entry, affected_user_entry, name_entry, email_entry,
#                       serviceId_entry, lastBackupDate_entry, sizeInGb_entry):
#             entry.configure(bg='#333333', fg='#ffffff', insertbackground='#ffffff')
#     else:
#         # Dark mode is currently on, so disable dark mode
#         root.configure(bg='')
#         dark_mode_button.configure(bg='', fg='', activebackground='')
#         format_text.configure(bg='', fg='')

#         # Configure tab_checkbox using ttk.Style
#         style = ttk.Style()
#         style.configure("Light.TCheckbutton", background='', foreground='', indicatorbackground='')
#         tab_checkbox.configure(style="Light.TCheckbutton")

#         # Configure other entry widgets
#         for entry in (customer_data_entry, customer_id_entry, node_pod_entry, domain_entry,
#                       summary_entry, affected_user_entry, name_entry, email_entry,
#                       serviceId_entry, lastBackupDate_entry, sizeInGb_entry):
#             entry.configure(bg='', fg='', insertbackground='')

# ... (rest of your code remains unchanged)

root = tk.Tk()
root.title("Ticket Machine")

# BooleanVar to determine whether to use tab-separated values
use_tab_values = tk.BooleanVar(value=True)

# Button to Toggle Dark Mode
# dark_mode_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode)
# dark_mode_button.pack()

# Checkbox to choose between tab-separated values and direct entry
tab_checkbox = ttk.Checkbutton(root, text="Use Tab-Separated Values", variable=use_tab_values)
tab_checkbox.pack()

# Define your variable list here
affected_suite = [
    "Office365Teams",
    "Office365Exchange",
    "Office365SharePoint",
    "Office365OneDrive",
    "GoogleMail",
    "GoogleCalendar",
    "GoogleContacts",
    "GoogleDrive",
    "GoogleTeamDrives",
    "GWS",
    "MS 365"
]

selected_variable = tk.StringVar()
failure_type_variable = tk.StringVar()

variable_label = tk.Label(root, text="Select a variable:")
variable_label.pack()

# Use your defined variable as the values for the dropdown
variable_dropdown = ttk.Combobox(root, textvariable=selected_variable, values=affected_suite)
variable_dropdown.pack()

failure_type_label = tk.Label(root, text="Select failure type:")
failure_type_label.pack()

# Dropdown for selecting failure type
failure_type_dropdown = ttk.Combobox(root, textvariable=failure_type_variable, values=["Full", "Partial"])
failure_type_dropdown.pack()

# Entry for Customer Data
customer_data_label = tk.Label(root, text="Copy/Paste SQL Data (Customer ID, Node/Pod, Domain separated by tabs):")
customer_data_label.pack()

customer_data_entry = tk.Entry(root)
customer_data_entry.pack()

# Labels and Entry Widgets for Data Input
customer_id_label = tk.Label(root, text="Customer ID:")
customer_id_label.pack()

customer_id_entry = tk.Entry(root)
customer_id_entry.pack()

node_pod_label = tk.Label(root, text="Node/Pod:")
node_pod_label.pack()

node_pod_entry = tk.Entry(root)
node_pod_entry.pack()

domain_label = tk.Label(root, text="Domain:")
domain_label.pack()

domain_entry = tk.Entry(root)
domain_entry.pack()

# Entry for Summary
summary_label = tk.Label(root, text="Summary:")
summary_label.pack()

summary_entry = tk.Entry(root)
summary_entry.pack()

# Entry for affected_user
affected_user_label = tk.Label(root, text="Copy/Paste SQL Data (name, email, serviceId, lastBackupDate, sizeInGb):")
affected_user_label.pack()

affected_user_entry = tk.Entry(root)
affected_user_entry.pack()

# Labels and Entry Widgets for Additional Data Input
name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

serviceId_label = tk.Label(root, text="Service ID:")
serviceId_label.pack()

serviceId_entry = tk.Entry(root)
serviceId_entry.pack()

lastBackupDate_label = tk.Label(root, text="Last Backup Date:")
lastBackupDate_label.pack()

lastBackupDate_entry = tk.Entry(root)
lastBackupDate_entry.pack()

sizeInGb_label = tk.Label(root, text="Size in GB:")
sizeInGb_label.pack()

sizeInGb_entry = tk.Entry(root)
sizeInGb_entry.pack()

# Button to Insert Variable and Format Data
insert_and_format_button = tk.Button(root, text="Submit", command=insert_and_format)
insert_and_format_button.pack()

openSearchURL_Button = tk.Button(root, text="OpenSearch", command=call_openSearchURL)
openSearchURL_Button.pack()

# Format Text Area
format_text = tk.Text(root, height=12, width=40)
format_text.pack()

root.mainloop()


#v1.0
#By Corey Pazmino 
#modified by Lilith DuBuisson