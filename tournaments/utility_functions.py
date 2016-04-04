import xlrd

def get_rosters_from_excel(django_file):
    workbook = xlrd.open_workbook(file_contents=django_file.read())
    worksheet = workbook.sheet_by_name('Match_Rosters')

    num_rows = worksheet.nrows - 1
    cur_row = -1

    rosters = []

    while cur_row < num_rows:
        cur_row += 1

        if worksheet.cell_value(cur_row, 0) == "NCTTA Team Match Player Selection Form":
            row = worksheet.row(cur_row + 4)
            roster = {
                "round_match" : worksheet.cell_value(cur_row + 2, 6), # consider adding the time in +2, 8
                "left_team_label" : worksheet.cell_value(cur_row + 4, 3),
                "right_team_label" : worksheet.cell_value(cur_row + 4, 8),
                "left_team_title" : worksheet.cell_value(cur_row + 5, 1),
                "right_team_title" : worksheet.cell_value(cur_row + 5, 6),
                "players" : [],
                "opponents" : [],
                # Don't forget about doubles!
            }
            roster["players"].append({
                "player_label" : worksheet.cell_value(cur_row + 11, 0),
                "player_name" : worksheet.cell_value(cur_row + 11, 1)
            })
            roster["players"].append({
                "player_label" : worksheet.cell_value(cur_row + 12, 0),
                "player_name" : worksheet.cell_value(cur_row + 12, 1),
            })
            roster["players"].append({
                "player_label" : worksheet.cell_value(cur_row + 13, 0),
                "player_name" : worksheet.cell_value(cur_row + 13, 1),
            })
            roster["players"].append({
                "player_label" : worksheet.cell_value(cur_row + 14, 0),
                "player_name" : worksheet.cell_value(cur_row + 14, 1),
            })
            roster["players"].append({
                "player_label" : worksheet.cell_value(cur_row + 15, 0),
                "player_name" : worksheet.cell_value(cur_row + 15, 1),
            })
            roster["players"].append({
                "player_label" : worksheet.cell_value(cur_row + 16, 0),
                "player_name" : worksheet.cell_value(cur_row + 16, 1),
            })
            roster["players"].append({
                "player_label" : worksheet.cell_value(cur_row + 17, 0),
                "player_name" : worksheet.cell_value(cur_row + 17, 1),
            })
            roster["players"].append({
                "player_label" : worksheet.cell_value(cur_row + 18, 0),
                "player_name" : worksheet.cell_value(cur_row + 18, 1),
            })
            # The opponents
            roster["opponents"].append({
                "player_name" : worksheet.cell_value(cur_row + 11, 6),
                "player_rating" : worksheet.cell_value(cur_row + 11, 9),
            })
            roster["opponents"].append({
                "player_name" : worksheet.cell_value(cur_row + 12, 6),
                "player_rating" : worksheet.cell_value(cur_row + 12, 9),
            })
            roster["opponents"].append({
                "player_name" : worksheet.cell_value(cur_row + 13, 6),
                "player_rating" : worksheet.cell_value(cur_row + 13, 9),
            })
            roster["opponents"].append({
                "player_name" : worksheet.cell_value(cur_row + 14, 6),
                "player_rating" : worksheet.cell_value(cur_row + 14, 9),
            })
            roster["opponents"].append({
                "player_name" : worksheet.cell_value(cur_row + 15, 6),
                "player_rating" : worksheet.cell_value(cur_row + 15, 9),
            })
            roster["opponents"].append({
                "player_name" : worksheet.cell_value(cur_row + 16, 6),
                "player_rating" : worksheet.cell_value(cur_row + 16, 9),
            })
            roster["opponents"].append({
                "player_name" : worksheet.cell_value(cur_row + 17, 6),
                "player_rating" : worksheet.cell_value(cur_row + 17, 9),
            })
            roster["opponents"].append({
                "player_name" : worksheet.cell_value(cur_row + 18, 6),
                "player_rating" : worksheet.cell_value(cur_row + 18, 9),
            })

            label_letter = ''.join(i for i in roster["players"][0]["player_label"] if not i.isdigit())
            if label_letter == str(roster["left_team_label"].strip()):
                roster["active_team"] = "left"
            else:
                roster["active_team"] = "right"


            #for key, value in roster.items():
            #    print " ", key, ":", value
            if roster["opponents"][0]["player_name"] != "" and roster["players"][0]["player_name"] and roster["round_match"] != "":
                rosters.append(roster)
    return rosters
