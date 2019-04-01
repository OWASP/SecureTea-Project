# [![OWASP Logo](https://github.com/OWASP/Amass/blob/master/images/owasp_logo.png) OWASP SECURETEA TOOL PROJECT](https://www.owasp.org/index.php/OWASP_SecureTea_Project)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7e1de11511084c06bbe25ed4d629e7fd)](https://app.codacy.com/app/rejahrehim/SecureTea-Project?utm_source=github.com&utm_medium=referral&utm_content=OWASP/SecureTea-Project&utm_campaign=Badge_Grade_Settings)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://www.owasp.org/index.php/OWASP_SecureTea_Project) [![Telegram](https://img.shields.io/badge/chat%20on-telegram-blue.svg)](https://t.me/joinchat/Az5yZxQg7Djs-UZWKKCRVQ) ![Version](https://img.shields.io/badge/version-1.1-orange.svg) ![GitHub issues](https://img.shields.io/github/issues/OWASP/SecureTea-Project.svg) ![GitHub pull requests](https://img.shields.io/github/issues-pr/OWASP/SecureTea-Project.svg) ![GSOC 2019](https://img.shields.io/static/v1.svg?label=GSOC&message=Google%20Summer%20of%20Code%202019&color=blue&logo=%20data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAABLFJREFUSA2tVV1sVFUQ/s45d7ulpT+63VSkQC1IIsHyAugDAWLwQSEQI/EnaGL0QWOQ6AMo+uAzJooJJJiIiQ8qkWDURIxGIlLUqEQTKz9REEpbMFhKt7ss7e49P35zb9jaqKEkTnL33jNn5ps538ycBa5D7MH8etuTX38dLlM3jQ+2rXRf1Q/LI99T9VRTMYy/rF+hUflAIeTEPkANe2Tvz9w1fuha/pMChE/RbDNRd83JWnigwzTO2Gma5+ec6eCWgnEDcMXfhl35j43cH4yiqOYSxbZX3YviVcXEDjVWR4tMRvUEegUXQzfNRtT1PJBbw7WFjocTv5DJwZgoZy7t3+N/34YwdhbKZKA0MO6i5UQ6/K8BYBC8gNsYKr8a6rZdCJePwx97EmH0e+rTxFTUDNW8FHrOs9CLD8OdeBp+6BOoKAPBuAou70knSDaYucrfA73wXbhTW+EHdqX2ypCdlNHgigjDn8Pz0R1PwSx8B+7oBuDi/n9ATgoQW+vqp8+EWrCb4C/B9xPciMnfSuVjLhlMM1sm6/vfSNZmwZvwR5YilAZdmlH6S9YmxFjMVl2bEcon08wTcO4LqEhwMHNfhm65E+BJE2GB/SCpLP8K3bUFgpFupL+1AGNfTF8ZtbbtQNt9zOo17iaV5ltDz3iErzpyTO7bH6KOBZ/xYHoSBmXl4M++ymZYh6g1v0OwaJRIEiBwcOrMlX26cV4+eAU/+l2yqTJtiLr3Qd1EMDsONNzKzMvwpaPUbYC5fS9AG5FQZBMwJ8EQLMEUvbaH2tZ6lD4kbM7pmwl0CagOQzXOh1ncg1D9E66XWTNT1byELXmaNmW4Xx6m3RAi2ohtqNLPjsCZmTyzzwmmPdS+VhvYQmBp0gaRDmNBZSG829GUFtPAAFS33AEUf0i/RUfK6E7bqiRLkWYQQ/kOJYNKQasVhR7nMmt8QJ/xA3S6EUJNGDsD++MqHvsKqXiPgaZBNTDT4hGeO6JuT0KX/elu2vZB1eUTX8EQLEtMwU5qkF1V7rUe6/zlU6eV5hzcsDxJBH4M7tjjaQEbyT8n2JdPEKiOjbAd7vgTDDKWJt26jJPMq6V08rRgCaaco9ZF2VXoDcXCJlzYwwndzP5nnwtVnH8/9JkcGf7cbiAm16TED3Go5G4QG86E7qQPfePiyCbBEnCRWgBZhAxG/JnXSRHvms4XmJ0VbRIsuTL6XuFaCE5Bkz25o27ZklDkz2yHJwYNajJpksmtDvEQaXkUZtFHiZHr28ZALKJmLuQ+AZV+5KWlDGdj7laY2c/B/byOpxvioSIaSmKpTA5AnSY1vvANPB30greg82vg+ncgFA4nbZm4ZdugWpcT+BnWowW+l+CFr9PLzkonTsjkAKSbHTDuFfkf+ZZ3yzLoWRvrzLwXdVDSkqW0EU0T3yX48+97P7CzGqoXmTl9iB2IMQGfElpbh72YhvZsR6VCVZYPP0wFM9X0prdNU+ccpziIpN+E8/zD6TsbLpcec1mcE2Mxl5/BC5XBWQ+ArZWKVOyaUjlQ1x3p+GOtQqcY+6D6rM+wFau1bvkvkCkFEOfKgcbuyMTsTTLlMquv9rms/zepHmheIs/1AP4F9DYB6+AcwCcAAAAASUVORK5CYII=)

