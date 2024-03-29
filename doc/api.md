# Qutrub Web API

يمكن إستعمال موقع قطرب كواجهة برمجية API، والحصول على نتية بصيغة json
يسمح الموقع باستقبال الطلبات عبر الرابط
http://qutrub.arabeyes.org/api/

## طرائق الاستعلام
يمكن استدعاء التصريف بالطريقة GET
على سبيل المثال:
```
http://qutrub.arabeyes.org/api?verb=كتب&haraka=u&trans=1

http://qutrub.arabeyes.org/api?verb=استعمل
```
المعلمات:
* الفعل verb
* الحركة haraka ويأخذ حرفا لاتينيا a فتحة،u ضمة،i كسرة.
* التعدي : ويأخذ قيمة منطقية رقمية: 0 للازم، 1 للمتعدي


في المثال الأول نريد تصريف الفعل "كتب"، ونريد بالضبط الفعل "كتب يكتُب" بالضمة عند تصريفه في المضارع،
في المثال الثاني، نريدتصريف الفعل "استعمل" ولسنا بحاجة إلى تحديد حركة عين الفعل في المضارع
الحركة تأخذ القيم الآتية، حرف لاتيني:
-  فتحة:a
-  ضمة : u
-  كسرة : i

أما الفعل: يمكنه استقبال أي فعل عربي، ويستحسن أن يكون مشكولا. لتقليل الالتباس
## شكل النتائج
تسترجع النتائج في شكل بيانات جيسون JSON
```
{
"verb_info":"",
"result": { {},},
 "suggest":[{}]
 }  
                  
```
-  verb_info تعريف الفعل ومعلوماته
-  result: 
- تصريف الأفعال مع الضمائر والأزمنة

تصريف الأفعال مع الضمائر
السطر الأول يحوي على الأزمنة،
الأسطر الموالية فيها : الضمير في أول عمود،
ثم تصريف كل فعل حسب الزمن المذكور في السطر الأول.
```json
{
    "result": {
        "0": {
            "0": "الضمائر",
            "1": "الماضي المعلوم",
            "2": "المضارع المعلوم",
            "3": "المضارع المجزوم",
            "4": "المضارع المنصوب",
            "5": "المضارع المؤكد الثقيل",
            "6": "الأمر",
            "7": "الأمر المؤكد",
            "8": "الماضي المجهول",
            "9": "المضارع المجهول",
            "10": "المضارع المجهول المجزوم",
            "11": "المضارع المجهول المنصوب",
            "12": "المضارع المؤكد الثقيل المجهول "
        },
        "1": {
            "0": "أنا",
            "1": "كَتَبْتُ",
            "2": "أَكْتُبُ",
            "3": "أَكْتُبْ",
            "4": "أَكْتُبَ",
            "5": "أَكْتُبَنَّ",
            "6": "",
            "7": "",
            "8": "كُتِبْتُ",
            "9": "أُكْتَبُ",
            "10": "أُكْتَبْ",
            "11": "أُكْتَبَ",
            "12": "أُكْتَبَنَّ"
        },
        "2": {
            "0": "نحن",
            "1": "كَتَبْنَا",
            "2": "نَكْتُبُ",
            "3": "نَكْتُبْ",
            "4": "نَكْتُبَ",
            "5": "نَكْتُبَنَّ",
            "6": "",
            "7": "",
            "8": "كُتِبْنَا",
            "9": "نُكْتَبُ",
            "10": "نُكْتَبْ",
            "11": "نُكْتَبَ",
            "12": "نُكْتَبَنَّ"
        },
    },

}
```

- suggest: اقتراحات أفعال مشابهة
- قائمة بمقترحات الأفعال من الشكل
```
 {
 'verb': 'كَتَّبَ', 
 'haraka': 'فتحة',
 'future': 'يُكَتِّبُ'
 'transitive': true,
}
```
- الفعل Verb
- حركة عين المضارع للفعل الثلاثي، تساوي تلقائيا فتحة، ولا معنى لها مع الفعل غير الثلاثي
- صيغة الفعل في المضارع
- متعدي true، لازم false

** مثال **
```json
{"suggest": [
        {
            "transitive": true,
            "haraka": "ضمة",
            "verb": "كَتَبَ",
            "future": "يَكْتُبُ"
        },
        {
            "transitive": true,
            "haraka": "كسرة",
            "verb": "كَتَبَ",
            "future": "يَكْتِبُ"
        },
 
    ]
}
```

- 
- 
 verb_info -  تعريف الفعل ومعلوماته

مثال
```
'verb_info': '"الفعل \n        كَتَبَ - يَكْتُبُ فعل ثلاثي متعدي صحيح سالم [في قاعدة البيانات]'
```
توضح نوع الفعل
- ثلاثي أو رباعي أو خماسي
- متعدي أو لازم
- صحيح/ معتل
- نوع العلة
- موجود في قاعدة البيانات أو غير موجود

