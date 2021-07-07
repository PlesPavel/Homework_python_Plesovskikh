from requests import get

req = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')


def pars_str(i):
    f = i.find(' ')
    f1 = i.find('"')
    f2 = i.find(' /')
    f3 = i.find('HTTP')
    a = f + 1
    b = f1 + 1
    return (i[:a], i[b:f2], i[f2:f3])


task_list = []

for line in req.iter_lines(decode_unicode=True):
    i = pars_str(line)
    task_list.append(i)

print(task_list)
