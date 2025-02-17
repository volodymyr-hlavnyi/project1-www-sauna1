from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import calendar

app = Flask(__name__)


def calc_past_years(days_old):
    return days_old // 365


def verify_age(years_old):
    if years_old > 120:
        return ".. you're already dead"
    elif years_old > 60:
        return " are an old Man"
    elif years_old == 21:
        return "can drink alco in USA"
    elif years_old > 18:
        return "are an adult"
    elif years_old > 13:
        return "are a teenager"
    else:
        return "are a child"


def verify_born_input(born_date):
    try:
        parts = born_date.split()
        if len(parts) == 1:
            year = int(parts[0])
            month, day = 1, 1
        elif len(parts) == 2:
            year = int(parts[0])
            month = int(parts[1])
            day = 1
        elif len(parts) == 3:
            year, month, day = map(int, parts)
        else:
            return None, "Invalid date format. Use YYYY MM DD"
        days_in_month = calendar.monthrange(year, month)[1]
        if day > days_in_month:
            return None, "Incorrect day value"
        specific_date = datetime(year, month, day)
        if specific_date > datetime.now():
            return None, "Date is in the future"
        return specific_date, None
    except ValueError:
        return None, "Invalid date input. Use YYYY MM DD"
    except OverflowError:
        return None, "Overflow input value"


def is_specific_day(specific_date):
    today = datetime.now()
    if specific_date.month == today.month and specific_date.day == today.day:
        return "Happy Birthday! You "
    else:
        return "You "


@app.route('/age-calculator', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        born_date = request.form.get("born_date")
        specific_date, message = verify_born_input(born_date)
        if specific_date:
            current_date = datetime.now()
            time_difference = (current_date - specific_date).days
            years_old = calc_past_years(time_difference)
            result = f"{is_specific_day(specific_date)} {verify_age(years_old)}. You're {years_old} full years, or exactly {time_difference} days old."
            return result
        else:
            return message
    return render_template('age-calculator.html')


#For base and page2 html

@app.route('/page2')
def page2():
    return render_template('page2.html')


@app.route('/')
def base():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=False)