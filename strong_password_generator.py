# This programme generates a strong, random password 
# This is done using a combination of words, numbers, special characters.

import secrets # Approprite for this project as it provides cryptographically strong random numbers.
import string
import time

adjectives_list = ['adamant', 'adroit',  'amatory', 'animistic', 'antic', 'arcadian', 'baleful', 'bellicose', 'bilious',
'boorish', 'calamitous', 'caustic', 'cerulean', 'comely', 'concomitant',  'contumacious', 'corpulent', 'crapulous', 
'defamatory', 'didactic', 'dilatory', 'dowdy', 'efficacious', 'effulgent', 'egregious', 'endemic', 'equanimous', 'execrable', 
'fastidious', 'feckless', 'fecund', 'friable', 'fulsome', 'garrulous', 'guileless', 'gustatory', 'heuristic', 'histrionic'
'hubristic',  'incendiary', 'insidious', 'insolent', 'intransigent', 'inveterate', 'invidious', 'irksome', 'jejune', 'jocular', 'judicious',
'lachrymose', 'limpid', 'loquacious', 'luminous', 'mannered', 'mendacious', 'meretricious', 'minatory', 'mordant',
'munificent', 'nefarious', 'noxious', 'obtuse', 'parsimonious', 'pendulous', 'pernicious', 'pervasive', 'petulant', 'platitudinous',
'precipitate', 'propitious', 'puckish', 'querulous', 'quiescent', 'rebarbative', 'recalcitrant', 'redolent', 'rhadamanthine',
'risible', 'ruminative', 'sagacious', 'salubrious', 'sartorial', 'sclerotic', 'serpentine', 'spasmodic', 'strident', 'taciturn',
'tenacious', 'tremulous', 'trenchant', 'turbulent', 'turgid', 'ubiquitous', 'uxorious', 'verdant', 'voluble', 'voracious', 'wheedling', 'withering', 'zealous']

nouns_list = ['air', 'area', 'art', 'back', 'body', 'book', 'business' 'car', 'case'
'change', 'child', 'city', 'community', 'company', 'country', 'day', 'door', 'education'
'end', 'eye', 'face', 'fact', 'family', 'father', 'force', 'friend' 'game', 'girl' 'government'
'group', 'guy', 'hand', 'head', 'health', 'history', 'home', 'hour', 'house', 'idea', 'information'
'issue', 'job', 'kid', 'kind', 'law', 'level', 'life', 'line', 'lot', 'man', 'member', 'minute', 'moment'
'money', 'month',  'morning' 'mother', 'name', 'night', 'number', 'office', 'others', 'parent', 'part', 'party'
'people', 'person', 'place', 'point', 'power', 'president', 'problem', 'program' 'question', 'reason', 'research' 
'result', 'right', 'room', 'school', 'service', 'side', 'state', 'story', 'student', 'study', 'system', 'teacher',
'team', 'thing', 'time', 'war', 'water', 'way', 'week', 'woman', 'word', 'work', 'world', 'year']

vowels_list = ['a', 'e', 'i', 'o', 'u']

special_char_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\' , ']' ,  '^', '_', '`', '{', '|', '}', '~']

def main():
    intro()  # Calling the introduction_text function
    generate_pwd()  # Generates a strong password

# This will display the introduction of this program
def intro():
    print('')
    print('Hello')
    print('Welcome to the "Strong and Random Password Generator"!')
    print('This programme will generate a super STRONG and RANDOM password for you!')

# generates the password using above lists
def generate_pwd():
    while True:
        # random word from adjectives list
        adjective = secrets.choice(adjectives_list)

        # uppercase vowels in adjective element for extra 'randomness'
        for char in adjective:
            if char in vowels_list:
                adjective = adjective.replace(char,(char.upper()))
        
        # appends a random LOWER case letter to the adjective
        adjective_1 = str(adjective) + secrets.choice(string.ascii_lowercase)

        # random noun from nouns list
        noun = secrets.choice(nouns_list)

        # appends a random UPPER case letter to the noun
        noun_1 = str(noun) + secrets.choice(string.ascii_uppercase)

        # random number generated between between 0 and 100
        number = secrets.randbelow(100)

        # appends a random digit to number
        number_1 = str(number) + secrets.choice(string.digits)

        # randaom character from special characters list
        special_char = secrets.choice(special_char_list)

        # appends random punctuation mark to special character
        special_char1 = str(special_char) + secrets.choice(string.punctuation)

        password = (adjective_1 + noun_1 + str(number_1) + special_char1)


        # time element adds some delay, giving an impression of an 'arduous' password generation process
        print('')
        print('Starting the process...')
        time.sleep(1)
        print('Making it strong...')
        time.sleep(1)
        print('Adding some randomness...')
        time.sleep(1.25)
        print('Making it super strong...')
        time.sleep(1)
        print('Final touch of randomness...')
        time.sleep(1.5)
        print('...')
        print('')
        print('----------------------------------------------')
        print('BAM! Your new strong password is: ' + '--> ' + str(password) + ' <--')
        print('----------------------------------------------')
        print('')  
        time.sleep(1)

        print('Phew, that password is both STRONG and RANDOM!')
        # ability to generate another password 
        check = input('\nWould you like to generate another password (y/n)? ')

        while check != 'y' and check != 'n':
            check = input()

        if check == 'n':
            break

if __name__ == '__main__':
    main()