

def new_sheet(service, inp_values):
    spreadsheet_id = inp_values['spreadsheet_id_input']
    update_sheet = {
        "requests": [{
            "addSheet": {
                "properties": {
                    "title": inp_values['sheet_name'],
                },
            }
        }]
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=update_sheet)
    response = request.execute()

    replies = response['replies'][0]
    add_sheet = replies['addSheet']
    properties = add_sheet['properties']
    sheet_id = properties['sheetId']

    return sheet_id
