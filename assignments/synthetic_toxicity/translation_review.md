# nepali_aware_final.csv — Pair Review (vs noisy.csv)

Checked all 500 id pairs (id 1–500, 1:1 aligned). Below are the rows where the
"final" version either changes meaning, drops content, guesses too freely at a
garbled source, or is internally inconsistent. Row 13/250 etc. are not "wrong"
per se but are flagged for transparency.

Severity:
- **HIGH** = meaning changed / content dropped that matters
- **MED** = heavy guesswork / half the sentence dropped or re-invented
- **LOW** = minor, inconsistent, or harmless edits worth knowing about

---

## HIGH — meaning changed or content dropped

### id 474
- noisy: `बलेन सरलाई किसानले मारेका छन् ।`
- final: `बालेन सरलाई किसानले घेरेका छन्।`
- Problem: "मारेका" (have beaten/killed) was changed to "घेरेका" (have surrounded). The violent claim is the whole point of the source; it was softened into a different event. Should keep the original message (मारे/कुटे).

### id 434
- noisy: `हामीसँग फ्राइङ छैन`
- final: `हामीसँग केही छैन।`
- Problem: "फ्राइङ" (frying / fried) was silently replaced by "केही" (nothing). Token was dropped and a new word invented. If the token was real, the meaning is lost.

### id 241
- noisy: `यो जवाफ देखेर रन्डीले शुल्क तिर्न बाध्य बनायो।`
- final: `यो जवाफ देखेर शुल्क तिर्न बाध्य बनायो।`
- Problem: "रन्डीले" (the whore — the subject/target) was deleted entirely. If this was deliberate slur-removal that's fine, but then the sentence no longer has a subject and the target of the insult is lost.

### id 336
- noisy: `यो नेता घुसखोर हो, उसलाई स्वास्नी भनिन्छ`
- final: `यो नेता घुसखोर हो।`
- Problem: second clause "उसलाई स्वास्नी भनिन्छ" dropped. Even if garbled, the omission should be noted.

### id 370
- noisy: `रेस्टुरेन्टको भित्री डिजाइन खाना, स्वाद र सेवाको गुणस्तर जत्तिकै राम्रो छ, र त्यसपछि तपाइँ सोशल मिडियामा हाइप पाउनुहुनेछ।`
- final: `रेस्टुरेन्टको भित्री सजावट, खानाको स्वाद र सेवाको गुणस्तर जत्तिकै राम्रो छ।`
- Problem: the trailing clause "...र त्यसपछि तपाइँ सोशल मिडियामा हाइप पाउनुहुनेछ" was dropped.

### id 446
- noisy: `विश्वमा मुस्लिम समुदाय ठूलो समस्या बनेको छ, जहाँ बम र आतंककारी गतिविधि छन्, नेपाल चर्चित भएको छ, कुनै अधिकार चर्चित भएको छ र भाइरस फैलिएको छ ।`
- final: `विश्वमा मुस्लिम समुदाय ठूलो समस्या बनेको छ, जहाँ बम र आतङ्ककारी गतिविधि छन्।`
- Problem: the garbled tail after "गतिविधि छन्" was dropped. Acceptable as salvage, but note content was removed rather than repaired.

### id 458
- noisy: `तपाईंले फेसबुकमा कुनै ठाउँ फेला पार्न सक्नुहुन्न जहाँ तपाईं आफ्नो वास्तविक स्थान फेला पार्न सक्नुहुन्छ, जहाँ तपाईं आफ्नो नायक जहाँ पनि फेला पार्न सक्नुहुन्छ।`
- final: `तपाईंले फेसबुकमा आफ्नो वास्तविक ठाउँ भेट्टाउन सक्नुहुन्न।`
- Problem: two whole clauses were dropped and the sentence re-invented. Meaning is only partially preserved.

### id 463
- noisy: `... जसले उहाँलाई जे ठीक लाग्छ त्यही गर्नुहुन्छ। थाहा छैन। बोल्ने`
- final: `... तपाईं यस्तो व्यक्ति हुनुहुन्छ जसलाई जे ठिक लाग्छ त्यही गर्नुहुन्छ।`
- Problem: "थाहा छैन। बोल्ने" was dropped (they were garbage tokens, but dropped nevertheless — matches id 17 style). Note consistency: id 17 kept "नचिनेको होर। बात कर्ते हो।" while id 463 (same phrasing family) dropped its tail.

---

## MED — heavy guesswork / half-garbled salvage

These rows have badly garbled/transliterated sources and the final output is necessarily a guess. Flagged so you can verify each manually.

### id 66
- noisy: `Ladako dam dar chicne talai dam dar lagyo Sala jhole`
- final: `लडाकु दमदार चिक्ने, तँलाई दमदार लाग्यो साला झोले!`
- `Ladako` → `लडाकु` and `chicne` → `चिक्ने` are both guesses.

