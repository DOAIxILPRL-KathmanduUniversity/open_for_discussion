# Taxonomy of Roboflow Classification Datasets

**Overview**: Analysis of **300 classification projects** harvested from Roboflow Universe (`classification downloads>10`).

This document outlines the domain taxonomy, data scale distributions, sample class schemas, and cross-application patterns for computer vision classification datasets.

---
## Summary Statistics across Domains

| Domain Category | Dataset Count | Typical Image Scale | Key Problem Types |
|-----------------|---------------|---------------------|-------------------|
| **Agriculture, Crop Pathology & Plant Health** | 34 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |
| **Human Action, Pose, Emotion & Safety** | 23 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |
| **Art, Architecture, Fashion & Geology** | 28 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |
| **Medical & Healthcare Diagnostics** | 59 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |
| **Animal, Insects & Wildlife** | 21 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |
| **Benchmarks, Gaming & Synthetic Datasets** | 4 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |
| **Industrial, Waste & Environmental Monitoring** | 24 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |
| **Other Specialized Applications** | 79 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |
| **Vehicles, Aerospace & Transportation** | 18 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |
| **Document, OCR, Currency & Security** | 10 | 500 – 70,000 images | Fine-grained classification, Binary anomaly, Multi-class multi-label |

---

## Agriculture, Crop Pathology & Plant Health (34 Projects)

### Banana Ripeness Classification
- **Author / Source**: `Roboflow Universe Projects`
- **Scale**: `5.62k images` | `3 models` | `1.89k downloads/stars`
- **Classes / Taxonomy**: `overripe`, `ripe`, `freshripe`, `freshunripe`, `rotten`, `unripe`

### Potato Image Classification
- **Author / Source**: `Potato blight`
- **Scale**: `1.5k images` | `N/A` | `103 downloads/stars`
- **Classes / Taxonomy**: `Potato___Early_blight`, `Potato___Late_blight`, `Potato___healthy`

### cassava disease
- **Author / Source**: `Moneypuckyow`
- **Scale**: `5.28k images` | `N/A` | `19 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `cbb`, `cbsd`, `cgm`, `cmd`

### bd_plant_diseases
- **Author / Source**: `plantdiseasesdataset`
- **Scale**: `30.6k images` | `1 model` | `19 downloads/stars`
- **Classes / Taxonomy**: `Cauliflower_Bacterial_spot_rot`, `Cauliflower_Black_Rot`, `Cauliflower_Downy_Mildew`, `Cauliflower_Healthy`, `Corn_Cercospora_leaf_spot_(Gray_leaf_spot)`, `Corn_Common_rust`, `Corn_Northern_Leaf_Blight`, `Corn_healthy`, `EggPlant_Healthy_Leaf`, `EggPlant_Insect_Pest_Disease` ... (+10 more)

### Vegetable Detection
- **Author / Source**: `Capstone`
- **Scale**: `9.01k images` | `1 model` | `21 downloads/stars`
- **Classes / Taxonomy**: `apple`, `banana`, `guava`, `lemon`, `mango`, `orange`, `pomegranate`, `strawberry`, `tomato`, `Bitter_Gourd_new` ... (+10 more)

### crop test
- **Author / Source**: `GJ Lee`
- **Scale**: `3.3k images` | `1 model` | `39 downloads/stars`
- **Classes / Taxonomy**: `banana`, `cabbage`, `carrot`, `guava`, `mango`, `papaya`, `pineapple`, `pumpkin`, `atemoya`, `bareland` ... (+1 more)

### cattle diseases
- **Author / Source**: `sliit`
- **Scale**: `834 images` | `1 model` | `481 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `(BRD)`, `Bovine`, `Contagious`, `Dermatitis`, `Disease`, `Ecthym`, `Respiratory`, `Unlabeled`, `lumpy` ... (+1 more)

### Pineapple Maturity Detection
- **Author / Source**: `Pineapple maturity`
- **Scale**: `805 images` | `2 models` | `15 downloads/stars`
- **Classes / Taxonomy**: `ripen`, `ripen unripen`, `unripen`

### Level of Disease in leaf
- **Author / Source**: `Titan Workspace`
- **Scale**: `2.57k images` | `1 model` | `27 downloads/stars`
- **Classes / Taxonomy**: `Aphids`, `Early Blight`, `Healthy Leaf-`, `Leaf Curl`, `Leafhoppers and Jassids`, `Molds`, `Mosaic Virus`, `Septoria`, `Unlabeled`, `bactarial canker` ... (+9 more)

### Ayurved
- **Author / Source**: `Ayurved`
- **Scale**: `993 images` | `1 model` | `11 downloads/stars`
- **Classes / Taxonomy**: `Ashwagandha`, `Cardamom`, `Cumin`, `Neem`, `Test`, `Turmeric`, `rama`, `tulsi`

### rust_detection２
- **Author / Source**: `p5l65lca@s.okayama-u.ac.jp`
- **Scale**: `48 images` | `N/A` | `48 downloads/stars`
- **Classes / Taxonomy**: `rust`

### Red and Green Apples Single Classification
- **Author / Source**: `Apples`
- **Scale**: `603 images` | `1 model` | `39 downloads/stars`
- **Classes / Taxonomy**: `green`, `red`, `Unlabeled`

### Rotten apples detection
- **Author / Source**: `Universidadde de TrsosMontes e Alto Douro`
- **Scale**: `396 images` | `3 models` | `84 downloads/stars`
- **Classes / Taxonomy**: `Good Apple`, `Rotten Apple`

### Mushroom Identifier
- **Author / Source**: `university`
- **Scale**: `4k images` | `1 model` | `18 downloads/stars`
- **Classes / Taxonomy**: `Abrupta`, `Agaricus`, `Alloclavaria`, `Amanita`, `Bisporella`, `Boletus`, `Chanterelle`, `Chlorociboria`, `Clathrus`, `Cordyceps` ... (+10 more)

### Fruits & Vegetable Status Detect
- **Author / Source**: `LearningHub`
- **Scale**: `9.12k images` | `N/A` | `14 downloads/stars`
- **Classes / Taxonomy**: `FreshApple`, `FreshBanana`, `FreshBellpepper`, `FreshCarrot`, `FreshCucumber`, `FreshMango`, `FreshOrange`, `FreshPotato`, `FreshStrawberry`, `FreshTomato` ... (+10 more)

### Invasive Plant Species Detection
- **Author / Source**: `Jordan+Pedro Projects`
- **Scale**: `1.4k images` | `N/A` | `34 downloads/stars`
- **Classes / Taxonomy**: `American skunk cabbage`, `Chilean rhubarb`, `Curly waterweed`, `Floating pennywort`, `Giant hogweed`, `Himalayan balsam`, `Non-invasive`, `Nuttalls waterweed`, `Parrots feather`

### Klasifikasi Kematangan Sawit
- **Author / Source**: `Klasifikasi Testing`
- **Scale**: `486 images` | `1 model` | `40 downloads/stars`
- **Classes / Taxonomy**: `Matang`, `Mengkal`, `Mentah`, `Unlabeled`

### banana-shelf-life
- **Author / Source**: `Ranjan`
- **Scale**: `2.28k images` | `1 model` | `27 downloads/stars`
- **Classes / Taxonomy**: `overripe`, `ripe`, `freshripe`, `freshunripe`, `rotten`, `unripe`

### gaba
- **Author / Source**: `myApple`
- **Scale**: `993 images` | `2 models` | `12 downloads/stars`
- **Classes / Taxonomy**: `good`, `bad`, `fresh_apple`, `fresh_apple rotten_apple`, `rotten_apple`

### Rice leaf disease detection
- **Author / Source**: `Project`
- **Scale**: `2.45k images` | `1 model` | `49 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `bacterial_leaf_blight`, `brown_spot`, `leaf_blast`, `leaf_scald`, `narrow_brown_spot`

### Cannabis
- **Author / Source**: `Byron Wade`
- **Scale**: `387 images` | `3 models` | `12 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `Indica`, `Unlabeled`, `bud`, `female`, `hybrid`, `male`, `sativa`, `young`

### palm-fruit-ripeness-classificationcnn
- **Author / Source**: `Palm Fruit Classification`
- **Scale**: `3.02k images` | `1 model` | `271 downloads/stars`
- **Classes / Taxonomy**: `overripe`, `ripe`, `empty_bunch`, `rotten`, `underripe`, `unripe`

### VegetableYolov8Classification
- **Author / Source**: `Suchit Bapatla`
- **Scale**: `9.84k images` | `1 model` | `36 downloads/stars`
- **Classes / Taxonomy**: `Bean`, `Bitter_Gourd`, `Bottle_Gourd`, `Brinjal`, `Broccoli`, `Cabbage`, `Capsicum`, `Carrot`, `Cauliflower`, `Cucumber` ... (+5 more)

### Chili leaves disease classification
- **Author / Source**: `Chili leaves disease classification`
- **Scale**: `1.15k images` | `1 model` | `30 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `leaf spot`, `whitefly`, `leaf curl`, `powdery mildew`, `yellowish`

### Cattle Detection
- **Author / Source**: `Cattle`
- **Scale**: `29 images` | `1 model` | `12 downloads/stars`
- **Classes / Taxonomy**: `cattle`, `Unlabeled`

### Cucumber_Leaf
- **Author / Source**: `agriDetect`
- **Scale**: `799 images` | `N/A` | `11 downloads/stars`
- **Classes / Taxonomy**: `Anthracnose`, `Bacterial_Wilt`, `Downy_Mildew`, `Fresh_Leaf`, `Gummy_Stem_Blight`

### Plants Classification
- **Author / Source**: `PTIT`
- **Scale**: `1.69k images` | `1 model` | `28 downloads/stars`
- **Classes / Taxonomy**: `bạc hà - mentha spicata`, `cau tiểu trâm - chamaedorea elegans`, `chuỗi ngọc - sedum morganianum`, `cúc centaurea montana - centaurea montana`, `cải bó xôi - spinacia oleracea`, `cải bắp - brassica oleracea`, `cải bẹ xanh - brassica juncea`, `cải làn - nasturtium officinale`, `cải ngọt - lactuca sativa`, `cải thìa - lactuca sativa` ... (+10 more)

### Pepper
- **Author / Source**: `ApisInaturalist10`
- **Scale**: `3.08k images` | `1 model` | `23 downloads/stars`
- **Classes / Taxonomy**: `Fusarium`, `Healthy`, `Leaf Blight`, `Leaf Curl`, `Mosaic`, `Septoria`

### Mushroom Classification
- **Author / Source**: `project`
- **Scale**: `258 images` | `1 model` | `27 downloads/stars`
- **Classes / Taxonomy**: `non-toxic`, `toxic`

### mushroom
- **Author / Source**: `huurhuntergel`
- **Scale**: `1.55k images` | `1 model` | `18 downloads/stars`
- **Classes / Taxonomy**: `edible`, `poisonous`

### bananaClassification
- **Author / Source**: `ChuoiPro`
- **Scale**: `2.85k images` | `1 model` | `13 downloads/stars`
- **Classes / Taxonomy**: `overripe`, `freshripe`, `freshunripe`

### crop_recognition
- **Author / Source**: `SYED ZAIN UL ABIDIN`
- **Scale**: `2.43k images` | `N/A` | `21 downloads/stars`
- **Classes / Taxonomy**: `cotton`, `rice`, `wheat`, `maize`, `sugarcane`

### olive_Classification_crop
- **Author / Source**: `Dataset`
- **Scale**: `1.33k images` | `N/A` | `14 downloads/stars`
- **Classes / Taxonomy**: `Ragham_1`, `Ragham_2`, `Ragham_3`, `Ragham_4`, `Ragham_5`

### pepper
- **Author / Source**: `plant virus`
- **Scale**: `1.35k images` | `1 model` | `12 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `anthracnose`

