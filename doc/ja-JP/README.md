# [![OWASP Logo](https://github.com/OWASP/Amass/blob/master/images/owasp_logo.png) OWASP SECURETEA TOOL PROJECT](https://www.owasp.org/index.php/OWASP_SecureTea_Project)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7e1de11511084c06bbe25ed4d629e7fd)](https://app.codacy.com/app/rejahrehim/SecureTea-Project?utm_source=github.com&utm_medium=referral&utm_content=OWASP/SecureTea-Project&utm_campaign=Badge_Grade_Settings)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://www.owasp.org/index.php/OWASP_SecureTea_Project) [![Telegram](https://img.shields.io/badge/chat%20on-telegram-blue.svg)](https://t.me/joinchat/Az5yZxQg7Djs-UZWKKCRVQ) ![Version](https://img.shields.io/badge/version-1.1-orange.svg) ![GitHub issues](https://img.shields.io/github/issues/OWASP/SecureTea-Project.svg) ![GitHub pull requests](https://img.shields.io/github/issues-pr/OWASP/SecureTea-Project.svg) ![GSOC 2019](https://img.shields.io/static/v1.svg?label=GSOC&message=Google%20Summer%20of%20Code%202019&color=blue&logo=%20data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAABLFJREFUSA2tVV1sVFUQ/s45d7ulpT+63VSkQC1IIsHyAugDAWLwQSEQI/EnaGL0QWOQ6AMo+uAzJooJJJiIiQ8qkWDURIxGIlLUqEQTKz9REEpbMFhKt7ss7e49P35zb9jaqKEkTnL33jNn5ps538ycBa5D7MH8etuTX38dLlM3jQ+2rXRf1Q/LI99T9VRTMYy/rF+hUflAIeTEPkANe2Tvz9w1fuha/pMChE/RbDNRd83JWnigwzTO2Gma5+ec6eCWgnEDcMXfhl35j43cH4yiqOYSxbZX3YviVcXEDjVWR4tMRvUEegUXQzfNRtT1PJBbw7WFjocTv5DJwZgoZy7t3+N/34YwdhbKZKA0MO6i5UQ6/K8BYBC8gNsYKr8a6rZdCJePwx97EmH0e+rTxFTUDNW8FHrOs9CLD8OdeBp+6BOoKAPBuAou70knSDaYucrfA73wXbhTW+EHdqX2ypCdlNHgigjDn8Pz0R1PwSx8B+7oBuDi/n9ATgoQW+vqp8+EWrCb4C/B9xPciMnfSuVjLhlMM1sm6/vfSNZmwZvwR5YilAZdmlH6S9YmxFjMVl2bEcon08wTcO4LqEhwMHNfhm65E+BJE2GB/SCpLP8K3bUFgpFupL+1AGNfTF8ZtbbtQNt9zOo17iaV5ltDz3iErzpyTO7bH6KOBZ/xYHoSBmXl4M++ymZYh6g1v0OwaJRIEiBwcOrMlX26cV4+eAU/+l2yqTJtiLr3Qd1EMDsONNzKzMvwpaPUbYC5fS9AG5FQZBMwJ8EQLMEUvbaH2tZ6lD4kbM7pmwl0CagOQzXOh1ncg1D9E66XWTNT1byELXmaNmW4Xx6m3RAi2ohtqNLPjsCZmTyzzwmmPdS+VhvYQmBp0gaRDmNBZSG829GUFtPAAFS33AEUf0i/RUfK6E7bqiRLkWYQQ/kOJYNKQasVhR7nMmt8QJ/xA3S6EUJNGDsD++MqHvsKqXiPgaZBNTDT4hGeO6JuT0KX/elu2vZB1eUTX8EQLEtMwU5qkF1V7rUe6/zlU6eV5hzcsDxJBH4M7tjjaQEbyT8n2JdPEKiOjbAd7vgTDDKWJt26jJPMq6V08rRgCaaco9ZF2VXoDcXCJlzYwwndzP5nnwtVnH8/9JkcGf7cbiAm16TED3Go5G4QG86E7qQPfePiyCbBEnCRWgBZhAxG/JnXSRHvms4XmJ0VbRIsuTL6XuFaCE5Bkz25o27ZklDkz2yHJwYNajJpksmtDvEQaXkUZtFHiZHr28ZALKJmLuQ+AZV+5KWlDGdj7laY2c/B/byOpxvioSIaSmKpTA5AnSY1vvANPB30greg82vg+ncgFA4nbZm4ZdugWpcT+BnWowW+l+CFr9PLzkonTsjkAKSbHTDuFfkf+ZZ3yzLoWRvrzLwXdVDSkqW0EU0T3yX48+97P7CzGqoXmTl9iB2IMQGfElpbh72YhvZsR6VCVZYPP0wFM9X0prdNU+ccpziIpN+E8/zD6TsbLpcec1mcE2Mxl5/BC5XBWQ+ArZWKVOyaUjlQ1x3p+GOtQqcY+6D6rM+wFau1bvkvkCkFEOfKgcbuyMTsTTLlMquv9rms/zepHmheIs/1AP4F9DYB6+AcwCcAAAAASUVORK5CYII=)

