import io, os, sys

out = sys.stdout.write
inp = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for i in range(int(inp().decode())):
    data = inp().decode()
    length = len(data)
    if length > 12:
        out(data[0] + str(length-4) + data[length-3] + "\n")
    else:
        out(data)
