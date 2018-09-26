from flaskr.internal.config import huey # import the huey we instantiated in config.py


@huey.task()
def count_beans(num):
    print('-- counted %s beans --' % num)