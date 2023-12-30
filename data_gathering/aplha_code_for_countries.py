countries = {}

# To extract the countries from the html file, I used the following code:
with open("countries_from_iban.txt", "r") as f:
    current = ""
    for line in f.readlines():
        if "</tr>" in line:
            current = (
                current.replace("<tr>", "")
                .replace("<td>", ",")
                .replace("</td>", ",")
                .replace(",,", ",")
            )
            current = current[1:-1]
            current = current.split(",")
            countries[current[0]] = current[2]
            current = ""
        else:
            current += line.strip()

print(countries)
