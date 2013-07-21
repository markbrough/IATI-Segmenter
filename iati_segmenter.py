#!/usr/bin/env python

# Takes apart large IATI XML files and outputs one file per country or region.

# Copyright 2013 Mark Brough.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License v3.0 as 
# published by the Free Software Foundation, either version 3 of the License, 
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

from lxml import etree
import csv
import lxml
import sys
import os

# FIXME: if there are multiple countries/countries+regions, then don't
# output to the same file.
def segment_file(prefix, filename):
    print "Segmenting file", filename
    doc=etree.parse(os.path.join(filename))
    countries = set(doc.xpath('//iati-activity/recipient-country/@code'))
    regions = set(doc.xpath('//iati-activity/recipient-region/@code'))
    print "Found countries", list(countries)
    print "Found regions", list(regions)
    
    out = {}

    iatiactivities = doc.xpath('//iati-activities')[0]

    for country in countries:
        out[country] = etree.Element('iati-activities')
        for attribute, attribute_value in iatiactivities.items():
            out[country].set(attribute, attribute_value)

    for region in regions:
        out[region] = etree.Element('iati-activities')
        for attribute, attribute_value in iatiactivities.items():
            out[region].set(attribute, attribute_value)

    out['NULL'] = etree.Element('iati-activities')
    for attribute, attribute_value in iatiactivities.items():
        out['NULL'].set(attribute, attribute_value)

    activities = doc.xpath('//iati-activity')

    for activity in activities:
        if (activity.xpath('recipient-country')) and (activity.xpath('recipient-country/@code')[0] != ""):
            country = activity.xpath('recipient-country/@code')[0]
            out[country].append(activity)
        elif (activity.xpath('recipient-region')) and (activity.xpath('recipient-region/@code')[0] != ""):
            region = activity.xpath('recipient-region/@code')[0]
            out[region].append(activity)
        else:
            # catch activities without a country or region
            # (should not happen, but possible)
            out['NULL'].append(activity)

    # Create metadata file...
    fieldnames = ['country_code', 'filename', 'package_name']
    metadata_file = open('data/metadata.csv', 'w')
    metadata = csv.DictWriter(metadata_file, fieldnames)
    metadata.writeheader()

    for country, data in out.items():
        print "Writing data for", country
        # Check not empty
        if data.xpath('//iati-activity'):
            data = etree.ElementTree(data)
            data.write("data/"+prefix+"-"+country+".xml")
            metadata.writerow({
                'country_code':country, 
                'filename':prefix+"-"+country+'.xml',
                'package_name': prefix+"-"+country})
    print "Finished writing data, find the files in data/"

    metadata_file.close()

if __name__ == '__main__':
    arguments = sys.argv
    arguments.pop(0)
    prefix = arguments[0]
    arguments.pop(0)
    filenames = arguments

    if not filenames:
        print "No filenames"
    else:
        for filename in filenames:
            segment_file(prefix, filename)
