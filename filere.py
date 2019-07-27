try:
    word_count = 0
    line_count = 0
    with open("filere.txt") as f:
        lines = f.readlines()
        line_count = len(lines)
        for line in lines:
           word_count += len(line.split())
           print(line,end= "")
           print(f"no of words {word_count}")
           print(f"no of lines {line_count}")
except Exception as e:
    print(f"file not found please check path {e}")
    