## Human Action, Pose, Emotion & Safety (23 Projects)

### Violence&not_violence
- **Author / Source**: `Dinesh Nariani`
- **Scale**: `10k images` | `1 model` | `130 downloads/stars`
- **Classes / Taxonomy**: `non_violence`, `violence`

### Detected Images Violence
- **Author / Source**: `KietWS`
- **Scale**: `9.91k images` | `1 model` | `128 downloads/stars`
- **Classes / Taxonomy**: `non_violence`, `violence`

### gender
- **Author / Source**: `Seeed Studio`
- **Scale**: `10k images` | `1 model` | `238 downloads/stars`
- **Classes / Taxonomy**: `Female`, `Male`

### Yoga Pose
- **Author / Source**: `New Workspace`
- **Scale**: `5.89k images` | `N/A` | `539 downloads/stars`
- **Classes / Taxonomy**: `adho mukha svanasana`, `adho mukha vriksasana`, `agnistambhasana`, `ananda balasana`, `anantasana`, `anjaneyasana`, `ardha bhekasana`, `ardha chandrasana`, `ardha matsyendrasana`, `ardha pincha mayurasana` ... (+10 more)

### Sign Language Detectiom
- **Author / Source**: `nmims`
- **Scale**: `9.98k images` | `N/A` | `91 downloads/stars`
- **Classes / Taxonomy**: `stand`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `A` ... (+9 more)

### Emotion Recognition
- **Author / Source**: `tenifayo`
- **Scale**: `9.84k images` | `1 model` | `75 downloads/stars`
- **Classes / Taxonomy**: `angry`, `neutral`, `Unlabeled`, `disgust`, `fear`, `happy`, `sad`, `surprise`

### Child Adult Classifier
- **Author / Source**: `Object Detection`
- **Scale**: `797 images` | `1 model` | `78 downloads/stars`
- **Classes / Taxonomy**: `adults`, `children`

### data-set-person-armed-segmented
- **Author / Source**: `Miguel Alejandro Ponce Proaño`
- **Scale**: `808 images` | `N/A` | `65 downloads/stars`
- **Classes / Taxonomy**: `person-armed`, `person-not-armed`

### Yoga Pose
- **Author / Source**: `SeeThrough`
- **Scale**: `4.59k images` | `1 model` | `28 downloads/stars`
- **Classes / Taxonomy**: `Adho`, `Alanasana`, `Anjaneyasana`, `Ardha`, `Ashta`, `Baddha`, `Bakasana`, `Balasana`, `Bandha`, `Bhujangasana` ... (+10 more)

### Blind Assist
- **Author / Source**: `Samrat`
- **Scale**: `5.7k images` | `1 model` | `18 downloads/stars`
- **Classes / Taxonomy**: `1-rupee-coin`, `10`, `10-Rupees`, `10-rupee-coin`, `100`, `100-Rupees`, `2`, `20`, `20-Rupees`, `200` ... (+9 more)

### FER Final Project
- **Author / Source**: `FER Group 6`
- **Scale**: `5.5k images` | `1 model` | `47 downloads/stars`
- **Classes / Taxonomy**: `Anger`, `Disgust`, `Fear`, `Happy`, `N`, `Sadness`, `Surprise`

### Face Shape Classification
- **Author / Source**: `Project`
- **Scale**: `5k images` | `1 model` | `13 downloads/stars`
- **Classes / Taxonomy**: `Heart`, `Oblong`, `Oval`, `Round`, `Square`

### BAD GOOD sitting position
- **Author / Source**: `Zouari Rami`
- **Scale**: `67 images` | `N/A` | `90 downloads/stars`
- **Classes / Taxonomy**: `Bad`, `Good`, `Unlabeled`

### Gym or yoga
- **Author / Source**: `1st`
- **Scale**: `9.67k images` | `1 model` | `14 downloads/stars`
- **Classes / Taxonomy**: `bench`, `hammer`, `Unlabeled`, `adho`, `agnistambhasana`, `ananda`, `anantasana`, `anjaneyasana`, `ardha`, `ashtanga` ... (+10 more)

### Face Shape Classification
- **Author / Source**: `Project`
- **Scale**: `4.9k images` | `1 model` | `75 downloads/stars`
- **Classes / Taxonomy**: `Heart`, `Oblong`, `Oval`, `Round`, `Square`

### Workout Pose Detection
- **Author / Source**: `Serena Suni`
- **Scale**: `370 images` | `1 model` | `18 downloads/stars`
- **Classes / Taxonomy**: `bicep curl`, `jumping jack`, `lunge`, `plank exercise`, `pushup`

### Violence Detection
- **Author / Source**: `SecureCampus`
- **Scale**: `9.39k images` | `1 model` | `23 downloads/stars`
- **Classes / Taxonomy**: `NonViolence`, `Violence`

### Sleep poses
- **Author / Source**: `Sleep pose`
- **Scale**: `137 images` | `N/A` | `147 downloads/stars`
- **Classes / Taxonomy**: `Back`, `Fetal`, `Side`, `Stomach`

### subway surfer auto play
- **Author / Source**: `Sapienza`
- **Scale**: `151 images` | `1 model` | `250 downloads/stars`
- **Classes / Taxonomy**: `down`, `Unlabeled`, `left`, `nothing`, `right`, `up`

### Pose
- **Author / Source**: `lingfeng Gu`
- **Scale**: `4.94k images` | `N/A` | `11 downloads/stars`
- **Classes / Taxonomy**: `Lying`, `Sitting`, `Standing`

### train 7 pose
- **Author / Source**: `UPI`
- **Scale**: `642 images` | `1 model` | `36 downloads/stars`
- **Classes / Taxonomy**: `bridge pose`, `cobra pose`, `downward dog pose`, `mountain pose`, `tree pose`, `triangle pose`, `warrior pose`

### Face Shape
- **Author / Source**: `yes`
- **Scale**: `4.78k images` | `1 model` | `20 downloads/stars`
- **Classes / Taxonomy**: `short`, `88`, `Heart`, `Oblong`, `Oval`, `Round`, `Square`, `Unlabeled`, `heart`, `oblong` ... (+1 more)

### Yoga_Postures
- **Author / Source**: `SeeThrough`
- **Scale**: `4.58k images` | `N/A` | `24 downloads/stars`
- **Classes / Taxonomy**: `Adho`, `Alanasana`, `Anjaneyasana`, `Ardha`, `Ashta`, `Baddha`, `Bakasana`, `Balasana`, `Bandha`, `Bhujangasana` ... (+44 more)

## Art, Architecture, Fashion & Geology (28 Projects)

### MIT Indoor Scene Recognition
- **Author / Source**: `Popular Benchmarks`
- **Scale**: `15.6k images` | `1 model` | `609 downloads/stars`
- **Classes / Taxonomy**: `bakery`, `kitchen`, `airport_inside`, `artstudio`, `auditorium`, `bar`, `bathroom`, `bedroom`, `bookstore`, `bowling` ... (+10 more)

### Rock clasfication
- **Author / Source**: `William CWSR`
- **Scale**: `1.75k images` | `1 model` | `34 downloads/stars`
- **Classes / Taxonomy**: `Basalt`, `Clay`, `Conglomerate`, `Diatomite`, `Shale-(Mudstone)`, `Siliceous-sinter`, `chert`, `gypsum`, `olivine-basalt`

### wiki art
- **Author / Source**: `Art Dataset`
- **Scale**: `6.42k images` | `2 models` | `322 downloads/stars`
- **Classes / Taxonomy**: `Abstract_Expressionism`, `Action_painting`, `Analytical_Cubism`, `Art_Nouveau_Modern`, `Baroque`, `Color_Field_Painting`, `Contemporary_Realism`, `Cubism`, `Early_Renaissance`, `Expressionism` ... (+10 more)

### Nike Adidas and Converse Shoes Classification
- **Author / Source**: `Popular Benchmarks`
- **Scale**: `825 images` | `2 models` | `266 downloads/stars`
- **Classes / Taxonomy**: `nike`, `adidas`, `converse`

### Rooms
- **Author / Source**: `TD Bryant`
- **Scale**: `5.19k images` | `N/A` | `37 downloads/stars`
- **Classes / Taxonomy**: `Bathroom`, `Bedroom`, `Dinning`, `Kitchen`, `Livingroom`

### Shape Color Classifier
- **Author / Source**: `UAS2030`
- **Scale**: `1.01k images` | `N/A` | `14 downloads/stars`
- **Classes / Taxonomy**: `blue`, `green`, `orange`, `red`, `yellow`, `black`, `brown`, `gray`, `purple`, `white`

### Cannavizion
- **Author / Source**: `Cannavizion Workspace`
- **Scale**: `198 images` | `2 models` | `18 downloads/stars`
- **Classes / Taxonomy**: `Aphids`, `Calcium Deficiency`, `Iron Deficiency`, `Magnesium Deficiency`, `Manganese Deficiency`, `Nitrogen Deficiency`, `PH Fluctuation`, `Phosphorus Deficiency`, `Potassium Deficiency`, `Powdery Mildew` ... (+1 more)

### oxford flowers 102
- **Author / Source**: `workspace`
- **Scale**: `8.19k images` | `1 model` | `20 downloads/stars`
- **Classes / Taxonomy**: `10`, `100`, `101`, `102`, `11`, `12`, `13`, `14`, `15`, `16` ... (+9 more)

### rock life detection
- **Author / Source**: `William CWSR`
- **Scale**: `1.75k images` | `1 model` | `12 downloads/stars`
- **Classes / Taxonomy**: `(Mudstone)`, `Basalt`, `Clay`, `Conglomerate`, `Diatomite`, `Shale`, `Siliceous`, `basalt`, `chert`, `gypsum` ... (+2 more)

### Indonesia Batik Classification
- **Author / Source**: `Muhammad Rendi`
- **Scale**: `716 images` | `1 model` | `20 downloads/stars`
- **Classes / Taxonomy**: `Batik Barong`, `Batik Betawi`, `Batik Buketan`, `Batik Endek Bali`, `Batik Gunungan`, `Batik Jepara`, `Batik Kawung`, `Batik Megamendung`, `Batik Parang`, `Batik Prada` ... (+5 more)

### Laptop
- **Author / Source**: `Fernanda Mendoza`
- **Scale**: `171 images` | `N/A` | `19 downloads/stars`
- **Classes / Taxonomy**: `Laptop`

### arch2
- **Author / Source**: `umut`
- **Scale**: `9.64k images` | `1 model` | `20 downloads/stars`
- **Classes / Taxonomy**: `Achaemenid`, `American`, `AmericanFoursquare`, `AncientEgyptian`, `ArtDeco`, `ArtNouveau`, `Baroque`, `Bauhaus`, `Beaux-Arts`, `Byzantine` ... (+10 more)

