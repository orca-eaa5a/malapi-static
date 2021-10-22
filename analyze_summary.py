import json
import operator

if __name__ == '__main__':
    _apiset = []
    with open('./all_analysis_data.txt', 'rt') as api_f:
        _apiset = api_f.readlines()
    _INFODICT_ = {

    }
    line_counter = 0
    while len(_apiset) > line_counter:
        api_line = _apiset[line_counter]
        if api_line[-1] == "\n":
            api_line = api_line[0:-1]
        apis = api_line.split(" ")

        for api in apis:
            if api not in _INFODICT_:
                _INFODICT_[api] = 1
            else:
                _INFODICT_[api] += 1
        line_counter += 1

    _INFODICT_ = {k: v for k, v in sorted(_INFODICT_.items(), key=operator.itemgetter(1), reverse=True)}

    with open("analysis_summary.json", "w") as json_file:
        json.dump(_INFODICT_ ,json_file, indent=4)

    print("analysis finished!")