"""
Dictionary of emoji unicode to sentiment score mappings
Only emojis of clear sentiment (facial expressions, popular symbols, etc) were selected
Subset of data used from the following research paper
    @article{Kralj2015emojis,
    author={{Kralj Novak}, Petra and Smailovi{\'c}, Jasmina and Sluban, Borut and Mozeti\v{c}, Igor},
    title={Sentiment of emojis},
    journal={PLoS ONE},
    volume={10},
    number={12},
    pages={e0144296},
    url={http://dx.doi.org/10.1371/journal.pone.0144296},
    year={2015}
For more info see -> http://kt.ijs.si/data/Emoji_sentiment_ranking/index.html
"""
emoji2sentiment = {
    u'\U0001F602': 0.308920547,  # FACE WITH TEARS OF JOY
    u'\U00002764': 0.894282311,  # HEAVY BLACK HEART
    u'\U00002665': 0.903114187,  # BLACK HEART SUIT
    u'\U0001F60D': 0.86757899,  # SMILING FACE WITH HEART-SHAPED EYES
    u'\U0001F62D': -0.119777159,  # LOUDLY CRYING FACE
    u'\U0001F618': 0.868974881,  # FACE THROWING A KISS
    u'\U0001F60A': 0.844572368,  # SMILING FACE WITH SMILING EYES
    u'\U0001F44C': 0.750568958,  # OK HAND SIGN
    u'\U0001F495': 0.884682586,  # TWO HEARTS
    u'\U0001F44F': 0.714453584,  # CLAPPING HANDS SIGN
    u'\U0001F601': 0.639195328,  # GRINNING FACE WITH SMILING EYES
    u'\U0000263A': 0.841289523,  # WHITE SMILING FACE
    u'\U00002661': 0.866404715,  # WHITE HEART SUIT
    u'\U0001F629': -0.452445652,  # WEARY FACE
    u'\U0001F64F': 0.721661055,  # PERSON WITH FOLDED HANDS
    u'\U0000270C': 0.672967864,  # VICTORY HAND
    u'\U0001F60F': 0.598108747,  # SMIRKING FACE
    u'\U0001F609': 0.700396825,  # WINKING FACE
    u'\U0001F64C': 0.735191638,  # PERSON RAISING BOTH HANDS IN CELEBRATION
    u'\U0001F648': 0.569620253,  # SEE-NO-EVIL MONKEY
    u'\U0001F4AA': 0.794923858,  # FLEXED BICEPS
    u'\U0001F604': 0.606995885,  # SMILING FACE WITH OPEN MOUTH AND SMILING EYES
    u'\U0001F612': -0.463806971,  # UNAMUSED FACE
    u'\U0001F483': 0.893405601,  # DANCER
    u'\U0001F496': 0.89296333,  # SPARKLING HEART
    u'\U0001F603': 0.796449704,  # SMILING FACE WITH OPEN MOUTH
    u'\U0001F614': -0.186836518,  # PENSIVE FACE
    u'\U0001F631': 0.265104809,  # FACE SCREAMING IN FEAR
    u'\U0001F389': 0.906318083,  # PARTY POPPER
    u'\U0001F61C': 0.672364672,  # FACE WITH STUCK-OUT TONGUE AND WINKING EYE
    u'\U0001F338': 0.892908828,  # CHERRY BLOSSOM
    u'\U0001F49C': 0.88252149,  # PURPLE HEART
    u'\U0001F499': 0.920110193,  # BLUE HEART
    u'\U00002728': 0.776623377,  # SPARKLES
    u'\U0001F633': 0.026362039,  # FLUSHED FACE
    u'\U0001F497': 0.867716535,  # GROWING HEART
    u'\U00002605': 0.824561404,  # BLACK STAR
    u'\U0001F621': -0.194074074,  # POUTING FACE
    u'\U0001F60E': 0.701886792,  # SMILING FACE WITH SUNGLASSES
    u'\U0001F622': 0.008605852,  # CRYING FACE
    u'\U0001F48B': 0.900884956,  # KISS MARK
    u'\U0001F60B': 0.875706215,  # FACE SAVOURING DELICIOUS FOOD
    u'\U0001F64A': 0.632575758,  # SPEAK-NO-EVIL MONKEY
    u'\U0001F634': -0.105839416,  # SLEEPING FACE
    u'\U0001F49E': 0.904255319,  # REVOLVING HEARTS
    u'\U0001F60C': 0.633858268,  # RELIEVED FACE
    u'\U0001F525': 0.362549801,  # FIRE
    u'\U0001F4AF': 0.177011494,  # HUNDRED POINTS SYMBOL
    u'\U0001F52B': -0.246861925,  # PISTOL
    u'\U0001F49B': 0.895615866,  # YELLOW HEART
    u'\U0001F49A': 0.811926606,  # GREEN HEART
    u'\U0001F61E': -0.140939597,  # DISAPPOINTED FACE
    u'\U0001F606': 0.572559367,  # SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES
    u'\U0001F61D': 0.618768328,  # FACE WITH STUCK-OUT TONGUE AND TIGHTLY-CLOSED EYES
    u'\U0001F62A': -0.103448276,  # SLEEPY FACE
    u'\U0001F62B': -0.176165803,  # TIRED FACE
    u'\U0001F605': 0.235127479,  # SMILING FACE WITH OPEN MOUTH AND COLD SWEAT
    u'\U0001F44A': 0.30259366,  # FISTED HAND SIGN
    u'\U0001F480': -0.285285285,  # SKULL
    u'\U0001F600': 0.772307692,  # GRINNING FACE
    u'\U0001F61A': 0.883381924,  # KISSING FACE WITH CLOSED EYES
    u'\U0001F63B': 0.82278481,  # SMILING CAT FACE WITH HEART-SHAPED EYES
    u'\U0001F440': 0.122641509,  # EYES
    u'\U0001F498': 0.883116883,  # HEART WITH ARROW
    u'\U0001F44B': 0.569892473,  # WAVING HAND SIGN
    u'\U0000270B': 0.162162162,  # RAISED HAND
    u'\U0001F625': 0.162790698,  # DISAPPOINTED BUT RELIEVED FACE
    u'\U0001F615': -0.496350365,  # CONFUSED FACE
    u'\U0001F494': -0.172413793,  # BROKEN HEART
    u'\U0001F624': -0.281632653,  # FACE WITH LOOK OF TRIUMPH
    u'\U0001F608': 0.397260274,  # SMILING FACE WITH HORNS
    u'\U0001F630': -0.023255814,  # FACE WITH OPEN MOUTH AND COLD SWEAT
    u'\U0001F611': -0.439252336,  # EXPRESSIONLESS FACE
    u'\U0001F451': 0.896995708,  # CROWN
    u'\U0001F639': 0.19266055,  # CAT FACE WITH TEARS OF JOY
    u'\U0001F449': 0.741935484,  # WHITE RIGHT POINTING BACKHAND INDEX
    u'\U0001F620': -0.364016736,  # ANGRY FACE
    u'\U00002606': 0.884057971,  # WHITE STAR
    u'\U0001F613': -0.102803738,  # FACE WITH COLD SWEAT
    u'\U0001F623': -0.245762712,  # PERSEVERING FACE
    u'\U0001F610': -0.546391753,  # NEUTRAL FACE
    u'\U0001F628': -0.193877551,  # FEARFUL FACE
    u'\U0001F616': -0.19266055,  # CONFOUNDED FACE
    u'\U0001F493': 0.852941176,  # BEATING HEART
    u'\U0001F4A6': 0.631578947,  # SPLASHING SWEAT SYMBOL
    u'\U0001F637': -0.21875,  # FACE WITH MEDICAL MASK
    u'\U0001F64B': 0.659090909,  # HAPPY PERSON RAISING ONE HAND
    u'\U0001F4A9': -0.167701863,  # PILE OF POO
    u'\U0001F61B': 0.788235294,  # FACE WITH STUCK-OUT TONGUE
    u'\U0001F62C': 0.269230769,  # GRIMACING FACE
    u'\U0001F382': 0.796178344,  # BIRTHDAY CAKE
    u'\U0001F31F': 0.75,  # GLOWING STAR
    u'\U0001F3C6': 0.922580645,  # TROPHY
    u'\U0001F619': 0.961783439,  # KISSING FACE WITH SMILING EYES
    u'\U0001F48F': 0.525179856,  # KISS
    u'\U0001F52A': 0.146067416,  # HOCHO
    u'\U0001F339': 0.945945946,  # ROSE
    u'\U0001F646': 0.743589744,  # FACE WITH OK GESTURE
    u'\U0001F4B0': 0.452631579,  # MONEY BAG
    u'\U0001F37B': 0.716666667,  # CLINKING BEER MUGS
    u'\U0001F645': -0.288135593,  # FACE WITH NO GOOD GESTURE
    u'\U0001F31E': 0.93877551,  # SUN WITH FACE
    u'\U0001F649': 0.495145631,  # HEAR-NO-EVIL MONKEY
    u'\U0001F446': 0.58974359,  # WHITE UP POINTING BACKHAND INDEX
    u'\U0001F607': 0.818181818,  # SMILING FACE WITH HALO
    u'\U0001F63F': -0.485714286,  # CRYING CAT FACE
    u'\U0001F4A3': 0.012345679,  # BOMB
    u'\U0001F37A': 0.804878049,  # BEER MUG
    u'\U0001F632': -0.098901099,  # ASTONISHED FACE
    u'\U0001F636': -0.204819277,  # FACE WITHOUT MOUTH
    u'\U0001F49D': 0.826086957,  # HEART WITH RIBBON
    u'\U0001F635': 0.12,  # DIZZY FACE
    u'\U0001F638': 0.650793651,  # GRINNING CAT FACE WITH SMILING EYES
    u'\U0001F447': 0.48,  # WHITE DOWN POINTING BACKHAND INDEX
    u'\U0001F627': -0.090909091,  # ANGUISHED FACE
    u'\U0001F62E': 0.438596491,  # FACE WITH OPEN MOUTH
    u'\U0001F63D': 0.702702703,  # KISSING CAT FACE WITH CLOSED EYES
    u'\U0001F640': 0.517241379,  # WEARY CAT FACE
    u'\U0001F450': -0.03125,  # OPEN HANDS SIGN
    u'\U0001F491': 0.848484848,  # COUPLE WITH HEART
    u'\U0001F61F': 0.096774194,  # WORRIED FACE
    u'\U0001F49F': 0.882352941,  # HEART DECORATION
    u'\U0001F62F': 0.2,  # HUSHED FACE
    u'\U0001F626': -0.538461538,  # FROWNING FACE WITH OPEN MOUTH
    u'\U0001F386': 0.906976744,  # FIREWORKS
    u'\U0001F63A': 0.515151515,  # SMILING CAT FACE WITH OPEN MOUTH
    u'\U0001F63E': -0.428571429,  # POUTING CAT FACE
    u'\U0001F63C': 0.523809524,  # CAT FACE WITH WRY SMILE
    u'\U00002620': -0.076923077,  # SKULL AND CROSSBONES
    u'\U0001F387': 0.894736842,  # FIREWORK SPARKLER
    u'\U00002639': -0.75,  # WHITE FROWNING FACE
    u'\U0001F64E': -0.066666667,  # PERSON WITH POUTING FACE
    u'\U0001F617': 0.846153846,  # KISSING FACE
    u'\U0001F320': 0.692307692,  # SHOOTING STAR
}
