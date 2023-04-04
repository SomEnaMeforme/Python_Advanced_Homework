import os
from itertools import groupby
import json
from typing import List, Dict
import time




def analyze_log() -> List[Dict[str, str]]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logs_file = os.path.join(base_dir, 'skillbox_json_messages.log')
    logs_as_list = []
    with open(logs_file, 'r') as logs:
        for i_line in logs.readlines():
            logs_as_list.append(json.loads(i_line))
    return logs_as_list


def analyze_log_subtask1(logs: List[Dict[str, str]]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for i_level, i_elements in groupby(logs, lambda x: x['level']):
        if not(i_level in result):
            result.update({i_level: 0})
        result[i_level] += len(list(i_elements))
    return result


def analyze_log_subtask2(logs: List[Dict[str, str]]) -> int:
    hours_analyze = {}

    for i_hour, el in groupby(logs, lambda x: time.strptime(x['time'], '%H:%M:%S').tm_hour):
        hours_analyze.update({i_hour: len(list(el))})
    maximum_count = max(hours_analyze.values())
    for hour, count in hours_analyze.items():
        if count == maximum_count:
            return hour



def condition_for_subtask3(el: Dict[str, int]) -> bool:
    date = time.strptime(str(el['time']), '%H:%M:%S')
    return date.tm_hour == 5 and date.tm_min >= 0 and date.tm_min <= 20 and el['level'] == 'CRITICAL'


def analyze_log_subtask3(logs: List[Dict[str, str]]) -> int:
   for key, elements in groupby(logs, lambda x: condition_for_subtask3(x)):
       if (key):
           return len(list(elements))


def analyze_log_subtask4(logs: List[Dict[str, str]]) -> int:
    count = 0
    for i_key, i_elements in groupby(logs, lambda x: 'dog' in x['message']):
        if (i_key): count += len(list(i_elements))
    return count


def analyze_log_subtask5(logs: List[Dict[str, str]]) -> str:
    words_analyze: Dict[str, int] = {}
    max_word: str = ''
    max_count: int = 0
    for i_word in [words for data in logs for words in data['message'].split()]:
        if i_word in words_analyze:
            words_analyze[i_word] += 1
        else:
            words_analyze.update({i_word: 1})
        if words_analyze[i_word] > max_count:
            max_word = i_word
            max_count = words_analyze[i_word]
    return max_word

if __name__ == '__main__':
    logs = analyze_log()
    print(analyze_log_subtask1(logs))
    print(analyze_log_subtask2(logs))
    print(analyze_log_subtask3(logs))
    print(analyze_log_subtask4(logs))
    print(analyze_log_subtask5(logs))