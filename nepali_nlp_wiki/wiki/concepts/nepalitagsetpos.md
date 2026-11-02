---
okf_version: "0.2"
type: "concept"
title: "Nelralec Part-of-Speech Tagset (NT-01)"
description: "Comprehensive specification of the Nelralec Part-of-Speech Tagset for contemporary Nepali, detailing noun categories, honorific pronouns, agreement adjectives, and verbal paradigms."
status: "active"
version: "1.0.0"
timestamp: "2026-11-02T14:15:00Z"
tags:
  - pos-tagset
  - nelralec
  - morphology
  - syntax
  - pos-tagging
---

# NELRALEC TAGSET

### Nepali POS Tagset: Main Categories

| Category definition | Examples (Latin) | Examples (Devanagari) | Tag |
| :--- | :--- | :--- | :--- |
| **Common noun** | `keTo, keTaa, kalam` | `केटो, केटा, कलम` | `NN` |
| **Proper noun** | `raam` | `राम` | `NP` |
| **Masculine adjective** | `moTo, raamro` | `मोटो, राम्रो` | `JM` |
| **Feminine adjective** | `moTii, raamrii` | `मोटी, राम्री` | `JF` |
| **Other-agreement adjective** | `moTaa, raamraa` | `मोटा, राम्रा` | `JO` |
| **Unmarked adjective** | `saphaa, dhanii, asal` | `सफा, धनी, असल` | `JX` |
| **Sanskrit-derived comparative or superlative adjective** | `uccatar, uccatam` | `उच्चतर, उच्चतम` | `JT` |
| **First person pronoun** | `ma, haamii, mai#` | `म, हामी, मै#` | `PMX` |
| **First person possessive pronoun with masculine agreement** | `mero, haamro` | `मेरो, हाम्रो` | `PMXKM` |
| **First person possessive pronoun with feminine agreement** | `merii, haamrii` | `मेरी, हाम्री` | `PMXKF` |
| **First person possessive pronoun with other agreement** | `meraa, haamraa` | `मेरा, हाम्रा` | `PMXKO` |
| **Non-honorific second person pronoun** | `ta~, tai#` | `तँ, तै#` | `PTN` |
| **Non-honorific second person possessive pronoun with** | `tero` | `तेरो` | `PTNKM` |
| **Non-honorific second person possessive pronoun with feminine agreement** | `terii` | `तेरी` | `PTNKF` |
| **Non-honorific second person possessive pronoun with other agreement** | `teraa` | `तेरा` | `PTNKO` |
| **Medial-honorific second person pronoun** | `timii` | `तिमी` | `PTM` |
| **Medial-honorific second person possessive pronoun with masculine agreement** | `timro` | `तिम्रो` | `PTMKM` |
| **Medial-honorific second person possessive pronoun with feminine agreement** | `timrii` | `तिम्री` | `PTMKF` |
| **Medial-honorific second person possessive pronoun with other agreement** | `timraa` | `तिम्रा` | `PTMKO` |
| **High-honorific second person pronoun** | `tapaai~, hajur` | `तपाईं, हजुर` | `PTH` |
| **High-honorific unspecified-person pronoun** | `yahaa~, wahaa~⁷` | `यहाँ, वहाँ` | `PXH` |
| **Royal-honorific unspecified-person pronoun** | `sarkaar, mausuph` | `सरकार, मौसुफ` | `PXR` |
| **Reflexive pronoun** | `aaphnu` | `आफु` | `PRF` |
| **Possessive reflexive pronoun with masculine agreement** | `aaphno` | `आफ्नो` | `PRFKM` |
| **Possessive reflexive pronoun with feminine agreement** | `aaphnii` | `आफ्नी` | `PRFKF` |
| **Possessive reflexive pronoun with other agreement** | `aaphnaa` | `आफ्ना` | `PRFKO` |
| **Masculine demonstrative determiner** | `yasto, yatro` | `यस्तो, यत्रो` | `DDM` |
| **Feminine demonstrative determiner** | `yastii, yatrii` | `यस्ती, यत्री` | `DDF` |
| **Other-agreement demonstrative determiner** | `yastaa, yatraa` | `यस्ता, यत्रा` | `DDO` |
| **Unmarked demonstrative determiner** | `yo, yas#, yi, yin#, yinii, yati, yatti` | `यो, यस#, यी, यिन#, यिनी, यति, यत्ति` | `DDX` |
| **Masculine interrogative determiner** | `kasto, katro` | `कस्तो, कत्रो` | `DKM` |
| **Feminine interrogative determiner** | `kastii, katrii` | `कस्ती, कत्री` | `DKF` |
| **Other-agreement interrogative determiner** | `kastaa, katraa` | `कस्ता, कत्रा` | `DKO` |
| **Unmarked interrogative determiner** | `ko, kas#, ke, kun, kati` | `को, कस#, के, कुन, कति` | `DKX` |
| **Masculine relative determiner** | `jasto, jatro` | `जस्तो, जत्रो` | `DJM` |
| **Feminine relative determiner** | `jastii, jatrii` | `जस्ती, जत्री` | `DJF` |
| **Other-agreement relative determiner** | `jastaa, jatraa` | `जस्ता, जत्रा` | `DJO` |
| **Unmarked relative determiner** | `jo, jas#, je, jati, josukai` | `जो, जस#, जे, जति, जोसुकै` | `DJX` |
| **Masculine general determiner-pronoun** | `arko` | `अर्को` | `DGM` |
| **Feminine general determiner-pronoun** | `arkii` | `अर्की` | `DGF` |
| **Other-agreement general determiner-pronoun** | `arkaa` | `अर्का` | `DGO` |
| **Unmarked general determiner-pronoun** | `aruu` | `अरु` | `DGX` |
| **Infinitive verb** | `garnu, garna, garnaa, nagarnu, nagarna, nagarnaa` | `गर्नु, गर्न, गर्ना, नगर्नु, नगर्न, नगर्ना` | `VI` |
| **Masculine d-participle verb** | `gardo, nagardo` | `गर्दै, नगर्दै` | `VDM` |
| **Feminine d-participle verb** | `gardii, nagardii` | `गर्दी, नगर्दी` | `VDF` |
| **Other-agreement d-participle verb** | `gardaa, nagardaa` | `गर्दा, नगर्दा` | `VDO` |
| **Unmarked d-participle verb** | `gardai, nagardai` | `गर्दै, नगर्दै` | `VDX` |
| **e(ko)-participle verb** | `gae (as in gae saal), gare (as in garejati or gareko)` | `गरे` | `VE` |
| **ne-participle verb::** | `garne, nagarne` | `गर्ने, नगर्ने` | `VN` |
| **Sequential participle-verb** | `garera, garikana, garii, nagarera, nagariikana, nagarii` | `गरेर, गरीकन, गरी, नगरेर, नगरीकन, नगरी` | `VQ` |
| **Command-form verb, non-honorific** | `gar, jaa` | `गर, जा` | `VCN` |
| **Command-form verb, mid-honorific** | `gara, jaau, jaao` | `गर, जाऊ, जाओ` | `VCM` |
| **Command-form verb, high-honorific** | `garnos, jaanos` | `गर्नोस्, जानोस्` | `VCH` |
| **Subjunctive / conditional e-form verb** | `gare, nagare` | `गरे, नगरे` | `VS` |
| **i-form verb** | `gari` | `गरि` | `VR` |
| **First person singular verb** | `gare~, garthe~, garina~, chu, hu~, garnechu` | `गरेँ, गर्थें, गरिनँ, छु, हुँ, गर्नेछु` | `VVMX1` |
| **First person plural verb** | `garyau~, garthyau~, garenau~, chau~, hau~, garnechau~` | `गर्यौं, गर्थ्यौं, गरेनौं, छौं, हौं, गर्नेछौं` | `VVMX2` |
| **Second person non-honorific singular verb** | `garis, garthis, garinas, chas, hos, garnechas` | `गरिस्, गर्थिस्, गरिन्, छस्, होस्, गर्नेछस्` | `VVTN1` |
| **Second person plural (or medial-honorific singular) verb** | `garyau, garthyau, garenau, chau, hau, garnechau` | `गर्यौ, गर्थ्यौ, गरेनौ, छौ, हौ, गर्नेछौ` | `VVTX2` |
| **Third person non-honorific singular verb** | `garyo, garthyo, garena, cha, ho, garnecha` | `गर्यो, गर्थ्यो, गरेन, छ, हो, गर्नेछ` | `VVYN1` |
| **Third person plural (or medial-honorific singular) verb** | `gare, garthe, garenan, chan, hun, garnechan` | `गरे, गर्थे, गरेनन्, छन्, हुन्, गर्नेछन्` | `VVYX2` |
| **Feminine second person non-honorific singular verb** | `garlis, ches, garthis` | `गर्लिस्, छेस्, गर्थिस्` | `VVTN1F` |
| **Feminine second person non-honorific singular verb** | `garthyau, chyau` | `गर्थ्यौ, छ्यौ` | `VVTM1F` |
| **Feminine third person non-honorific singular verb** | `garina, garthi, che, garthii` | `गरिन, गर्थी, छे, गर्थी` | `VVYN1F` |
| **Feminine third person medial-honorific singular verb** | `garin, garthin, garinan, chin` | `गरिन्, गर्थिन्, गरिनन्, छिन्` | `VVYM1F` |
| **First person singular optative verb** | `jaau~, garu~` | `जाऊँ, गरुँ` | `VOMX1` |
| **First person plural optative verb** | `jaaaau~, garau~` | `जाऔं, गरौं` | `VOMX2` |
| **Second person non-honorific singular optative verb** | `gaes, gares` | `गएस्, गरेस्` | `VOTN1` |
| **Second person plural (or medial-honorific singular) optative verb** | `gae, gare` | `गए, गरे` | `VOTX2` |
| **Third person non-honorific singular optative verb** | `jaaos, garos` | `जाओस्, गरोस्` | `VOYN1` |
| **Third person plural (or medial-honorific singular) optative verb** | `jaauun, garuun` | `जाऊन्, गरुन्` | `VOYX2` |
| **Adverb** | `raamrarii, ekdam, chiTo` | `राम्ररी, एकदम, छिटो` | `RR` |
| **Demonstrative adverb** | `yataa, utaa, tyataa; ahile, ahilyai, yahii~, yasarii, aba` | `यता, उता, त्यहाँ; अहिले, अहिल्यै, यहीं, यसरी, अब` | `RD` |
| **Interrogative adverb** | `kataa, kahaa~, kahile, kasarii` | `कता, कहाँ, कहिले, कसरी` | `RK` |
| **Relative adverb** | `jataa, jahaa~, jahile, jasarii, jaba` | `जता, जहाँ, जहिले, जसरी, जब` | `RJ` |
| **Postposition** | `agaaDi, pachaaDi, baaTa, dwaaraa, maa, maathi, saath, purvak, tira, tarpha, vasa, sanga, binaa` | `अगाडि, पछाडि, बाट, द्वारा, मा, माथि, पूर्वक, तिर, तर्फ, वस, संग, बिना` | `II` |
| **Plural-collective postposition** | `haruu` | `हरू` | `IH` |
| **Ergative-instrumental postposition** | `le` | `ले` | `IE` |
| **Accusative-dative postposition** | `laaii` | `लाई` | `IA` |
| **Masculine genitive postposition** | `ko` | `को` | `IKM` |
| **Feminine genitive postposition** | `kii` | `की` | `IKF` |
| **Other-agreement genitive postposition** | `kaa` | `का` | `IKO` |
| **Cardinal number** | `ek, eu#, yau#, dui, tin, caar, paa~c` | `एक, दुई, तीन, चार, पाँच` | `MM` |
| **Masculine ordinal number** | `pahilo, dosro, tesro, cautho` | `पहिलो, दोस्रो, तेस्रो, चौथो` | `MOM` |
| **Feminine ordinal number** | `pahilii, dosrii, tesrii, cauthii` | `पहिली, दोस्री, तेस्री, चौथी` | `MOF` |
| **Other-agreement ordinal number** | `pahilaa, dosraa, tesraa, cauthaa` | `पहिला, दोस्रा, तेस्रा, चौठा` | `MOO` |
| **Unmarked ordinal number** | `paa~cau~` | `पाँचौं` | `MOX` |
| **Masculine numeral classifier** | `#To [as in euTo]` | `#टो` | `MLM` |
| **Feminine numeral classifier** | `(#)waTii, #Tii, #oTii, #auTii` | `(#)वटी, #टी, #ओटी, #औटी` | `MLF` |
| **Other-agreement numeral classifier** | `(#)waTaa, #Taa, #oTaa, #auTaa` | `(#)वटा, #टा, #ओटा, #औटा` | `MLO` |
| **Unmarked numeral classifier** | `(#)janaa` | `(#)जना` | `MLX` |
| **Coordinating conjunction** | `ra, tathaa` | `र, तथा` | `CC` |
| **Subordinating conjunction appearing *after* the clause it subordinates** | `bhanne, bhanii, bhanera` | `भन्ने, भनी, भनेर` | `CSA` |
| **Subordinating conjunction appearing *before* the clause it subordinates** | `ki, yadi, yaddyapi, kinaki` | `कि, यदि, यद्यपि, किनकि` | `CSB` |
| **Particle** | `nai, caahi~, pani, hai, ra, re, kyaare, ho, khai` | `नै, चाहिँ, पनि, है, र, रे, क्यारे, हो, खै` | `TT` |
| **Question marker** | `ke` | `के` | `QQ` |
| **Interjection** | `oho, aahaa, hare` | `ओहो, आहा, हरे` | `UU` |
| **Possessive reflexive pronoun without agreement** | `merai` | `मेरै` | `PMXKX` |
| **Non-honorific second person possessive pronoun without agreement** | `terai` | `तेरै` | `PTNKX` |
| **Medial-honorific second person possessive pronoun without agreement** | `timrai` | `तिम्रै` | `PTMKX` |
| **Possessive reflexive pronoun without agreement** | `aaphnai` | `आफ्नै` | `PRFKX` |
| **Unmarked genitive postposition** | `kai` | `कै` | `IKX` |
| **Sentence-final punctuation** | `? ! . ।। ॥` | | `YF` |

**Note:**
⁷ There is an alternative form for `wahaa~`: `uhaa~`. This form would also take the `PXH` tag.

---

### Punctuation, Foreign Words, and Miscellaneous Tags

| Category definition | Examples | Tag |
| :--- | :--- | :--- |
| **Sentence-medial punctuation** | `, ; : :: / -` | `YM` |
| **Quotation marks** | `' "` | `YQ` |
| **Brackets** | `( ) { } [ ]` | `YB` |
| **Foreign word in Devanagari** | | `FF` |
| **Foreign word, not in Devanagari** | | `FS` |
| **Abbreviation** | `M.P.P.` / `म. पु. पु.` | `FB` |
| **Mathematical formula (and similar)** | `e=mc²` | `FO` |
| **Letter of the alphabet** | | `FZ` |
| **Unclassifiable** | | `FU` |
| **Null tag: an element of the text which does not need a tag** | `<p>` | `NULL` |