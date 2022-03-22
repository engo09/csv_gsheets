import os
import sys


def push_csv_to_gsheet(service, spreadsheet_id, sheet_id):
    cwd = os.getcwd()
    csv_file = sys.argv[2]
    with open(f'MAIN_DIRECTORY_FROM_WHERE_THE_CSV_WILL_BE_PULLED/{csv_file}', 'r') as csv_file:
        csv_contents = csv_file.read()
    body = {
        'requests': [{
            'pasteData': {
                "coordinate": {
                    "sheetId": sheet_id,
                    "rowIndex": "0",
                    "columnIndex": "0",
                },
                "data": csv_contents,
                "type": 'PASTE_NORMAL',
                "delimiter": ',',
            }
        }]
    }
    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body)
    response = request.execute()

    sheet_url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit#gid={sheet_id}'

    return sheet_url
