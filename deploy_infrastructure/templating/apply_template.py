from string import Template

substitution_dict = {}

filein = open('modules/emperor/manifests/init.pp')
src = Template(filein.read())
result = src.safe_substitute(substitution_dict)

fileout = open('modules/emperor/manifests/init.pp', 'w')
fileout.write(result)
fileout.close()