**OWASP SecureTea Project**はノートPCなどのコンピュータ、サーバー等のデバイスをIoTを使用してセキュリティを高め、そのデバイスが意図しない他のユーザーによって操作された場合ユーザーに通知を行います。タッチパッド、マウス、ワイヤレスマウス等のアクティビティを使用して検知します。このアプリケーションはPythonで書かれておりマルチプラットフォーム（Linux、Mac、Windows）に対応しています。<br>
現在このソフトウェアは開発途中ですが、このアプリケーション上にIDS/IPS、ファイアーウォール、アンチウイルス、WEBの改ざん検知等のインテリジェントログモニタリング等を実装し、多数の通信媒体に対応することを目指しております。

![](/img/setup_all.gif)<br>


## 目次
- [ターゲットユーザー](#target-user)
- [目的](#objective)
- [必要要件](#pre-requisites)
- [インストール手順](#procedure-installation)
- [このプロジェクトへの助言や貢献](#suggestions-and-contributing)
- [倫理要綱](https://github.com/OWASP/SecureTea-Project/blob/master/CODE_OF_CONDUCT.md)
- [チャットグループ](#chat-group)
- [ユーザーガイド](/doc/user_guide.md)
- [開発者用ガイド](/doc/dev_guide.md)

## 対象ユーザー:


IoTセキュリティに関心のある方なら誰でもご利用できるよう開発されておりますが開発途上です。

### 動作について:

- マウスやタッチパッドの動きを追跡します
- マウスやタッチパッドがインストールされているノートPCを誰が使用しているのかを検知します
- Twitter/SMS/Slack/Telegram等で警告メッセージを送信します


## 目的:

コンピュータやサーバーが攻撃者や想定外のユーザーからのアクセスを受けている際に様々なコミュニケーション方法で警告します。
また、防御のためにシステムやSecureTeaファイアーウォールの監視を行います。


## インストール手順:

## ユーザーガイド:

ユーザーガイドをご参照ください [User Guide](/doc/user_guide.md)

## 開発者用ガイド:

開発者用ガイドをご参照ください [Developer guide](/doc/dev_guide.md)


## [Suggestions and Contributing:](https://github.com/OWASP/SecureTea-Project/blob/master/CONTRIBUTING.md)

- For contributors, please add your name below:
- [Ade Yoseman](https://www.owasp.org/index.php/Ade_Yoseman_Putra)
- [Bambang Kurniawan](https://www.owasp.org/index.php/User:Idbmb)
- [Lojislav Bezimenov](https://github.com/lojikil/)
- [Rejah Rehim](https://rejahrehim.com)
- [Ananthu S](https://github.com/sananthu)


## チャットグループ

[
![Telegram](https://github.com/OWASP/SecureTea-Project/blob/master/img/telegram.png "Telegram")](https://t.me/joinchat/Az5yZxQg7Djs-UZWKKCRVQ)

## Google Summer of Code

<img src="https://betanews.com/wp-content/uploads/2016/03/vertical-GSoC-logo.jpg" width="200"></img>
