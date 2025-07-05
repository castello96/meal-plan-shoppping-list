from extract_links import LinkExtractor
from scrape import Scraper
import json

"""
- Open the email.
- Gmail: Click More (⋮) > Show Original
Copy all the text and paste into the below link extractor to extract the URLs.
"""

# Paste your email content here (ensure proper indentation)
email_text = """Hi ,

Here's your weekly healing menu curated by me, your personal
Integrative Nutrition & Gut Health Coach!

Below are the exact recipes on my meal plan for next week. I
hope you find some healthy eating inspiration!

Don't forget to hit the 'Jump to Recipe' button at the top of
most recipes to jump straight to the goods!

For breakfast this week, I'm making:

* Turkey & Butternut Squash Skillet=20
( https://email.e.kajabimail.net/c/eJxskE2u2yAUhVdjTyoswNjYAwat2kgddwHWNdzE=
NBj84DpVdl_lT6r6MuQ7hyP4YNumCCuaM_yG2bNCKeMxp0iFbTm53ZJPsXaGK-e0qNEI3Q5yHHs=
ua1zBh8lh8BfM18k7I4dRdJ1Quuuf6Q2KTvVDq9SLrVgKnHCi64bmgeacwFko9KxkLGnPFt_eL_=
ixY3yEL7TP97Uft9O3_8beJYvRQusZeeuEOPZK9VxrIdvjrMEpYQFqbySXHRet4B3nXDZqkIPjF=
qRSnPdqqBTH5iHuNt5EpDqYhWgrVfu1kodKHoIntBkuPp5KY9NayUPZvEXHaM9nvDKIjs07Eea4=
EysfO5SFlbMPAYn98bSwUwJidkEsWMlD_bJXMDrMk0sr-Gg-PSSb6O2SApTm9mEMIYlK8dO9YNN=
aZ7R-8xjp7lipUXLJB1EXT0_tSmsutRprMr884Zef3yvZ_oMvRv4NAAD__39pwO0 )

* Egg Muffins with Spinach & Goat Feta=20
( https://email.e.kajabimail.net/c/eJxskM2u2yAQhZ_GbCpbMB7_LVi0aiN13QewxjCO=
aW1wAd_qvn0VJ5Gq3iz5zuEgPtr30dPG-hf9pMmVKYfIcww-p3KPwR4mu-CF1RKt7ZRgrbq6h2F=
oJQjeyK2j5dW9cXwfndXQD6ppFHZN-0hvUDXY9jXik22cEl15zO876zuaYiBrKOVHJXIKRzT88n=
7i3wf7e_hEx3Sufbudvvw39ipZ9GDIdGSxJzXXbdOSNTBNjW1nsigRhdMgoZGqVrKRUkKFPfRWG=
gJEKVvsC5Rc3cXdxivPWax6yXlPRf25gEsBl4lz5riEjSdKXJmwFXDh67Xcjnl2PpV_XF7KtDtP=
ZinJ23LmTAXUkY3bWTxdJfaW42jDRs7rD89G7Z1Zwkqpun2P1zWoAuX1LJiwiXPOsc-nUcQBJMh=
eieTyQzJ2nYQOB5H1D5f50_evBdT_4DcNfwMAAP__XSK6gw )

* Flaxseed Mini Loaves=20
( https://email.e.kajabimail.net/c/eJxskEGPmzAQhX8NvlRB9jAEc_ChVRup5_4ANNjD=
xl2wqW1W3f76CpJIVTdHf-_5zcyjdR0CLWxe6SeN_pRLTDylGEo-rSm6zRYfg3BGonOdEmxU12j=
o-7MEwQv5eXA8-zdO74N3BnSv2lZh157v6g5Vi2fdID7YwjnTCw_lfWVzQ2OK5CzlcrckznFLlp=
_-z_xr43ATH2gbj7Rv--vLf2HPlKvp90WRLdGEurUgJzVi5_oRdQO9nYQ3IKGVqlGylVJCjRq0k=
5YAUcoz6gol17fi9vA6cBGzuZay5qr5XMGlgsvoKVj6QyuVV6ptXCq4cKjgMs30OzO705iY3GFu=
Elu_snj0kzk4ToOLC_lgPoxKJnh7jTPlej-J5zmqCuXLYbBxEUec51COFhF7kCC1EtmXe7HYdRI=
67EUxP3zhT9-_VtD8g98M_A0AAP__9bu0Vg ) with PB &
honey

For lunch this week, I'm making:

* Ranch Spinach Turkey Meatballs=20
( https://email.e.kajabimail.net/c/eJxskMGO3CoQRb_G3jzZAlw29oLFi5KWss4HWGWo=
HpPB4EB5pP77qN3dUpTMknMvR3Bx3-eIG5l3_ImLbwqnTNecIpdmz8kdln2KtTMCnNOyJiN1N6p=
pGoSqaUMfZkfBf1C-zd4ZNU6y7yXofnimdyh7GMYO4MU2KgXfaObbTuaBlpzQWSz8rGQq6ciWPr=
1f6NdB8RG-0LGctm_305e_ZJ8lq5Ha2VEvSyfVcHVXC0C4CKmts8MEXV97o4Tqheyk6IUQqoVRj=
U5YVABCDDBWIKh9DHeXt5G4DmZl3kvV_V-pS6UuvFJEPjKGeGQ-MuXWpq1Sl5Uw8HprMka7NmX3=
Ee3a8JHf6dZshLxgCOWUdJms36l-7VYoOsqzSxv6aP55QjbR2zUFLO39qxRCkhWIt7Ng01afOk-=
Rz3UBJiWUGGVdPD8HB62F0jDVbH54pv--f61U9wf-MOp3AAAA__-RVr8o )

* Paleo Egg Roll Soup=20
( https://email.e.kajabimail.net/c/eJxskU2O3CAUhE-DN5Fb_NngBYtEnZayzgGsZ3jj=
JsFAAM9obh-5f6RRMkt_Va8sqiDnOcKG5jf8gsX3taWCLyXFVvtckttt8yl2zlDpnGIdGqaE5tM=
0Ut7hBj7MDoN_xfI-e2e4ntgwMKmG8aEekA1y1ELKJ9uwVlhxbu8ZzR0tJYGzUNvDUrCmvVj89L=
7inx3jXXyifbmlfT--vv0T9plyNXZaQC0C9KA5lRIXtygQDF8Q5Ih06LzhlA-UCUYHSik_Sc21o=
xa4lJSOUhNJ8XQv7gg_RWxdMNfWciXiK-EXwi97XNIe3RuGELHWk00b4ZcMAVOP69qXFEJf0577=
t2sKKGgPPh-n4rK3bd7Q-X0j4lyT9RAIHw9674aIc_axYcHaHoKFLYNfIxHnBj68-ejmVvyC9Wl=
IsWFsh_4RNyzHT6RmfFJ6ojMbJzpMis-caaFU95ysYnRYZpc28NH89_piorfXFKCejpYxhMSIpO=
vNYNPWFbQ-e4ztNqyUE6ecatZV3x5bS6UoV3LqmvnpG375cSZcfMCvhv8NAAD__8Hn54A )
- yum!
* Turmeric Carrot Soup=20
( https://email.e.kajabimail.net/c/eJxskU9vozwQxj8NXF4R2cYEOPjwRimrrdSqTZtm=
yyUa7GniBNvUNkV8-1X6R1rt9ujfM_5JMw8Mw96CQXGGE3Q6C9F5fPHOxpAN3qlRRu1sqgThSpU=
0RUHLvGJ1vSQsRQO63yvs9Rv6ea-VYFVNi4Lyslh-phdIC76scs6_mMEQ4ID7OA8oPlDnHSgJIX=
6OeAxu9BK__R_wdUT7EX6hsXu3XV1eq79k3yVHURBKaA4gFeOqxJoWJZRlB9BVilQvkGrBCCsIz=
SkpCCFswStWKSKBcU7IklcJJ7j4ONxFvrAY014cYxxCkv-fsCZhzTRNi6DN0M-vo7YOFtKZhDVg=
o860fenBGIjOz9lB2wP6LI7eoNcyk-C9i1lw43Ax5Q0O-pzka3Ui87Xd1o-Ngs42561RVze7wJ7=
J0-5xe1xuzvXNQ37U8nRtbu2Gb86VkWsyXRte706r182PBtrdND39es5vtzcFrNvxnrZ37dySu2=
2zut82qw17gtbebtKvpgJahX6vnAFtxT9Le2G1PLoewuJyXOx7RxNODu8D0pnUo9SDRhvf--S8Z=
oSRiqZBx8-KeVkSVvI6jeJBR_zv5zph-R_4TbDfAQAA__84mOST )


For dinner this week, I'm making:

* Teriyaki Turkey Bowls=20
( https://email.e.kajabimail.net/c/eJxskN2u1CAUhZ-m3Jg2m11o6QUXGp3Eax-gYWA7=
g4cCAj3JeXvT-UmMziXfWizCZ3Jeo9lIv5lf5uz72lKhnyXFVvtckttt8ykyp0E4N3NGms-jwmW=
ZABltxofVUfDvVD5W7zSqhUvJxSynR3pALsWkRiGebKNazYXW9pFJ39G5JOOsqe1RKVTTXiy9vF=
_p907xHj7Rfr6tfTtOX_4Ze5VctZELLBKNdWcruR3VpJQdceY0SU4omdcIKIGPHCQA4CAUKgfWo=
BAAk1CdABru4o7xIVJjQV9by7UbP3d46vBUyITqtxzokpIbbNo6PNmy1xao1t5evX2j2OfU-uyp=
wxN72qkUHZXVpc34qP97qOjo7TUFU4fjQxRC4p2Ay61g08YKWZ89xXZzKMSCgKA4q749tIp5Bpz=
Fwpr-4Rt9-v61w_Ev_K7xTwAAAP__5le0ag ) - I'll
use monkfruit sweetener & gluten-free Tamari
* Crustless Chicken Pot Pie=20
( https://email.e.kajabimail.net/c/eJxskN2u1CAUhZ-m3Jg2m11o6QUXGp3Eax-gYWA7=
g4cCAj3JeXvT-UmMziXfWizCZ3Jeo9lIv5lf5uz72lKhnyXFVvtckttt8ykyp0E4N3NGms-jwmW=
ZABltxofVUfDvVD5W7zSqhUvJxSynR3pALsWkRiGebKNazYXW9pFJ39G5JOOsqe1RKVTTXiy9vF=
_p907xHj7Rfr6tfTtOX_4Ze5VctZELLBKNdWcruR3VpJQdceY0SU4omdcIKIGPHCQA4CAUKgfWo=
BAAk1CdABru4o7xIVJjQV9by7UbP3d46vBUyITqtxzokpIbbNo6PNmy1xao1t5evX2j2OfU-uyp=
wxN72qkUHZXVpc34qP97qOjo7TUFU4fjQxRC4p2Ay61g08YKWZ89xXZzKMSCgKA4q749tIp5Bpz=
Fwpr-4Rt9-v61w_Ev_K7xTwAAAP__5le0ag )
* Sundried Tomato Tahinin Pasta=20
( https://email.e.kajabimail.net/c/eJxskMGOmzAQhp8GLhVobAYwBx9atSv13AdAE3uy=
uAWb2pNd5e2rkESq2j36-3__lj_a9znSxvYX_aRTaIqkzOecopRmz8lfnIQUa28BvR9VzVaNndH=
TNICueaOwzp7X8Mb5OgdvtZlU3ysc--GR3qDqcTAd4pNtXAq98izXne0dnXIi76jIo5K5pEt2_O=
H9wr8vHO_hE11Ox9q32-nLP2MfJYtVbiScDHVnxajGsZtO6J0ZenDT-QyuDlaD7kF1CnoA0C0ab=
Tw40ogAA5oKgdu7uNt4G1nq1S4ie6m6z5V-qfQLk7wHWdxKOci1dWmr9IvQEmJodipCR6173_PW=
ZHZh58alKBQi50ZNymD91FU4es6zTxuFaP97OdsY3JJWKu3th7yuSVUIr0fBpa0-5gNHOaQiTho=
0GFWXIA_POI6gR5xqsT-C8KfvXyvd_YXfrP4TAAD__zg2ufA )
- I'll use lentil penne

For snacking this week, I'm munching on:

* Dairy-free Dill Pickle Dip with veggies=20
( https://email.e.kajabimail.net/c/eJxskM2u2yAQhZ_G3lSxhvFg4wWLVm2krvsAFobJ=
DQ0GF8iV8vaV8yNVvXcH3xkOms9s2xzNyvpifpvFH0pNmU85xVoOW07uaqtPsXUayLlRtKzF2Cu=
cpgGw5dX4MDsO_p3zbfZOo5qElIJGOTzTHQpJg-qJXmzlUswbz_W2sX6gJSfjrCn1OZK5pGu2_O=
n7wn-uHB_hC12Xe9uP_fbtv7LPkrM-SQSSrGiYjMNlkKTcInCcFsFWErReI6AE0QuQAIAdKVQOr=
EEigIFUQ8DdQ9xe3kWubdDnWrfS9F8bPDZ4jLdSTLn4as8cO5vWBo_O-Hw7nDLzwfkQDpu3l7Cf=
twaP7ctO4eg4zy6txkf94aOso7fnFEzp9oU4hCQagrf7gE1rm9n6zXOsd4dEEwKCEm3x9amVxhF=
wpKmt-pev_OXn9wb7f_C7xr8BAAD__6fTtA4 )

For dessert this week, I'm making:

* Almond Flour Chocolate Chip Cookies=20
( https://email.e.kajabimail.net/c/eJxskEuu1DAQRVeTTFBa5YrzG3gAgpYYs4CoYlc6=
5iWuYDst3u5R_yQEb-hzr6_lQ_s-BtrYvNFPmnyVskSeo4Scqj2KO2z2EkpnQDvXqZKN6uoeh6E=
FLHkjv46OV3_l-D56Z7AfVNMo3TXtM71B1ei2r7V-sY1ToguP-X1n80BTFHKWUn5WIic5ouUP7y=
f-dXB4hC90TPe1b7fTl3_GPkoW00E7aTU1PQ4TzTPxAI0bFM8danJgS28QsAFVK2gAAE-6x96BJ=
dQaoNV9oYFPD3G38VPgXK5myXlPRf25wHOBZ8dZfvvgU6aTla3A85UvFCpaNwmumlc5YmUXsbJS=
5soufq-syJvnVOC5fKlKHBzH0clGPpj_Xo0meLvISul0-x2vq6hCw-VesLKVka3fPYd8F6r1gID=
QqzL5_HSsuw6w00OZzQ-f-dP3rwXWf-GrwT8BAAD__1FFuf4 )


In good health,

Lisa xx"""

meal_plan = LinkExtractor.extract_links(email_text)

for title, url in meal_plan["Breakfast"].items():
    print(f"Title: {title}\n")
    print(f"URL: {url}\n")
    try:
        recipe = Scraper.scrape(url)
        print(f"Successfully scraped recipe!")
        print(f"Ingredients: {recipe.ingredients}")
        print(f"help.(recipe): {help(recipe)}")
    except Exception as e:
        print(f"Failed to scrape site {e.message}")
        continue