### cans
- **Author / Source**: `cans and remotes object recognition`
- **Scale**: `468 images` | `1 model` | `47 downloads/stars`
- **Classes / Taxonomy**: `heavy-damage`, `light-damage`, `no damage`

### Fashion MNIST
- **Author / Source**: `Popular Benchmarks`
- **Scale**: `70k images` | `N/A` | `245 downloads/stars`
- **Classes / Taxonomy**: `bag`, `dress`, `shirt`, `trouser`, `ankle boot`, `coat`, `pullover`, `sandal`, `sneaker`, `tshirt_top`

### colorball
- **Author / Source**: `dataset`
- **Scale**: `114 images` | `1 model` | `28 downloads/stars`
- **Classes / Taxonomy**: `blue`, `green`, `red`, `Unlabeled`

### Alphanumeric Color Classifier
- **Author / Source**: `UAS2030`
- **Scale**: `1.01k images` | `N/A` | `13 downloads/stars`
- **Classes / Taxonomy**: `blue`, `green`, `orange`, `red`, `yellow`, `black`, `brown`, `gray`, `purple`, `white`

### ColorDataset
- **Author / Source**: `Narely Lima`
- **Scale**: `6.45k images` | `1 model` | `16 downloads/stars`
- **Classes / Taxonomy**: `blue`, `green`, `orange`, `red`, `yellow`, `black`, `brown`, `grey`, `pink`, `purple` ... (+3 more)

### Flowers
- **Author / Source**: `Joseph Nelson`
- **Scale**: `1.82k images` | `N/A` | `323 downloads/stars`
- **Classes / Taxonomy**: `daisy`, `dandelion`

### Flowers
- **Author / Source**: `National University of Science and Technology Pakistan`
- **Scale**: `3.34k images` | `N/A` | `156 downloads/stars`
- **Classes / Taxonomy**: `sunflower`, `Common Lanthana`, `Hibiscus`, `Jatropha`, `Marigold`, `Rose`, `champaka`, `chitrak`, `honeysuckle`, `indian mallow` ... (+3 more)

### Gemstone Classification
- **Author / Source**: `fma04@fayoum.edu.eg`
- **Scale**: `2.82k images` | `N/A` | `86 downloads/stars`
- **Classes / Taxonomy**: `Alexandrite`, `Almandine`, `Amazonite`, `Amber`, `Amethyst`, `Ametrine`, `Andalusite`, `Andradite`, `Aquamarine`, `Aventurine Green` ... (+10 more)

### Tables
- **Author / Source**: `Dimitar Dimitrov`
- **Scale**: `808 images` | `N/A` | `14 downloads/stars`
- **Classes / Taxonomy**: `table`, `images`

### Rock Paper Scissors
- **Author / Source**: `Joseph Nelson`
- **Scale**: `2.93k images` | `N/A` | `1.27k downloads/stars`
- **Classes / Taxonomy**: `paper`, `rock`, `scissors`

### Art Styles
- **Author / Source**: `Eric Xiong`
- **Scale**: `2.31k images` | `1 model` | `19 downloads/stars`
- **Classes / Taxonomy**: `Renaissance`, `Surrealism`, `Unlabeled`, `baroque`, `cubism`, `cubsim`, `minimalist`, `popart`, `realism`, `renaissance` ... (+1 more)

### door_cls
- **Author / Source**: `Miguel Ortiz`
- **Scale**: `811 images` | `N/A` | `67 downloads/stars`
- **Classes / Taxonomy**: `door_cls`

### Door
- **Author / Source**: `Door`
- **Scale**: `627 images` | `1 model` | `27 downloads/stars`
- **Classes / Taxonomy**: `close`, `open`, `semi-open`

### MyShroomClassifier
- **Author / Source**: `MyShroom Dataset Preprocessing`
- **Scale**: `6.51k images` | `1 model` | `16 downloads/stars`
- **Classes / Taxonomy**: `Agaricus`, `Amanita`, `Boletus`, `Cortinarius`, `Entoloma`, `Hygrocybe`, `Lactarius`, `Russula`, `Suillus`

### personal color
- **Author / Source**: `Capstonea`
- **Scale**: `230 images` | `N/A` | `50 downloads/stars`
- **Classes / Taxonomy**: `fall`, `spring`, `summer`, `winter`

### motif batik
- **Author / Source**: `scripsweet`
- **Scale**: `950 images` | `N/A` | `65 downloads/stars`
- **Classes / Taxonomy**: `batik-bali`, `batik-betawi`, `batik-celup`, `batik-cendrawasih`, `batik-ceplok`, `batik-ciamis`, `batik-garutan`, `batik-gentongan`, `batik-kawung`, `batik-keraton` ... (+10 more)

## Medical & Healthcare Diagnostics (59 Projects)

### Skin Cancer Detection
- **Author / Source**: `North South University`
- **Scale**: `9.9k images` | `1 model` | `196 downloads/stars`
- **Classes / Taxonomy**: `akiec`, `bcc`, `bkl`, `df`, `mel`, `nv`, `vasc`

### Diabetic Retinopathy Screening AI
- **Author / Source**: `UCLA Master of Quantitative Economics`
- **Scale**: `2.84k images` | `1 model` | `121 downloads/stars`
- **Classes / Taxonomy**: `Mild`, `Moderate`, `No_DR`, `Proliferate_DR`, `Severe`

### Sugar eye
- **Author / Source**: `Kiwidolas`
- **Scale**: `9.08k images` | `N/A` | `14 downloads/stars`
- **Classes / Taxonomy**: `Mild`, `Moderate`, `No_DR`, `Proliferate_DR`, `Severe`

### Chest X-Rays
- **Author / Source**: `Mohamed Traore`
- **Scale**: `5.82k images` | `1 model` | `632 downloads/stars`
- **Classes / Taxonomy**: `NORMAL`, `PNEUMONIA`

### GlaucomaData
- **Author / Source**: `Classification`
- **Scale**: `1.54k images` | `3 models` | `18 downloads/stars`
- **Classes / Taxonomy**: `normal`, `advanced`, `early`

### Bone Break Classification
- **Author / Source**: `Curso`
- **Scale**: `1.52k images` | `1 model` | `272 downloads/stars`
- **Classes / Taxonomy**: `Avulsion fracture`, `Comminuted fracture`, `Compression-Crush fracture`, `Fracture Dislocation`, `Greenstick fracture`, `Hairline Fracture`, `Impacted fracture`, `Intra-articular fracture`, `Longitudinal fracture`, `Oblique fracture` ... (+2 more)

### Diagnosis of Diabetic Retinopathy
- **Author / Source**: `Personal`
- **Scale**: `2.84k images` | `N/A` | `89 downloads/stars`
- **Classes / Taxonomy**: `Mild`, `Moderate`, `No_DR`, `Proliferate_DR`, `Severe`

### Skin Detection
- **Author / Source**: `SDD`
- **Scale**: `694 images` | `1 model` | `97 downloads/stars`
- **Classes / Taxonomy**: `FU-nail-fungus`, `FU-ringworm`, `NormalSkin`, `VI-chickenpox`

### Detection Of Diabetic Retinopathy Using Machine Learning
- **Author / Source**: `DIABETIC RETINOPATHY`
- **Scale**: `3.64k images` | `1 model` | `92 downloads/stars`
- **Classes / Taxonomy**: `Mild`, `Moderate`, `No_DR`, `Proliferate_DR`, `Severe`

### Diseases Classifier on CheXpert dataset
- **Author / Source**: `Bauman Moscow State University`
- **Scale**: `4.44k images` | `2 models` | `13 downloads/stars`
- **Classes / Taxonomy**: `Atelectasis`, `Cardiomegaly`, `Consolidation`, `Edema`, `Enlarged Cardiomediastinum`, `Fracture`, `Lung Lesion`, `Lung Opacity`, `No Finding`, `Pleural Effusion` ... (+2 more)

### Skin-Problem-MultiLabel
- **Author / Source**: `Parin Kittipongdaja`
- **Scale**: `4.83k images` | `1 model` | `100 downloads/stars`
- **Classes / Taxonomy**: `Acne`, `Blackheads`, `Dark Spots`, `Dry Skin`, `Eye bags`, `Normal Skin`, `Oily Skin`, `Pores`, `Skin Redness`, `Wrinkles`

### alzheimer2
- **Author / Source**: `tevfikagdas`
- **Scale**: `9.9k images` | `N/A` | `39 downloads/stars`
- **Classes / Taxonomy**: `MildDemented`, `ModerateDemented`, `NonDemented`, `VeryMildDemented`

### Renal-Failure-Analysis
- **Author / Source**: `Mini Project`
- **Scale**: `9.57k images` | `2 models` | `13 downloads/stars`
- **Classes / Taxonomy**: `Cyst`, `Normal`, `Stone`, `Tumor`

### Skin Cancer Types
- **Author / Source**: `BreastCancerPrediction`
- **Scale**: `1k images` | `1 model` | `25 downloads/stars`
- **Classes / Taxonomy**: `benign`, `malignant`

### ECG Signal Classification
- **Author / Source**: `Muhammad Faizan`
- **Scale**: `375 images` | `1 model` | `68 downloads/stars`
- **Classes / Taxonomy**: `normal`, `abnormal`

### Skin Disease
- **Author / Source**: `nagesh`
- **Scale**: `4.54k images` | `N/A` | `26 downloads/stars`
- **Classes / Taxonomy**: `cell`, `Actinic`, `Atopic`, `Benign`, `Candidiasis`, `Dermatitis`, `Dermatofibroma`, `Melanocytic`, `Melanoma`, `Ringworm` ... (+7 more)

### eyes
- **Author / Source**: `DƯƠNG ĐỨC CƯỜNG`
- **Scale**: `591 images` | `N/A` | `16 downloads/stars`
- **Classes / Taxonomy**: `Bulging_Eyes`, `Cataracts`, `Crossed_Eyes`, `Normal`, `Styes_Eyes`

### Skin-Disease-Latest
- **Author / Source**: `LUMS`
- **Scale**: `551 images` | `N/A` | `17 downloads/stars`
- **Classes / Taxonomy**: `BCC`, `M`, `SCC`

### Medical Waste
- **Author / Source**: `periysami`
- **Scale**: `2.71k images` | `1 model` | `19 downloads/stars`
- **Classes / Taxonomy**: `gloves`, `masks`, `medicine`, `syringe`

### Cataract-Detection
- **Author / Source**: `FY Project`
- **Scale**: `1.01k images` | `2 models` | `57 downloads/stars`
- **Classes / Taxonomy**: `Cataract`, `No Cataract`

### skin-disease3
- **Author / Source**: `skin`
- **Scale**: `2.39k images` | `N/A` | `48 downloads/stars`
- **Classes / Taxonomy**: `Actinic`, `Atopic`, `Candidiasis`, `Contact`, `Contagiosum`, `Dermatitis`, `Genital`, `Herpes`, `Keratosis`, `Molluscum` ... (+2 more)

### Eye-disease-classification
- **Author / Source**: `coursework`
- **Scale**: `1.18k images` | `1 model` | `42 downloads/stars`
- **Classes / Taxonomy**: `Cataracts`, `Normal_Eyes`, `Uveitis`

