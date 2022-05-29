import glob

file_list = glob.glob('/storage5/shawn/coronavirus/github/design_view.io/mol/designed_structure/S2/*pdb')
with open('iframe_tmp','r+') as f:
    txt_original = f.read()

txt = ''
for i in range(len(file_list)):
    toks = file_list[i].split('/')
    pdb_name = toks[-1][:-4]
    txt += txt_original.replace('TMP_pdb', pdb_name)

#save txt
with open('iframe_out','w+') as f:
        f.write(txt)


