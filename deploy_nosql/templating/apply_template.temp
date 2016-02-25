from string import Template

substitution_dict = $templ_substitution_dict

filein = open('modules/$templ_module_name/manifests/init.pp')
src = Template(filein.read())
result = src.safe_substitute(substitution_dict)

fileout = open('modules/$templ_module_name/manifests/init.pp', 'w')
fileout.write(result)
fileout.close()
