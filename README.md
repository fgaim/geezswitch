GeezSwitch
==========

![GitHub issues](https://img.shields.io/github/issues/fgaim/geezswitch.svg)
[![PyPI](https://img.shields.io/pypi/v/geezswitch.svg)](https://pypi.org/project/geezswitch/)
[![CircleCI](https://circleci.com/gh/fgaim/geezswitch.svg?style=shield)](https://circleci.com/gh/fgaim/geezswitch)


Language Identification (LI) library for 60 languages,
adapted from Michal Danilak's great package [langdetect](https://github.com/Mimino666/langdetect), adding support for low-resource languages that use the [Ge'ez script](https://en.wikipedia.org/wiki/Ge'ez_script) as a writing system based on the [GeezSwitch dataset](https://github.com/fgaim/geezswitch-data).


> The GeezSwitch dataset was published in the paper *"GeezSwitch: Language Identification in Typologically Related Low-resourced East African Languages"* at LREC 2022 and the data can be found [here](https://github.com/fgaim/GeezSwitch-data.git).

Installation
============

    $ pip install geezswitch

Supported Python versions 2.7, 3.4+.


Languages
=========

The library supports identification across 60 languages in total.

Support for five languages that use the [Ge'ez script](https://en.wikipedia.org/wiki/Ge'ez_script) based on the [GeezSwitch dataset](https://github.com/fgaim/geezswitch-data). Using [ISO 639-3](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Languages/List_of_ISO_639-3_language_codes_(2019)) codes since some of these languages were not included in [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

    amh (Amharic), byn (Blin), gez (Ge'ez), tig (Tigre), tir (Tigrinya)

Support for 55 languages inherited from the original `langdetect` package. Keeping [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) codes for backward compatibility:

    af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
    hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
    pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn,
    zh-tw


Basic usage
===========

To detect the language of the text:

```python
>>> from geezswitch import detect
>>> detect("ብኮምፒዩተር ናይ ምስራሕ ክእለት")
'tir'
>>> detect("ኳዅረስ ይድ ባሪ ፣ ይት እሺ ይት ገውሪ")
'byn'
>>> detect("ወዲብለ ታክያተ ክልኦት አሕድ")
'tig'
>>> detect("ነጭ አበባ ያለው ተክል")
'amh'
>>> detect("ወይቤሎ ዮናታን ሐሰ ለከ ወእምከመሰ")
'gez'
```

To find out the probabilities for the top languages:

```python
>>> from geezswitch import detect_langs
>>> detect_langs("Otec matka syn.")
[sk:0.572770823327, pl:0.292872522702, cs:0.134356653968]
```

**NOTE**

The language detection algorithm is non-deterministic, which means that if you run it on a text which is either too short or too ambiguous, you might get different results everytime you run it.

To enforce consistent results, call following code before the first language detection:

```python
from geezswitch import DetectorFactory
DetectorFactory.seed = 0
```

How to add new language?
========================

> New language contributions are very welcome, particularly, for languagees written in the Ge'ez script.
You can either use the steps below or just contribute example text for the target language, and we can help with the integration.

Language identification works best when the model is trained on examples of many languages.

To add a new language, you need to create a new language profile. The easiest way to do it is to use the [langdetect.jar](https://github.com/shuyo/language-detection/raw/master/lib/langdetect.jar) tool, which can generate language profiles from Wikipedia abstract database files or plain text.

Wikipedia abstract database files can be retrieved from "Wikipedia Downloads" ([http://download.wikimedia.org/](http://download.wikimedia.org/)). They form '(language code)wiki-(version)-abstract.xml' (e.g. 'enwiki-20101004-abstract.xml' ).

usage: ``java -jar langdetect.jar --genprofile -d [directory path] [language codes]``

- Specify the directory which has abstract databases by -d option.
- This tool can handle gzip compressed file.

Remark: The database filename in Chinese is like 'zhwiki-(version)-abstract-zh-cn.xml' or zhwiki-(version)-abstract-zh-tw.xml', so that it must be modified 'zh-cnwiki-(version)-abstract.xml' or 'zh-twwiki-(version)-abstract.xml'.

To generate language profile from a plain text, use the genprofile-text command.

usage: ``java -jar langdetect.jar --genprofile-text -l [language code] [text file path]``

For more details see [language-detection Wiki](https://code.google.com/archive/p/language-detection/wikis/Tools.wiki).


Original project
================

This library is adapted from [langdetect](https://github.com/Mimino666/langdetect), which in return is a direct port of Google's [language-detection](https://code.google.com/p/language-detection/) library from Java to Python. For more information, please refer to those repos.


Citation
========

If you use GeezSwitch in your research, please cite as follows:

``` markdown
@inproceedings{fgaim2022geezswitch,
  title={GeezSwitch: Language Identification in Typologically Related Low-resourced East African Languages},
  author={Fitsum Gaim and Wonsuk Yang and Jong C. Park},
  booktitle={Proceedings of the 13th Language Resources and Evaluation Conference},
  year={2022}
}
```