### Ct scan
- **Author / Source**: `student`
- **Scale**: `847 images` | `1 model` | `19 downloads/stars`
- **Classes / Taxonomy**: `normal`, `adenocarcinoma`, `adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib`, `large.cell.carcinoma`, `large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa`, `squamous.cell.carcinoma`, `squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa`

### Skin types3
- **Author / Source**: `theaskin`
- **Scale**: `1.03k images` | `N/A` | `53 downloads/stars`
- **Classes / Taxonomy**: `normal`, `combination`, `dry`, `oily`

### Eye Disease
- **Author / Source**: `Student`
- **Scale**: `3.69k images` | `1 model` | `46 downloads/stars`
- **Classes / Taxonomy**: `1_normal`, `2_cataract`, `2_glaucoma`, `3_retina_disease`

### Lung cancer DATASET
- **Author / Source**: `lung cancer`
- **Scale**: `2.98k images` | `1 model` | `215 downloads/stars`
- **Classes / Taxonomy**: `normal`, `adenocarcinoma`, `adenocarcinoma_left`, `adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib`, `large`, `large.cell.carcinoma`, `large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa`, `squamous`, `squamous.cell.carcinoma`, `squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa`

### ECG image classification
- **Author / Source**: `computer science`
- **Scale**: `1.93k images` | `N/A` | `18 downloads/stars`
- **Classes / Taxonomy**: `AHB`, `COVID-19`, `HMI`, `MI`, `Normal`

### Liver tumor classification
- **Author / Source**: `gowtham`
- **Scale**: `564 images` | `N/A` | `24 downloads/stars`
- **Classes / Taxonomy**: `Cholangiocarcinoma`, `HCC`, `Normal_Liver`

### ShoulderMRI
- **Author / Source**: `shoulderMRI`
- **Scale**: `4.82k images` | `1 model` | `15 downloads/stars`
- **Classes / Taxonomy**: `normal`, `full_tear`, `partial_tear`

### autism
- **Author / Source**: `autism`
- **Scale**: `3.04k images` | `1 model` | `23 downloads/stars`
- **Classes / Taxonomy**: `Autistic`, `Non_Autistic`, `Unlabeled`

### Brain Tumor Detection w/ YoloV8
- **Author / Source**: `Arjans Workspace`
- **Scale**: `200 images` | `1 model` | `29 downloads/stars`
- **Classes / Taxonomy**: `object`, `MENINGIOMA`

### tumor-classifier
- **Author / Source**: `Batch B Brilliant Butterflies`
- **Scale**: `5.37k images` | `N/A` | `34 downloads/stars`
- **Classes / Taxonomy**: `glioma`, `meningioma`, `no-tumor`, `pituitary`

### Fetal Brain Abnormalities Ultrasound
- **Author / Source**: `Hritwik Trivedi`
- **Scale**: `1.77k images` | `1 model` | `231 downloads/stars`
- **Classes / Taxonomy**: `normal`, `anold-chiari-malformation`, `arachnoid-cyst`, `cerebellah-hypoplasia`, `colphocephaly`, `encephalocele`, `holoprosencephaly`, `hydracenphaly`, `intracranial-hemorrdge`, `intracranial-tumor` ... (+6 more)

### MelanomaCancer
- **Author / Source**: `Daisy`
- **Scale**: `9.9k images` | `N/A` | `17 downloads/stars`
- **Classes / Taxonomy**: `Benign`, `Malignant`

### Mass classification
- **Author / Source**: `Muhammad Ali Jinnah University`
- **Scale**: `1.51k images` | `1 model` | `75 downloads/stars`
- **Classes / Taxonomy**: `BENIGN`, `MALIGNANT`

### skin cancer classification
- **Author / Source**: `Smart Healthcare Mnaagement`
- **Scale**: `9.9k images` | `1 model` | `231 downloads/stars`
- **Classes / Taxonomy**: `akiec`, `bcc`, `bkl`, `df`, `mel`, `nv`, `vasc`

### Cataract v01
- **Author / Source**: `Cataract`
- **Scale**: `299 images` | `N/A` | `186 downloads/stars`
- **Classes / Taxonomy**: `normal`, `immature`, `mature`

### Diabetic Retinopathy (GP33)
- **Author / Source**: `Jlaestologa`
- **Scale**: `2.91k images` | `3 models` | `18 downloads/stars`
- **Classes / Taxonomy**: `Mild`, `Moderate`, `No_DR`, `Proliferate_DR`, `Severe`

### eye_v2
- **Author / Source**: `DƯƠNG ĐỨC CƯỜNG`
- **Scale**: `398 images` | `N/A` | `58 downloads/stars`
- **Classes / Taxonomy**: `normal`, `tired_eyes`

### bone cancer detection
- **Author / Source**: `normal bones`
- **Scale**: `8.81k images` | `1 model` | `32 downloads/stars`
- **Classes / Taxonomy**: `normal`, `cancer`

### Domain Knowledge vs AI: Detecting Cervical Spine Fractures from CT Scans
- **Author / Source**: `CSRSEF`
- **Scale**: `4.12k images` | `2 models` | `12 downloads/stars`
- **Classes / Taxonomy**: `fracture`, `normal`

### diabeticretinopathy
- **Author / Source**: `magic techs`
- **Scale**: `283 images` | `N/A` | `16 downloads/stars`
- **Classes / Taxonomy**: `Proliferate_DR`

### health_coral
- **Author / Source**: `nab`
- **Scale**: `429 images` | `N/A` | `26 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `bleached`, `partially`

### skin classification
- **Author / Source**: `ciputra`
- **Scale**: `70 images` | `1 model` | `84 downloads/stars`
- **Classes / Taxonomy**: `Combination`, `Dry`, `Normal`, `Oily`

### Varicose detection
- **Author / Source**: `Varicose`
- **Scale**: `111 images` | `1 model` | `39 downloads/stars`
- **Classes / Taxonomy**: `normal`, `varicose`

### hist_thesis
- **Author / Source**: `thesis`
- **Scale**: `6.2k images` | `N/A` | `33 downloads/stars`
- **Classes / Taxonomy**: `0`

### facial-skin-classification
- **Author / Source**: `skinsightproject`
- **Scale**: `800 images` | `3 models` | `12 downloads/stars`
- **Classes / Taxonomy**: `Acne`, `Skin Redness`, `blackhead`

### echoview
- **Author / Source**: `echo`
- **Scale**: `1.97k images` | `1 model` | `24 downloads/stars`
- **Classes / Taxonomy**: `Apical`, `Parasternal_Short`, `Parasternal_long`, `Subcostal_CS`, `Subcostal_IVC`, `Suprasternal_Arch`

### Dental
- **Author / Source**: `Musah Abdulazeez`
- **Scale**: `1.5k images` | `1 model` | `15 downloads/stars`
- **Classes / Taxonomy**: `Fractured`, `UnFractured`

### skin_disease_AK
- **Author / Source**: `kelixo`
- **Scale**: `13.2k images` | `1 model` | `51 downloads/stars`
- **Classes / Taxonomy**: `Acne and Rosacea Photos`, `Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions`, `Atopic Dermatitis Photos`, `Bullous Disease Photos`, `Cellulitis Impetigo and other Bacterial Infections`, `Eczema Photos`, `Exanthems and Drug Eruptions`, `Hair Loss Photos Alopecia and other Hair Diseases`, `Herpes HPV and other STDs Photos`, `Light Diseases and Disorders of Pigmentation` ... (+10 more)

### Brain Tumor Detection
- **Author / Source**: `DLPBrain Tumor Detection`
- **Scale**: `3.79k images` | `N/A` | `15 downloads/stars`
- **Classes / Taxonomy**: `Brain Tumor`

### sovitrath-diabetic-retinopathy
- **Author / Source**: `pracainzidrid`
- **Scale**: `3.53k images` | `N/A` | `15 downloads/stars`
- **Classes / Taxonomy**: `Mild`, `Moderate`, `No_DR`, `Proliferate_DR`, `Severe`

### Plant Health
- **Author / Source**: `Spencer Wueste`
- **Scale**: `542 images` | `N/A` | `13 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `mildew`, `spots`

### chest-xray-dataset
- **Author / Source**: `Kennys Personal Workspace`
- **Scale**: `2.1k images` | `N/A` | `11 downloads/stars`
- **Classes / Taxonomy**: `normal`, `pneumonia_bacterial`, `pneumonia_viral`

### Skin Disease IA Detection
- **Author / Source**: `Health AI Detection`
- **Scale**: `3.5k images` | `1 model` | `26 downloads/stars`
- **Classes / Taxonomy**: `akiec`, `bcc`, `bkl`, `df`, `mel`, `nv`, `vasc`

### Tumor,Cancer,Aneurysm Detection
- **Author / Source**: `DiscoverAI`
- **Scale**: `255 images` | `1 model` | `14 downloads/stars`
- **Classes / Taxonomy**: `tumor`, `Aneurysm Photos`, `aneurysm`, `cancer`

### glaucoma detection
- **Author / Source**: `PSIT`
- **Scale**: `5.38k images` | `2 models` | `31 downloads/stars`
- **Classes / Taxonomy**: `normal`, `advanced`, `early`

### Dental Caries Classification
- **Author / Source**: `Dental Caries`
- **Scale**: `957 images` | `1 model` | `11 downloads/stars`
- **Classes / Taxonomy**: `caries`, `deep caries`, `null`

### boneage_classification
- **Author / Source**: `Community`
- **Scale**: `N/A` | `N/A` | `N/A downloads/stars`
- **Classes / Taxonomy**: `by`, `8.19k images`, `11`, `DIPFirst_1`, `DIPFirst_10`, `DIPFirst_11`, `DIPFirst_2`, `DIPFirst_3`, `DIPFirst_4`, `DIPFirst_5` ... (+13 more)

## Animal, Insects & Wildlife (21 Projects)

### Bird Species detector
- **Author / Source**: `Bird Species Predictor`
- **Scale**: `9.88k images` | `1 model` | `68 downloads/stars`
- **Classes / Taxonomy**: `ABBOTTS BABBLER`, `ABBOTTS BOOBY`, `ABYSSINIAN GROUND HORNBILL`, `AFRICAN CROWNED CRANE`, `AFRICAN EMERALD CUCKOO`, `AFRICAN FIREFINCH`, `AFRICAN OYSTER CATCHER`, `AFRICAN PIED HORNBILL`, `AFRICAN PYGMY GOOSE`, `ALBATROSS` ... (+10 more)

### Bird detection
- **Author / Source**: `Guy`
- **Scale**: `9.99k images` | `N/A` | `19 downloads/stars`
- **Classes / Taxonomy**: `ABBOTTS BOOBY`, `AFRICAN CROWNED CRANE`, `AMERICAN ROBIN`, `AMERICAN WIGEON`, `APAPANE`, `ASIAN CRESTED IBIS`, `AUSTRALASIAN FIGBIRD`, `BAY-BREASTED WARBLER`, `BLACK HEADED CAIQUE`, `BLACK NECKED STILT` ... (+10 more)

### fish disease detection
- **Author / Source**: `pfe`
- **Scale**: `698 images` | `1 model` | `32 downloads/stars`
- **Classes / Taxonomy**: `healthy-fish`, `sick-fish`

