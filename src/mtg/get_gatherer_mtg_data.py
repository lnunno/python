'''
Created on Jun 10, 2013

@author: lnunno
'''
import urllib as ul
from bs4 import BeautifulSoup
import re,os,csv

def get_card_data(mtg_set,outdir=''):
    '''Get text info for all cards in the mtg_set.
    ''' 
    mtg_set = mtg_set.replace(' ', '_')
    file_path = outdir+'/%s_cards.txt' % mtg_set
    mtg_set = mtg_set.replace('_','+')
    url = "http://gatherer.wizards.com/Pages/Search/Default.aspx?output=spoiler&method=text&sort=cn+&action=advanced&set=%7c%5b%22"+mtg_set+"%22%5d"
    html = ul.urlopen(url).read()
    f = open(file_path,'w')
    soup = BeautifulSoup(html)
    i = 0
    names = map(lambda x: x.string, soup.find_all('a',{'class':'nameLink'}))
    for td in soup.find_all('td'):
        tag_text = td.string
        if tag_text: 
            tag_text = tag_text.strip()
            f.write(tag_text)
            if tag_text == 'Name':
                f.write(':%s' % names[i])
                i += 1
            if not re.match('[\w|/|Rules Text]+:', tag_text): f.write('\n')
    f.close()
    fix_card_data(file_path)

def fix_card_data(file_path):
    '''Fix some weird errors in the initial pass.
    '''
    fr = open(file_path)
    f_str = fr.read()
    fr.close()
    fw = open(file_path,'w')
    f_str = f_str.replace('Rules Text:Set/Rarity:','Rules Text:\nSet/Rarity:')
    f_str = re.sub(r'(\w+)Name:',r'\1\nName:' , f_str)
    fw.write(f_str)
    fw.close()

def get_card_images(mtg_set,outdir=''):
    mtg_set = mtg_set.replace(' ','%20')
    url = "http://gatherer.wizards.com/Pages/Search/Default.aspx?sort=cn+&output=spoiler&method=visual&action=advanced&set=|[%22"+mtg_set+"%22]"
    html = ul.urlopen(url).read()
    soup = BeautifulSoup(html)
    image_dir = outdir+'/images'
    if not os.path.exists(image_dir): 
        os.mkdir(image_dir)
    else:
        #Assume we already have the images and everything is good. 
        return
    i = 1
    for img in soup.find_all('img'):
        src = img.get('src')
        if 'card' in src:
            src = 'http://gatherer.wizards.com/'+src.lstrip('../../')
            ul.urlretrieve(src, image_dir+os.sep+str(i).zfill(4)+".jpg")
            i += 1
            
def get_set_data(mtg_set,collect_text=True,collect_images=True):
    print "Getting set data for",mtg_set,"..."
    set_dir = 'card_data/'+mtg_set
    if not os.path.exists(set_dir): os.mkdir(set_dir)
    if collect_text:
        print "\tCollecting card data..."
        get_card_data(mtg_set,set_dir)
        print "\tCard data collected."
    if collect_images:
        get_card_images(mtg_set,set_dir)
        print "\tCollecting card images..."
        print "\tCard images collected."
    print "Finished getting set data for",mtg_set+"."
    
def get_mtg_sets():    
    f = open('mtg_set_list.txt')
    lines = f.readlines()
    f.close()
    mtg_sets = []
    for line in lines:
        line = line.strip()
        if line.startswith('['): continue
        mtg_sets.append(line)
    return mtg_sets

def get_card_csv_list(card_data_path):
    card_txt_file = open(card_data_path)
    card_strs_data = card_txt_file.readlines()
    done_card = False
    cards = []
    dict_acc = {}
    for ln in card_strs_data:
        line_tokens = ln.split(':',1)
        if len(line_tokens) == 2:
            attr_name, attr_value = line_tokens[0].strip(),line_tokens[1].strip()
            if attr_name == 'Set/Rarity':
                dict_acc[attr_name] = attr_value
                done_card = True
            elif done_card: 
                    done_card = False
                    if not dict_acc.has_key('Loyalty'):
                        dict_acc['Loyalty'] = ''
                    if not dict_acc.has_key('Color'):
                        dict_acc['Color'] = ''
                    cards.append(dict_acc)
                    dict_acc = {attr_name:attr_value}
            else:
                dict_acc[attr_name] = attr_value
    return cards
    
def mtg_csv_writer():     
    f = open('magic_card_db.csv','w')
    fieldnames = ['Name','Cost','Type','Pow/Tgh','Rules Text','Set/Rarity', 'Loyalty', 'Color']
    dw = csv.DictWriter(f, fieldnames)
    dw.writeheader()
    for mtg_set in get_mtg_sets():
        card_data_path = 'card_data/%s/%s_cards.txt' % (mtg_set,re.sub(' ', '_', mtg_set))
        cards = get_card_csv_list(card_data_path)
        for c in cards:
            dw.writerow(c)
    f.close()

def get_all_sets_data():
    '''Get data from all sets from Gatherer.
    '''
    mtg_sets = get_mtg_sets()
    for mtg_set in mtg_sets:
        get_set_data(mtg_set,collect_images=False)

def run():
    mtg_csv_writer()
        
if __name__ == '__main__':
    run()