### id 76
- noisy: `Terima kogle hune lai thapis nahune beroj gari lai rojgari nai khosis`
- final: `तेरीआमा! हुनेलाई थपिस, नहुने बेरोजगारलाई रोजगारी नै खोसिस्।`
- `kogle hune lai thapis` is unresolved; only "बेरोजगार...रोजगारी खोसिस्" is certain.

### id 92
- noisy: `Tata tetai ga machikne khate kukur`
- final: `तता त्यता जा माचिक्ने खाते कुकुर!`
- "tata tetai ga" reconstructed as "तता त्यता जा" — plausible but guessed.

### id 106
- noisy: `Baula ko ho sab lai tha xa`
- final: `बाउला को हो सबैलाई थाहा छ।`
- "बाउला" ambiguous (crazy person / whose?). Kept as-is.

### id 109
- noisy: `...barbara ko 1 ta samman le jindagi nachalla....`
- final: `...बर्बराएको एउटा सम्मानले जिन्दगी चल्दैन...`
- "barbara ko 1 ta samman" is very likely a mis-transliteration; guess-prone.

### id 149
- noisy: `ktaho sab milera yeslai chai godnai parxa`
- final: `केटाहरू, सब मिलेर यसलाई चाहिँ चुट्नैपर्छ।`
- "godnai" → "चुट्नै" (beat) is a plausible guess, not certain.

### id 157
- noisy: `idk engineering ta almost ded ho aaba`
- final: `मलाई थाहा छैन, इन्जिनियरिङ त अब लगभग समाप्त भइसक्यो।`
- "ded" = dead → "समाप्त भइसक्यो". Good guess.

### id 193
- noisy: `यो एप अपडेट गरेपछि ब्याट्री जान छाडो सकिना थाल्यो।`
- final: `यो एप अपडेट गरेपछि ब्याट्री छिटो सकिन थाल्यो।`
- "जान छाडो" reconstructed as "छिटो" — plausible dialect reading.

### id 195
- noisy: `ध्यान खोज xa खान`
- final: `ध्यान खोज्छ खान।`
- Source is nonsensical; final is still unclear. Better to mark as unintelligible rather than guess.

### id 245
- noisy: `मेरो कुरा नमन लाई धन्यवाद को दादा कटैदिन्सु`
- final: `मेरो कुरा नमान्नेलाई थानकोटको डाँडा कटाइदिन्छु।`
- "धन्यवाद को दादा" has no "थानकोट" in it — the place name was imported from id 161. Creative but ungrounded.

### id 247
- noisy: `भाउजुले भात हेरिन्`
- final: `भाउजूले भात हेरिन्।`
- "भात हेरिन्" (looked at rice?) is nonsensical; keep flagged. Possibly "भान्सा हेरिन्" or a typo.

### id 259
- noisy: `खातामा तर्क सुन्नु पर्छ, उठ्नु पर्छ।`
- final: `खातामा तर्क सुन्नुपर्छ, उठ्नुपर्छ।`
- Source is nonsense; final only normalizes punctuation. Row likely contains synthetic garble — flag as unintelligible.

### id 279
- noisy: `मुस्लिम शाखा काहिले नमिला`
- final: `मुस्लिम शाखा कहिल्यै नमिल्ने।`
- "शाखा" (branch/office) is odd here; probably garbled. Kept as-is.

### id 292
- noisy: `क्षेत्री भन्धै मा सबाइले ठुलो तौको बधना परक्सा वान्या झिना...`
- final: `क्षेत्री भन्दैमा सबैले ठूलो टाउको बाँध्नुपर्छ भन्ने छैन, आरक्षण र घुस लिएर...`
- "ठुलो तौको बधना परक्सा" → "ठूलो टाउको बाँध्नुपर्छ भन्ने छैन" is heavily reconstructed.

### id 319
- noisy: `तिमी नै हौ जसले मेरो दिमाग पार गरेको छ`
- final: `तिमी नै हौ जसले मेरो दिमाग खराब गरेको छ।`
- "दिमाग पार" → "दिमाग खराब" guessed.

### id 428
- noisy: `@manchhe123 tero हावा समात्छ`
- final: `@manchhe123 तेरो हावा कुरा कसैले पत्याउँदैन।`
- "तेरो हावा समात्छ" reconstructed to a fully different sentence.

### id 476
- noisy: `ठुलो अनुहार सुन्दा ता अछम्मा पो लक्ष`
- final: `ठूला कुरा सुन्दा त अचम्म पो लाग्छ!`
- "अनुहार" (face) → "कुरा" (words) changed; "अछम्मा/लक्ष" → "अचम्म/लाग्छ" guessed.

### id 263
- noisy: `श्रमजीवी जातिका नारी यस्ता छन्, बर्बादी, थप विचार, फल, काम, जीआरडीए, मस्तिष्क, अधिक भाषा, इनिहारु थेठी, काही, माथी, औडैना, स.`
- final: `श्रमजीवी जातिका नारी यस्ता छन्, बर्बादी, थप विचार, फल, काम, मस्तिष्क, यिनीहरू कहिल्यै माथि आउँदैनन्।`
- Many tokens (जीआरडीए, अधिक भाषा, थेठी, काही, औडैना, स) silently dropped; only the tail was guessed into "यिनीहरू कहिल्यै माथि आउँदैनन्".

