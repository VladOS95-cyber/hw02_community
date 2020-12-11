import datetime as dt


def year(request):
    """
    Добавляет переменную с текущим годом.
    """
    
    current_yr = dt.datetime.today().year
    return {
        'year': current_yr
    }
