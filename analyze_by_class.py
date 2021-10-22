import json
import operator

if __name__ == '__main__':
    _label = []
    _apiset = []
    with open('./labels.txt', 'rt') as lab_f:
        _label = lab_f.readlines()
    with open('./all_analysis_data.txt', 'rt') as api_f:
        _apiset = api_f.readlines()
    _INFODICT_ = {

    }
    line_counter = 0
    while len(_label) > line_counter:
        api_line = _apiset[line_counter]
        cur_lab = _label[line_counter]
        if api_line[-1] == "\n":
            api_line = api_line[0:-1]
        if cur_lab[-1] == "\n":
            cur_lab = cur_lab[0:-1]
        
        if cur_lab not in _INFODICT_:
            _INFODICT_[cur_lab] = {}
        apis = api_line.split(" ")

        for api in apis:
            if api not in _INFODICT_[cur_lab]:
                _INFODICT_[cur_lab][api] = 1
            else:
                _INFODICT_[cur_lab][api] += 1
        line_counter += 1

    for key in _INFODICT_:
        label_info = _INFODICT_[key]
        _INFODICT_[key] = {k: v for k, v in sorted(label_info.items(), key=operator.itemgetter(1), reverse=True)}

    with open("analysis_result.json", "w") as json_file:
        json.dump(_INFODICT_ ,json_file, indent=4)

    print("analysis finished!")