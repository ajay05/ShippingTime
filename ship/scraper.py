from lxml import etree
import requests


def scrape_usps(tracking, carrier):
    # without session, site enters infinite redirects (need to accept cookies)
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2)'\
        ' AppleWebKit/537.36 (KHTML, like Gecko)' +\
        ' Chrome/34.0.1847.131 Safari/537.36'

    page = s.get('https://tools.usps.com/go/TrackConfirmAction?'
                 'qtc_tLabels1=' + tracking)
    tree = etree.HTML(page.text)
    status = tree.xpath('//*[@id="tc-hits"]/tbody/tr[1]/td[2]/p[1]/text()')
    time = tree.xpath('//*[@id="tc-hits"]/tbody/tr[1]/td[1]/p/text()')

    status = status[0].translate(str.maketrans('\r\t\n', '   '))
    time = time[0].translate(str.maketrans('\r\t\n', '   '))
    status = status.replace(' ', '')
    time = time.replace(' ', '')

    return (status, time)


def scrape_fedex(tracking, carrier):
    pass


def scrape_ups(tracking, carrier):
    pass


def get_status(tracking, carrier):
    """
    Takes string of tracking id and string of carrier and
    calls appropriate scraping function to get shipment
    status.

    Returns shipment's (status, time) as string.
    """
    if carrier == 'UPS':
        return scrape_ups(tracking, carrier)
    elif carrier == 'Fedex':
        return scrape_fedex(tracking, carrier)
    elif carrier == 'USPS':
        return scrape_usps(tracking, carrier)
    else:
        return 'Cannot find carrier to scrape'


def main():
    tracking = '9361289877941113340680'
    carrier = 'USPS'

    print(get_status(tracking, carrier))

if __name__ == '__main__':
    main()