### Underwater-object-detection-and-classification
- **Author / Source**: `Capstone`
- **Scale**: `3.51k images` | `1 model` | `28 downloads/stars`
- **Classes / Taxonomy**: `Crabs`, `Dolphin`, `Fish`, `Jelly_Fish`, `Lobster`, `Sea_Urchins`, `Starfish`

### Insect_Detect_classification_v2
- **Author / Source**: `Maximilian Sittinger`
- **Scale**: `21k images` | `1 model` | `157 downloads/stars`
- **Classes / Taxonomy**: `bee`, `ant`, `bee_apis`, `bee_bombus`, `beetle`, `beetle_cocci`, `beetle_oedem`, `bug`, `bug_grapho`, `fly` ... (+10 more)

### Moulouya_Bird_detection
- **Author / Source**: `UMP`
- **Scale**: `9.53k images` | `1 model` | `22 downloads/stars`
- **Classes / Taxonomy**: `ABBOTTSBABBLER`, `ABBOTTSBOOBY`, `ABYSSINIANGROUNDHORNBILL`, `AFRICANCROWNEDCRANE`, `AFRICANEMERALDCUCKOO`, `AFRICANFIREFINCH`, `AFRICANOYSTERCATCHER`, `AFRICANPIEDHORNBILL`, `ALBATROSS`, `ALBERTSTOWHEE` ... (+10 more)

### BirdDetection
- **Author / Source**: `Object detection`
- **Scale**: `3.35k images` | `1 model` | `44 downloads/stars`
- **Classes / Taxonomy**: `ABBOTTS BABBLER`, `ABBOTTS BOOBY`, `ABYSSINIAN GROUND HORNBILL`, `AFRICAN CROWNED CRANE`, `AFRICAN EMERALD CUCKOO`, `AFRICAN FIREFINCH`, `AFRICAN OYSTER CATCHER`, `AFRICAN PIED HORNBILL`, `AFRICAN PYGMY GOOSE`, `ALBATROSS` ... (+10 more)

### fish classification
- **Author / Source**: `objectdetection`
- **Scale**: `110 images` | `1 model` | `63 downloads/stars`
- **Classes / Taxonomy**: `0`, `commoncarp`, `pangas`

### Fish disease classification
- **Author / Source**: `Shrimp Project`
- **Scale**: `454 images` | `N/A` | `28 downloads/stars`
- **Classes / Taxonomy**: `Bacterial Red disease`, `Bacterial diseases - Aeromoniasis`, `Bacterial gill disease`, `Fungal diseases Saprolegniasis`, `Healthy Fish`, `Parasitic diseases`, `Viral diseases White tail disease`

### dogPoses
- **Author / Source**: `cudo`
- **Scale**: `5.01k images` | `N/A` | `35 downloads/stars`
- **Classes / Taxonomy**: `scratch`, `stand`, `bite`, `lie`, `shaking`, `sit`, `sleep`, `spinRound`, `yawn`

### butterfly
- **Author / Source**: `weather`
- **Scale**: `6.5k images` | `N/A` | `14 downloads/stars`
- **Classes / Taxonomy**: `88`, `ADMIRAL`, `ADONIS`, `AFRICAN`, `AMERICAN`, `AN`, `APPOLLO`, `ATALA`, `AWL`, `BANDED` ... (+10 more)

### Fish Disease
- **Author / Source**: `Eki`
- **Scale**: `454 images` | `1 model` | `58 downloads/stars`
- **Classes / Taxonomy**: `Bacterial Red disease`, `Bacterial diseases - Aeromoniasis`, `Bacterial gill disease`, `Fungal diseases Saprolegniasis`, `Healthy Fish`, `Parasitic diseases`, `Viral diseases White tail disease`

### classify_butterfly_and_moth
- **Author / Source**: `Navrachana University`
- **Scale**: `9.96k images` | `1 model` | `13 downloads/stars`
- **Classes / Taxonomy**: `88`, `ADMIRAL`, `ADONIS`, `AFRICAN`, `AMERICAN`, `AN`, `APPOLLO`, `ARCIGERA`, `ARGUS`, `ATALA` ... (+10 more)

### fish_1
- **Author / Source**: `James`
- **Scale**: `8.41k images` | `1 model` | `11 downloads/stars`
- **Classes / Taxonomy**: `Bangus`, `Big Head Carp`, `Black Sea Sprat`, `Black Spotted Barb`, `Catfish`, `Climbing Perch`, `Fourfinger Threadfin`, `Freshwater Eel`, `Gilt-Head Bream`, `Glass Perchlet` ... (+10 more)

### fish
- **Author / Source**: `Aquaculture`
- **Scale**: `193 images` | `1 model` | `25 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `EUS`

### Bird
- **Author / Source**: `Class`
- **Scale**: `7.06k images` | `1 model` | `14 downloads/stars`
- **Classes / Taxonomy**: `B_0`, `B_1`, `B_10`, `B_100`, `B_101`, `B_102`, `B_103`, `B_104`, `B_105`, `B_106` ... (+10 more)

### cow diseae identifier
- **Author / Source**: `project for grd 10`
- **Scale**: `814 images` | `1 model` | `57 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `lumpy skin`

### Cows
- **Author / Source**: `Operating room`
- **Scale**: `1.24k images` | `1 model` | `60 downloads/stars`
- **Classes / Taxonomy**: `FMD`, `Lumpy Skin`, `Normal Skin`

### dog excrements
- **Author / Source**: `Benito`
- **Scale**: `1.64k images` | `1 model` | `16 downloads/stars`
- **Classes / Taxonomy**: `Type1`, `Type1 Type2`, `Type1 Type2 Type3`, `Type1 Type3`, `Type1 Type5`, `Type2`, `Type2 Type3`, `Type2 Type3 Type4`, `Type2 Type3 Type5`, `Type2 Type3 Type7` ... (+8 more)

### cow face
- **Author / Source**: `IIT jammu`
- **Scale**: `4.92k images` | `1 model` | `12 downloads/stars`
- **Classes / Taxonomy**: `cattle_0100`, `cattle_0200`, `cattle_0300`, `cattle_0400`, `cattle_0500`, `cattle_0600`, `cattle_0700`, `cattle_0800`, `cattle_0900`, `cattle_1000` ... (+10 more)

### KOI_FISH_CLASSFICATION_2
- **Author / Source**: `Test`
- **Scale**: `765 images` | `N/A` | `40 downloads/stars`
- **Classes / Taxonomy**: `Asagi`, `Bekko`, `Doitsu_koi`, `Ghosiki`, `Goromo`, `Hikarimoyo`, `Hikarimuji_mono`, `Hikariutsuri`, `Kanoko_koi`, `Kawarimono` ... (+8 more)

## Benchmarks, Gaming & Synthetic Datasets (4 Projects)

### MNIST
- **Author / Source**: `Popular Benchmarks`
- **Scale**: `70k images` | `2 models` | `375 downloads/stars`
- **Classes / Taxonomy**: `0`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`

### Pokedex
- **Author / Source**: `Robert Demo`
- **Scale**: `6.99k images` | `6 models` | `220 downloads/stars`
- **Classes / Taxonomy**: `Abra`, `Aerodactyl`, `Alakazam`, `Alolan Sandslash`, `Arbok`, `Arcanine`, `Articuno`, `Beedrill`, `Bellsprout`, `Blastoise` ... (+10 more)

### 227
- **Author / Source**: `asas`
- **Scale**: `6.67k images` | `1 model` | `107 downloads/stars`
- **Classes / Taxonomy**: `banana`, `sunflower`, `Bush Clock Vine`, `Common Lanthana`, `Datura`, `Hibiscus`, `Jatropha`, `Marigold`, `Nityakalyani`, `Rose` ... (+10 more)

### SKETCHFUL.AI
- **Author / Source**: `MANGOES`
- **Scale**: `7.62k images` | `1 model` | `18 downloads/stars`
- **Classes / Taxonomy**: `baseball`, `carrot`, `donut`, `fish`, `leaf`, `moon`, `pencil`, `sailboat`, `star`, `triangle` ... (+10 more)

## Industrial, Waste & Environmental Monitoring (24 Projects)

### Road Sign Detecting
- **Author / Source**: `Projects`
- **Scale**: `9.11k images` | `1 model` | `139 downloads/stars`
- **Classes / Taxonomy**: `0`, `13`, `14`, `17`, `19`, `2`, `20`, `21`, `22`, `23` ... (+9 more)

### Synthetic Corrosion Dataset
- **Author / Source**: `Synthetic Corrosion`
- **Scale**: `76 images` | `2 models` | `510 downloads/stars`
- **Classes / Taxonomy**: `Corrosion`, `no-corrosion`

### Power Grid Inspection
- **Author / Source**: `DBIS 2023 Capstone`
- **Scale**: `1.62k images` | `1 model` | `46 downloads/stars`
- **Classes / Taxonomy**: `Bent_Insulator`, `Broken_Insulator_Cap`, `Damaged_Cable_Jackets`, `Damper`, `Frayed_Cable`, `Insulator`, `Insulator_Cap`, `Power_Cable`, `Spacer`, `Tangled_Object` ... (+3 more)

### Railway track fault detection
- **Author / Source**: `Chinmay Ranganath`
- **Scale**: `380 images` | `N/A` | `39 downloads/stars`
- **Classes / Taxonomy**: `Defective`, `Non-defective`

### Road_Surface_CLS
- **Author / Source**: `RoadCLS`
- **Scale**: `5.42k images` | `N/A` | `36 downloads/stars`
- **Classes / Taxonomy**: `asphalt`, `concrete`, `rain`, `unpaved`

### Weather
- **Author / Source**: `UmitLearning`
- **Scale**: `199 images` | `1 model` | `22 downloads/stars`
- **Classes / Taxonomy**: `fog`, `smog`

### Weather classification
- **Author / Source**: `University of Wolverhampton`
- **Scale**: `9.36k images` | `1 model` | `43 downloads/stars`
- **Classes / Taxonomy**: `cloudy`, `foggy`, `rainy`, `snowy`, `sunny`

### Garbage Clasification
- **Author / Source**: `Garbage Clasification`
- **Scale**: `9.46k images` | `2 models` | `34 downloads/stars`
- **Classes / Taxonomy**: `0`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18` ... (+9 more)

### solar_panel_dirt_classify
- **Author / Source**: `Solar Panel`
- **Scale**: `2.17k images` | `N/A` | `20 downloads/stars`
- **Classes / Taxonomy**: `Clean`, `Dusty`, `Poop`

### Foggy-pexels
- **Author / Source**: `Diffusion`
- **Scale**: `407 images` | `N/A` | `35 downloads/stars`
- **Classes / Taxonomy**: `Good`

### garbage waste
- **Author / Source**: `Abdulrahman mohammed`
- **Scale**: `3.14k images` | `N/A` | `28 downloads/stars`
- **Classes / Taxonomy**: `0`, `2`

### Manhole_Classification
- **Author / Source**: `BITS`
- **Scale**: `1.03k images` | `N/A` | `19 downloads/stars`
- **Classes / Taxonomy**: `closed_manhole`, `improperly_closed_manhole`, `open_manhole`

### Road_surface_CLS
- **Author / Source**: `Cranfield University`
- **Scale**: `4.69k images` | `N/A` | `20 downloads/stars`
- **Classes / Taxonomy**: `asphalt`, `concrete`, `unpaved`

