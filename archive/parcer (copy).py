import webbrowser

def tts_table():
    f = open("ttspage6.html", "r")
    read_result = f.read().split('>')
    f.close()

    parcer_args_list = ['''itemQualityClass: QualityID,
                                    text: Name"''', 'data-bind="text: PlayerID', "StringResource['TraderLocation' + DBData.GuildKioskLocation[GuildKioskLocationID]]", 'text: GuildName', 'localizedNumber: UnitPrice', 'localizedNumber: Amount', 'localizedNumber: TotalPrice', 'minutesElapsed: DiscoverUnixTime']

    f1 = open("tts_table.html", "w")
    f1.write('''
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    table {
      font-family: arial, sans-serif;
      border-collapse: collapse;
      width: 100%;
    }

    td, th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }

    tr:nth-child(even) {
      background-color: #dddddd;
    }
    </style>
    </head>
    <body>

    <h2>"TTS Table" Table</h2>

    <table id="url_table">
    <tr>
    ''')

    k = 0
    h = 0
    for i in read_result:
        for j in parcer_args_list:
            if j in i:
                print(len(read_result[k+1]))
                '''if len(read_result[k+1]) < 6:
                    print(read_result[k+1])
                    f1.write('<th>' + ' ' + '</th>')'''
                if read_result[k+1][-4] == '<':
                    print(read_result[k+1][:-4], end = ' ')
                    f1.write('<th>' + read_result[k+1][:-4] + '</th>')
                '''elif read_result[k+1][-6] == '<':
                    print('<th>' + read_result[k+1][:-6] + '</th>', end = ' ')
                    f1.write('<th>' + read_result[k+1][:-6] + '</th>')'''
                else:
                    print(read_result[k+1][:-5], end = ' ')
                    f1.write('<th>' + read_result[k+1][:-5] + '</th>')
                h += 1
                if h%8==0:
                    print()
                    f1.write('</tr>' + '\n' + '<tr>')
            k += 1


    f1.write('''
    </table>

    </body>
    </html>
    ''')
    f1.close()

    webbrowser.open_new_tab('/home/linp/Beetroot/diplom/tts_table.html')

tts_table()
if __name__ == "main":
    tts_table()
