import os
import json

def reading_a_json_file(path):
    preporcessed_file_path = 'Preprocessed_data/'
    dir_list = os.listdir(path)
    for file in dir_list:
        with open(path+file) as f:
            data = json.loads(f.read())
            contents = converting_json_to_list(data)
            with open(preporcessed_file_path+'Q_A_survey.jsonl','w') as file:
                for item in contents:
                    file.write(json.dumps(item)+'\n')
                file.close()
            f.close()

def converting_json_to_list(dialogues):
    text = {}
    Q_A_dialogues = []

    for dialogue_object in dialogues:
        for key,value in dialogue_object.items():
            text = {'prompt':value, 'completion':key}
            Q_A_dialogues.append(text)
    
    return Q_A_dialogues


reading_a_json_file('Preprocessed_data/')        

                 