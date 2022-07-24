import json
import os


def reading_multiple_json_files(path):
    id = 0
    preprocessed_file_path = 'Preprocessed_data/'
    dir_list = os.listdir(path)
    for file in dir_list:
        with open(path+file) as f:
            data = json.loads(f.read())
            contents = parsing_json_to_list(data)
            with open(preprocessed_file_path+'dialogue'+str(id)+".jsonl",'w') as file:
                for item in contents:
                    file.write(json.dumps(item) + "\n")
                    id+=1
                file.close()
            f.close()
                
def parsing_json_to_list(contents):
    text = {}
    dialogues = []
    dialogue_string = None

    for json_object in contents:

        print(dialogue_string)

        if json_object['speaker'] == 'user':
            
            if dialogue_string  != None:
                text = {'text':dialogue_string}
                dialogues.append(text)

            dialogue_string =json_object['utterance']['nlg']
            

        if json_object['speaker'] == 'system':
            if (json_object['utterance']['nlg']==None):
                for image_object in json_object['utterance']['images']:
                    dialogue_string = dialogue_string + " "+ image_object                    
            else:
                dialogue_string = dialogue_string + " "+ json_object['utterance']['nlg']
    #print(dialogues)
    return dialogues
            

reading_multiple_json_files('Preprocessing_data/')
