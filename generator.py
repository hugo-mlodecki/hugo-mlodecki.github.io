import os
# import markdown
import time

# path_md   = os.path.join(os.getcwd(), "content_md")
path_html = os.path.join(os.getcwd(), "content_html")
path_res  = os.path.join(os.getcwd(), "")

# """ From content_md to content_html """
# for filename in os.listdir(path_md):
#     inpath  = os.path.join(path_md, filename)
#     input   = open(inpath, 'r')
#     lines   = "".join(input.readlines())
#     input.close()
#     outpath = os.path.join(path_html, filename[:-3] + ".html")
#     res     = open(outpath, 'w')
#     res.write("""<div class="container">\n<div class="row">\n<div class="col-md-8" style="height: 100vh;">""")
#     lines = markdown.markdown(lines, extensions=['extra', 'sane_lists', 'tables'])
#     res.writelines(lines)
#     res.write("""</div>\n</div>\n</div>""")
#     res.close()

""" From content_html to site """

header       = open(os.path.join(os.getcwd(), "head.html"), 'r')
header_lines = header.readlines()
header.close()
navigation       = open(os.path.join(os.getcwd(), "header.html"), 'r')
navigation_lines = navigation.readlines()
navigation.close()
footer       = open(os.path.join(os.getcwd(), "footer.html"), 'r')
footer_lines = footer.readlines()
footer.close()

for filename in os.listdir(path_html):
    res = open(os.path.join(path_res, filename), 'w')
    with open(os.path.join(path_html, filename), 'r') as f:
        res.write("<!--Generated automatically by Hugo, " + time.asctime() + "-->\n")
        res.writelines(header_lines)
        res.write("  <body>")
        res.writelines(navigation_lines)
        lines = f.readlines()
        res.writelines(lines)
        res.writelines(footer_lines)
        res.write("  </body>\n</html>")
    res.close()