### FDM_defect_dectection
- **Author / Source**: `2022 AICP`
- **Scale**: `384 images` | `N/A` | `27 downloads/stars`
- **Classes / Taxonomy**: `Blobs`, `OK`, `blobs`, `cracks`, `spaghetti`, `stringing`, `under_exstrosion`

### Oil Spill Classification
- **Author / Source**: `Dmitry Karanov`
- **Scale**: `389 images` | `1 model` | `11 downloads/stars`
- **Classes / Taxonomy**: `0 0 0 0 1 1 1 1 0`, `images`

### Clouds
- **Author / Source**: `ThomasTest`
- **Scale**: `87 images` | `2 models` | `21 downloads/stars`
- **Classes / Taxonomy**: `Altocumulus`, `Altostratus`, `Cirrus`, `Cumulonimbus`, `Cumulus`, `Nimbostratus`, `Stratocumulus`, `Stratus`, `Unlabeled`

### Pothole Classification
- **Author / Source**: `pothole classification`
- **Scale**: `13.1k images` | `2 models` | `20 downloads/stars`
- **Classes / Taxonomy**: `Not Pothole`, `Pothole`

### waste classification
- **Author / Source**: `Waste segregation`
- **Scale**: `6.15k images` | `1 model` | `19 downloads/stars`
- **Classes / Taxonomy**: `can`, `empty`, `Background`, `Background_multiple`, `Cig_bud`, `Cig_bud_multiple`, `Cig_pack`, `Cig_pack_multiple`, `Disposable`, `Disposable_multiple` ... (+10 more)

### litterr
- **Author / Source**: `MS`
- **Scale**: `1.84k images` | `N/A` | `19 downloads/stars`
- **Classes / Taxonomy**: `Garbage`, `Unlabeled`

### ReycleSorter
- **Author / Source**: `swittuthworkspace`
- **Scale**: `1.98k images` | `1 model` | `13 downloads/stars`
- **Classes / Taxonomy**: `CARDBOARD`, `PAPER`, `Paper`

### Weather Recognition
- **Author / Source**: `Research`
- **Scale**: `597 images` | `N/A` | `14 downloads/stars`
- **Classes / Taxonomy**: `lightning`, `rainbow`

### fog
- **Author / Source**: `MTUCI`
- **Scale**: `354 images` | `1 model` | `16 downloads/stars`
- **Classes / Taxonomy**: `Unlabeled`, `fog`

### Waste Classification
- **Author / Source**: `LI YI YING HCI`
- **Scale**: `8.2k images` | `N/A` | `14 downloads/stars`
- **Classes / Taxonomy**: `battery`, `cardboard`, `metal`, `paper`, `plastic`, `trash`, `biological`, `brown-glass`, `green-glass`, `white-glass`

### Road Quality Classification
- **Author / Source**: `Carto`
- **Scale**: `4.69k images` | `N/A` | `23 downloads/stars`
- **Classes / Taxonomy**: `01_asphalt(Good)`, `02_asphalt(Regular)`, `03_asphalt(Bad)`, `05_paved(Regular)`, `06_paved(Bad)`, `07_unpaved(Regular)`, `08_unpaved(Bad)`

## Other Specialized Applications (79 Projects)

### Food Calorie Estimation
- **Author / Source**: `ElDoradooo`
- **Scale**: `6.68k images` | `N/A` | `102 downloads/stars`
- **Classes / Taxonomy**: `burger`, `rice`, `sprite`, `AW cola`, `Beijing Beef`, `Chow Mein`, `Fried Rice`, `Hashbrown`, `Honey Walnut Shrimp`, `Kung Pao Chicken` ... (+10 more)

### Acne detection
- **Author / Source**: `Bangkit Academy`
- **Scale**: `8.87k images` | `1 model` | `30 downloads/stars`
- **Classes / Taxonomy**: `Acne`, `Blackhead`, `Conglobata`, `Crystanlline`, `Cystic`, `Flat_wart`, `Folliculitis`, `Keloid`, `Milium`, `Papular` ... (+6 more)

### Longitudinal Crack
- **Author / Source**: `ragulabhindra`
- **Scale**: `148 images` | `N/A` | `44 downloads/stars`
- **Classes / Taxonomy**: `longitudinalcrack`

### Tongue
- **Author / Source**: `Medical`
- **Scale**: `9.89k images` | `1 model` | `27 downloads/stars`
- **Classes / Taxonomy**: `colorResult_grey`, `colorResult_white`, `colorResult_yellow`, `shapeResult_ToothMarks`, `shapeResult_fat`, `shapeResult_normal`, `shapeResult_thin`, `textureResult_dark`, `textureResult_normal`, `textureResult_tender` ... (+5 more)

### DA
- **Author / Source**: `Crash Course CV`
- **Scale**: `18.4k images` | `N/A` | `84 downloads/stars`
- **Classes / Taxonomy**: `Atopic Dermatitis`, `Basal Cell Carcinoma (BCC)`, `Benign Keratosis-like Lesions (BKL)`, `Eczema`, `Melanocytic Nevi (NV)`, `Melanoma`, `Psoriasis pictures Lichen Planus and related diseases`, `Seborrheic Keratoses and other Benign Tumors`, `Tinea Ringworm Candidiasis and other Fungal Infections`, `Warts Molluscum and other Viral Infections`

### DR Detection
- **Author / Source**: `Carey AI Course`
- **Scale**: `2.84k images` | `N/A` | `30 downloads/stars`
- **Classes / Taxonomy**: `Mild`, `Moderate`, `No_DR`, `Proliferate_DR`, `Severe`

### test_trash
- **Author / Source**: `Test Merge`
- **Scale**: `5.13k images` | `1 model` | `18 downloads/stars`
- **Classes / Taxonomy**: `can`, `cellphone`, `glove`, `metal`, `plastic`, `sunglasses`, `tire`, `Mask`, `electronics`, `gbottle` ... (+5 more)

### CoffeBeans
- **Author / Source**: `Universitas Gunadarma`
- **Scale**: `1.19k images` | `2 models` | `93 downloads/stars`
- **Classes / Taxonomy**: `DarkRoasting`, `GreenRoasting`, `LightRoasting`, `MediumRoasting`

### Jenis kopi multiinput
- **Author / Source**: `Deteksi kopi Multiinput`
- **Scale**: `2.71k images` | `1 model` | `32 downloads/stars`
- **Classes / Taxonomy**: `Arabika`, `Robusta`, `Unlabeled`, `arabika`, `liberika`, `robusta`

### COVID
- **Author / Source**: `BERRAHAL MOHAMMED`
- **Scale**: `2.48k images` | `3 models` | `15 downloads/stars`
- **Classes / Taxonomy**: `fire`, `COVID`, `non-COVID`

### PTEC2023
- **Author / Source**: `PTEC 2023`
- **Scale**: `552 images` | `1 model` | `14 downloads/stars`
- **Classes / Taxonomy**: `fresh banana`, `raw banana`, `rotten banana`

### numbers
- **Author / Source**: `t`
- **Scale**: `4.64k images` | `2 models` | `28 downloads/stars`
- **Classes / Taxonomy**: `benign`, `malignant`

### disease testing
- **Author / Source**: `project for grd 10`
- **Scale**: `56 images` | `1 model` | `15 downloads/stars`
- **Classes / Taxonomy**: `Unlabeled`, `lumpy skin`, `ringworm`

### BuildingsDetection
- **Author / Source**: `school`
- **Scale**: `1k images` | `1 model` | `53 downloads/stars`
- **Classes / Taxonomy**: `building`, `Unlabeled`

### Acne Severity Classification
- **Author / Source**: `Taschenbier`
- **Scale**: `2.46k images` | `1 model` | `47 downloads/stars`
- **Classes / Taxonomy**: `IGA0`, `IGA1`, `IGA2`, `IGA3`, `IGA3_Level3`, `IGA4`

### thesis
- **Author / Source**: `Scancer`
- **Scale**: `25.2k images` | `N/A` | `14 downloads/stars`
- **Classes / Taxonomy**: `BasalCellCarcinoma`, `Melanoma`, `Nevus`, `SquamousCellCarcinoma`

### Weight Detection
- **Author / Source**: `iqra university`
- **Scale**: `1.65k images` | `1 model` | `14 downloads/stars`
- **Classes / Taxonomy**: `10kg - 20kg`, `120kg - 140kg`, `140kg - 160kg`, `160kg - 180kg`, `1kg - 10kg`, `200kg - 220kg`, `20kg - 40kg`, `220kg - 240kg`, `240kg - 260kg`, `280kg - 300kg` ... (+10 more)

### alhassan
- **Author / Source**: `alhassan123`
- **Scale**: `657 images` | `1 model` | `14 downloads/stars`
- **Classes / Taxonomy**: `Healthy`, `coryza`, `crd`

### classification of bottles
- **Author / Source**: `HTW Berlin University of Applied Sciences`
- **Scale**: `396 images` | `1 model` | `80 downloads/stars`
- **Classes / Taxonomy**: `glass`, `plastic`

### chat_luoi3
- **Author / Source**: `1652010377msvutmeduvn`
- **Scale**: `580 images` | `1 model` | `17 downloads/stars`
- **Classes / Taxonomy**: `binhthuong`, `do`, `nhot`, `tim`

### Coral Reef Bleach Detection
- **Author / Source**: `coralreef`
- **Scale**: `5.76k images` | `1 model` | `11 downloads/stars`
- **Classes / Taxonomy**: `Bleached`, `Healthy`

### PhytoAI
- **Author / Source**: `Alex Alman`
- **Scale**: `1.45k images` | `1 model` | `32 downloads/stars`
- **Classes / Taxonomy**: `Black`, `Blight`, `Mildew`, `Mold`, `Powdery`, `Rust`, `Scab`, `Spot`, `rot`

### whea- diseas- detection
- **Author / Source**: `FAST`
- **Scale**: `2.94k images` | `1 model` | `34 downloads/stars`
- **Classes / Taxonomy**: `Brown_rust`, `Healthy`, `Yellow_rust`

### Image Classes
- **Author / Source**: `MediaVault`
- **Scale**: `6.04k images` | `1 model` | `32 downloads/stars`
- **Classes / Taxonomy**: `ANIME`, `DEMOTIVATOR`, `MESSENGERS_AND_COMMENTS`, `OTHER`, `RAGE_COMICS`, `THREADSHOT`

### MyGroceryProducts
- **Author / Source**: `Dmitri Kaslov`
- **Scale**: `3.35k images` | `N/A` | `25 downloads/stars`
- **Classes / Taxonomy**: `apple`, `banana`, `beef`, `bread`, `broccoli`, `butter`, `carrot`, `cheese`, `chicken`, `chocolate` ... (+10 more)

### recyclingman
- **Author / Source**: `jeyoung`
- **Scale**: `5.24k images` | `3 models` | `41 downloads/stars`
- **Classes / Taxonomy**: `can`, `cardboard`, `glass`, `metal`, `paper`, `plastic`, `trash`

### Natural Disaster Damage
- **Author / Source**: `Model v3`
- **Scale**: `384 images` | `1 model` | `19 downloads/stars`
- **Classes / Taxonomy**: `Earthquake`, `Flood Damage`, `Forest Fire`, `Sinkhole`

