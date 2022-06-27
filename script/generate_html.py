
import os
import sys

block_list = []

def generate_file_index(root):
    items = []
    if not os.path.exists(root):
        return
    if os.path.isdir(root):
        lst = os.listdir(root)
        for f in lst:
            fn = os.path.join(root, f)
            if f.startswith('.') or fn in block_list:
                continue # hidden file or block files
            if os.path.isdir(fn):
                generate_file_index(fn)
                items.append('<li><a href="%s/">%s/</a></li>' % (f, f))
            else:
                items.append('<li><a href="%s">%s</a></li>' % (f, f))
        with open('%s/index.html' % root, 'w') as f:
            f.write('<html>\n<body>\n')
            f.write('<ul>\n')
            for i in items:
                f.write('%s\n' % i)
            f.write('</ul>\n')
            f.write('</body>\n</html>\n')

if __name__ == '__main__':
    generate_file_index(sys.argv[1])
