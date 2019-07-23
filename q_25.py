names =["kajju","gojirra","kotohomine","bazzette","kiritzuga","iris",\
    "illyasviel","bazzette","iris","iris","kotohomine"]
c_name = {}
for name in names:
    if c_name.get(name)==None:
        c_name[name] = 1
    else:
        c_name[name]+=1
print(c_name)        