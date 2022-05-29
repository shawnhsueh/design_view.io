import glob

file_list = glob.glob('/storage5/shawn/coronavirus/github/design_view.io/mol/designed_structure/S2/*pdb')
with open('/storage5/shawn/coronavirus/github/design_view.io/scripts/template_md_file_POI','r+') as f:
    txt_original = f.read()
for i in range(len(file_list)):
    toks = file_list[i].split('/')
    pdb_name = toks[-1][:-4]
    txt = txt_original.replace('TMP_pdb_html', pdb_name.replace('+','%2b'))
    txt = txt.replace('TMP_pdb', pdb_name)
    txt = txt.replace('TMP_order', str(i+1))
    with open('/storage5/shawn/coronavirus/github/design_view.io/docs/POI/S2/'+pdb_name+'.md','w+') as f:
        f.write(txt)


