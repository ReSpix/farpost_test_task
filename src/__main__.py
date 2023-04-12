import database_creator
import database_filler
import csv_export


def main():
    database_creator.main()
    database_filler.main()
    csv_export.main()


if __name__ == '__main__':
    main()