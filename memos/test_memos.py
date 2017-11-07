import flask_main
import arrow

def test_dates():
    assert humanize_arrow_date(arrow.utcnow().isoformat()) == "Today"
    assert humanize_arrow_date(arrow.utcnow().shift(days=+1).isoformat()) == "Tomorrow"
    assert humanize_arrow_date(arrow.utcnow().shift(days=+1).isoformat()) == "Yesterday"