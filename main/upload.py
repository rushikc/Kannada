from firebase import firebase
firebase = firebase.FirebaseApplication('https://hackathon-ab821.firebaseio.com/', None)
happy=['ಸಂತೋಷ','ಹರ್ಷಚಿತ್ತ','ಜಾಲಿ','ಉಲ್ಲಾಸ','ಸಂತುಷ್ಟ','ತೃಪ್ತಿ','ಉತ್ಸಾಹ','ಹರ್ಷಿತ','ಸುಖ','ನೆಮ್ಮದಿ']
sad=['ದುಃಖ','ಅತೃಪ್ತಿ','ಶೋಚನೀಯ','ನಿರುತ್ಸಾಹ','ಖಿನ್ನತೆ','ವಿಷ್ಣತೆ','ಖೇದ','ನಿರ್ಭಾಗ್ಯ','ಅವಮಾನ','ಅಸಂತೋಷ']
surprise=['ಆಶ್ಚರ್ಯ','ವಿಸ್ಮಯ','ಬೆರಗು','ಚಕಿತ','ಅಚ್ಚರಿ']
angry=['ಕೋಪ','ಹುಚ್ಚು','ಅಸಹ್ಯ']
fear=['ಭಯ','ಹೆದರಿಕೆ','ಅಂಜಿಕೆ','ದಿಗಿಲು']
stop_words = ['ಈ','ಇವರ','ಅದು','ಇನ್ನೂ','ಇದಕ್ಕೆ','ಮತ್ತು','ಅದೇ','ಅವಳಿಗೆ','ಇವು','ಹಾಗೂ','ಇದು','ಅವನಿಗೆ','ಈಗಿನ','ಎಲ್ಲಾ','ಅವರು','ಅವರಿಗೆ','ಈಗಲು','ಎಲ್ಲ','ಅಥವಾ','ಎಲ್ಲರೂ','ಅದರ','ಇಲ್ಲ','ಎಂಬ','ಎಂಬಾ','ಆದರೆ','ಅವನು','ಅವರ','ಹೀಗೆ','ಈಗ','ಇದೇ','ತಾನು','ಎಂದು','ಇದನ್ನು','ಇದರ','ಅಲ್ಲ','ಆಗಾಗ','ಹಾಗು','ಆಗದೆ','ಅಥವ','ಹೋಗಿ','ಆತನ','ಹೇಗೆ','ಏನೂ','ಇಲ್ಲವೆ','ಇಲ್ಲವೇ','ಹಾಗೆಯೇ','ತಮ್ಮ','ಬಗೆ','ಯವರ','ನಾವು','ನಮ್ಮ','ಎಲ್ಲಿ','ಇವರು','ಆದ','ಅದನ್ನು','ಇಂದು','ತನಗೆ','ಯಾವ','ನನ್ನ','ಇಂದ','ಎನ್ನುವ','ಎಷ್ಟು','ಇದ್ದ','ಎರಡು','ಯಾವುದೇ','ಇತ್ತು','ಬಂದು','ಅದರ','ಅಂದರೆ','ಯಾಗುವ','ಅಲ್ಲಿ','ಇದರಿಂದ','ನಿಮ್ಮ','ಹಾಗಾಗಿ','ಎಂಬುದು','ಹೀಗೆ','ಇವರಿಗೆ','ನಾನು','ಅಲ್ಲಿಂದ','ಇವೆಂದರೆ','ಇದೇ','ಅಲ್ಲಿಂದ','ಅಲ್ಲಿನ','ನಂಗೆ','ನನಗೆ','ಆಗಿನ','ಇವೆಲ್ಲವೂ','ತಾವು','ಅವರೇ','ಅವನ','ಅವಳ','ಅದಕ್ಕೆ','ಅದಕೊಸ್ಕರ','ಎಲ್ಲವನು','ಎಲ್ಲಿಂದ','ತಾನೇ','ತನಗಾಗಿ','ಎಂದು','ಅವನ್ನು','ನನ್ನನ್ನು','ಅದರಿಂದ','ಇವು','ಅಂತ','ಅದಕ್ಕಾಗಿ','ಈತನ','ಇವಳ','ಏಕೆಂದರೆ','ಅಷ್ಟೇ','ಹಾಗೆ','ಅಲ್ಲಿಗೆ','ಇಲ್ಲಿಗೆ','ಏನಾದರೂ','ಅಂದು','ಇಂದು','ಎಂದೆಂದೂ','ಇರುತ್ತದೆ','ಇದ್ದರೆ','ಇರದಿದ್ದರೆ','ಇವಳಿಗೆ','ಆದುದರಿಂದ']

import json

past_future = [b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86']

tenses = [b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86'
b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86',
b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86'
b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86'
b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86']

item={}
item['tenses'] = [t.decode('utf-8') for t in tenses]
item['past_future'] = [t.decode('utf-8') for t in past_future]

firebase.put('','past_future',item['past_future'])
firebase.put('','tenses',item['tenses'])

firebase.put('','stop_words',stop_words)
firebase.put('','happy',happy)
firebase.put('','sad',sad)
firebase.put('','surprise',surprise)
firebase.put('','angry',angry)
firebase.put('','fear',fear)
# res = firebase.get('/happy',None)
# print(item['title'])
# print(type(json.dumps(tenses)))

