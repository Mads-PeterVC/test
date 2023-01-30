from nbformat import read, write # Can be pip installed. 

def strip_output(nb):
    for cell in nb.cells:
        if hasattr(cell, "outputs"):
            cell.outputs = []
        if hasattr(cell, "prompt_number"):
            del cell["prompt_number"]

if __name__ == '__main__':
    import glob
    files = glob.glob('*.ipynb')

    for file in files:

        if 'working' not in file:
            print(f'Skipping {file}')
            continue

        cleaned_file = file
        cleaned_file = cleaned_file.replace('_working', '')

        with open(file) as f:
           nb = read(f, 4)

        strip_output(nb)

        with open(cleaned_file, 'w') as f:
            write(nb, f, 4)