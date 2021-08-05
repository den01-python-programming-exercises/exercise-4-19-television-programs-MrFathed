from television_program import TelevisionProgram

def main():
    #write your code below this line
    shows = []

    while True:
        name = input("Name:")

        if not name:
            break

        duration = int(input("Duration:"))

        shows.append(TelevisionProgram(name, duration))

    max_duration = int(input("Program's maximum duration?"))

    for show in shows:
        if show.get_duration() <= max_duration:
            print(show)

if __name__ == '__main__':
    main()
