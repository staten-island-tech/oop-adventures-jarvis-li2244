import json
with open('dontmesswiththis.json')  as dmwt:
    dwmt = json.load(dmwt)
with open('character.json')  as infile:
    char = json.load(infile)
def change(mode):
    if mode  == 'story':
        for i,(v,k) in enumerate(dwmt.items()):
            if k[0]['locationname'] ==  char[0]['location']:
                indexing = k[0]['sublocations'].index(char[0]['sub_location'])
                if indexing == len(k[0]['sublocations']) -1:
                    print('locationname changing')
                    modifiant = 'location'
                    algae = dwmt[f'location{i+2}'][0]['locationname']
                else:
                    modifiant = 'sub_location'
                    algae = k[0]['sublocations'][indexing+1] 
                with open('character.json')  as inf: 
                    charac = json.load(inf)
                    charac[0][modifiant] = algae
                    if modifiant == 'location':
                        charac[0]['sub_location'] = dwmt[f'location{i+2}'][0]['sublocations'][0]
                with open('character.json', 'w+')  as false:
                    false.write(json.dumps(charac,indent=2))
                    false.seek(0)
                
change('story')