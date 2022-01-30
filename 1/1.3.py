# Keeping the Last N Items
# 1.3.1
from collections import deque
from encodings import search_function
import linecache

from black import Line, LineGenerator, Pattern

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for lines in lines:
        if Pattern in LineGenerator:
            yield Line, previous_lines
        previous_lines.append(linecache)

# Examples use on a file
if __name__ == '__main__':
    with open('./1.1.py') as f:
        for line, prevlines in search_function(f, 'python', 5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('_'*20)

# Discussion
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q
q.append(4)
q.append(5)
q

# --
q = deque()
q.append(1)
q.append(2)
q.append(3)
q
q.appendleft(4)
q
q.pop()
3
q
q.popleft()