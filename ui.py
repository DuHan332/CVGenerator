import tkinter as tk
from render_pdf import generate_pdf

def _generate_pdf():
    name = name_input.get()
    email = email_input.get()
    phone = phone_input.get()
    if name: data_dict['name'] = name
    if email: data_dict['email'] = email
    if phone: data_dict['phone'] = phone
    filename = f"{name}_cv.pdf" if name else "new_cv.pdf"
    generate_pdf(data_dict, template_file='template1.jinja', output_pdf_name=filename, replace=False)


if __name__ == '__main__':
        # Example data dictionary
    data_dict = {
        'name': 'Tom',
        'email': 'zxcvbnm@asdf.com',
        'phone': '123456789',
        'job_company1': 'Github',
        'job_title1': 'software engineer',
        'job_date_range1': 'Aug 2001 - Sep 2005',
        'job_location1': 'Moon',
        'job_desc_item1': 'job desc item1',
        'job_desc_item2': 'job desc item2',
        'job_desc_item3': 'job desc item3',
    }
    
    root = tk.Tk()
    root.title("CV Generator")
    
    input_frame = tk.Frame(root)
    input_frame.grid(row=0, column=0)
    
    name_label = tk.Label(input_frame, text = "Name:")
    name_label.grid(row=0, column=0)
    name_input = tk.Entry(input_frame)
    name_input.grid(row=0, column=1)
    
    email_label = tk.Label(input_frame, text = "Email:")
    email_label.grid(row=1, column=0)
    email_input = tk.Entry(input_frame)
    email_input.grid(row=1, column=1)
    
    phone_label = tk.Label(input_frame, text = "Phone:")
    phone_label.grid(row=2, column=0)
    phone_input = tk.Entry(input_frame)
    phone_input.grid(row=2, column=1)
    
    btn = tk.Button(input_frame, text = "Submit", command=_generate_pdf)
    btn.grid(row=3, column=2)
    
    
    root.mainloop()
    