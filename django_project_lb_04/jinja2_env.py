from jinja2 import Environment

def environment(**options):
    # env_01=Environment(**options)
    env = Environment(**options)
    # 2.将自定义的过滤器添加到 环境中
    env.filters['do_listreverse'] = do_listreverse
    env.filters['add']=add
    return env


def do_listreverse(li):
    return li**2

def add(num):
    return num+1