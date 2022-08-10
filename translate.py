import googletrans
from googletrans import Translator


def get_langKey(val):
    for key, value in googletrans.LANGUAGES.items():
         if val == value:
             return key
 
    return -1





def translate(userString):
    
    userString = userString.lower()
    
    try: list = userString.split('"', 1)
    
    except IndexError as e:
       return ""
        
 
    else: 
  
        language = list[0]
        
        language = language.replace(" ", "")
        string = list[1]
        string = string.replace('"', "")
        
        
        if ( get_langKey(language) == -1 ):
            return  "Sorry but that language doesn't exist or cannot be translated to, check your spelling"
        else: 
            lang = get_langKey(language)
        translator = Translator()

        result = translator.translate(string, lang)

        return ("In " + language + " this is: " + "\"" + result.text + "\"") 
     