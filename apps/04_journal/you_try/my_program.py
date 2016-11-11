import my_journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------')
    print('      JOURNAL APP ')
    print('-------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_name = 'default'
    journal_data = my_journal.load(journal_name)

    while cmd !='x':
        cmd = input('{L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Done, goodbye.')
    my_journal.save(journal_name)


def list_entries(data):
    print('Your journal entries:')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print(idx, entry)


def add_entry(data):
    text = input('Add your entry, <enter> to exit: ')
    my_journal.add_entry(text)


main()