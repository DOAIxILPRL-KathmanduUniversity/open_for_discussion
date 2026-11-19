import json
import re
import difflib
from pathlib import Path

DIR = Path("/Users/paramanada/Desktop/opencode_data/articles_eval_nepali_journals/nepali_papers/translation")
ROOT = DIR.parent
INCOMING = DIR / "_incoming"
DEV = re.compile(r"[\u0900-\u097F]")

paper_1 = {
    "paper_id": "nepjol_foarticle53824",
    "american_english": (
        "Abstract: Hindu society is fundamentally based on the caste system. "
        "It is found that castes developed from the four varnas—Brahmin, Chhetri, Vaishya, and Shudra—described in the Later Vedic period. "
        "Hindu sacraments have also played an important role in giving continuity to the caste system for 3,500 years. "
        "Sacraments perform the function of putting religious ideas into practical practice. "
        "In this study, the role played by the Hindu Upanayana sacrament in the caste system is explored. "
        "This study is based on secondary sources, namely the provisions regarding the Upanayana sacrament found in Hindu religious scriptures. "
        "How these provisions have structured the caste system is analyzed. "
        "The Upanayana sacrament confers upon an individual the eligibility for acquiring knowledge and a level of purity. "
        "Among Hindus, the Shudra varna and women do not have the opportunity for Upanayana. "
        "Only Brahmins, Chhetris, and Vaishyas have the opportunity for Upanayana; however, discriminatory arrangements exist within this sacrament. "
        "The Upanayana sacrament establishes provisions for prohibition and discrimination among Hindus. "
        "This has maintained caste stratification among Hindus themselves and is found to have played an important role in sustaining the caste system."
    ),
    "british_english": (
        "Abstract: Hindu society is fundamentally based on the caste system. "
        "It is found that castes developed from the four varnas—Brahmin, Chhetri, Vaishya and Shudra—described in the Later Vedic period. "
        "Hindu sacraments have also played an important role in providing continuity to the caste system for 3,500 years. "
        "Sacraments perform the function of translating religious ideas into practical application. "
        "In this study, the role played by the Hindu Upanayana sacrament in the caste system is investigated. "
        "This study is based on secondary sources, namely the provisions relating to the Upanayana sacrament found in Hindu religious scriptures. "
        "How these provisions have structured the caste system is analysed. "
        "The Upanayana sacrament confers upon an individual the eligibility for acquiring knowledge and a degree of purity. "
        "Among Hindus, the Shudra varna and women have no opportunity for Upanayana. "
        "Only Brahmins, Chhetris and Vaishyas have the opportunity for Upanayana; however, discriminatory arrangements exist within this sacrament. "
        "The Upanayana sacrament establishes provisions for prohibition and discrimination among Hindus. "
        "This has maintained caste stratification amongst Hindus themselves and is found to have played an important role in sustaining the caste system."
    ),
    "australian_english": (
        "Abstract: Hindu society is fundamentally based on the caste system. "
        "Castes are found to have developed out of the four varnas described in the Later Vedic period—Brahmin, Chhetri, Vaishya and Shudra. "
        "Hindu sacraments have also played an important part in giving continuity to the caste system for 3,500 years. "
        "Sacraments do the work of putting religious ideas into practical practice. "
        "In this study, the role played by the Hindu Upanayana sacrament in the caste system is examined. "
        "This study is based on secondary sources, namely the provisions regarding the Upanayana sacrament in Hindu religious scriptures. "
        "How these provisions have structured the caste system is analysed. "
        "The Upanayana sacrament gives an individual the eligibility for acquiring knowledge and a level of purity. "
        "Among Hindus, the Shudra varna and women do not have the opportunity for Upanayana. "
        "Only Brahmins, Chhetris and Vaishyas have the opportunity for Upanayana; however, discriminatory arrangements exist within this sacrament. "
        "The Upanayana sacrament sets up provisions for prohibition and discrimination among Hindus. "
        "This has maintained caste stratification among Hindus themselves and is found to have played an important role in sustaining the caste system."
    ),
    "informal_english": (
        "Abstract: Hindu society is basically based on the caste system, eh. "
        "Turns out castes developed out of the four varnas described in the Later Vedic period—Brahmin, Chhetri, Vaishya and Shudra. "
        "Hindu rituals have also played a bloody big part in keeping the caste system going for 3,500 years. "
        "Rituals do the work of putting religious ideas into everyday practice. "
        "In this study, the role played by the Hindu Upanayana ritual in the caste system is checked out. "
        "This study is based on secondary sources, namely the rules on the Upanayana ritual in Hindu religious scriptures. "
        "How these rules have structured the caste system is analysed. "
        "The Upanayana ritual gives a person the qualification for gaining knowledge and a level of purity. "
        "Among Hindus, the Shudra varna and women don't get a look-in for Upanayana. "
        "Only Brahmins, Chhetris and Vaishyas get the opportunity for Upanayana; however, discriminatory setups exist within this ritual. "
        "The Upanayana ritual sets up provisions for prohibition and discrimination among Hindus. "
        "This has maintained caste stratification among Hindus themselves and is found to have played a big role in keeping the caste system going."
    ),
    "translator_notes": "The source begins with the heading 'लेखसार' (Abstract); 'महŒवपूर्ण' represents ligature OCR for 'महत्त्वपूर्ण'. Strict sentence order and clause structure preserved across all 12 sentences. Varna names and the rite 'उपनयन संस्कार' (Upanayana sacrament) transliterated. Informal flavour: New Zealand casual."
}