**The OWASP SecureTea** प्रोजेक्ट एक ऐसा एप्लिकेशन है जो किसी व्यक्ति के लैपटॉप या कंप्यूटर / सर्वर को IoT (इंटरनेट ऑफ थिंग्स) और उपयोगकर्ताओं को सूचित करने में मदद करने के लिए डिज़ाइन किया गया है (विभिन्न संचार तंत्र के माध्यम से), जब भी कोई अपने कंप्यूटर / सर्वर का उपयोग करता है। यह एप्लिकेशन गतिविधि निर्धारित करने के लिए टचपैड / माउस / वायरलेस माउस का उपयोग करता है और इसे पायथन में विकसित किया गया है और विभिन्न मशीनों (लिनक्स, मैक और विंडोज) पर परीक्षण किया गया है।<br>
सॉफ्टवेयर अभी भी विकास के अधीन है। अंतत: इसके पास स्वयं की आईडीएस (घुसपैठ का पता लगाने वाली प्रणाली) / आईपीएस (इंस्ट्रक्शन प्रिवेंशन सिस्टम), फ़ायरवॉल, एंटी-वायरस, वेब डिसेप्शन डिटेक्शन के साथ बुद्धिमान लॉग मॉनिटरिंग क्षमताएं और बहुत अधिक संचार माध्यमों का समर्थन होगा।

![](/img/setup_all.gif)<br>

## सूची
*   [उपयोगकर्ता](#उपयोगकर्ता)
*   [लक्ष्य](#लक्ष्य)
*   [स्थापना प्रक्रिया](#स्थापना-प्रक्रिया)
*   [सुझाव और योगदान](#सुझाव-और-योगदान)
*   [आचार संहिता](https://github.com/OWASP/SecureTea-Project/blob/master/CODE_OF_CONDUCT.md)
*   [समूह बातचीत](#समूह-बातचीत)
*   [उपयोगकर्ता गाइड](/doc/en-US/user_guide.md)
*   [डेवलपर गाइड](/doc/en-US/dev_guide.md)
*   [जापानी में अनुवाद / 日本語の翻訳 ](/doc/ja-JP/README.md)
*   [अंग्रेज़ी अनुवाद / Translation in English ](README.md)

## उपयोगकर्ता

यह उन लोगों द्वारा उपयोग किए जाने के लिए लिखा गया था जो IoT Security (इंटरनेट ऑफ थिंग्स) में रुचि रखते हैं। इसे अभी और विकास की जरूरत है।

## यह कैसे कार्य करता है।

*   माउस / टचपैड की गति पर नज़र रखें।
*   पता लगाएँ कि माउस / टचपैड के साथ लैपटॉप का उपयोग कौन स्थापित करता है।
*   ट्विटर / एसएमएस / स्लैक / टेलीग्राम पर चेतावनी संदेश भेजें।

## लक्ष्य

*   जब भी कंप्यूटर / सर्वर को किसी व्यक्ति / हमलावर द्वारा एक्सेस किया जा रहा हो, तो उपयोगकर्ता को संचार संचार तंत्र के माध्यम से सचेत करने के लिए।
*   इसका उपयोग रक्षा के रूप में आपके सिस्टम और सिक्योरटी फायरवाल की निगरानी के लिए किया जा सकता है।

## स्थापना प्रक्रिया

### उपयोगकर्ता गाइड

इस पर अधिक देखें।[User Guide](/doc/en-US/user_guide.md)

### डेवलपर गाइड

इस पर अधिक देखें।[Developer guide](/doc/en-US/dev_guide.md)

## [सुझाव और योगदान](https://github.com/OWASP/SecureTea-Project/blob/master/CONTRIBUTING.md)

योगदानकर्ताओं के लिए-कृपया अपना नाम नीचे जोड़ें।
*   [Ade Yoseman](https://www.owasp.org/index.php/Ade_Yoseman_Putra)
*   [Bambang Kurniawan](https://www.owasp.org/index.php/User:Idbmb)
*   [Lojislav Bezimenov](https://github.com/lojikil/)
*   [Rejah Rehim](https://rejahrehim.com)
*   [Ananthu S](https://github.com/sananthu)

## समूह बातचीत

[![Telegram](https://github.com/OWASP/SecureTea-Project/blob/master/img/telegram.png "Telegram")](https://t.me/joinchat/Az5yZxQg7Djs-UZWKKCRVQ)

## गूगल समर ऑफ़ कोड
[![Google Summer of Code](https://betanews.com/wp-content/uploads/2016/03/vertical-GSoC-logo.jpg)](https://summerofcode.withgoogle.com/organizations/6362925392986112/)
