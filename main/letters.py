

a = 'ಅ'
aa = 'ಆ'
e = 'ಇ'
ee = 'ಈ'
u = 'ಉ'
uu = 'ಊ'
ru = 'ಋ'
ae = 'ಎ'
aee = 'ಏ'
i = 'ಐ'
o = 'ಒ'
oo = 'ಓ'
aw = 'ಔ'
ka = 'ಕ'
kha = 'ಖ'
ga = 'ಗ'
gha = 'ಘ'
ch = 'ಚ'
cha = 'ಛ'
ja = 'ಜ'
jha = 'ಝ'
ta = 'ಟ'
tha = 'ಠ'
da = 'ಡ'
dha = 'ಢ'
ta = 'ತ'
tha = 'ಥ'
da = 'ದ'
dha = 'ಧ'
na = 'ನ'
pa = 'ಪ'
pha = 'ಫ'
ba = 'ಬ'
bha = 'ಭ'
ma = 'ಮ'
ya = 'ಯ'
ra = 'ರ'
la = 'ಲ'
va = 'ವ'
sha = 'ಶ'
shaa = 'ಷ'
sa = 'ಸ'
ha = 'ಹ'

klist = ['ಅ',  'ಆ',  'ಇ'  ,'ಈ', 'ಉ' , 'ಊ' , 'ಋ' , 'ಎ' , 'ಏ' , 'ಐ' , 'ಒ' , 'ಓ' , 'ಔ' , 'ಕ' , 'ಖ' , 'ಗ' , 'ಘ' , 'ಚ' , 'ಛ' , 'ಜ' , 'ಝ' , 'ಟ' , 'ಠ' , 'ಡ' , 'ಢ' ,'ತ' , 'ಥ' , 'ದ' , 'ಧ' , 'ನ' , 'ಪ' , 'ಫ' , 'ಬ' , 'ಭ' , 'ಮ' , 'ಯ' , 'ರ' , 'ಲ' , 'ವ' , 'ಶ' , 'ಷ' , 'ಸ' , 'ಹ']


stop_words = ['ಈ','ಇವರ','ಅದು','ಇನ್ನೂ','ಇದಕ್ಕೆ','ಮತ್ತು','ಅದೇ','ಅವಳಿಗೆ','ಇವು','ಹಾಗೂ','ಇದು','ಅವನಿಗೆ','ಈಗಿನ','ಎಲ್ಲಾ','ಅವರು','ಅವರಿಗೆ','ಈಗಲು','ಎಲ್ಲ','ಅಥವಾ','ಎಲ್ಲರೂ','ಅದರ','ಇಲ್ಲ','ಎಂಬ','ಎಂಬಾ','ಆದರೆ','ಅವನು','ಅವರ','ಹೀಗೆ','ಈಗ','ಇದೇ','ತಾನು','ಎಂದು','ಇದನ್ನು','ಇದರ','ಅಲ್ಲ','ಆಗಾಗ','ಹಾಗು','ಆಗದೆ','ಅಥವ','ಹೋಗಿ','ಆತನ','ಹೇಗೆ','ಏನೂ','ಇಲ್ಲವೆ','ಇಲ್ಲವೇ','ಹಾಗೆಯೇ','ತಮ್ಮ','ಬಗೆ','ಯವರ','ನಾವು','ನಮ್ಮ','ಎಲ್ಲಿ','ಇವರು','ಆದ','ಅದನ್ನು','ಇಂದು','ತನಗೆ','ಯಾವ','ನನ್ನ','ಇಂದ','ಎನ್ನುವ','ಎಷ್ಟು','ಇದ್ದ','ಎರಡು','ಯಾವುದೇ','ಇತ್ತು','ಬಂದು','ಅದರ','ಅಂದರೆ','ಯಾಗುವ','ಅಲ್ಲಿ','ಇದರಿಂದ','ನಿಮ್ಮ','ಹಾಗಾಗಿ','ಎಂಬುದು','ಹೀಗೆ','ಇವರಿಗೆ','ನಾನು','ಅಲ್ಲಿಂದ','ಇವೆಂದರೆ','ಇದೇ','ಅಲ್ಲಿಂದ','ಅಲ್ಲಿನ','ನಂಗೆ','ನನಗೆ','ಆಗಿನ','ಇವೆಲ್ಲವೂ','ತಾವು','ಅವರೇ','ಅವನ','ಅವಳ','ಅದಕ್ಕೆ','ಅದಕೊಸ್ಕರ','ಎಲ್ಲವನು','ಎಲ್ಲಿಂದ','ತಾನೇ','ತನಗಾಗಿ','ಎಂದು','ಅವನ್ನು','ನನ್ನನ್ನು','ಅದರಿಂದ','ಇವು','ಅಂತ','ಅದಕ್ಕಾಗಿ','ಈತನ','ಇವಳ','ಏಕೆಂದರೆ','ಅಷ್ಟೇ','ಹಾಗೆ','ಅಲ್ಲಿಗೆ','ಇಲ್ಲಿಗೆ','ಏನಾದರೂ','ಅಂದು','ಇಂದು','ಎಂದೆಂದೂ','ಇರುತ್ತದೆ','ಇದ್ದರೆ','ಇರದಿದ್ದರೆ','ಇವಳಿಗೆ','ಆದುದರಿಂದ']

