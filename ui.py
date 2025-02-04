import tkinter as tk
from render_pdf import generate_pdf

work_exp_counter = 0
work_exp_entries = []

def _generate_pdf():
    data_dict = {
        'name': 'Tom',
        'email': 'zxcvbnm@asdf.com',
        'phone': '123456789',
        'jobs': []
    }
    data_dict['name'] = name_input.get()
    data_dict['email'] = email_input.get()
    data_dict['phone'] = phone_input.get()
    for _, entry_set in enumerate(work_exp_entries, start=1):
        company_val = entry_set['company'].get()
        title_val = entry_set['title'].get()
        date_val = entry_set['date_range'].get()
        location_val = entry_set['location'].get()
        desc1_val = entry_set['desc1'].get()
        desc2_val = entry_set['desc2'].get()
        desc3_val = entry_set['desc3'].get()
        data_dict['jobs'].append({
            'company': company_val,
            'title': title_val,
            'date_range': date_val,
            'location': location_val,
            'desc_items': [desc1_val, desc2_val, desc3_val]
        })
    filename = f"{data_dict['name']}_cv.pdf" if data_dict['name'] else "new_cv.pdf"
    generate_pdf(data_dict, template_file='template1.jinja', output_pdf_name=filename, replace=True)

def add_work_experience():
    global work_exp_counter
    # Create a new frame (container) for the work experience entry.
    entry_frame = tk.Frame(work_exp, bd=1, relief="groove", padx=10, pady=10)
    # Place the frame in a new row within the work_exp frame.
    entry_frame.grid(row=work_exp_counter+1, column=0, sticky="nsew", pady=5, padx=5)
    
    # Create labels and entry widgets for each field.
    # Company:
    company_label = tk.Label(entry_frame, text="Company:")
    company_label.grid(row=0, column=0, sticky="w")
    company_entry = tk.Entry(entry_frame)
    company_entry.grid(row=0, column=1, padx=(5, 0))
    
    # Title:
    title_label = tk.Label(entry_frame, text="Title:")
    title_label.grid(row=1, column=0, sticky="w")
    title_entry = tk.Entry(entry_frame)
    title_entry.grid(row=1, column=1, padx=(5, 0))
    
    # Date Range:
    date_label = tk.Label(entry_frame, text="Date Range:")
    date_label.grid(row=2, column=0, sticky="w")
    date_entry = tk.Entry(entry_frame)
    date_entry.grid(row=2, column=1, padx=(5, 0))
    
    # Location:
    location_label = tk.Label(entry_frame, text="Location:")
    location_label.grid(row=3, column=0, sticky="w")
    location_entry = tk.Entry(entry_frame)
    location_entry.grid(row=3, column=1, padx=(5, 0))
    
    # Description 1:
    desc1_label = tk.Label(entry_frame, text="Description 1:")
    desc1_label.grid(row=4, column=0, sticky="w")
    desc1_entry = tk.Entry(entry_frame)
    desc1_entry.grid(row=4, column=1, padx=(5, 0))
    
    # Description 2:
    desc2_label = tk.Label(entry_frame, text="Description 2:")
    desc2_label.grid(row=5, column=0, sticky="w")
    desc2_entry = tk.Entry(entry_frame)
    desc2_entry.grid(row=5, column=1, padx=(5, 0))
    
    # Description 3:
    desc3_label = tk.Label(entry_frame, text="Description 3:")
    desc3_label.grid(row=6, column=0, sticky="w")
    desc3_entry = tk.Entry(entry_frame)
    desc3_entry.grid(row=6, column=1, padx=(5, 0))
    
    # Make the second column expandable.
    entry_frame.columnconfigure(1, weight=1)
    
    # Store references to all the Entry widgets in a dictionary.
    work_exp_entries.append({
        'company': company_entry,
        'title': title_entry,
        'date_range': date_entry,
        'location': location_entry,
        'desc1': desc1_entry,
        'desc2': desc2_entry,
        'desc3': desc3_entry
    })
    
    # Increment the counter for the next entry.
    work_exp_counter += 1


if __name__ == '__main__':
    root = tk.Tk()
    root.title("CV Generator")
    
    person_info = tk.Frame(root, bd=2, relief="groove", padx=20, pady=20)
    person_info.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    
    person_info.columnconfigure(1, weight=0)
    
    name_label = tk.Label(person_info, text = "Name:")
    name_label.grid(row=0, column=0, sticky="w")
    name_input = tk.Entry(person_info)
    name_input.grid(row=0, column=1)
    
    email_label = tk.Label(person_info, text = "Email:")
    email_label.grid(row=1, column=0, sticky="w")
    email_input = tk.Entry(person_info)
    email_input.grid(row=1, column=1)
    
    phone_label = tk.Label(person_info, text = "Phone:")
    phone_label.grid(row=2, column=0, sticky="w")
    phone_input = tk.Entry(person_info)
    phone_input.grid(row=2, column=1)
    
    work_exp = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
    work_exp.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    work_exp.columnconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    
    add_work_exp_button = tk.Button(work_exp, text="Add Work Experience", command=add_work_experience, relief="groove", borderwidth=2)
    add_work_exp_button.grid(row=0, column=0, sticky="w")
    
    btn = tk.Button(root, text = "Submit", command=_generate_pdf)
    btn.grid(row=10, column=0, sticky='e', padx=10, pady=10)
    
    root.mainloop()
    