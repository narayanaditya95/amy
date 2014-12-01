import sys
import sqlite3

old_cnx = sqlite3.connect(sys.argv[1])
old_crs = old_cnx.cursor()
new_cnx = sqlite3.connect(sys.argv[2])
new_crs = new_cnx.cursor()

# Site
new_crs.execute('delete from workshops_site;')
old_crs.execute('select site, fullname, country from site;')
site_lookup = {}
i = 1
for (site, fullname, country) in old_crs.fetchall():
    site_lookup[site] = i
    try:
        new_crs.execute('insert into workshops_site values(?, ?, ?, ?);', \
                        (i, site, fullname, country))
    except Exception, e:
        print >> sys.stderr, 'failing on site with', (site, fullname, country), 'because', str(e)
    i += 1
new_cnx.commit()

# Person
new_crs.execute('delete from workshops_person;')
old_crs.execute('select person, personal, middle, family, email from person;')
person_lookup = {}
i = 1
for (person, personal, middle, family, email) in old_crs.fetchall():
    person_lookup[person] = i
    try:
        new_crs.execute('insert into workshops_person values(?, ?, ?, ?, ?);', \
                        (i, personal, middle, family, email))
    except Exception, e:
        print >> sys.stderr, 'failing on person with', (person, personal, middle, family, email), 'because', str(e)
    i += 1
new_cnx.commit()

# Event
new_crs.execute('delete from workshops_event;')
old_crs.execute('select startdate, enddate, event, site, kind, eventbrite, attendance from event;')
i = 1
for (startdate, enddate, event, site, kind, eventbrite, attendance) in old_crs.fetchall():
    try:
        new_crs.execute('insert into workshops_event values(?, ?, ?, ?, ?, ?, ?, ?);', \
                        (i, startdate, event, kind, eventbrite, attendance, site_lookup[site], enddate))
    except Exception, e:
        print >> sys.stderr, 'failing on event with', (i, site, startdate, enddate, event, kind, eventbrite, attendance), 'because', str(e)
    i += 1
new_cnx.commit()

# Airport
new_crs.execute('delete from workshops_airport;')
old_crs.execute('select fullname, country, latitude, longitude, iata from airport;')
i = 1
for (fullname, country, lat, long, iata) in old_crs.fetchall():
    try:
        new_crs.execute('insert into workshops_airport values(?, ?, ?, ?, ?, ?);', \
                        (i, fullname, country, lat, long, iata))
    except Exception, e:
        print >> sys.stderr, 'failing on airport with', (i, fullname, country, lat, long, iata), 'because', str(e)
    i += 1
new_cnx.commit()
