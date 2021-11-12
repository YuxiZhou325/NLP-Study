"""

Submitted by: Yuxi Zhou
Email: yxzhou325@gmail.com

Project start time: 2021-02-19 10:31:22
project complete time: 2021-02-19 14:35:30

"""

import os
import argparse
import sys
import json
import datetime
import tkinter as tk
import tkinter.messagebox
from itertools import groupby
from operator import itemgetter
from statistics import mean, stdev


def parse_log_file(filename):
    # Take file from input argument file path
    # filename = sys.argv[1]
    if os.path.exists(filename):
        # Open log file and read lines
        with open(filename) as f:
            lines = f.read().splitlines()
        count = 0
        log_dict_list = []
        date_parser = '%d/%m/%Y:%H:%M:%S +%f'  # Get Date
        for log in lines:
            # if count == 10:
            #     break
            # date are stored in [ ] in apache log format
            date_str = log.split("[")[1].split(']')[0]
            date_obj = datetime.datetime.strptime(date_str, date_parser)

            # a dictionary store features of whole log file
            log_dict_list.append({
                'log': log,
                'day': date_obj.date().day,
                'month_numb': date_obj.date().month,
                'month': date_obj.strftime("%B"),
                'year': date_obj.date().year,
                'request': log.split('"')[1].split()[0],  # + " " + log.split('"')[1].split()[-1],
                'filename': log.split('/')[4].split()[0],
                'language': log.split('/')[3],
                'status': log.split(' ')[8],
                'size': int(log.split(' ')[9]),
            })
            count += 1
        return log_dict_list

    else:
        print("Input File Does Not Exist")


def group_dict_by_month(log_dict_list):
    # the general log report list sorted by months and years
    list_dict_by_month_year = []
    sorted_log_dict_list = sorted(log_dict_list, key=itemgetter('month_numb', 'year'))

    for key, value in groupby(sorted_log_dict_list, key=itemgetter('month', 'year')):
        # the general dictionary contains languages, month, year and other features
        dict = {}
        dict['month'] = list(key)[0]
        dict['year'] = str(list(key)[1])

        # logs sorted by months and years
        grouped_logs = list(value)

        # a new list contains all language dictionary within a month
        list_language_dict = []
        for key1, value1 in groupby(sorted(grouped_logs, key=itemgetter('language')), key=itemgetter('language')):
            # a dictionary contains features (name, size..) of each language
            dict_language = {}
            # print("value1: ", value1)
            grouped_languages = list(value1)
            # print(grouped_languages)
            # print(dict_language)

            total_size = sum(int(item['size']) for item in grouped_languages)

            # use similar way to calculate mean value and standard deviation value
            # note that standard deviation can only be calculated when there are more than 1 elements
            grouped_languages_sizes = []
            for item in grouped_languages:
                # print(int(item['size']))
                grouped_languages_sizes.append(int(item['size']))

            # print(grouped_languages_sizes)
            if len(grouped_languages_sizes) > 1:
                mean_size = mean(grouped_languages_sizes) / 1048576  # convert into MB
                stddev_value = stdev(grouped_languages_sizes) / 1048576  # convert into MB
            else:
                mean_size = mean(grouped_languages_sizes) / 1048576
                stddev_value = None
                # print(grouped_languages_sizes)
                print(
                    "Note: Only 1 file of {0} language in {1} Can not calculate Standard Deviation of files!".format(
                        key1, key))

            # print(grouped_languages_sizes)
            # mean_size = ((total_size / len(grouped_languages)) / 1048576)
            # print(mean_size)

            # store all features into the language dictionary
            dict_language['name'] = key1
            dict_language['total_GB'] = (total_size / 1073741824)  # convert into GB
            dict_language['mean_MB'] = mean_size
            dict_language['stddev_MB'] = stddev_value

            # append all the dictionaries into the list
            list_language_dict.append(dict_language)

        # a new dictionary contains all the requests
        request_dict = {}
        for key2, value2 in groupby(sorted(grouped_logs, key=itemgetter('request')), key=itemgetter('request')):
            # dict_request = {}
            # sorted logs with requests (there is only GET in the ./example.log)
            grouped_request = list(value2)
            # dict_request['request'] = key2
            # print(dict_request)

            success_counter = 0
            # failed_counter = 0
            # iter all the request status in the sorted log and count success ones
            for item in grouped_request:
                # print(item['status'])
                # if item['status'] == 200 or item['status'] == 202:
                if int(item['status']) <= 299:
                    success_counter += 1
            # print(success_counter)
            # store request information into the request dictionary
            request_dict['percent_success'] = (success_counter / len(grouped_request)) * 100
            request_dict['success'] = success_counter
            request_dict['total'] = len(grouped_request)

        # a new list to store non ascii file names
        list_non_ascii = []
        for key3, value3 in groupby(sorted(grouped_logs, key=itemgetter('filename')), key=itemgetter('filename')):
            grouped_filename = list(value3)
            dict_filename = {}
            dict_filename['filename'] = key3
            # print(dict_filename)
            # iter the sorted log and find non ascii file names
            for item in grouped_filename:
                # print(str(item['filename']))
                if str(item['filename']).isascii():
                    pass
                else:
                    # file name is not ascii and then check whether request is succeed
                    if int(item['status']) == 200 or int(item['status']) == 202:
                        list_non_ascii.append(str(item['filename']) + "  Request: %s (Success)" % str(item['status']))
                    else:
                        list_non_ascii.append(str(item['filename']) + "  Request: %s (Failed)" % str(item['status']))
                    # print(list_non_ascii)

        # append language, request and non_ascii dictionaries to the general log report list
        dict['languages'] = sorted(list_language_dict, key=itemgetter('total_GB'), reverse=True)[:5]
        dict['request'] = request_dict
        dict['non_ascii'] = list_non_ascii
        list_dict_by_month_year.append(dict)

    return list_dict_by_month_year


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Please Pass a File Path for Input Log Files!")

    else:
        with open(sys.argv[2], 'w') as outfile:
            json.dump(group_dict_by_month(log_dict_list=parse_log_file(sys.argv[1])), outfile, indent=4, sort_keys=True)
            # print("\n" + "Log Report is successfully generated at %s !" % sys.argv[2])
            root = tk.Tk()
            root.withdraw()
            tkinter.messagebox.showinfo('Log Parser', "Log Report is successfully generated at %s !" % sys.argv[2])