**ملاحظة :** يمكن لقطرب تصريف أي فعل عربي غير موجود في قاعدة البيانات.
**مثال كامل**

```json
{
    "verb_info": "الفعل كَتَبَ - يَكْتُبُ فعل ثلاثي متعدي صحيح سالم [في قاعدة البيانات]",
    "result": {
        "0": {
            "0": "الضمائر",
            "1": "الماضي المعلوم",
            "2": "المضارع المعلوم",
            "3": "المضارع المجزوم",
            "4": "المضارع المنصوب",
            "5": "المضارع المؤكد الثقيل",
            "6": "الأمر",
            "7": "الأمر المؤكد",
            "8": "الماضي المجهول",
            "9": "المضارع المجهول",
            "10": "المضارع المجهول المجزوم",
            "11": "المضارع المجهول المنصوب",
            "12": "المضارع المؤكد الثقيل المجهول "
        },
        "1": {
            "0": "أنا",
            "1": "كَتَبْتُ",
            "2": "أَكْتُبُ",
            "3": "أَكْتُبْ",
            "4": "أَكْتُبَ",
            "5": "أَكْتُبَنَّ",
            "6": "",
            "7": "",
            "8": "كُتِبْتُ",
            "9": "أُكْتَبُ",
            "10": "أُكْتَبْ",
            "11": "أُكْتَبَ",
            "12": "أُكْتَبَنَّ"
        },
        "2": {
            "0": "نحن",
            "1": "كَتَبْنَا",
            "2": "نَكْتُبُ",
            "3": "نَكْتُبْ",
            "4": "نَكْتُبَ",
            "5": "نَكْتُبَنَّ",
            "6": "",
            "7": "",
            "8": "كُتِبْنَا",
            "9": "نُكْتَبُ",
            "10": "نُكْتَبْ",
            "11": "نُكْتَبَ",
            "12": "نُكْتَبَنَّ"
        },
        "3": {
            "0": "أنت",
            "1": "كَتَبْتَ",
            "2": "تَكْتُبُ",
            "3": "تَكْتُبْ",
            "4": "تَكْتُبَ",
            "5": "تَكْتُبَنَّ",
            "6": "اُكْتُبْ",
            "7": "اُكْتُبَنَّ",
            "8": "كُتِبْتَ",
            "9": "تُكْتَبُ",
            "10": "تُكْتَبْ",
            "11": "تُكْتَبَ",
            "12": "تُكْتَبَنَّ"
        },
        "4": {
            "0": "أنتِ",
            "1": "كَتَبْتِ",
            "2": "تَكْتُبِينَ",
            "3": "تَكْتُبِي",
            "4": "تَكْتُبِي",
            "5": "تَكْتُبِنَّ",
            "6": "اُكْتُبِي",
            "7": "اُكْتُبِنَّ",
            "8": "كُتِبْتِ",
            "9": "تُكْتَبِينَ",
            "10": "تُكْتَبِي",
            "11": "تُكْتَبِي",
            "12": "تُكْتَبِنَّ"
        },
        "5": {
            "0": "أنتما",
            "1": "كَتَبْتُمَا",
            "2": "تَكْتُبَانِ",
            "3": "تَكْتُبَا",
            "4": "تَكْتُبَا",
            "5": "تَكْتُبَانِّ",
            "6": "اُكْتُبَا",
            "7": "اُكْتُبَانِّ",
            "8": "كُتِبْتُمَا",
            "9": "تُكْتَبَانِ",
            "10": "تُكْتَبَا",
            "11": "تُكْتَبَا",
            "12": "تُكْتَبَانِّ"
        },
        "6": {
            "0": "أنتما مؤ",
            "1": "كَتَبْتُمَا",
            "2": "تَكْتُبَانِ",
            "3": "تَكْتُبَا",
            "4": "تَكْتُبَا",
            "5": "تَكْتُبَانِّ",
            "6": "اُكْتُبَا",
            "7": "اُكْتُبَانِّ",
            "8": "كُتِبْتُمَا",
            "9": "تُكْتَبَانِ",
            "10": "تُكْتَبَا",
            "11": "تُكْتَبَا",
            "12": "تُكْتَبَانِّ"
        },
        "7": {
            "0": "أنتم",
            "1": "كَتَبْتُم",
            "2": "تَكْتُبُونَ",
            "3": "تَكْتُبُوا",
            "4": "تَكْتُبُوا",
            "5": "تَكْتُبُنَّ",
            "6": "اُكْتُبُوا",
            "7": "اُكْتُبُنَّ",
            "8": "كُتِبْتُم",
            "9": "تُكْتَبُونَ",
            "10": "تُكْتَبُوا",
            "11": "تُكْتَبُوا",
            "12": "تُكْتَبُنَّ"
        },
        "8": {
            "0": "أنتن",
            "1": "كَتَبْتُنَّ",
            "2": "تَكْتُبْنَ",
            "3": "تَكْتُبْنَ",
            "4": "تَكْتُبْنَ",
            "5": "تَكْتُبْنَانِّ",
            "6": "اُكْتُبْنَ",
            "7": "اُكْتُبْنَانِّ",
            "8": "كُتِبْتُنَّ",
            "9": "تُكْتَبْنَ",
            "10": "تُكْتَبْنَ",
            "11": "تُكْتَبْنَ",
            "12": "تُكْتَبْنَانِّ"
        },
        "9": {
            "0": "هو",
            "1": "كَتَبَ",
            "2": "يَكْتُبُ",
            "3": "يَكْتُبْ",
            "4": "يَكْتُبَ",
            "5": "يَكْتُبَنَّ",
            "6": "",
            "7": "",
            "8": "كُتِبَ",
            "9": "يُكْتَبُ",
            "10": "يُكْتَبْ",
            "11": "يُكْتَبَ",
            "12": "يُكْتَبَنَّ"
        },
        "10": {
            "0": "هي",
            "1": "كَتَبَتْ",
            "2": "تَكْتُبُ",
            "3": "تَكْتُبْ",
            "4": "تَكْتُبَ",
            "5": "تَكْتُبَنَّ",
            "6": "",
            "7": "",
            "8": "كُتِبَتْ",
            "9": "تُكْتَبُ",
            "10": "تُكْتَبْ",
            "11": "تُكْتَبَ",
            "12": "تُكْتَبَنَّ"
        },
        "11": {
            "0": "هما",
            "1": "كَتَبَا",
            "2": "يَكْتُبَانِ",
            "3": "يَكْتُبَا",
            "4": "يَكْتُبَا",
            "5": "يَكْتُبَانِّ",
            "6": "",
            "7": "",
            "8": "كُتِبَا",
            "9": "يُكْتَبَانِ",
            "10": "يُكْتَبَا",
            "11": "يُكْتَبَا",
            "12": "يُكْتَبَانِّ"
        },
        "12": {
            "0": "هما مؤ",
            "1": "كَتَبَتَا",
            "2": "تَكْتُبَانِ",
            "3": "تَكْتُبَا",
            "4": "تَكْتُبَا",
            "5": "تَكْتُبَانِّ",
            "6": "",
            "7": "",
            "8": "كُتِبَتَا",
            "9": "تُكْتَبَانِ",
            "10": "تُكْتَبَا",
            "11": "تُكْتَبَا",
            "12": "تُكْتَبَانِّ"
        },
        "13": {
            "0": "هم",
            "1": "كَتَبُوا",
            "2": "يَكْتُبُونَ",
            "3": "يَكْتُبُوا",
            "4": "يَكْتُبُوا",
            "5": "يَكْتُبُنَّ",
            "6": "",
            "7": "",
            "8": "كُتِبُوا",
            "9": "يُكْتَبُونَ",
            "10": "يُكْتَبُوا",
            "11": "يُكْتَبُوا",
            "12": "يُكْتَبُنَّ"
        },
        "14": {
            "0": "هن",
            "1": "كَتَبْنَ",
            "2": "يَكْتُبْنَ",
            "3": "يَكْتُبْنَ",
            "4": "يَكْتُبْنَ",
            "5": "يَكْتُبْنَانِّ",
            "6": "",
            "7": "",
            "8": "كُتِبْنَ",
            "9": "يُكْتَبْنَ",
            "10": "يُكْتَبْنَ",
            "11": "يُكْتَبْنَ",
            "12": "يُكْتَبْنَانِّ"
        }
    },
    "suggest": [
        {
            "transitive": true,
            "haraka": "ضمة",
            "verb": "كَتَبَ",
            "future": "يَكْتُبُ"
        },
        {
            "transitive": true,
            "haraka": "كسرة",
            "verb": "كَتَبَ",
            "future": "يَكْتِبُ"
        },
        {
            "transitive": true,
            "haraka": "فتحة",
            "verb": "كَتَبَ",
            "future": "يَكْتَبُ"
        },
        {
            "transitive": false,
            "haraka": "فتحة",
            "verb": "اِكْتَأَبَ",
            "future": "يَكْتَئِبُ"
        },
        {
            "transitive": false,
            "haraka": "فتحة",
            "verb": "اِكْتَبَى",
            "future": "يَكْتَبِي"
        },
        {
            "transitive": true,
            "haraka": "فتحة",
            "verb": "كَتَّبَ",
            "future": "يُكَتِّبُ"
        },
        {
            "transitive": true,
            "haraka": "فتحة",
            "verb": "كاتَبَ",
            "future": "يُكَاتِبُ"
        },
        {
            "transitive": true,
            "haraka": "فتحة",
            "verb": "أَكْتَبَ",
            "future": "يُكْتِبُ"
        }
    ]
}
```

