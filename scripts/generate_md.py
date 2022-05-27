import glob

file_list = glob.glob('/storage5/shawn/coronavirus/github/design_view.io/mol/*/*')
with open('/storage5/shawn/coronavirus/github/design_view.io/scripts/template_md_file','r+') as f:
    txt_original = f.read()
for i in range(len(file_list)):
    toks = file_list[i].split('/')
    design_name = toks[-2]
    pdb_name = toks[-1]
    txt = txt_original.replace('TMP_identifier', design_name)
    txt = txt.replace('TMP_pdb', design_name+'/'+pdb_name)
    txt = txt.replace('TMP_order', str(i+1))
    with open('/storage5/shawn/coronavirus/github/design_view.io/docs/S2/'+design_name+'.md','w+') as f:
        f.write(txt)


