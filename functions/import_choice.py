

def get_args_spreadsheet():
    spreadsheet_name = input("Spreadsheet name: ")
    sheet_name = input("Sheet name: ")

    args_spreadsheet = {
        "spreadsheet_name": spreadsheet_name,
        "sheet_name": sheet_name
    }

    return args_spreadsheet


def get_args_sheet():
    spreadsheet_id_input = input("Spreadsheet ID: ")
    sheet_name = input("Sheet name: ")

    args_sheet = {
        "spreadsheet_id_input": spreadsheet_id_input,
        "sheet_name": sheet_name
    }

    return args_sheet
