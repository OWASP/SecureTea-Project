<img align="left" width="120" height="120" src="img/logo/secure-tea-white.png">

# [OWASP SecureTea][SecureTea-OWASP]

[![Build Status][Travis-badge]][Travis]
[![Codacy Badge][Codacy-badge]][Codacy]
[![PyPI][PyPi-badge]][PyPi]
[![GitHub][License-badge]][License]
[![Telegram][Telegram-badge]][Telegram]
[![Version][Version-badge]][Version]
[![Tag][Tag-badge]][Tag]
[![GitHub issues][Issues-badge]][Issues]
[![GitHub pull requests][PR-badge]][PRs]
[![GSOC 2019][GSOC-2019-badge]][GSOC-OWASP]
[![Follow Us](https://img.shields.io/twitter/url/https/secureteatool.svg?label=SecureTea%20Project&style=social)](https://twitter.com/secureteatool)

**The OWASP SecureTea Project** is an application designed to help secure a person's laptop or computer / server with IoT (Internet Of Things) and notify users (via various communication mechanisms), whenever someone accesses their computer / server. This application uses the touchpad/mouse/wireless mouse to determine activity and is developed in Python and tested on various machines (Linux, Mac & Windows).<br>
The software is still under development, and will eventually have it's own IDS(Intrusion Detection System) / IPS(Instrusion Prevention System), firewall, anti-virus, intelligent log monitoring capabilities with web defacement detection, and support for much more communication medium.

![Setup Intro][Setup-help-animation]

## Table Of Contents
-   [Target User](#target-user)
-   [Objective](#objective)
-   [Pre-requisites](#pre-requisites)
-   [Installation Procedure](#installation-procedure)
-   [Suggestions and Contribution](#suggestions-and-contributing)
-   [Code Of Conduct](/CODE_OF_CONDUCT.md)
-   [Chat Group](#chat-group)
-   [User guide](/doc/en-US/user_guide.md)
-   [Developer guide](/doc/en-US/dev_guide.md)
-   [Translation-Japanese](/doc/ja-JP/README.md)
-   [Translation-Hindi](/doc/hi-IN/README.md)

## Target User

It was written to be used by anyone who is interested in IoT Security (Internet of Things) and still needs further development.

### How it functions:

-   Keep track of the movement of the mouse/touchpad
-   Detect who accesses your device(laptop/server/other iot device) with mouse/touchpad installed.
-   Send warning messages on Twitter/Twilio-SMS/Slack/Telegram. More features on the way.

## Objective

To alert the user via various communication mechanism, whenever The Computer / Server had been accessed by someone / attacker.
And also it can be used to monitor your system & SecureTea firewall as Defense.

## Installation Procedure

### User Guide

See more at [User Guide](/doc/en-US/user_guide.md)
for translated user guides
### Developer Guide

See more at [Developer guide](/doc/en-US/dev_guide.md)
for translated developer guides

## [Suggestions and Contributing](/CONTRIBUTING.md)

For contributors, please add your name below:

-   [Ade Yoseman][Ade]
-   [Bambang Kurniawan][Bambang]
-   [Lojislav Bezimenov][Lojislav]
-   [Rejah Rehim][Rejah]
-   [Ananthu S][Ananthu]

| **Chat Group** | **Google Summer of Code** | **YouTube** |
| -------------- | ------------------------- |---------------------|
| [<img src="/img/telegram.png" width="50" title="Telegram">][Telegram]  | [<img src="/img/GSoC-logo.jpg" width="100"></img>][GSOC-OWASP]  | [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/1024px-YouTube_Logo_2017.svg.png" width="90" title="YouTube">][YouTube] | 

[YouTube]: https://www.youtube.com/channel/UCGdl9tpc1qZYcM3WRRFRPPA
[OWASP-logo]: https://github.com/OWASP/Amass/blob/master/images/owasp_logo.png
[SecureTea-OWASP]: https://www.owasp.org/index.php/OWASP_SecureTea_Project
[GSOC-OWASP]: https://summerofcode.withgoogle.com/organizations/6362925392986112/
[Telegram]: https://t.me/joinchat/Az5yZxQg7Djs-UZWKKCRVQ
[Telegram-badge]: https://img.shields.io/badge/chat%20on-telegram-blue.svg
[Codacy]: https://app.codacy.com/app/rejahrehim/SecureTea-Project?utm_source=github.com&utm_medium=referral&utm_content=OWASP/SecureTea-Project&utm_campaign=Badge_Grade_Settings
[Codacy-badge]: https://api.codacy.com/project/badge/Grade/7e1de11511084c06bbe25ed4d629e7fd
[Travis-badge]: https://travis-ci.com/OWASP/SecureTea-Project.svg?branch=master
[Travis]: https://travis-ci.com/OWASP/SecureTea-Project
[PyPi]: https://pypi.org/project/securetea/
[PyPi-badge]: https://img.shields.io/pypi/v/securetea.svg
[GSOC-2019-badge]: https://img.shields.io/static/v1.svg?label=GSOC&message=Google%20Summer%20of%20Code%202019&color=blue&logo=%20data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAABLFJREFUSA2tVV1sVFUQ/s45d7ulpT+63VSkQC1IIsHyAugDAWLwQSEQI/EnaGL0QWOQ6AMo+uAzJooJJJiIiQ8qkWDURIxGIlLUqEQTKz9REEpbMFhKt7ss7e49P35zb9jaqKEkTnL33jNn5ps538ycBa5D7MH8etuTX38dLlM3jQ+2rXRf1Q/LI99T9VRTMYy/rF+hUflAIeTEPkANe2Tvz9w1fuha/pMChE/RbDNRd83JWnigwzTO2Gma5+ec6eCWgnEDcMXfhl35j43cH4yiqOYSxbZX3YviVcXEDjVWR4tMRvUEegUXQzfNRtT1PJBbw7WFjocTv5DJwZgoZy7t3+N/34YwdhbKZKA0MO6i5UQ6/K8BYBC8gNsYKr8a6rZdCJePwx97EmH0e+rTxFTUDNW8FHrOs9CLD8OdeBp+6BOoKAPBuAou70knSDaYucrfA73wXbhTW+EHdqX2ypCdlNHgigjDn8Pz0R1PwSx8B+7oBuDi/n9ATgoQW+vqp8+EWrCb4C/B9xPciMnfSuVjLhlMM1sm6/vfSNZmwZvwR5YilAZdmlH6S9YmxFjMVl2bEcon08wTcO4LqEhwMHNfhm65E+BJE2GB/SCpLP8K3bUFgpFupL+1AGNfTF8ZtbbtQNt9zOo17iaV5ltDz3iErzpyTO7bH6KOBZ/xYHoSBmXl4M++ymZYh6g1v0OwaJRIEiBwcOrMlX26cV4+eAU/+l2yqTJtiLr3Qd1EMDsONNzKzMvwpaPUbYC5fS9AG5FQZBMwJ8EQLMEUvbaH2tZ6lD4kbM7pmwl0CagOQzXOh1ncg1D9E66XWTNT1byELXmaNmW4Xx6m3RAi2ohtqNLPjsCZmTyzzwmmPdS+VhvYQmBp0gaRDmNBZSG829GUFtPAAFS33AEUf0i/RUfK6E7bqiRLkWYQQ/kOJYNKQasVhR7nMmt8QJ/xA3S6EUJNGDsD++MqHvsKqXiPgaZBNTDT4hGeO6JuT0KX/elu2vZB1eUTX8EQLEtMwU5qkF1V7rUe6/zlU6eV5hzcsDxJBH4M7tjjaQEbyT8n2JdPEKiOjbAd7vgTDDKWJt26jJPMq6V08rRgCaaco9ZF2VXoDcXCJlzYwwndzP5nnwtVnH8/9JkcGf7cbiAm16TED3Go5G4QG86E7qQPfePiyCbBEnCRWgBZhAxG/JnXSRHvms4XmJ0VbRIsuTL6XuFaCE5Bkz25o27ZklDkz2yHJwYNajJpksmtDvEQaXkUZtFHiZHr28ZALKJmLuQ+AZV+5KWlDGdj7laY2c/B/byOpxvioSIaSmKpTA5AnSY1vvANPB30greg82vg+ncgFA4nbZm4ZdugWpcT+BnWowW+l+CFr9PLzkonTsjkAKSbHTDuFfkf+ZZ3yzLoWRvrzLwXdVDSkqW0EU0T3yX48+97P7CzGqoXmTl9iB2IMQGfElpbh72YhvZsR6VCVZYPP0wFM9X0prdNU+ccpziIpN+E8/zD6TsbLpcec1mcE2Mxl5/BC5XBWQ+ArZWKVOyaUjlQ1x3p+GOtQqcY+6D6rM+wFau1bvkvkCkFEOfKgcbuyMTsTTLlMquv9rms/zepHmheIs/1AP4F9DYB6+AcwCcAAAAASUVORK5CYII=
[License]:  /LICENSE
[License-badge]: https://img.shields.io/github/license/mashape/apistatus.svg
[Version]: https://github.com/OWASP/SecureTea-Project/releases
[Version-badge]: https://img.shields.io/github/release/OWASP/SecureTea-Project.svg
[Tag]: https://github.com/OWASP/SecureTea-Project/tags
[Tag-badge]: https://img.shields.io/github/tag/OWASP/SecureTea-Project.svg?color=orange&label=version
[Issues]: https://github.com/OWASP/SecureTea-Project/issues
[Issues-badge]: https://img.shields.io/github/issues/OWASP/SecureTea-Project.svg
[PRs]: https://github.com/OWASP/SecureTea-Project/pulls
[PR-badge]: https://img.shields.io/github/issues-pr/OWASP/SecureTea-Project.svg
[Setup-help-animation]: /img/setup_all.gif
[Rejah]: https://rejahrehim.com
[Ananthu]: https://github.com/sananthu
[Ade]: https://www.owasp.org/index.php/Ade_Yoseman_Putra
[Bambang]: https://www.owasp.org/index.php/User:Idbmb
[Lojislav]: https://github.com/lojikil/
