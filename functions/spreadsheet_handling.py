

def new_spreadsheet(service, inp_values):
    spreadsheet_body = {
        "properties": {
            "title": inp_values['spreadsheet_name'],
            "locale": 'de_DE',
            "timeZone": 'Europe/Berlin',
        },
    }

    request = service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()

    spreadsheet_id = response['spreadsheetId']

    update_sheet = {
        "requests": [{
            "updateSheetProperties": {
                "properties": {
                    "title": inp_values['sheet_name'],
                    "sheetId": '0',
                },
                "fields": "title"
            }
        }]
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=update_sheet)
    response = request.execute()

    return spreadsheet_id