happy=['ಸಂತೋಷ','ಹರ್ಷಚಿತ್ತ','ಜಾಲಿ','ಉಲ್ಲಾಸ','ಸಂತುಷ್ಟ','ತೃಪ್ತಿ','ಉತ್ಸಾಹ','ಹರ್ಷಿತ','ಸುಖ','ನೆಮ್ಮದಿ']
sad=['ದುಃಖ','ಅತೃಪ್ತಿ','ಶೋಚನೀಯ','ನಿರುತ್ಸಾಹ','ಖಿನ್ನತೆ','ವಿಷ್ಣತೆ','ಖೇದ','ನಿರ್ಭಾಗ್ಯ','ಅವಮಾನ','ಅಸಂತೋಷ']
surprise=['ಆಶ್ಚರ್ಯ','ವಿಸ್ಮಯ','ಬೆರಗು','ಚಕಿತ','ಅಚ್ಚರಿ']
angry=['ಕೋಪ','ಹುಚ್ಚು','ಅಸಹ್ಯ']
fear=['ಭಯ','ಹೆದರಿಕೆ','ಅಂಜಿಕೆ','ದಿಗಿಲು']

dhappy={}
dsad = {}
dsurprise ={}
dangry = {}
dfear = {}

dhappy['ಸಂತೋಷ'] = ['ಸಂತೋಷ','noun',0.92]
dhappy['ಹರ್ಷಚಿತ್ತ'] = ['ಹರ್ಷಚಿತ್ತ','noun',0.91]
dhappy['ಜಾಲಿ'] = ['ಜಾಲಿ','noun',0.8]
dhappy['ಉಲ್ಲಾಸ'] = ['ಉಲ್ಲಾಸ','noun',0.95]
dhappy['ಉತ್ಸಾಹ'] = ['ಉತ್ಸಾಹ','noun',0.95]

dhappy['ಸಂತುಷ್ಟ'] = ['ಸಂತುಷ್ಟ','noun',0.8]
dhappy['ತೃಪ್ತಿ'] = ['ತೃಪ್ತಿ','noun',0.75]
dhappy['ಹರ್ಷಿತ'] = ['ಹರ್ಷಿತ','noun',0.8]
dhappy['ಸುಖ'] = ['ಸುಖ','noun',0.95]
dhappy['ನೆಮ್ಮದಿ'] = ['ನೆಮ್ಮದಿ','noun',0.8]

dsad['ದುಃಖ'] = ['ದುಃಖ','noun',0.93]
dsad['ಅತೃಪ್ತಿ'] = ['ಅತೃಪ್ತಿ','noun',0.75]
dsad['ಶೋಚನೀಯ'] = ['ಶೋಚನೀಯ','noun',0.8]
dsad['ನಿರುತ್ಸಾಹ'] = ['ನಿರುತ್ಸಾಹ','noun',0.95]
dsad['ಖಿನ್ನತೆ'] = ['ಖಿನ್ನತೆ','noun',0.85]
dsad['ವಿಷ್ಣತೆ'] = ['ವಿಷ್ಣತೆ','noun',0.81]
dsad['ಖೇದ'] = ['ಖೇದ','noun',0.85]
dsad['ನಿರ್ಭಾಗ್ಯ'] = ['ನಿರ್ಭಾಗ್ಯ','noun',0.8]
dsad['ಅವಮಾನ'] = ['ಅವಮಾನ','noun',0.75]
dsad['ಅಸಂತೋಷ'] = ['ಅಸಂತೋಷ','noun',0.91]

dsurprise['ಆಶ್ಚರ್ಯ'] = ['ಆಶ್ಚರ್ಯ','noun',0.93]
dsurprise['ವಿಸ್ಮಯ'] = ['ವಿಸ್ಮಯ','noun',0.8]
dsurprise['ಬೆರಗು'] = ['ಬೆರಗು','noun',0.9]
dsurprise['ಚಕಿತ'] = ['ಚಕಿತ','noun',0.9]
dsurprise['ಅಚ್ಚರಿ'] = ['ಅಚ್ಚರಿ','noun',0.85]

dangry['ಕೋಪ'] = ['ಕೋಪ','noun',0.95]
dangry['ಹುಚ್ಚು'] = ['ಹುಚ್ಚು','noun',0.8]
dangry['ಅಸಹ್ಯ'] = ['ಅಸಹ್ಯ','noun',0.75]

dfear['ಭಯ'] = ['ಭಯ','noun',0.95]
dfear['ಹೆದರಿಕೆ'] = ['ಹೆದರಿಕೆ','noun',0.92]
dfear['ಅಂಜಿಕೆ'] = ['ಅಂಜಿಕೆ','noun',0.9]
dfear['ದಿಗಿಲು'] = ['ದಿಗಿಲು','noun',0.8]


# ಸಂತೋಷವಾಗಿದ್ದೆ
# ಸಂತೋಷವಾಗಿತ್ತು
# ಜಾಲಿಯಾಗಿರಬಹುದು
# ತೃಪ್ತಿಗೊಳಿಸುತ್ತದೆ


past_future = [b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86']

tenses = [b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86'
b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86',
b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86'
b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86'
b'\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa6\xe0\xb3\x86',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81',b'\xe0\xb2\xac\xe0\xb2\xb9\xe0\xb3\x81\xe0\xb2\xa6\xe0\xb3\x81',b'\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xa6\xe0\xb3\x86']