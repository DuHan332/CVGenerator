import os
import subprocess
from jinja2 import Environment, FileSystemLoader

def generate_pdf(data, template_file='template1.jinja', output_pdf_name='output.pdf'):
    """
    Renders a LaTeX Jinja template from the 'templates' folder and compiles it to PDF.
    """

    # 1. Create a Jinja2 environment, pointing to the 'templates' directory
    #    and set custom delimiters to avoid LaTeX curly-brace conflicts.
    env = Environment(
        loader=FileSystemLoader('templates'),
        block_start_string='((%',
        block_end_string='%))',
        variable_start_string='(((',
        variable_end_string=')))',
        comment_start_string='((#',
        comment_end_string='#))'
    )

    # 2. Load the specified template
    template = env.get_template(template_file)

    # 3. Render the template with the provided data
    rendered_tex = template.render(**data)

    # 4. Write the rendered content to a temporary .tex file
    temp_tex = 'templates/temp_output.tex'
    with open(temp_tex, 'w', encoding='utf-8') as f:
        f.write(rendered_tex)

    # 5. Run pdflatex to compile .tex -> .pdf
    subprocess.run(['pdflatex', '-interaction=batchmode', 'temp_output.tex'], cwd="templates")

    # 6. Rename the generated PDF to your desired output name
    if os.path.exists('templates/temp_output.pdf'):
        output_pdf_name = create_new_file_name(output_pdf_name)
        os.rename('templates/temp_output.pdf', output_pdf_name)

    # 7. Clean up auxiliary files if desired
    for ext in ['.aux', '.log', '.out', '.tex']:
        aux_file = 'templates/temp_output' + ext
        if os.path.exists(aux_file):
            os.remove(aux_file)

    return output_pdf_name


def create_new_file_name(new_pdf):
    """
    If `new_pdf` already exists, append (1), (2), etc. until we find a free filename.
    Then rename `original_pdf` to that new filename.
    """
    base, ext = os.path.splitext(new_pdf)
    candidate = new_pdf
    counter = 1

    while os.path.exists(candidate):
        candidate = f"{base}({counter}){ext}"
        counter += 1
    return candidate

if __name__ == '__main__':
    # Example data dictionary
    data_dict = {
        'name': 'Alice',
        'years': 27
    }

    pdf_file = generate_pdf(data_dict, template_file='template1.jinja', output_pdf_name='example_output.pdf')
    print("PDF generated:", pdf_file)