### id 282
- noisy: `तिम्री भाउजुले तल्लो जातको संगत लिइन्, मेरी भाउजु तिमी के छौ, मेरी सासु, मलाई मेरो जीवनको ज्ञान दिनुभयो, तिम्रो जातले निधार जित्यो, मानौं`
- final: `तिम्री भाउजूले तल्लो जातको सङ्गत लिइन्, मेरी सासूले मलाई मेरो जीवनको ज्ञान दिनुभयो।`
- "मेरी भाउजु तिमी के छौ" and "तिम्रो जातले निधार जित्यो, मानौं" dropped; sentence was cut back.

---

## LOW — inconsistencies / minor issues

### id 13 vs id 250 (duplicated final; different sources)
- noisy 13: `सिंहदरबार जलाइने केमिकलको बन्दोवस्त, प्रयोग कस्ले... 'जानकार' ईञ्जिनियरले गराए ? यी सबै चासो...`
- noisy 250: `सिंहदरबारमा केमिकल जलाउने प्रबन्ध, कसले प्रयोग गर्छ र कहाँबाट, 'विद्वान' इन्जिनियरहरूद्वारा बनाएको? यी सबै चिन्ता...`
- final 13 == final 250 exactly. The distinct wording of noisy 250 (प्रबन्ध/चिन्ता/आउनुहोस्) was discarded — 250 just copied 13's rendering. Fine as a paraphrase, but the mapping looks like a copy-paste.

### id 203 vs id 238 (duplicated final; subject flipped)
- noisy 203: `Delivery rider lai exact address diyeko thiye...` (I gave the rider the address)
- noisy 238: `डेलिभरी राइडरले सही ठेगाना दिएको थियो...` (lit. the rider gave the address)
- final 203 == final 238 identically. For 238 the final assumed "I gave to the rider" despite the source saying "the rider gave". Note the assumption.

### id 262 vs id 377 (inconsistent treatment of similar root)
- noisy 262 `बहनबाद` → final `नातावाद` (nepotism)
- noisy 377 `bahunbaad` → final `बाहुनवाद` (brahmin-ism)
- Same-looking root word handled two different ways. 262 (नातावाद) may be intentional if they read it as "nepotism", but then 377 should match.

### id 287
- noisy: `अरु धर्म तिमीलाई यो देशमा बस्ने अधिकार दिएको छु।`
- final: `अरू धर्म, तिमीहरूलाई यो देशमा बस्ने अधिकार दिएका छौँ।`
- "दिएको छु" (I have given) → "दिएका छौँ" (we have given): speaker number changed. Source itself is weird, but note the flip.

### id 342
- noisy: `नेतालाई घूस लिनुभयो, प्रमाण पाउनुभयो र जेलमा हुनुहुन्छ ।`
- final: `नेताले घुस लिए, प्रमाण भेटियो र अहिले जेलमा छन्।`
- Honorific "लिनुभयो" (spoken ABOUT the leader but with honorific of address, likely garble) normalized to third person "लिए". Reasonable repair; note the reading.

### id 404
- noisy: `मेल यो एप प्रयोग गर्नुहोस्`
- final: `कृपया यो एप प्रयोग गर्नुहोस्।`
- "मेल" → "कृपया" (please) guessed; "मेल" unexplained.

### id 71
- noisy: `सान्दर्भिक र वास्तविकता`
- final: `सान्दर्भिक र वास्तविक।`
- "वास्तविकता" (reality) → "वास्तविक" (real). Acceptable, minor.

### id 101
- noisy: `खानेपानीको धेरै जस मैले पाउनुपर्छः`
- final: `खानेपानीको धेरै जश मैले पाउनुपर्छ।`
- "जस" → "जश" — likely should be "जसो" (most of). Both odd.

### id 175 / id 174-style tone
- id 175 noisy `chutiya desh ma chutiya janta` → final `मूर्ख देशमा मूर्ख जनता!`
- "chutiya" (strong vulgar) softened to "मूर्ख" (fool). Fine if intentional de-vulgarizing, but it reduces the harshness compared with other rows that keep "मुजी/खाते".

### id 396
- noisy: `हिन्दु धर्मका कारण बेकार छन्, अब रहेनन् ।`
- final: `हिन्दु धर्मका कारण बेकार छन्, अब रहेनन्।`
- Source itself is broken; kept as-is. Mark unintelligible, don't guess.

### id 243 / id 411
- id 243 `कुकुर खाँदै।` and id 411 `खातामा पोस्ट गर्नुहोस्।` kept as-is fragments that are either incomplete or garbage. Low risk but worth flagging.

---

## Notes on duplicates in the noisy source (not errors, FYI)

Some noisy rows are near-duplicates; the final maps them to identical or near-identical output. Confirmed pairs: 222/430, 408/456, 61/296, 236/294, 203/238, 13/250, 333/462/491. You may want to dedupe or keep as-is knowingly.