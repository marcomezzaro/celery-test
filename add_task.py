import tasks


if __name__ == '__main__':
    try:
        tasks.add.delay(1, 2)
    except Exception as e:
        print(str(e))
