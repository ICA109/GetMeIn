from flaskr.internal.config import huey  # import our "huey" object
from flaskr.internal.tasks import count_beans  # import our task


if __name__ == '__main__':
    beans = raw_input('How many beans? ')
    count_beans(int(beans))
    print('Enqueued job to count %s beans' % beans)