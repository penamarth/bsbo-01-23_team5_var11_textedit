from menu import main_loop

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nПрервано пользователем. До свидания!')