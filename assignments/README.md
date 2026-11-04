# open_for_discussion
some random dataset for understanding NLP and finding suitable answer







- flicker_8k is popular dataset and its been translated across multiple language . Folder has a lot of its online translation done. How good this translation work across cross lingual/modal retrieval and translation evaluation.(Data taken from various kaggle datasets )


- synthetic_toxicity is translated using antigravity with two varients translated. The data is from amazing ( (https://huggingface.co/datasets/biraj-bhusal/rakshak-nepali-toxicity-final) ). The two method of translation was to show properly problem with roman typing and post correction. How it behaves with your sentiment/toxicity classification system given 3 varients of data ?


- asr_postcorrection is a inference from asr engine and shows why sometime only a domain specific asr shall work else would be hard problem to solve. This also asks what and how well postcorrection shall be done where sometimes a dialect that sounds a bit different shall be treated as noise when it is correct.



- close_translatin is a opinionanted translation dataset. Domain adaptation is not just (government, medical, news and such ) rather a general term of style a area has. This dataset is meant to explore how you can adapt to certain style of translation. 



- imagenet_nepali data is translated in word level using google translate (2025) and was an attempt to solve the problem to make such that an accessible tool for blinds following paper of (https://scholar.google.com/citations?view_op=view_citation&hl=en&user=wgrnT1oAAAAJ&cstart=20&pagesize=80&sortby=pubdate&citation_for_view=wgrnT1oAAAAJ:BrmTIyaxlBUC) but the problem is the native words and such thats missing a lot the file is incomplete in sense that it was work in progress and obvious mistakes were attempted to delete. With rise of image captionining itself https://ilprl.ku.edu.np/publications/55 following this paper the problem still persists about how nepali native caption dataset isnt still available. One idea is meaning level translation and mapping embeddings of meaning to nepali dictionary. 