import urllib.request
import json


class Fetch():

    def _fetch(self, url):

        if type(url) is not str:
            raise TypeError("url should be a string but is " + str(type(url)))

        request = urllib.request.Request(url)

        try:
            requested_data_json = urllib.request.urlopen(request).read()
        except Exception as e:
            print("Failed to fetch data with URL: " + url)
            raise

        requested_data = json.loads(requested_data_json)

        return requested_data
