from calendar import HTMLCalendar
from events.models import Conference
import locale
locale.setlocale(locale.LC_ALL, '')


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        day_events = events.filter(start_time__day=day)
        output_day = ''
        if day_events.count() > 0:
            output_day += f'<span class = "badge bg-primary rounded-pill">{day_events.count()}</span>'
        else:
            output_day += f'<span>&nbsp</span>'

        #for event in day_events:
        #    output_day += f'<li class="cal-event-name"> {event.name} </li>'

        if day != 0:
            return f'<td class="cal-day"><div class="date">{day}</div>{output_day}</td>'
        return '<td class="no-day"></td>'

    def formatweek(self, theweek, events):
        output_week = ''
        for day, weekday in theweek:
            output_week += self.formatday(day, events)
        return f'<tr class="cal-row-week"> {output_week} </tr>'
    
    def formatmonth(self, withyear=True):
        events = Conference.objects.filter(start_time__year=self.year, start_time__month=self.month)

        calendar = f'<table class="calendar">\n'
        calendar += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        calendar += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            calendar += f'{self.formatweek(week, events)}\n'
        return calendar