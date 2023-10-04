import nbformat
import nbconvert
import sys

if len(sys.argv) < 2:
    print("Usage:", sys.argv[0], 'filename.ipynb', '[--slides]')
    exit(-1)

with open(sys.argv[1], encoding='utf-8') as nb_file:
    nb_contents = nb_file.read()

# Convert using the ordinary exporter
notebook = nbformat.reads(nb_contents, as_version=4)
if len(sys.argv) >= 4 and sys.argv[2] == '--to' and sys.argv[3] == 'slides':
    outname = sys.argv[1].split('.ipynb')[0] + '.slides.html'
    print("Converting to slides:", outname)    
    if '--SlidesExporter.reveal_scroll=True' in sys.argv:
        nbconvert.SlidesExporter().reveal_scroll = True
    exporter = nbconvert.SlidesExporter()
elif len(sys.argv) >= 4 and sys.argv[2] == '--to' and sys.argv[3] == 'latex':
    outname = sys.argv[1].split('.ipynb')[0] + '.tex'
    print("Converting to latex:", outname)
    exporter = nbconvert.LatexExporter()
else:
    outname = sys.argv[1].split('.ipynb')[0] + '.html'
    print("Converting to HTML:", outname)
    exporter = nbconvert.HTMLExporter()
    
body, res = exporter.from_notebook_node(notebook)

# Create a list saving all image attachments to their base64 representations
images = []
for cell in notebook['cells']:
    if 'attachments' in cell:
        attachments = cell['attachments']
        for filename, attachment in attachments.items():
            for mime, base64 in attachment.items():
                images.append( [f'attachment:{filename}', f'data:{mime};base64,{base64}'] )

# Fix up the HTML and write it to disk
for itmes in images:
    src = itmes[0]
    base64 = itmes[1]
    print(src, len(base64))
    body = body.replace(f'src="{src}"', f'src="{base64}"', 1)

if '/' in outname:
    outcleanname = outname.rsplit('/', 1)[-1]
elif '\\' in outname:
    outcleanname = outname.rsplit('\\', 1)[-1]
else:
    outcleanname = outname

with open(outcleanname, 'w', encoding='utf-8') as output_file:
    output_file.write(body)

if len(sys.argv) >= 6 and sys.argv[2] == '--to' and sys.argv[3] == 'slides' and sys.argv[4] == '--post' and sys.argv[5] == 'serve':
    nbconvert.postprocessors.serve.ServePostProcessor().postprocess(outcleanname)
