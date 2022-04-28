import sys
import webbrowser
from auth import g_auth
from functions import import_choice, spreadsheet_handling, sheet_handling, csv_upload

scopes = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/spreadsheets']
service_type = 'sheets'
version = 'v4'
service = g_auth.g_auth(scopes, service_type, version)


def initial_option():
    import_type = sys.argv[1]
    print(import_type)
    if import_type == "new":
        print('')
        sheet_id = '0'
        inp_values = import_choice.get_args_spreadsheet()
        spreadsheet_id = spreadsheet_handling.new_spreadsheet(service, inp_values)
        sheet_url = csv_upload.push_csv_to_gsheet(service, spreadsheet_id, sheet_id)
        print(sheet_url)
        webbrowser.open(f'{sheet_url}', new=2)
    elif import_type == "sheet":
        print('')
        inp_values = import_choice.get_args_sheet()
        spreadsheet_id = inp_values['spreadsheet_id_input']
        sheet_id = sheet_handling.new_sheet(service, inp_values)
        sheet_url = csv_upload.push_csv_to_gsheet(service, spreadsheet_id, sheet_id)
        print(sheet_url)
        webbrowser.open(f'{sheet_url}', new=2)


if __name__ == '__main__':
    initial_option()
