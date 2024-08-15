import sys
print('\\begin{python}',end='')
print('[' + sys.argv[1] + ']',end='')
print('(style=one-dark){colback=gray!40!black,colframe=blue}')
print(open(sys.argv[2]).read())
print('\\end{python}')
