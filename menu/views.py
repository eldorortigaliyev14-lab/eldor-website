from django.shortcuts import render


MENU_SECTIONS = (
    ("taom", "Taomlar", (
        ("Cheeseburger", 35000, "Mol go‘shti, cheddar pishlog‘i va maxsus sous", "photo-1568901346375-23c9450c58cd"),
        ("Pepperoni pizza", 65000, "Mozzarella va achchiq pepperoni", "photo-1513104890138-7c749659a591"),
        ("Tovuqli lavash", 32000, "Shirali tovuq, sabzavot va sarimsoqli sous", "photo-1555939594-58d7cb561ad1"),
        ("Grill burger", 42000, "Grilda pishgan go‘sht, piyoz va pishloq", "photo-1550547660-d9450f859349"),
        ("Margarita pizza", 58000, "Pomidor, rayhon va mozzarella", "photo-1574071318508-1cdbab80d002"),
        ("Tovuqli pasta", 48000, "Qaymoqli sous, tovuq filesi va parmesan", "photo-1473093295043-cdd812d0e601"),
        ("Sezar salati", 39000, "Tovuq, parmesan, ko‘kat va kruton", "photo-1546069901-ba9599a7e63c"),
        ("Mol go‘shtli steyk", 89000, "Yumshoq steyk va gril sabzavotlari", "photo-1558030006-450675393462"),
        ("Klub sendvich", 36000, "Tovuq, pishloq va yangi sabzavotlar", "photo-1528735602780-2552fd46c7af"),
        ("Qo‘ziqorinli pizza", 69000, "Qo‘ziqorin, mozzarella va qaymoqli sous", "photo-1571407970349-bc81e7e96d47"),
        ("Tovuqli ramen", 52000, "Issiq bulyon, ramen ugra va tovuq", "photo-1569718212165-3a8278d5f624"),
        ("Gril qanotlar", 44000, "Achchiq-shirin sousdagi qarsildoq qanotlar", "photo-1527477396000-e27163b481c2"),
        ("Avokadoli bowl", 46000, "Avokado, guruch, ko‘kat va kunjut", "photo-1512621776951-a57141f2eefd"),
    )),
    ("milliy", "Milliy taomlar", (
        ("Osh", 38000, "An’anaviy palov, no‘xat va mayiz bilan", "photo-1512621776951-a57141f2eefd"),
        ("Mol go‘shtli manti", 42000, "Qo‘lda tugilgan, bug‘da pishgan manti", "photo-1547592180-85f173990554"),
        ("Lag‘mon", 39000, "Cho‘zma ugra, go‘sht va sabzavotlar", "photo-1569718212165-3a8278d5f624"),
        ("Shashlik", 55000, "Ko‘mirda pishgan go‘sht va piyoz", "photo-1555939594-58d7cb561ad1"),
        ("Qozon kabob", 62000, "Qozonda qovurilgan go‘sht va kartoshka", "photo-1544025162-d76694265947"),
        ("Chuchvara", 34000, "Uy usulida tugilgan go‘shtli chuchvara", "photo-1551326844-4df70f78d0e9"),
        ("Norin", 40000, "Yupqa ugra, mayin go‘sht va ziravorlar", "photo-1547592180-85f173990554"),
        ("Mastava", 31000, "Guruchli, to‘yimli uy sho‘rvasi", "photo-1547592180-85f173990554"),
        ("Tandir go‘sht", 72000, "Tandirda sekin pishgan shirali go‘sht", "photo-1544025162-d76694265947"),
        ("Dimlama", 37000, "Go‘sht va mavsumiy sabzavotlar dimlamasi", "photo-1547592180-85f173990554"),
        ("Qiyma kabob", 49000, "Ko‘mirda pishgan ziravorli qiyma kabob", "photo-1555939594-58d7cb561ad1"),
        ("Tovuqli sho‘rva", 30000, "Tovuq va sabzavotlardan tiniq sho‘rva", "photo-1547592180-85f173990554"),
        ("Go‘shtli somsa", 12000, "Tandirda pishgan shirali go‘shtli somsa", "photo-1601050690597-df0568f70950"),
    )),
    ("desert", "Desertlar", (
        ("Shokoladli tort", 28000, "Yumshoq biskvit va shokolad kremi", "photo-1578985545062-69928b1d9587"),
        ("Tiramisu", 32000, "Qahvali biskvit va mascarpone kremi", "photo-1571877227200-a0d98ea607e9"),
        ("Asalli tort", 26000, "Mayin qatlamlar va asal kremi", "photo-1606313564200-e75d5e30476c"),
        ("Cheesecake", 30000, "Pishloqli krem va rezavor meva sousi", "photo-1533134242443-d4fd215305ad"),
        ("Kruassan", 18000, "Sariyog‘li, qat-qat fransuz kruassani", "photo-1555507036-ab1f4038808a"),
        ("Shokoladli fondan", 29000, "Iliq pirojniy, ichida erigan shokolad", "photo-1606313564200-e75d5e30476c"),
        ("Pankeyk", 24000, "Yumshoq pankeyk, asal va rezavorlar bilan", "photo-1528207776546-365bb710ee93"),
        ("Mevali tart", 27000, "Qarsildoq asos, krem va yangi mevalar", "photo-1488477181946-6428a0291777"),
        ("Muzqaymoq", 16000, "Uch xil ta’mli qaymoqli muzqaymoq", "photo-1563805042-7684c019e1cb"),
        ("Brauni", 22000, "Yong‘oqli va shokoladga boy brauni", "photo-1606313564200-e75d5e30476c"),
        ("Ekler", 19000, "Vanilli krem solingan yengil ekler", "photo-1551024506-0bccd828d307"),
        ("Mevali salat", 25000, "Mavsumiy mevalar va yengil yogurt kremi", "photo-1490474418585-ba9bad8fd0ea"),
        ("Krem-brule", 23000, "Usti karamellangan vanilli desert", "photo-1470324161839-ce2bb6fa6bc3"),
    )),
    ("ichimlik", "Ichimliklar", (
        ("Limonad", 18000, "Limon, yalpiz va muzli gazlangan ichimlik", "photo-1513558161293-cdaf765edfd4"),
        ("Muzli qahva", 22000, "Espresso, sut va muz bilan tayyorlangan", "photo-1517701550927-30cf4ba1dba5"),
        ("Apelsin sharbati", 20000, "Yangi siqilgan tabiiy apelsin sharbati", "photo-1600271886742-f049cd451bba"),
        ("Qulupnayli smuzi", 24000, "Qulupnay va yogurtli quyuq smuzi", "photo-1505252585461-04db1eb84625"),
        ("Kapuçino", 19000, "Espresso va ko‘pirtirilgan sut", "photo-1534778101976-62847782c213"),
        ("Moxito", 22000, "Yalpiz, laym va muz bilan tetiklantiruvchi", "photo-1551538827-9c037cb4f32a"),
        ("Mango sharbati", 21000, "Shirin mango mevasidan tayyorlangan", "photo-1600271886742-f049cd451bba"),
        ("Kakao", 18000, "Issiq sutli kakao va qaymoq", "photo-1542990253-0b8be8e9dc4a"),
        ("Yashil choy", 12000, "Xushbo‘y, yangi damlangan ko‘k choy", "photo-1544787219-7f47ccb76574"),
        ("Vanilli milkshake", 23000, "Muzqaymoq va sutdan quyuq kokteyl", "photo-1572490122747-3968b75cc699"),
        ("Sovuq choy", 16000, "Shaftoli ta’mli muzdek qora choy", "photo-1556679343-c7306c1976bc"),
        ("Mineral suv", 8000, "Tabiiy buloq suvi, gazli yoki gazsiz", "photo-1523362628745-0c100150b504"),
        ("Latte", 21000, "Espresso va ko‘pirtirilgan sut uyg‘unligi", "photo-1461023058943-07fcbe16d735"),
    )),
)


def home(request):
    products = [
        {
            "name": name,
            "price": price,
            "formatted_price": f"{price:,}".replace(",", " "),
            "description": description,
            "category": category,
            "category_name": category_name,
            "image": f"https://images.unsplash.com/{photo}?auto=format&fit=crop&w=800&q=85",
        }
        for category, category_name, items in MENU_SECTIONS
        for name, price, description, photo in items
    ]
    return render(request, "menu/index.html", {"products": products})