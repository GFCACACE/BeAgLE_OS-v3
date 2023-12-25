import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Organization Selector")
root.configure(bg='dark green')

# Create labels and buttons for each organization
org1_label = tk.Label(root, text="ORG_1\n200B assigned", bg="white", fg="black")
org1_label.pack(pady=10)

org2_label = tk.Label(root, text="ORG_2\n40B assigned", bg="white", fg="black")
org2_label.pack(pady=10)

new_org_button = tk.Button(root, text="NEW ORGANIZATION", bg="white", fg="black")
new_org_button.pack(pady=10)

# Create a label for space management
space_label = tk.Label(root, text="24GB / 30GB\nSPACE MANAGEMENT", bg="white", fg="black")
space_label.pack(pady=10)

# Run the main loop
root.mainloop()