paper_2 = {
    "paper_id": "nepjol_foarticle51577",
    "american_english": (
        "The article concerning the educational participation of Magar children studying at the primary level is a study based on primary schools in Tanahun district. "
        "The main objectives of this study include identifying the participation and analyzing the access of Magar children in school education, and identifying the hindering factors of Magar children's educational problems in education and discovering measures for problem-solving. "
        "To make the study systematic and orderly, a review of related literature was conducted to examine comparatively with various theories and studies, analyze, and draw conclusions. "
        "Paulo Freire's Pedagogy of Oppressed was taken as the main theory of the study. "
        "Under the study methodology, a research design was developed, and the population and sample were selected. "
        "Two schools in Tanahun district where Magar-speaking students were studying were selected for the study. "
        "Using diverse research tools, the obtained facts and data were comparatively analyzed. "
        "Toward solving the problems, the study has pointed out several recommendations. "
        "Among these, it appears that special concessions must be provided to underprivileged Magar children, non-discriminatory teaching must be given to Magar children, and the school must prepare an environment according to an inclusive concept. "
        "The involvement of the Magar community in school development and management must be increased, whereby it was seen that the sense of school ownership in the Magar community would increase. "
        "Matters such as increasing the access of indigenous nationalities and linguistic minority children to education, providing education in the mother tongue, and teaching in a child-friendly environment are pointed out in this study."
    ),
    "british_english": (
        "The article concerning the educational participation of Magar children studying at the primary level is a study based on primary schools in Tanahun district. "
        "The main objectives of this study include identifying the participation and analysing the access of Magar children in school education, and identifying the hindering factors of Magar children's educational problems in education and discovering measures for problem-solving. "
        "To make the study systematic and orderly, a review of related literature was conducted to examine comparatively with various theories and studies, analyse, and draw conclusions. "
        "Paulo Freire's Pedagogy of Oppressed was taken as the main theory of the study. "
        "Under the study methodology, a research design was developed, and the population and sample were selected. "
        "Two schools in Tanahun district where Magar-speaking students were studying were selected for the study. "
        "Using diverse research tools, the obtained facts and data were comparatively analysed. "
        "Towards solving the problems, the study has pointed out several recommendations. "
        "Amongst these, it appears that special concessions must be provided to underprivileged Magar children, non-discriminatory teaching must be given to Magar children, and the school must prepare an environment according to an inclusive concept. "
        "The involvement of the Magar community in school development and management must be increased, whereby it was seen that the sense of school ownership in the Magar community would increase. "
        "Matters such as increasing the access of indigenous nationalities and linguistic minority children to education, providing education in the mother tongue, and teaching in a child-friendly environment are pointed out in this study."
    ),
    "australian_english": (
        "The article concerning the educational participation of Magar children studying at the primary level is a study based on primary schools in Tanahun district. "
        "The main objectives of this study include identifying the participation and analysing the access of Magar children in school education, and identifying the hindering factors of Magar children's educational problems in education and discovering measures for problem-solving. "
        "To make the study systematic and orderly, a review of related literature was conducted to examine comparatively with various theories and studies, analyse, and draw conclusions. "
        "Paulo Freire's Pedagogy of Oppressed was taken as the main theory of the study. "
        "Under the study methodology, a research design was developed, and the population and sample were selected. "
        "Two schools in Tanahun district where Magar-speaking students were studying were selected for the study. "
        "Using diverse research tools, the obtained facts and data were comparatively analysed. "
        "Towards solving the problems, the study has pointed out several recommendations. "
        "Among these, it appears that special concessions must be provided to underprivileged Magar children, non-discriminatory teaching must be given to Magar children, and the school must prepare an environment according to an inclusive concept. "
        "The involvement of the Magar community in school development and management must be increased, whereby it was seen that the sense of school ownership in the Magar community would increase. "
        "Matters such as increasing the access of indigenous nationalities and linguistic minority children to education, providing education in the mother tongue, and teaching in a child-friendly environment are pointed out in this study."
    ),
    "informal_english": (
        "This article about the educational participation of Magar children studying at the primary level is a study based on primary schools in Tanahun district. "
        "The main goals of this study include identifying the participation and analyzing the access of Magar children in school education, and pinpointing the roadblock factors behind Magar kids' educational problems in education and finding ways to solve them. "
        "To keep the study organized and systematic, a review of related literature was conducted to examine comparatively with various theories and studies, analyze, and draw conclusions. "
        "Paulo Freire's Pedagogy of Oppressed was taken as the main theory of the study. "
        "Under the study methodology, a research framework was put together, and the population and sample were selected. "
        "Two schools in Tanahun district where Magar-speaking students were studying were picked for the study. "
        "Using various research tools, the obtained facts and data were comparatively analyzed. "
        "To help solve the problems, the study has pointed out several recommendations. "
        "Among these, it looks like special concessions must be provided to underprivileged Magar kids, non-discriminatory teaching must be given to Magar kids, and the school has to set up an environment according to an inclusive concept. "
        "Magar community involvement in school development and management must be boosted, whereby it was seen that a sense of school ownership in the Magar community would increase. "
        "Things like expanding educational access for indigenous nationalities and linguistic minority kids, providing schooling in their mother tongue, and teaching in a child-friendly environment are all pointed out in this study."
    ),
    "translator_notes": "OCR error 'जसबाटगर' in sentence 10 reflects 'जसबाट मगर' (whereby in the Magar community). The source abstract includes 'Pedagogy of Oppressed' verbatim in Roman script. Strict sentence order preserved across all 11 sentences. Informal flavour: American casual."
}