### Sweetness Watermelon
- **Author / Source**: `capstonesementara`
- **Scale**: `700 images` | `1 model` | `21 downloads/stars`
- **Classes / Taxonomy**: `manis`, `tidak_manis`

### hair_norwood_hamilton
- **Author / Source**: `onuralpszr`
- **Scale**: `5.78k images` | `N/A` | `31 downloads/stars`
- **Classes / Taxonomy**: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `Unlabeled`

### sign_language_project
- **Author / Source**: `signlanguage`
- **Scale**: `2.18k images` | `1 model` | `24 downloads/stars`
- **Classes / Taxonomy**: `A`, `B`, `C`, `Unlabeled`

### Research Project
- **Author / Source**: `Nutrient Deficiency`
- **Scale**: `2.86k images` | `2 models` | `14 downloads/stars`
- **Classes / Taxonomy**: `Healthier`, `NitrogenDeficiency`, `PotassiumDeficiency`, `Unlabeled`, `fn`, `k`, `n`, `p`

### plastic_PVC_2
- **Author / Source**: `wuttinan`
- **Scale**: `100 images` | `N/A` | `13 downloads/stars`
- **Classes / Taxonomy**: `pvc`

### RRD
- **Author / Source**: `Ilman Gifari`
- **Scale**: `1.74k images` | `N/A` | `16 downloads/stars`
- **Classes / Taxonomy**: `Cycle Zone`, `Danger Ahead`, `Deer Zone`, `End of Right Road -Go straight-`, `Give Way`, `Go Left or Straight`, `Go Right or Straight`, `Go Straight`, `Huddle Road`, `Left Curve Ahead` ... (+10 more)

### Covid-19-PIS
- **Author / Source**: `PyImageSearch`
- **Scale**: `1.28k images` | `N/A` | `3.27k downloads/stars`
- **Classes / Taxonomy**: `with_mask`, `without_mask`

### Test
- **Author / Source**: `Sejong University`
- **Scale**: `8.52k images` | `N/A` | `23 downloads/stars`
- **Classes / Taxonomy**: `Covid`, `Fibrosis`, `Normal`, `PNEUMONIA`, `Tuberculosis`

### final-medicine-classification
- **Author / Source**: `IdentifyingMedicines`
- **Scale**: `1.22k images` | `1 model` | `32 downloads/stars`
- **Classes / Taxonomy**: `A-Phyl_100_Capsule`, `A2__Tablet`, `AA_5_Tablet`, `AB-Flo-N_Tablet`, `AB-Flo_Capsule`, `AB-Flo_SR_Tablet`, `AB2_Kit`, `AB_Pas_N_Tablet`, `AB_Phylline_Capsule`, `AB_Phylline_N_Tablet` ... (+10 more)

### Footprint Classification
- **Author / Source**: `SML project`
- **Scale**: `1.43k images` | `1 model` | `15 downloads/stars`
- **Classes / Taxonomy**: `Bear`, `Bird`, `Cat`, `Dog`, `Leopard`, `Otter`

### satellite
- **Author / Source**: `nam`
- **Scale**: `10k images` | `N/A` | `18 downloads/stars`
- **Classes / Taxonomy**: `0`

### pygm3
- **Author / Source**: `pygmintations`
- **Scale**: `8.8k images` | `N/A` | `24 downloads/stars`
- **Classes / Taxonomy**: `Age-Changes`, `Inflammation`, `Normal-skin`, `Pigmentation`, `Rosacea`, `Unlabeled`

### MMC
- **Author / Source**: `Minstudio`
- **Scale**: `7.26k images` | `1 model` | `22 downloads/stars`
- **Classes / Taxonomy**: `blue`, `gold`, `green`, `orange`, `red`, `yellow`, `beige`, `black`, `brown`, `grey` ... (+5 more)

### posture_correction_v4
- **Author / Source**: `PostureCorrection`
- **Scale**: `4.67k images` | `1 model` | `147 downloads/stars`
- **Classes / Taxonomy**: `Unlabeled`, `looks good`, `sit up straight`, `straighten head`

### Wrinkle Classification
- **Author / Source**: `Alp Bora Kirte`
- **Scale**: `5.99k images` | `N/A` | `39 downloads/stars`
- **Classes / Taxonomy**: `non-wrinkle`, `wrinkle`

### Paper
- **Author / Source**: `Rijah`
- **Scale**: `303 images` | `N/A` | `18 downloads/stars`
- **Classes / Taxonomy**: `Paper`

### Acne type classification
- **Author / Source**: `Taschenbier`
- **Scale**: `270 images` | `N/A` | `88 downloads/stars`
- **Classes / Taxonomy**: `Dermatitis perioral`, `Eksim`, `Karsinoma`, `Pustula`, `Tinea facialis`, `acne fulminans`, `acne nodules`, `blackhead`, `flek hitam`, `folikulitis` ... (+10 more)

### Damaged Package Detection
- **Author / Source**: `IoT Project`
- **Scale**: `1k images` | `N/A` | `97 downloads/stars`
- **Classes / Taxonomy**: `damaged`, `damaged food packaging box`, `food item boxes`, `packaging boxes`, `packaging boxes that are damaged`

### Klasifikasi Jewarat
- **Author / Source**: `Klasifikasi`
- **Scale**: `1.28k images` | `1 model` | `16 downloads/stars`
- **Classes / Taxonomy**: `Kistik`, `Nodule`, `Papule`, `Pustule`

### Face_Shape
- **Author / Source**: `Train Model`
- **Scale**: `9.15k images` | `N/A` | `21 downloads/stars`
- **Classes / Taxonomy**: `Heart`, `Oblong`, `Oval`, `Round`, `Square`

### features
- **Author / Source**: `LVS370`
- **Scale**: `1.27k images` | `N/A` | `31 downloads/stars`
- **Classes / Taxonomy**: `data`

### melanoma detection
- **Author / Source**: `melanomadetection`
- **Scale**: `3.75k images` | `1 model` | `43 downloads/stars`
- **Classes / Taxonomy**: `normal`, `melanoma`

### Sign_Language
- **Author / Source**: `Signlanguage`
- **Scale**: `9.9k images` | `N/A` | `93 downloads/stars`
- **Classes / Taxonomy**: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `A`, `B` ... (+9 more)

### Uong
- **Author / Source**: `Mushroomify`
- **Scale**: `1.44k images` | `N/A` | `16 downloads/stars`
- **Classes / Taxonomy**: `edible`, `poisonous`

### mine
- **Author / Source**: `project`
- **Scale**: `555 images` | `1 model` | `14 downloads/stars`
- **Classes / Taxonomy**: `gold`, `benitoite`, `calcite`, `copper`, `cuprite`, `erythrite`, `gypsum`, `halite`, `limonite`, `magnetite` ... (+5 more)

### Ex-Guard 2
- **Author / Source**: `Mini project`
- **Scale**: `2.81k images` | `1 model` | `27 downloads/stars`
- **Classes / Taxonomy**: `Cheating`, `Not-cheating`

