row_length = 6
indent = "  "

students = [
    "김선형",
    "김승규",
    "김정락",
    "김준현",
    "박소민",
    "박영서",
    "박지환",
    "배미혜",
    "변정원",
    "유다은",
    "유승아",
    "윤경민",
    "이남곤",
    "이동현",
    "이예은",
    "이채림",
    "전주영",
    "조인혁",
    "지상일",
    "최용태",
    "하정호",
]

id_map = {
    "김선형": "tjsguddl96",
    "김승규": "pickac4rd",
    "김정락": "jlal1226",
    "김준현": "jhhhhhj",
    "박소민": "yygs321",
    "박영서": "Frog-Slayer",
    "박지환": "mycook3",
    "배미혜": "mihye126",
    "변정원": "Byungul",
    "유다은": "yudaeun",
    "유승아": "SeungAh-Yoo99",
    "윤경민": "ykm1256",
    "이남곤": "ng-lee",
    "이동현": "eastsage",
    "이예은": "synodical",
    "이채림": "chech2",
    "전주영": "juuyoungjeon",
    "조인혁": "InHyeok-J",
    "지상일": "sangilji",
    "최용태": "smc2315",
    "하정호": "hso8706",
    "": "",
}


while len(students) % row_length != 0:
    students.append("")


output = "<table>\n"

for base in range(0, len(students), row_length):
    output += indent + "<tr>\n"

    for i in range(row_length):
        idx = base + i
        github = "https://github.com/" + id_map[students[idx]]
        output += indent * 2 + '<td align="center">\n'
        if students[idx] != "":
            output += indent * 3 + '<a href="' + github + '">\n'
            output += (
                indent * 4
                + '<img src="'
                + github
                + '.png" '
                + 'alt="'
                + students[idx]
                + '" />\n'
            )
            output += indent * 3 + "</a>\n"
        output += indent * 2 + "</td>\n"

    output += indent + "</tr>\n"
    output += indent + "<tr>\n"

    for i in range(row_length):
        idx = base + i
        github = "https://github.com/" + id_map[students[idx]]
        output += indent * 2 + '<td align="center">\n'
        if students[idx] != "":
            output += indent * 3 + '<a href="' + github + '">\n'
            output += indent * 4 + "<b>" + students[idx] + "</b>\n"
            output += indent * 3 + "</a>\n"
        output += indent * 2 + "</td>\n"

    output += indent + "</tr>\n"

    output += "</table>\n"


print(output)
