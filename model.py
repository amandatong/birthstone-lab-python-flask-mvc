#process input
def get_display(form):
    birth_month = form['month'].lower()
    birthstone = ""

    if birth_month == "january":
        birthstone="garnet"
    elif birth_month == "february":
        birthstone="amethyst"
    elif birth_month == "march":
        birthstone="aquamarine"
    elif birth_month == "april":
        birthstone="diamond"
    elif birth_month == "may":
        birthstone="emerald"
    elif birth_month == "june":
        birthstone="pearl"
    elif birth_month == "july":
        birthstone="ruby"
    elif birth_month == "august":
        birthstone="peridot"
    elif birth_month == "september":
        birthstone="sapphire"
    elif birth_month == "october":
        birthstone="opal"
    elif birth_month == "november":
        birthstone="citrine"
    elif birth_month == "december":
        birthstone="topaz"
    else:
        birthstone="none"
        
    return birthstone