### WRM
- **Author / Source**: `New Workspace`
- **Scale**: `200 images` | `N/A` | `15 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `RB`, `RL`, `RR`

### blindness detection
- **Author / Source**: `shreya`
- **Scale**: `50 images` | `N/A` | `15 downloads/stars`
- **Classes / Taxonomy**: `Mild`

### Cricket-Football-Baseball Classification
- **Author / Source**: `Popular Benchmarks`
- **Scale**: `251 images` | `3 models` | `230 downloads/stars`
- **Classes / Taxonomy**: `baseball`, `football`, `cricket`

### hardpoker
- **Author / Source**: `fod`
- **Scale**: `141 images` | `N/A` | `45 downloads/stars`
- **Classes / Taxonomy**: `H_1`, `H_10`, `H_2`, `H_3`, `H_4`, `H_5`, `H_6`, `H_7`, `H_8`, `H_9` ... (+4 more)

### Hack ISU v2 CV Proof of Concept
- **Author / Source**: `Alex Luo`
- **Scale**: `2.55k images` | `N/A` | `18 downloads/stars`
- **Classes / Taxonomy**: `grape leaf`, `Apple Scab Leaf`, `Apple leaf`, `Apple rust leaf`, `Bell_pepper leaf`, `Bell_pepper leaf spot`, `Blueberry leaf`, `Cherry leaf`, `Corn Gray leaf spot`, `Corn leaf blight` ... (+10 more)

### eeg_classification
- **Author / Source**: `EEGClassification`
- **Scale**: `117 images` | `N/A` | `11 downloads/stars`
- **Classes / Taxonomy**: `left`, `rest`

### Signatures
- **Author / Source**: `shalini kumar`
- **Scale**: `2.64k images` | `1 model` | `17 downloads/stars`
- **Classes / Taxonomy**: `full_forg`, `full_org`

### PCOS
- **Author / Source**: `Luis Angelo Valerio`
- **Scale**: `1.92k images` | `N/A` | `22 downloads/stars`
- **Classes / Taxonomy**: `infected`, `notinfected`

### Chicken Classification
- **Author / Source**: `Fast Nuces Lahore`
- **Scale**: `997 images` | `2 models` | `24 downloads/stars`
- **Classes / Taxonomy**: `Aged`, `Dead`, `Healthy`

### brid
- **Author / Source**: `AgTech AI`
- **Scale**: `5.01k images` | `N/A` | `33 downloads/stars`
- **Classes / Taxonomy**: `B_160`, `B_161`, `B_162`, `B_163`, `B_164`, `B_165`, `B_166`, `B_167`, `B_168`, `B_169` ... (+10 more)

### haiwaipingce_v2
- **Author / Source**: `chickenbeauty`
- **Scale**: `309 images` | `N/A` | `12 downloads/stars`
- **Classes / Taxonomy**: `Cart`, `Desktop`, `Homepage`, `Order_detail`, `Order_list`, `Other`, `Product_detail`, `Search`, `Sourcing_venue`, `Start_order` ... (+1 more)

### Malaria Detection
- **Author / Source**: `Naslink`
- **Scale**: `6.26k images` | `1 model` | `17 downloads/stars`
- **Classes / Taxonomy**: `Parasitized`, `Uninfected`

### Paddy
- **Author / Source**: `Paddy`
- **Scale**: `458 images` | `3 models` | `70 downloads/stars`
- **Classes / Taxonomy**: `BLB`, `BLS`, `Bipolaris oryzae`, `bacterial panicle blight`

### gg
- **Author / Source**: `hyungeun`
- **Scale**: `2.61k images` | `N/A` | `42 downloads/stars`
- **Classes / Taxonomy**: `back`, `face`, `side_left`, `side_right`

### Real VS Fake Image
- **Author / Source**: `Real Fake Image Detection`
- **Scale**: `700 images` | `1 model` | `17 downloads/stars`
- **Classes / Taxonomy**: `Fake`, `Real`

### LCBSI-WBC-TRAIN
- **Author / Source**: `LCBSIWBC`
- **Scale**: `3.5k images` | `N/A` | `11 downloads/stars`
- **Classes / Taxonomy**: `basophil`, `eosinophil`, `lymphocyte`, `monocyte`, `neutrophil`

### FaceAttribute 2
- **Author / Source**: `HeheTeam`
- **Scale**: `9.18k images` | `1 model` | `23 downloads/stars`
- **Classes / Taxonomy**: `Beard`, `Earrings`, `Female`, `Glasses`, `Hat`, `Male`

### drunk detection
- **Author / Source**: `amal`
- **Scale**: `2.47k images` | `1 model` | `42 downloads/stars`
- **Classes / Taxonomy**: `============================== Drunk - v5 zibs`, `Drunk - v5 zibs`, `images`

### Snakes
- **Author / Source**: `Snakes`
- **Scale**: `2.96k images` | `N/A` | `26 downloads/stars`
- **Classes / Taxonomy**: `Abaco island boa`, `Amazon tree boa`, `Andaman cat snake`, `Andaman cobra`, `Arabian cobra`, `Arizona Coral snake`, `Asian cobra`, `Australian tiger snake`, `Ball python`, `Banded Krait` ... (+10 more)

### FVR
- **Author / Source**: `Stark Industries`
- **Scale**: `9.38k images` | `1 model` | `15 downloads/stars`
- **Classes / Taxonomy**: `fresh apple`, `fresh banana`, `fresh bellpepper`, `fresh carrot`, `fresh cucumber`, `fresh mango`, `fresh orange`, `fresh potato`, `rotten apple`, `rotten banana` ... (+7 more)

### IDK
- **Author / Source**: `R V College of Engineering`
- **Scale**: `89 images` | `N/A` | `30 downloads/stars`
- **Classes / Taxonomy**: `face`, `angledface`, `maskedangledface`

### gradpro
- **Author / Source**: `cobra team`
- **Scale**: `2.2k images` | `1 model` | `13 downloads/stars`
- **Classes / Taxonomy**: `healthy`, `Fresh Leaf`, `Gummy Stem Blight`, `Pythium Fruit Rot`, `downy-mildew`, `downy-mildew healthy`, `powdery-mildew`

### cat_behavior_classification
- **Author / Source**: `MASTER PROJECT`
- **Scale**: `225 images` | `N/A` | `13 downloads/stars`
- **Classes / Taxonomy**: `cat drinking`, `cat eating`, `cat fighting`, `cat laying`, `cat sitting`, `cat stratching`

### GERD
- **Author / Source**: `VIT Chennai`
- **Scale**: `8.95k images` | `1 model` | `16 downloads/stars`
- **Classes / Taxonomy**: `esophagitis`, `polyps`, `ulcerative-colitis`

### camera
- **Author / Source**: `Caleb Jett`
- **Scale**: `784 images` | `1 model` | `14 downloads/stars`
- **Classes / Taxonomy**: `bird`, `cat`, `deer`, `dog`, `raccoon`, `squirrel`, `skunk`

### Digital Otoscope
- **Author / Source**: `Otoscope`
- **Scale**: `241 images` | `1 model` | `35 downloads/stars`
- **Classes / Taxonomy**: `AOE`, `AOM`, `Normal`

## Vehicles, Aerospace & Transportation (18 Projects)

### Vehicle Classification
- **Author / Source**: `Paul Guerrie`
- **Scale**: `28k images` | `4 models` | `40 downloads/stars`
- **Classes / Taxonomy**: `Ambulance`, `Barge`, `Bicycle`, `Boat`, `Bus`, `Car`, `Cart`, `Caterpillar`, `Helicopter`, `Limousine` ... (+7 more)

### carColor
- **Author / Source**: `starco22`
- **Scale**: `4.21k images` | `1 model` | `128 downloads/stars`
- **Classes / Taxonomy**: `Black`, `Blue`, `Brown`, `Crimson`, `Gray`, `Green`, `Orange`, `Purple`, `Red`, `Silver` ... (+2 more)

### color_car
- **Author / Source**: `Mario Hernandez`
- **Scale**: `9.01k images` | `N/A` | `61 downloads/stars`
- **Classes / Taxonomy**: `blue`, `green`, `orange`, `red`, `yellow`, `black_grey`, `brown`, `pink`, `purple`, `white_silver_cream`

### Plane ML Classifier
- **Author / Source**: `Models`
- **Scale**: `21k images` | `2 models` | `31 downloads/stars`
- **Classes / Taxonomy**: `A10`, `A400M`, `AG600`, `AV8B`, `B1`, `B2`, `B52`, `Be200`, `C130`, `C17` ... (+10 more)

### Car tire life prediction
- **Author / Source**: `COMSATS`
- **Scale**: `410 images` | `1 model` | `25 downloads/stars`
- **Classes / Taxonomy**: `BALD_TYRES`, `Normal_tyres`, `Unlabeled`

### ModelsOfCars
- **Author / Source**: `JC`
- **Scale**: `4.36k images` | `1 model` | `25 downloads/stars`
- **Classes / Taxonomy**: `hyundai`, `Audi`, `Bentley`, `Benz`, `Bmw`, `Cadillac`, `Dodge`, `Ferrari`, `Ford`, `Ford mustang` ... (+9 more)

### Warship Classification 4Dec
- **Author / Source**: `SMU`
- **Scale**: `790 images` | `1 model` | `37 downloads/stars`
- **Classes / Taxonomy**: `AhmadYani`, `Anzac`, `ArleighBurke`, `FFS`, `LMV`, `Lekiu`, `Type45`

### vehicle-classification
- **Author / Source**: `Faiza`
- **Scale**: `2.22k images` | `N/A` | `12 downloads/stars`
- **Classes / Taxonomy**: `bus`, `car`, `truck`

### Car Damage Severity Assessment
- **Author / Source**: `CSP650`
- **Scale**: `1.69k images` | `2 models` | `13 downloads/stars`
- **Classes / Taxonomy**: `01-minor`, `02-moderate`, `03-severe`

### russian-military-vehicles
- **Author / Source**: `CapstoneProject`
- **Scale**: `400 images` | `N/A` | `45 downloads/stars`
- **Classes / Taxonomy**: `bm-21`, `btr-80`, `t-72`, `t-80`

### Cards clash royale
- **Author / Source**: `EVGENY`
- **Scale**: `8.72k images` | `N/A` | `13 downloads/stars`
- **Classes / Taxonomy**: `balloon`, `rocket`, `archer queen`, `archers`, `arrows`, `baby dragon`, `bandit`, `barbarian barrel`, `barbarian hut`, `barbarians` ... (+10 more)

### XFF- 5 Surface Ships
- **Author / Source**: `XForce`
- **Scale**: `611 images` | `1 model` | `15 downloads/stars`
- **Classes / Taxonomy**: `Aircraft Carrier(PNG)`, `Arleigh Burk(PNG)`, `Ticonderoga(PNG)`, `USS Freedom(PNG)`, `Zumwalt(PNG)`

### Car Make-Model Recognition
- **Author / Source**: `Car MakeModel`
- **Scale**: `200 images` | `1 model` | `28 downloads/stars`
- **Classes / Taxonomy**: `2008`, `208`, `3008`, `308`, `500`, `A`, `A4`, `A6`, `Audi`, `Avenger` ... (+9 more)

### CarRecognition
- **Author / Source**: `CarR`
- **Scale**: `2.85k images` | `1 model` | `42 downloads/stars`
- **Classes / Taxonomy**: `Unlabeled`, `honda_civic`, `toyota_altis`, `toyota_yaris`

### vehicle_color_class_new
- **Author / Source**: `NewOne`
- **Scale**: `9.89k images` | `1 model` | `48 downloads/stars`
- **Classes / Taxonomy**: `blue`, `gold`, `green`, `orange`, `red`, `yellow`, `beige`, `black`, `brown`, `grey` ... (+5 more)

### Aircraft Type Classification
- **Author / Source**: `Leo Ueno`
- **Scale**: `2.59k images` | `2 models` | `45 downloads/stars`
- **Classes / Taxonomy**: `Airbus A330`, `Airbus A380`, `Antonov AN-225 Mriya`, `Boeing 727`, `Boeing 737`, `Boeing 747`, `Boeing 757`, `Boeing 767`, `Boeing 777`, `Boeing 787`

### carcolor-2
- **Author / Source**: `Starvo`
- **Scale**: `2.19k images` | `1 model` | `18 downloads/stars`
- **Classes / Taxonomy**: `Black`, `Gray`, `Green`, `Orange`, `Purple`, `Red`, `Silver`, `White`, `Yellow`

### car damage
- **Author / Source**: `vit`
- **Scale**: `1.62k images` | `1 model` | `14 downloads/stars`
- **Classes / Taxonomy**: `01-minor`, `02-moderate`, `03-severe`

## Document, OCR, Currency & Security (10 Projects)

### Receipt or Invoice
- **Author / Source**: `Jakob`
- **Scale**: `1.8k images` | `1 model` | `1.55k downloads/stars`
- **Classes / Taxonomy**: `invoice`, `receipt`

### PRGTCMS
- **Author / Source**: `Pragmatech`
- **Scale**: `855 images` | `1 model` | `21 downloads/stars`
- **Classes / Taxonomy**: `941`, `Unlabeled`, `noname`

### Hexa
- **Author / Source**: `Mohit Srivastava`
- **Scale**: `2.75k images` | `N/A` | `35 downloads/stars`
- **Classes / Taxonomy**: `2`, `3`, `4`, `5`, `6`, `7`, `Unlabeled`

### Guns types
- **Author / Source**: `datasets`
- **Scale**: `7.91k images` | `1 model` | `16 downloads/stars`
- **Classes / Taxonomy**: `Cuchillos`, `Fusiles`, `Pistolas`, `Rifles`, `Unlabeled`, `escopetas`

### DOCUMENT CLASSIFICATION
- **Author / Source**: `TAHAR`
- **Scale**: `4.02k images` | `1 model` | `15 downloads/stars`
- **Classes / Taxonomy**: `CONTRAT`, `CV`, `FACTURES`

### currency detection
- **Author / Source**: `shanthan`
- **Scale**: `436 images` | `1 model` | `19 downloads/stars`
- **Classes / Taxonomy**: `10`, `100`, `20`, `200`, `2000`, `50`, `500`, `fake10`, `fake100`, `fake20` ... (+4 more)

### Coin detection
- **Author / Source**: `Coindetection`
- **Scale**: `2.83k images` | `1 model` | `52 downloads/stars`
- **Classes / Taxonomy**: `10c`, `1c`, `1e`, `20c`, `2c`, `2e`, `50c`, `5c`

### dataset-gun-segmented
- **Author / Source**: `Miguel Alejandro Ponce Proaño`
- **Scale**: `915 images` | `N/A` | `38 downloads/stars`
- **Classes / Taxonomy**: `person`, `Unlabeled`

### Label Characters
- **Author / Source**: `Projects`
- **Scale**: `20.8k images` | `6 models` | `32 downloads/stars`
- **Classes / Taxonomy**: `!`, `-`, `.`, `.I`, `/`, `0`, `11`, `13`, `2`, `3` ... (+9 more)

### Logo classification
- **Author / Source**: `Pierce Kelaita`
- **Scale**: `9.77k images` | `1 model` | `15 downloads/stars`
- **Classes / Taxonomy**: `A-bike`, `ANCAP`, `Abici`, `Accel`, `Acura`, `Adio`, `Alfa`, `Alfa Romeo`, `Alpine`, `American Bicycle` ... (+10 more)