paper_3 = {
    "paper_id": "nepjol_foarticle61656",
    "american_english": (
        "The Tharu people have traditionally been living in the Terai region of Nepal. "
        "Their main occupation is agriculture. "
        "Farming with full diligence during agricultural seasons, and catching fish and enjoying music and songs at other times, is their main daily routine; however, nowadays they have also begun to engage in various occupations, businesses, foreign employment, and so forth. "
        "They are also known as a fun-loving, straightforward, and honest community who practice no deceit against anyone. "
        "Whether celebrating any festival or performing rites of passage, and whether when starting cultivation or during leisure time after planting, they perform various dances and make merry singing various songs to accompany those dances. "
        "These songs or dances also vary from place to place. "
        "In this study, research has been conducted from the perspective of what kinds of songs are sung in the dances performed by the Tharu people residing in the Nawalpur area of Gandaki Province, Nepal. "
        "Studying from this perspective, it is concluded that the Tharu people of Nawalpur perform folk dances such as Mendari, Jhumra, Rasdhari, Jogeda, and Jatsari to the rhythm of traditional musical instruments on different occasions, and sing songs of their own respective styles in these dances."
    ),
    "british_english": (
        "The Tharu people have traditionally lived in the Terai region of Nepal. "
        "Their main occupation is agriculture. "
        "Farming with full diligence during agricultural seasons, and catching fish and enjoying music and songs at other times, is their main daily routine; however, nowadays they have also begun to engage in various occupations, businesses, foreign employment and so forth. "
        "They are also known as a fun-loving, straightforward and honest community who practice no deceit against anyone. "
        "Whether celebrating any festival or performing rites of passage, and whether when starting cultivation or during leisure time after planting, they perform various dances and make merry singing various songs to accompany those dances. "
        "These songs or dances also vary from place to place. "
        "In this study, research has been conducted from the perspective of what kinds of songs are sung in the dances performed by the Tharu people residing in the Nawalpur area of Gandaki Province, Nepal. "
        "Studying from this perspective, it is concluded that the Tharu people of Nawalpur perform folk dances such as Mendari, Jhumra, Rasdhari, Jogeda and Jatsari to the rhythm of traditional musical instruments on different occasions, and sing songs of their own respective styles in these dances."
    ),
    "australian_english": (
        "The Tharu people have traditionally lived in the Terai region of Nepal. "
        "Their main occupation is farming. "
        "Working hard at farming during agricultural seasons, and catching fish and enjoying music and songs at other times, is their main daily routine; though nowadays they have also begun to engage in various jobs, businesses, foreign employment and so forth. "
        "They are also known as a fun-loving, straightforward and honest community who don't practice deceit against anyone. "
        "Whether celebrating any festival or performing rites, and whether starting planting or during leisure time after planting, they perform various dances and enjoy singing various songs to accompany those dances. "
        "These songs or dances also differ from place to place. "
        "In this study, research has been carried out from the perspective of what kinds of songs are sung in the dances performed by the Tharu people living in the Nawalpur area of Gandaki Province, Nepal. "
        "Looking from this perspective, it is concluded that the Tharu people of Nawalpur perform folk dances such as Mendari, Jhumra, Rasdhari, Jogeda and Jatsari to the rhythm of traditional musical instruments on different occasions, and sing songs in their own respective styles in these dances."
    ),
    "informal_english": (
        "The Tharu folk have lived in the Terai region of Nepal since way back. "
        "Their main line of work is farming. "
        "Putting their backs into farming during planting seasons, and catching fish and enjoying tunes and songs at other times, is pretty much their daily routine; mind you, nowadays they have also started getting into all sorts of jobs, businesses, overseas work and what have you. "
        "They are also known as a good-humoured, straightforward and straight-up folk who wouldn't dream of pulling a fast one on anyone. "
        "Whether having a festival or doing a proper rite of passage, and whether starting planting or during a bit of downtime after planting, they put on all sorts of dances and have a right good time singing various songs along to those dances. "
        "These songs or dances also differ quite a bit from place to place. "
        "In this study, things are looked at from the perspective of what sorts of songs are sung in the dances put on by the Tharu folk living in the Nawalpur area of Gandaki Province, Nepal. "
        "Looking at it from this perspective, the takeaway is that the Tharu folk of Nawalpur perform folk dances such as Mendari, Jhumra, Rasdhari, Jogeda and Jatsari to the rhythm of traditional musical instruments on different occasions, and sing songs in their own styles during these dances."
    ),
    "translator_notes": "Source contains minor OCR artifacts including repeated subject 'थारू नवलपुरका थारू जातिले', 'गाउँर' for 'गाएर', and ligature 'आआÇनै' for 'आआफ्नै'. Traditional folk dance names (Mendari, Jhumra, Rasdhari, Jogeda, Jatsari) transliterated. Strict sentence order preserved across all 8 sentences. Informal flavour: British casual."
}

papers = [paper_1, paper_2, paper_3]

for p in papers:
    pid = p["paper_id"]
    us = p["american_english"]
    uk = p["british_english"]
    au = p["australian_english"]
    inf = p["informal_english"]
    r_uk = difflib.SequenceMatcher(None, us, uk).ratio()
    r_au = difflib.SequenceMatcher(None, us, au).ratio()
    r_inf = difflib.SequenceMatcher(None, us, inf).ratio()
    print(f"[{pid}] US/UK: {r_uk:.2f}, US/AU: {r_au:.2f}, US/INF: {r_inf:.2f}")

    for f in ["american_english", "british_english", "australian_english", "informal_english"]:
        dev_chars = len(DEV.findall(p[f]))
        assert dev_chars <= 12, f"{pid} {f} has {dev_chars} Devanagari chars"

    # Write to _incoming
    target_path = INCOMING / f"{pid}.json"
    target_path.write_text(json.dumps(p, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Wrote {target_path}")

print("All 3 papers written successfully.")
