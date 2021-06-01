import sys


argc = len(sys.argv)
if argc != 4:
    print(f"Ошибка! Ожидалось 3 аргумента, получено {argc - 1}")
    sys.exit(1)

CHAT_ID=int(sys.argv[1])
GROUP_ID=int(sys.argv[2])
TOKEN=str(sys.argv[3])

