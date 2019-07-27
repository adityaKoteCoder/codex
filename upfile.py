try:
    with open("filere.txt") as fin ,open("u_filere.txt","w")as fo
            lines = fin.readlines()
            lines = [1.upper() for l in lines]
            fout.writelines(lines)

except Expectation as e:
print(f"file not found please check path {e}")