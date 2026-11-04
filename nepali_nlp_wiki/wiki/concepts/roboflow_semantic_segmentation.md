# Taxonomy of Roboflow Semantic Segmentation Datasets

**Overview**: Analysis of **300 semantic segmentation projects** harvested from Roboflow Universe (`downloads>0 semantic segmentation`).

This document organizes pixel-level semantic segmentation datasets across autonomous driving roads, building facades, structural crack/corrosion inspection, medical/dental imagery, aerial/drone surveillance, and industrial infrastructure.

---
## Semantic Segmentation Dataset Taxonomy Summary

| Category | Project Count | Primary Segmentation Mask Focus |
|----------|---------------|--------------------------------|
| **Building Facades, Architecture & Interior Rooms** | 25 | Pixel-level mask segmentation, multi-class surface boundaries |
| **Structural Damage, Cracks & Corrosion Inspection** | 31 | Pixel-level mask segmentation, multi-class surface boundaries |
| **Aerial, Drone, Satellite & Environmental Monitoring** | 21 | Pixel-level mask segmentation, multi-class surface boundaries |
| **Medical, Dental & Anatomical Segmentation** | 27 | Pixel-level mask segmentation, multi-class surface boundaries |
| **Infrastructure, Roads, Lanes & Urban Autonomous Driving** | 56 | Pixel-level mask segmentation, multi-class surface boundaries |
| **General Object & Scene Semantic Segmentation** | 123 | Pixel-level mask segmentation, multi-class surface boundaries |
| **Industrial, Energy, Solar & Utilities** | 17 | Pixel-level mask segmentation, multi-class surface boundaries |

---

## Building Facades, Architecture & Interior Rooms (25 Projects)

### building-facade-segmentation-original
- **Author / Source**: `Building Facade`
- **Scale**: `598 images` | `1 model` | `104 downloads/stars`
- **Classes / Segmentation Masks**: `car`, `fence`, `vegetation`, `window`, `balcony-fence`, `facade`, `non-building-infrastructure`, `shop`, `street`, `traffic-infrastructure`

### facade-elements-try-for-converted-annotations
- **Author / Source**: `facade elements`
- **Scale**: `378 images` | `1 model` | `10 downloads/stars`
- **Classes / Segmentation Masks**: `door`, `window`, `shop`

### Room Separation 3
- **Author / Source**: `Neuramonks`
- **Scale**: `406 images` | `1 model` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `Room`

### Floor Segmentation
- **Author / Source**: `UNI`
- **Scale**: `347 images` | `N/A` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `floor`

### path123
- **Author / Source**: `Roboticsflow`
- **Scale**: `67 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `Floor`, `Paths`

### Windows Segmentation
- **Author / Source**: `Roboflow Universe Projects`
- **Scale**: `1.2k images` | `1 model` | `17 downloads/stars`
- **Classes / Segmentation Masks**: `Window`

### indoor
- **Author / Source**: `Jacks Workspace`
- **Scale**: `740 images` | `1 model` | `24 downloads/stars`
- **Classes / Segmentation Masks**: `basket`, `book`, `bottle`, `clock`, `clothes`, `door`, `floor`, `lamp`, `notebook`, `package` ... (+10 more)

### Floor_segmentation
- **Author / Source**: `New Workspace`
- **Scale**: `134 images` | `N/A` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `floor`

### fyp 2 - moving on
- **Author / Source**: `NSTP`
- **Scale**: `132 images` | `N/A` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `bed`, `chair`, `door`, `floor`, `lamp`, `light`, `mirror`, `plant`, `table`, `cupboard` ... (+8 more)

### FYP Dataset
- **Author / Source**: `NSTP`
- **Scale**: `262 images` | `N/A` | `42 downloads/stars`
- **Classes / Segmentation Masks**: `bed`, `chair`, `door`, `floor`, `lamp`, `light`, `mirror`, `plant`, `table`, `cupboard` ... (+8 more)

### Japanese house's floor plan2
- **Author / Source**: `ibaraki university`
- **Scale**: `50 images` | `N/A` | `10 downloads/stars`
- **Classes / Segmentation Masks**: `doors&windows`, `walls`

### wall
- **Author / Source**: `data`
- **Scale**: `200 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `0`

### WallSegmentation
- **Author / Source**: `BoxMaster`
- **Scale**: `141 images` | `1 model` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `2`, `3`, `4`, `5`

### windows_segmentation
- **Author / Source**: `Community`
- **Scale**: `N/A` | `N/A` | `N/A downloads/stars`
- **Classes / Segmentation Masks**: `by`, `403 images`, `1 model`, `cake`, `hot dog`, `sandwich`, `fat defect`, `fatty window`, `lean window`

### Japanese house's floor plan3
- **Author / Source**: `ibaraki university`
- **Scale**: `50 images` | `N/A` | `10 downloads/stars`
- **Classes / Segmentation Masks**: `doors&windows`, `walls`

### sdf
- **Author / Source**: `meow`
- **Scale**: `2.12k images` | `N/A` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `building`

### plan
- **Author / Source**: `RoyaTz`
- **Scale**: `696 images` | `1 model` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `wall`

### Test01
- **Author / Source**: `Gaming`
- **Scale**: `72 images` | `1 model` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `wall`, `Background`, `Barrier`, `Building`, `Ceiling`, `Container`, `Containers`, `Counter`, `Dead`, `DoorClosed` ... (+10 more)

### trucks
- **Author / Source**: `Vladimir Kacharov`
- **Scale**: `1.14k images` | `2 models` | `36 downloads/stars`
- **Classes / Segmentation Masks**: `box`, `floor`, `person`, `walls`

### Floor segmentation
- **Author / Source**: `RMI Flipkart`
- **Scale**: `1k images` | `2 models` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `Floor`, `\`

### Wall detection
- **Author / Source**: `Chinmay Bhalerao`
- **Scale**: `30 images` | `N/A` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `wall`

### room rover semantic
- **Author / Source**: `lalala`
- **Scale**: `245 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `walls`

### building_damages 2
- **Author / Source**: `zyf`
- **Scale**: `317 images` | `N/A` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `crack`, `graffiti`, `rust`, `brick_exposure`, `construction_crumb`, `spall`, `wood_damage`

### excelize_245_walls
- **Author / Source**: `ballonseg`
- **Scale**: `245 images` | `1 model` | `19 downloads/stars`
- **Classes / Segmentation Masks**: `walls`

### two people house plan1
- **Author / Source**: `IU`
- **Scale**: `561 images` | `1 model` | `13 downloads/stars`
- **Classes / Segmentation Masks**: `toilet`, `balcony`, `bath`, `cl`, `doors`, `entrance`, `garage`, `ldk`, `rouka`, `stairs` ... (+4 more)

## Structural Damage, Cracks & Corrosion Inspection (31 Projects)

### YoloV8Corrosion
- **Author / Source**: `Faisal Hazry`
- **Scale**: `770 images` | `1 model` | `205 downloads/stars`
- **Classes / Segmentation Masks**: `corrosion`

### dataset corrosao
- **Author / Source**: `corrosao`
- **Scale**: `800 images` | `1 model` | `169 downloads/stars`
- **Classes / Segmentation Masks**: `corrosion`

### Car Damages
- **Author / Source**: `Community`
- **Scale**: `N/A` | `N/A` | `N/A downloads/stars`
- **Classes / Segmentation Masks**: `by`, `2.32k images`, `51`, `Minor Damage (Dent)`, `Minor Damage (Scratch)`, `No Damage`, `Severe Damage`, `\`

### crcsegformer
- **Author / Source**: `DL`
- **Scale**: `439 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `Crack`

### dentalai
- **Author / Source**: `Pawan Valluri`
- **Scale**: `2.5k images` | `N/A` | `77 downloads/stars`
- **Classes / Segmentation Masks**: `Caries`, `Cavity`, `Crack`, `Tooth`

### crack detection
- **Author / Source**: `tishk`
- **Scale**: `359 images` | `2 models` | `23 downloads/stars`
- **Classes / Segmentation Masks**: `h c`, `hori crack`, `slanted`, `v c`, `verti crack`

### crackkk
- **Author / Source**: `connected wise`
- **Scale**: `319 images` | `1 model` | `18 downloads/stars`

### crack semantic
- **Author / Source**: `oumaima`
- **Scale**: `2.61k images` | `1 model` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `crack`

### Cracks 2.0
- **Author / Source**: `d`
- **Scale**: `1.73k images` | `1 model` | `17 downloads/stars`
- **Classes / Segmentation Masks**: `crack`, `horizontal crack`, `slanted`, `vertical crack`

### crack-shadyar-zhir
- **Author / Source**: `as`
- **Scale**: `3.12k images` | `1 model` | `15 downloads/stars`
- **Classes / Segmentation Masks**: `crack`, `horizontal crack`, `slanted`, `vertical crack`

### rust-seg-4
- **Author / Source**: `Omar EL GHATI`
- **Scale**: `2.53k images` | `N/A` | `71 downloads/stars`
- **Classes / Segmentation Masks**: `corrosion`, `rust-06-11 - v1 2024-11-06 7:29pm`

### cracks2
- **Author / Source**: `l`
- **Scale**: `3.15k images` | `1 model` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `h c`, `hori crack`, `slanted`, `v c`, `verti crack`

### segmentation
- **Author / Source**: `Rust`
- **Scale**: `51 images` | `1 model` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `rust-QtbZ`

### Crack semantic
- **Author / Source**: `shada`
- **Scale**: `478 images` | `1 model` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `crack`, `h c`, `slanted`, `v c`

### 4w_damage
- **Author / Source**: `4w`
- **Scale**: `436 images` | `1 model` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `damage`, `crack-hole`, `medium_deformation`, `medium_scratch`, `severe_deformation`, `severe_scratch`, `slight_deformation`, `slight_scratch`

### dental2
- **Author / Source**: `reza`
- **Scale**: `2.35k images` | `1 model` | `22 downloads/stars`
- **Classes / Segmentation Masks**: `Caries`, `Cavity`, `Crack`, `Tooth`

### crack
- **Author / Source**: `PCH`
- **Scale**: `3.68k images` | `1 model` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `object`

### Segmentation-yolov8
- **Author / Source**: `Crack EGY 2`
- **Scale**: `13.5k images` | `3 models` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `crack`, `Alligator crack - v1 2025-02-01 6:49pm`

### car-damage-type
- **Author / Source**: `Semantic Segment`
- **Scale**: `3.02k images` | `N/A` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `broken glass`, `crack`, `dent`, `scratch`, `broken light`, `flat tire`

### corrosion segmentation Jorge
- **Author / Source**: `corrosionjorge`
- **Scale**: `770 images` | `1 model` | `31 downloads/stars`
- **Classes / Segmentation Masks**: `corrosion`

### defect_n
- **Author / Source**: `os`
- **Scale**: `124 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `0`

### defect detection
- **Author / Source**: `incheon national university`
- **Scale**: `80 images` | `1 model` | `31 downloads/stars`
- **Classes / Segmentation Masks**: `Contamination`, `Crack`, `Spalling`

### Rust Segmentation
- **Author / Source**: `Rust`
- **Scale**: `770 images` | `1 model` | `172 downloads/stars`
- **Classes / Segmentation Masks**: `corrosion`

### apple-quality
- **Author / Source**: `bvod`
- **Scale**: `924 images` | `N/A` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `apple`, `apple-defect`

### CrackUnet
- **Author / Source**: `PavementCrack`
- **Scale**: `99 images` | `3 models` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `crack`

### guava_defect_segmentation 2
- **Author / Source**: `NCTU`
- **Scale**: `141 images` | `N/A` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `defect`

### Rust Segmentation-May2024
- **Author / Source**: `Sujon`
- **Scale**: `85 images` | `2 models` | `20 downloads/stars`
- **Classes / Segmentation Masks**: `Rust`

### Aquaculture Water
- **Author / Source**: `ADT`
- **Scale**: `140 images` | `1 model` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `1_defective`, `\`, `pond`, `remove`

### dentalai
- **Author / Source**: `MedithinQ`
- **Scale**: `2.5k images` | `N/A` | `27 downloads/stars`
- **Classes / Segmentation Masks**: `Caries`, `Cavity`, `Crack`, `Tooth`

### Weld defect detection
- **Author / Source**: `Basanth Kalanoor`
- **Scale**: `2.52k images` | `1 model` | `36 downloads/stars`
- **Classes / Segmentation Masks**: `weld`

### Crack_Dataset_rev3
- **Author / Source**: `Crack`
- **Scale**: `3.9k images` | `1 model` | `21 downloads/stars`
- **Classes / Segmentation Masks**: `crack`

## Aerial, Drone, Satellite & Environmental Monitoring (21 Projects)

### vegetation
- **Author / Source**: `segments`
- **Scale**: `713 images` | `4 models` | `26 downloads/stars`
- **Classes / Segmentation Masks**: `grass`

### water
- **Author / Source**: `test`
- **Scale**: `8.53k images` | `1 model` | `22 downloads/stars`
- **Classes / Segmentation Masks**: `water`, `load`

### Water Segmentation
- **Author / Source**: `WaterSegmentation`
- **Scale**: `9.15k images` | `1 model` | `15 downloads/stars`
- **Classes / Segmentation Masks**: `water`

### Water_Segmentation 2
- **Author / Source**: `Community`
- **Scale**: `N/A` | `N/A` | `N/A downloads/stars`
- **Classes / Segmentation Masks**: `by`, `1.59k images`, `79`, `water`

### Water detection
- **Author / Source**: `Riverdebrissegment`
- **Scale**: `644 images` | `1 model` | `16 downloads/stars`
- **Classes / Segmentation Masks**: `River`, `Water`

### warer
- **Author / Source**: `tiziano bardini`
- **Scale**: `180 images` | `N/A` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `water`

### Segformer Landslide Detection
- **Author / Source**: `LANDSLIDE`
- **Scale**: `1.01k images` | `1 model` | `29 downloads/stars`
- **Classes / Segmentation Masks**: `landslide`

### waterlevel detection
- **Author / Source**: `Bibek Basnet`
- **Scale**: `1.42k images` | `1 model` | `21 downloads/stars`
- **Classes / Segmentation Masks**: `water`, `River`

### FireSmokeSegmentation
- **Author / Source**: `moin`
- **Scale**: `201 images` | `N/A` | `10 downloads/stars`
- **Classes / Segmentation Masks**: `fire`, `smoke`

### drone semantic segmentation
- **Author / Source**: `01fe19bec236`
- **Scale**: `229 images` | `2 models` | `18 downloads/stars`
- **Classes / Segmentation Masks**: `drone`

### fire n smoke segmentatio
- **Author / Source**: `fire smoke detection`
- **Scale**: `160 images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `fire`, `smoke`

### Sattelite
- **Author / Source**: `Drone`
- **Scale**: `99 images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `City`, `Forest`, `Water`

### Clouds1500
- **Author / Source**: `Juliana`
- **Scale**: `1.49k images` | `N/A` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `Arvore`, `Cirriformes`, `Cumuliformes`, `Estratiformes`, `Estratocumuliformes`

### test
- **Author / Source**: `yuhan`
- **Scale**: `54 images` | `1 model` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `water`

### ARDIN
- **Author / Source**: `MINI`
- **Scale**: `537 images` | `N/A` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `WILDFIRE`

### Fire detection using YOLOv9
- **Author / Source**: `Fire detection Using YOLOv9`
- **Scale**: `75 images` | `N/A` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `Fire`

### fire_segmentation
- **Author / Source**: `Firedetectionsegmentation`
- **Scale**: `1.51k images` | `1 model` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `fire`

### fire-detection
- **Author / Source**: `firedetection`
- **Scale**: `275 images` | `1 model` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `Fire`

### Arial
- **Author / Source**: `Drone`
- **Scale**: `47 images` | `N/A` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `City`, `Forest`, `Water`

### wildfires smoke plumes segmentation
- **Author / Source**: `V1PlumasHumo`
- **Scale**: `1.06k images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `smoke`

### own-drone-ss
- **Author / Source**: `labelme dataset`
- **Scale**: `1.1k images` | `N/A` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `bitki`, `cubuk`, `insan`, `poset`

## Medical, Dental & Anatomical Segmentation (27 Projects)

### caries
- **Author / Source**: `niu workespeis`
- **Scale**: `34 images` | `N/A` | `13 downloads/stars`
- **Classes / Segmentation Masks**: `caries`

### semanticSeg
- **Author / Source**: `fracbone`
- **Scale**: `331 images` | `N/A` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `fracture-eDZa`

### Caries
- **Author / Source**: `Evident`
- **Scale**: `504 images` | `N/A` | `47 downloads/stars`
- **Classes / Segmentation Masks**: `Caries`, `deep caries`

### Dental Caries Detection-Deneme
- **Author / Source**: `Panoramic XRay Images`
- **Scale**: `213 images` | `1 model` | `13 downloads/stars`
- **Classes / Segmentation Masks**: `caries`, `restoration`

### PLAK - projectDens
- **Author / Source**: `projectDens`
- **Scale**: `84 images` | `2 models` | `40 downloads/stars`
- **Classes / Segmentation Masks**: `tooth`, `plaque`, `ty`

### 100 PA NEW
- **Author / Source**: `University of Alberta`
- **Scale**: `76 images` | `N/A` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `bone-loss`

### Liver Tumor Semantic Segmentation
- **Author / Source**: `RVB`
- **Scale**: `246 images` | `N/A` | `26 downloads/stars`
- **Classes / Segmentation Masks**: `Liver`, `Tumor`

### anterior PA Samane
- **Author / Source**: `University of Alberta`
- **Scale**: `51 images` | `N/A` | `21 downloads/stars`
- **Classes / Segmentation Masks**: `bone-loss`

### Caries detection
- **Author / Source**: `Digital Health BG`
- **Scale**: `198 images` | `1 model` | `29 downloads/stars`
- **Classes / Segmentation Masks**: `Childhood caries`, `Teeth`, `caries`

### TumorSeg
- **Author / Source**: `Seg`
- **Scale**: `2.15k images` | `1 model` | `23 downloads/stars`
- **Classes / Segmentation Masks**: `0`

### Osteoarthritis
- **Author / Source**: `Fracture Detection`
- **Scale**: `311 images` | `N/A` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `Bone Space Reduction`, `Bones Touching`, `Osteophyte`

### ss
- **Author / Source**: `test2`
- **Scale**: `4.38k images` | `N/A` | `10 downloads/stars`
- **Classes / Segmentation Masks**: `Caries`, `Crown`, `Filling`, `Implant`, `Root canal obturation`

### Single-tooth
- **Author / Source**: `University of Alberta`
- **Scale**: `123 images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `Bone-Loss`

### A4C Segmentation
- **Author / Source**: `IRPS354153`
- **Scale**: `498 images` | `N/A` | `18 downloads/stars`
- **Classes / Segmentation Masks**: `left-atrium`, `left-ventricle`, `right-atrium`, `right-ventricle`

### vehicle-parts-segmentation-for-recoloring
- **Author / Source**: `Vehiclerecolorsegment`
- **Scale**: `1.6k images` | `1 model` | `22 downloads/stars`
- **Classes / Segmentation Masks**: `Object - Boot`, `Object - Break`, `Object - Bumper-front`, `Object - Bumper-rear`, `Object - Car plate`, `Object - Disjoint`, `Object - Fracture`, `Object - Glass`, `Object - Grill`, `Object - Hood` ... (+10 more)

### dental 2
- **Author / Source**: `Yim`
- **Scale**: `4k images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `* annotate, and create datasets`, `* collaborate with your team on computer vision projects`, `* collect & organize images`, `* understand and search unstructured image data`, `==============================`, `Roboflow is an end-to-end computer vision platform that helps you`, `This dataset was exported via roboflow.com on December 7, 2023 at 6:16 AM GMT`, `tooth segmentation - v2 2023-01-09 11:28pm`

### train1+2
- **Author / Source**: `korrawiz`
- **Scale**: `36 images` | `N/A` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `tooth_11`, `tooth_12`, `tooth_13`, `tooth_14`, `tooth_15`, `tooth_16`, `tooth_17`, `tooth_18`, `tooth_21`, `tooth_22` ... (+10 more)

### Final anterior teeth
- **Author / Source**: `University of Alberta`
- **Scale**: `203 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `bone-loss`

### Brain Semantic
- **Author / Source**: `EXPAND AI`
- **Scale**: `1.46k images` | `N/A` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `abnormal`, `fetal skull`

### semantic_mammography2
- **Author / Source**: `mamografi`
- **Scale**: `844 images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `Calc`, `Mass`

### Semantic AutoPlaq
- **Author / Source**: `John Carson`
- **Scale**: `500 images` | `3 models` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `Plaque-Psoriasis`

### Bone_cropped_images
- **Author / Source**: `University of Alberta`
- **Scale**: `207 images` | `N/A` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `Bone`

### Lesion_Segmentation
- **Author / Source**: `ImageSeg`
- **Scale**: `46 images` | `N/A` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `lesion`

### elham PA
- **Author / Source**: `University of Alberta`
- **Scale**: `59 images` | `N/A` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `bone-loss`

### Individual bone loss segmentation 1
- **Author / Source**: `University of Alberta`
- **Scale**: `307 images` | `N/A` | `17 downloads/stars`
- **Classes / Segmentation Masks**: `tooth`, `apex`, `bone loss`

### Kidney-Liver Segmentation
- **Author / Source**: `Disertatie`
- **Scale**: `550 images` | `1 model` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `kidney`, `liver`

### Teeth
- **Author / Source**: `Dragulin Bogdan`
- **Scale**: `310 images` | `1 model` | `29 downloads/stars`
- **Classes / Segmentation Masks**: `Teeths`, `Explore Datasets and Models`, `Object Detection`, `Image Classification`, `Multimodal`, `Instance Segmentation`, `Research`, `Trending`, `Cited in Research`, `Computer Vision Projects` ... (+25 more)

## Infrastructure, Roads, Lanes & Urban Autonomous Driving (56 Projects)

### RoadVis Segmentation
- **Author / Source**: `Sankritya Rai`
- **Scale**: `3.17k images` | `1 model` | `38 downloads/stars`
- **Classes / Segmentation Masks**: `pothole`

### CDS_2023
- **Author / Source**: `FPT University`
- **Scale**: `287 images` | `1 model` | `56 downloads/stars`
- **Classes / Segmentation Masks**: `road-segmentation`

### Offroad-Dataset-II
- **Author / Source**: `xsianz`
- **Scale**: `1.44k images` | `N/A` | `148 downloads/stars`
- **Classes / Segmentation Masks**: `background`, `grass`, `object`, `obstacle`, `vegetation`, `dense-vegetation`, `high_vegetation`, `non_traversable_low_vegetation`, `path`, `puddle` ... (+4 more)

### Forest
- **Author / Source**: `DenisSleptsov`
- **Scale**: `50 images` | `1 model` | `13 downloads/stars`
- **Classes / Segmentation Masks**: `building`, `field`, `road`, `water`, `landscape-forest`

### Lane Area Semantic Segmentation
- **Author / Source**: `Demarcationbased Road Lane Segmentation`
- **Scale**: `857 images` | `1 model` | `26 downloads/stars`
- **Classes / Segmentation Masks**: `Road Lane`

### Tesla Wing
- **Author / Source**: `Senior Project`
- **Scale**: `191 images` | `1 model` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `obstacle`, `person`, `wall`, `drivable_surface`

### lane
- **Author / Source**: `lane1234`
- **Scale**: `2.51k images` | `1 model` | `19 downloads/stars`
- **Classes / Segmentation Masks**: `lane`

### SSG
- **Author / Source**: `ICS590 Semantic`
- **Scale**: `60 images` | `2 models` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `Agriculture`, `Barenland`, `Forest`, `Rangeland`, `Road`, `Unknown`, `Water`, `urban`

### crack detection
- **Author / Source**: `knu`
- **Scale**: `435 images` | `2 models` | `22 downloads/stars`
- **Classes / Segmentation Masks**: `concrete-crack`, `non crack`

### Road surface classification
- **Author / Source**: `Road Surface 2`
- **Scale**: `1.44k images` | `2 models` | `23 downloads/stars`
- **Classes / Segmentation Masks**: `asphalt`, `concrete`, `gravel`, `mud`

### AutoDriving2
- **Author / Source**: `Transportation`
- **Scale**: `289 images` | `1 model` | `40 downloads/stars`
- **Classes / Segmentation Masks**: `bike`, `car`, `pedestrian`, `road`, `sidewalk`, `sign`, `train`, `tree`, `wall`, `crossing-sign` ... (+7 more)

### 应急通道和普通通道的语义分割检测
- **Author / Source**: `szsti Project`
- **Scale**: `1.49k images` | `1 model` | `30 downloads/stars`
- **Classes / Segmentation Masks**: `common-lane`, `emergency-lane`

### CVUSA_aerials_prova_semantic_segmentation
- **Author / Source**: `Tesi`
- **Scale**: `84 images` | `1 model` | `22 downloads/stars`
- **Classes / Segmentation Masks**: `building`, `road`, `tree`, `pavement`

### IITJRoadSeg
- **Author / Source**: `RoadSegmentation`
- **Scale**: `526 images` | `2 models` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `Road`

### Sidewalk_segment
- **Author / Source**: `sidewalk`
- **Scale**: `33 images` | `1 model` | `18 downloads/stars`
- **Classes / Segmentation Masks**: `sidewalk`, `Road`, `Roadway`, `Sidewalk`, `downstairs`, `upstairs`

### sidewalk
- **Author / Source**: `school`
- **Scale**: `226 images` | `N/A` | `29 downloads/stars`
- **Classes / Segmentation Masks**: `object`, `sidewalk`

### MIT Indoor Semantic Segmentation
- **Author / Source**: `Test`
- **Scale**: `2.58k images` | `N/A` | `34 downloads/stars`
- **Classes / Segmentation Masks**: `airplane`, `apple`, `backpack`, `bag`, `ball`, `balloon`, `banana`, `baseball`, `basket`, `bear` ... (+10 more)

### Satellite Model
- **Author / Source**: `Bowdoin College`
- **Scale**: `265 images` | `2 models` | `26 downloads/stars`
- **Classes / Segmentation Masks**: `Roads`, `agriculture`

### Segmentation2
- **Author / Source**: `EvoDron2`
- **Scale**: `1.54k images` | `N/A` | `35 downloads/stars`
- **Classes / Segmentation Masks**: `Building`, `Field`, `Forest`, `Grass`, `Power lines`, `Road`, `Water`

### crosswalk
- **Author / Source**: `crosswalk`
- **Scale**: `5.19k images` | `1 model` | `20 downloads/stars`
- **Classes / Segmentation Masks**: `crosswalk`, `object`

### SafeCross
- **Author / Source**: `IMT Mines Als`
- **Scale**: `9.32k images` | `1 model` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `crosswalk`

### streetview-segmentation
- **Author / Source**: `Alexandra Conea`
- **Scale**: `126 images` | `1 model` | `17 downloads/stars`
- **Classes / Segmentation Masks**: `house`, `tree`

### 888888888
- **Author / Source**: `Rrr`
- **Scale**: `351 images` | `2 models` | `20 downloads/stars`
- **Classes / Segmentation Masks**: `car`, `construction`, `fence`, `people`, `tree`, `doroga`, `nebo`, `post`, `road-sign`, `roadway` ... (+6 more)

### Sidewalk_Semantics_Segmentation
- **Author / Source**: `Senior Design`
- **Scale**: `206 images` | `1 model` | `23 downloads/stars`
- **Classes / Segmentation Masks**: `sidewalk`

### objdetect
- **Author / Source**: `xyz`
- **Scale**: `2.67k images` | `N/A` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `auto`, `bag`, `bike`, `building`, `bus`, `car`, `cycle`, `dog`, `gate`, `grass` ... (+10 more)

### crosswalk
- **Author / Source**: `lane detection`
- **Scale**: `8.73k images` | `N/A` | `38 downloads/stars`
- **Classes / Segmentation Masks**: `crosswalk`

### LaneKeeping-TFrecords
- **Author / Source**: `DVision`
- **Scale**: `1.04k images` | `N/A` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `line`, `stop_line`

### SegFormer_01
- **Author / Source**: `IPMViT`
- **Scale**: `1.49k images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `insulator`, `window`, `concrete_wall`, `insulator_xps`, `masonry_wall`, `plasterboard_wall`

### lane detection
- **Author / Source**: `hahahahaha`
- **Scale**: `464 images` | `N/A` | `49 downloads/stars`
- **Classes / Segmentation Masks**: `lane`

### CVUSA_ground_semantic_segmentation
- **Author / Source**: `Tesi`
- **Scale**: `81 images` | `N/A` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `building`, `road`, `tree`, `pavement`

### lane detection
- **Author / Source**: `KIM`
- **Scale**: `74 images` | `1 model` | `16 downloads/stars`
- **Classes / Segmentation Masks**: `ddman`, `left_lane`, `right_lane`, `stop_lane`

### Crack and Pothole segmentation
- **Author / Source**: `Tecnologico`
- **Scale**: `245 images` | `1 model` | `85 downloads/stars`
- **Classes / Segmentation Masks**: `Crack`, `Pothole`

### road damage - Semantic
- **Author / Source**: `ComputerVision`
- **Scale**: `150 images` | `1 model` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `crack`, `pothole`, `D00`, `D20`, `D40`, `D44`, `alligator cracking`, `damaged markings`

### satelite
- **Author / Source**: `sateliteGSRL`
- **Scale**: `573 images` | `N/A` | `29 downloads/stars`
- **Classes / Segmentation Masks**: `pool`, `road`, `sidewalk`, `court`, `lake`, `parking_lot`, `yard`

### starview lab 1
- **Author / Source**: `starview`
- **Scale**: `573 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `pool`, `road`, `sidewalk`, `court`, `lake`, `parking_lot`, `yard`

### 盲人
- **Author / Source**: `myDataset`
- **Scale**: `367 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `ladder`, `person`, `road`, `blind_track`, `ecletric_cyclist`, `side_wall`, `zebra_crossing`

### Lane segment
- **Author / Source**: `Ho Chi Minh city University of Technology and Education`
- **Scale**: `300 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `road`

### SS_crosswalk
- **Author / Source**: `Community`
- **Scale**: `N/A` | `N/A` | `N/A downloads/stars`
- **Classes / Segmentation Masks**: `by`, `200 images`, `1 model`, `8`, `crosswalk`, `crosswalk-all`

### Lane
- **Author / Source**: `Jadeniphit`
- **Scale**: `337 images` | `1 model` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `lane`, `pavement`

### Lane Detection Real-World Dataset
- **Author / Source**: `UMARV`
- **Scale**: `1.92k images` | `1 model` | `34 downloads/stars`
- **Classes / Segmentation Masks**: `Lane-Lines`

### 멀칭 안 된+장애물 많은 곳
- **Author / Source**: `chungnam national university`
- **Scale**: `100 images` | `N/A` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `road`

### sidewalk
- **Author / Source**: `Dongeui University`
- **Scale**: `6.04k images` | `N/A` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `blocks`, `damaged`

### sidewalk and stair train image
- **Author / Source**: `Elvis`
- **Scale**: `853 images` | `1 model` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `sidewalk`, `stair`

### model_test
- **Author / Source**: `PAIK`
- **Scale**: `621 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `panel`, `PVC`, `concrete`, `concrete_load`, `mix`, `plasticpallet`, `plasticpallet_load`, `steel`, `steel_load`, `timber` ... (+1 more)

### realML
- **Author / Source**: `jML`
- **Scale**: `89 images` | `1 model` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `Curb`, `Grass`, `ParkConcrete`, `ParkDirt`, `Sidewalk`, `Street`, `Woodchips`

### SIDEWALK
- **Author / Source**: `coe 005`
- **Scale**: `1.07k images` | `2 models` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `non-walkable`, `walkable`

### Pothole Semantic Segmentation
- **Author / Source**: `Pothole Detection`
- **Scale**: `4.27k images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `Pothole`

### LaneKeeping
- **Author / Source**: `DVision`
- **Scale**: `1.04k images` | `3 models` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `line`, `stop_line`

### gravel road
- **Author / Source**: `trial`
- **Scale**: `32 images` | `1 model` | `19 downloads/stars`
- **Classes / Segmentation Masks**: `road`

### Segformer_SJ
- **Author / Source**: `IPMViT`
- **Scale**: `1.62k images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `concretewall`, `insulation`, `masonrywall`, `opening`, `plasterboard`

### Pothole segmentation
- **Author / Source**: `Segmentation`
- **Scale**: `420 images` | `1 model` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `Pothole`

### VanishingPointDetection
- **Author / Source**: `Vanishing Point and road detection`
- **Scale**: `219 images` | `1 model` | `15 downloads/stars`
- **Classes / Segmentation Masks**: `zebra`, `railing`, `road-lane`, `road-line`, `vnp`

### Road_detection
- **Author / Source**: `GGXR2`
- **Scale**: `1.31k images` | `N/A` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `Road`

### road detection self driving
- **Author / Source**: `Object detection`
- **Scale**: `1.16k images` | `2 models` | `19 downloads/stars`
- **Classes / Segmentation Masks**: `road`

### lane_test 2
- **Author / Source**: `changwon national university`
- **Scale**: `30 images` | `N/A` | `22 downloads/stars`
- **Classes / Segmentation Masks**: `lane`

### asdf
- **Author / Source**: `StanfordCS231N`
- **Scale**: `2.39k images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `crack`, `pothole`, `damaged markings`, `guardrail`

## General Object & Scene Semantic Segmentation (123 Projects)

### Golf Club Detection
- **Author / Source**: `Pronisi`
- **Scale**: `8.58k images` | `3 models` | `37 downloads/stars`
- **Classes / Segmentation Masks**: `object`, `0`, `3`

### Tennis Court Segmentation
- **Author / Source**: `Tennis Court Segmentation`
- **Scale**: `545 images` | `1 model` | `58 downloads/stars`
- **Classes / Segmentation Masks**: `tennis-court`

### 2_D2_Tile
- **Author / Source**: `TCC`
- **Scale**: `422 images` | `N/A` | `28 downloads/stars`
- **Classes / Segmentation Masks**: `Em amadurecimento`, `Maduro`, `Verde`

### pole
- **Author / Source**: `sample`
- **Scale**: `35 images` | `1 model` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `pole`

### Orion_cars
- **Author / Source**: `Denis Ermak`
- **Scale**: `424 images` | `1 model` | `34 downloads/stars`
- **Classes / Segmentation Masks**: `Car`, `сar`

### signs
- **Author / Source**: `Anna Winiewska`
- **Scale**: `101 images` | `2 models` | `21 downloads/stars`
- **Classes / Segmentation Masks**: `circle`, `sign`, `square`, `triangle`, `rectangle`, `rhombus`

### Raccoon Detection
- **Author / Source**: `Semantic Segmentation`
- **Scale**: `2.01k images` | `2 models` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `Raccoons`

### LaPa-SegFormer
- **Author / Source**: `segspace`
- **Scale**: `3.6k images` | `N/A` | `27 downloads/stars`
- **Classes / Segmentation Masks**: `background`, `nose`, `hair`, `inner mouth`, `left eye`, `left eyebrow`, `lower lip`, `right eye`, `right eyebrow`, `skin` ... (+1 more)

### hb
- **Author / Source**: `college`
- **Scale**: `463 images` | `N/A` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `2`, `3`, `4`, `5`, `6`, `7`

### WeedSeg_Niigata_2
- **Author / Source**: `GraduationThesis`
- **Scale**: `70 images` | `N/A` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `weed`

### rail-human
- **Author / Source**: `labelme dataset`
- **Scale**: `212 images` | `N/A` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `person`, `rail-track`

### court-segmented
- **Author / Source**: `Shukur Sabzaliev1`
- **Scale**: `36 images` | `1 model` | `25 downloads/stars`
- **Classes / Segmentation Masks**: `Volleyball-Court`

### pomo_3
- **Author / Source**: `Pratik Pawar`
- **Scale**: `923 images` | `1 model` | `19 downloads/stars`
- **Classes / Segmentation Masks**: `0`, `2`, `3`

### car
- **Author / Source**: `dddd`
- **Scale**: `785 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `10c`, `10d`, `10h`, `10s`, `2c`, `2d`, `2h`, `2s`, `3c`, `3d` ... (+10 more)

### exam
- **Author / Source**: `exam`
- **Scale**: `1.25k images` | `1 model` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `-`, `- annotate- and create datasets`, `- collaborate with your team on computer vision projects`, `- collect - organize images`, `- export- train- and deploy computer vision models`, `- understand and search unstructured image data`, `OMR Detect2_v2 - v1 2023-06-14 2-02pm`, `OMR Scanner - v7 2023-09-29 7-57pm`, `Roboflow is an end-to-end computer vision platform that helps you`, `This dataset was exported via roboflow` ... (+3 more)

### transport
- **Author / Source**: `zaz`
- **Scale**: `3.35k images` | `N/A` | `17 downloads/stars`
- **Classes / Segmentation Masks**: `bike`, `bus`, `truck`, `машина`

### ball3
- **Author / Source**: `11`
- **Scale**: `350 images` | `1 model` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `ball`

### PersonSegmentationSilviuLabeled
- **Author / Source**: `W1Check`
- **Scale**: `619 images` | `1 model` | `21 downloads/stars`
- **Classes / Segmentation Masks**: `person`

### Agro CV
- **Author / Source**: `max`
- **Scale**: `306 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `sistemas-de-riego`

### LandAnnot
- **Author / Source**: `HOPS Healthcare`
- **Scale**: `62 images` | `N/A` | `19 downloads/stars`
- **Classes / Segmentation Masks**: `land-Sx1C`

### Dataset Caixa Toledo
- **Author / Source**: `Thiago T Moura`
- **Scale**: `968 images` | `N/A` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `box_top`

### roller-seg
- **Author / Source**: `Purdue`
- **Scale**: `191 images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `0`, `2`, `3`

### Leaf Disease Segmentation
- **Author / Source**: `xfhor`
- **Scale**: `588 images` | `1 model` | `95 downloads/stars`
- **Classes / Segmentation Masks**: `Leaf Diseases`

### Eagle Steak
- **Author / Source**: `Clinton Anani`
- **Scale**: `102 images` | `N/A` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `bed`

### Tongue Detect Project 0.5
- **Author / Source**: `tongue detect`
- **Scale**: `2.66k images` | `N/A` | `64 downloads/stars`
- **Classes / Segmentation Masks**: `Tongue`

### Tennis Lines Advanced
- **Author / Source**: `test`
- **Scale**: `41 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `2`, `3`, `4`

### DK
- **Author / Source**: `Danil Korovaev`
- **Scale**: `3.63k images` | `1 model` | `13 downloads/stars`
- **Classes / Segmentation Masks**: `toy-tank`

### cell3
- **Author / Source**: `siom`
- **Scale**: `960 images` | `N/A` | `13 downloads/stars`
- **Classes / Segmentation Masks**: `cell`

### Wrinkle Segmentation
- **Author / Source**: `TeknoFest23`
- **Scale**: `350 images` | `N/A` | `70 downloads/stars`
- **Classes / Segmentation Masks**: `Wrinkle`

### Balloons
- **Author / Source**: `Paul Guerrie`
- **Scale**: `74 images` | `18 models` | `881 downloads/stars`
- **Classes / Segmentation Masks**: `object`

### Plant Vision
- **Author / Source**: `Testing`
- **Scale**: `79 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `arrowhead`, `dwarf`

### Dog Segmentation V2
- **Author / Source**: `Dogsegmentationnose`
- **Scale**: `2.46k images` | `N/A` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `dog-nose`

### COW_SEM_SEG
- **Author / Source**: `COW`
- **Scale**: `100 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `cow`

### Roofing
- **Author / Source**: `Alexandra Conea`
- **Scale**: `200 images` | `N/A` | `77 downloads/stars`
- **Classes / Segmentation Masks**: `roof`

### food_semantic_segmentation
- **Author / Source**: `Suhjeong Kim`
- **Scale**: `148 images` | `1 model` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `food`, `plate`

### CMP_Image_Segmentation_Fine_Tune_Segformer
- **Author / Source**: `Sawera Khadim`
- **Scale**: `756 images` | `N/A` | `21 downloads/stars`

### ffb
- **Author / Source**: `Thesis`
- **Scale**: `48 images` | `N/A` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `calças`, `calções`, `camisa`, `camisola`, `polo`, `vestido`

### gans-person-gun-segmentaion
- **Author / Source**: `Miguel Alejandro Ponce Proaño`
- **Scale**: `291 images` | `N/A` | `32 downloads/stars`
- **Classes / Segmentation Masks**: `person`

### signals_segmentation_001_Jan24
- **Author / Source**: `Priel Hazan`
- **Scale**: `375 images` | `1 model` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `signal`

### jiaolong_2
- **Author / Source**: `yuxun`
- **Scale**: `26 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `impurity-AFFD`

### football_field_segmentation
- **Author / Source**: `footballdetection`
- **Scale**: `379 images` | `2 models` | `23 downloads/stars`
- **Classes / Segmentation Masks**: `football-bumpers`, `football-field`, `football-gate`, `football-tribune`

### OCR
- **Author / Source**: `abcd`
- **Scale**: `584 images` | `1 model` | `13 downloads/stars`
- **Classes / Segmentation Masks**: `Invoice`

### semantic
- **Author / Source**: `tumorsize`
- **Scale**: `208 images` | `1 model` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `organ`

### plastic detection
- **Author / Source**: `michael prasan`
- **Scale**: `70 images` | `1 model` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `plastic`, `ignore`

### Material 1 scratch
- **Author / Source**: `claudio tapia`
- **Scale**: `48 images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `scratch`

### tracksem
- **Author / Source**: `Thiagarajar collegeof engineering`
- **Scale**: `200 images` | `N/A` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `track1`

### row_segmentaiton_vineyard
- **Author / Source**: `Achyut`
- **Scale**: `191 images` | `1 model` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `row`

### full_img_leaf segmentation
- **Author / Source**: `National university of sciences and technology`
- **Scale**: `537 images` | `N/A` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `\`, `wheat-leaf`

### flat_dataset
- **Author / Source**: `Khang Nguyn`
- **Scale**: `240 images` | `1 model` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `SM_Bed_b`, `SM_Bed_lamp_a`, `SM_Bed_lamp_b`, `SM_Bed_table_a`, `SM_Bed_table_b`, `SM_Ceiling_a`, `SM_Ceiling_lamp_a`, `SM_Ceiling_lamp_b`, `SM_Ceiling_lamp_f`, `SM_Ceiling_lamp_g` ... (+10 more)

### NHL-2K
- **Author / Source**: `Ajay R`
- **Scale**: `331 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `player`, `referee`, `blueLine`, `centerLine`, `centerSpot`, `faceOffCircle`, `faceOffSpot`, `goalPost`, `goalie`, `redSpot`

### BReCan-CellSeg-UH512
- **Author / Source**: `NucleiSeg`
- **Scale**: `106 images` | `3 models` | `24 downloads/stars`
- **Classes / Segmentation Masks**: `Cell`

### detecting chess board
- **Author / Source**: `MOmo`
- **Scale**: `70 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `left-half`, `right-half`

### cell counting7
- **Author / Source**: `jin`
- **Scale**: `121 images` | `2 models` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `cell`, `deadcell`, `null`

### newInvoices
- **Author / Source**: `Alpha`
- **Scale**: `44 images` | `N/A` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `Documents`, `bill details`, `document type`, `item count`, `items`, `other`, `shop details`, `total`

### test
- **Author / Source**: `Univesity`
- **Scale**: `266 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `Erythrocyte`, `Leukocyte`

### rice
- **Author / Source**: `yolov8begin`
- **Scale**: `540 images` | `1 model` | `10 downloads/stars`
- **Classes / Segmentation Masks**: `Bacterialblight`, `Blast`, `Brownspot`, `tungro`

### MSW Classification
- **Author / Source**: `rishis workspace`
- **Scale**: `191 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `plastic`, `fiber`

### ASL-SEG
- **Author / Source**: `Manu`
- **Scale**: `815 images` | `N/A` | `22 downloads/stars`
- **Classes / Segmentation Masks**: `computer`, `drink`, `go`, `help`, `trade`

### Membaca Tempat Tidur
- **Author / Source**: `Roby Maulana`
- **Scale**: `100 images` | `1 model` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `Tempat-Tidur`

### Test-ConvertedYoloV8-Small
- **Author / Source**: `Research`
- **Scale**: `614 images` | `N/A` | `20 downloads/stars`
- **Classes / Segmentation Masks**: `object`, `person`

### peach-diseases
- **Author / Source**: `Jhon Alan Fernandez Maturano`
- **Scale**: `213 images` | `1 model` | `10 downloads/stars`
- **Classes / Segmentation Masks**: `Moniliosis`, `Oidio`, `Roya`, `Taphrina`, `Tiro`, `manchaBaterial`

### Luggage-V22
- **Author / Source**: `s`
- **Scale**: `1.52k images` | `N/A` | `29 downloads/stars`
- **Classes / Segmentation Masks**: `Backpack`

### sky detection
- **Author / Source**: `FLying Wedge defence and aerospace`
- **Scale**: `59 images` | `N/A` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `sky`

### fashdrive
- **Author / Source**: `G4RegtengleData`
- **Scale**: `100 images` | `N/A` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `fashdrive`

### eraser
- **Author / Source**: `G4RegtengleData`
- **Scale**: `100 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `eraser`

### Vessel Segmentation
- **Author / Source**: `SRT`
- **Scale**: `50 images` | `2 models` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `Buoy`, `Cargo`, `Ferry`, `Fishing boat`, `Lifeboat`, `Military`, `Motorboat`, `RIB`, `Rowing boat`, `Tour boat` ... (+3 more)

### SemanticClothes
- **Author / Source**: `project`
- **Scale**: `143 images` | `N/A` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `bag`, `dress`, `face`, `glasses`, `hat`, `jeans`, `shirt`, `top`, `blouse`, `denim_shorts` ... (+10 more)

### Material 3 scratch
- **Author / Source**: `claudio tapia`
- **Scale**: `48 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `scratch`

### Map
- **Author / Source**: `Major Project`
- **Scale**: `32 images` | `2 models` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `Living Area`

### Unet 1
- **Author / Source**: `robot`
- **Scale**: `339 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `back`, `worms`

### Monitor Screen detection
- **Author / Source**: `monitor detection`
- **Scale**: `2k images` | `1 model` | `16 downloads/stars`
- **Classes / Segmentation Masks**: `screen`

### NHL
- **Author / Source**: `Lanit`
- **Scale**: `331 images` | `N/A` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `player`, `referee`, `blueLine`, `centerLine`, `centerSpot`, `faceOffCircle`, `faceOffSpot`, `goalPost`, `goalie`, `redSpot`

### Button_segmentation
- **Author / Source**: `5BHEL`
- **Scale**: `100 images` | `1 model` | `10 downloads/stars`
- **Classes / Segmentation Masks**: `Button`

### nintendo 2
- **Author / Source**: `jsy`
- **Scale**: `143 images` | `N/A` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `nintendo`, `toy`

### Barbados Pipe
- **Author / Source**: `Aqua`
- **Scale**: `1.79k images` | `N/A` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `barbados-pipe`

### PERSONs
- **Author / Source**: `TST`
- **Scale**: `6.5k images` | `1 model` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `neutral`, `person`, `person_bmp`, `person_poly`

### flashdisk segmentation 2
- **Author / Source**: `Machine Learning Class`
- **Scale**: `50 images` | `N/A` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `fashdrive`

### grocery products
- **Author / Source**: `stars`
- **Scale**: `33 images` | `N/A` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `basket`, `book`, `bread`, `honey`, `plastic bag`, `sprite`, `LCD`, `biskit`, `biskit pack`, `bonn` ... (+10 more)

### 123
- **Author / Source**: `teeth`
- **Scale**: `229 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `C1`, `C2`, `C3`, `C4`, `C5`

### cow
- **Author / Source**: `hank`
- **Scale**: `25 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `cow`

### Dog Segmentation
- **Author / Source**: `xfhor`
- **Scale**: `180 images` | `1 model` | `17 downloads/stars`
- **Classes / Segmentation Masks**: `Dogs`

### UPM Palm Oil Segmentation 2
- **Author / Source**: `Segmentation`
- **Scale**: `1.33k images` | `N/A` | `10 downloads/stars`
- **Classes / Segmentation Masks**: `ground`, `tree`

### test_new
- **Author / Source**: `1`
- **Scale**: `248 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `feed_hydrate`, `larva`

### Javeri
- **Author / Source**: `Sai Subhash`
- **Scale**: `400 images` | `1 model` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `Javeri`

### TrashLandsSeg
- **Author / Source**: `MazWORKS`
- **Scale**: `135 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `Trash`

### area
- **Author / Source**: `GOOD`
- **Scale**: `150 images` | `N/A` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `corn`

### Hand-gesture Segmentation 2
- **Author / Source**: `PROJECTCOE512`
- **Scale**: `2.42k images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `palm`, `rock`, `stop`, `G11`, `fist`, `four`, `like`, `ok`, `one`, `three2` ... (+1 more)

### pvcell-segmentation
- **Author / Source**: `swati`
- **Scale**: `120 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `pv`

### Excavator_Semantic_Segmentation
- **Author / Source**: `Abdurakhmon`
- **Scale**: `783 images` | `2 models` | `17 downloads/stars`
- **Classes / Segmentation Masks**: `car`, `crane`, `excavator`, `human`, `tractor`, `truck`, `bulldozer`, `caterpillar`, `crusher`, `driller` ... (+1 more)

### Late Blight
- **Author / Source**: `UPIDET`
- **Scale**: `63 images` | `1 model` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `Disease`, `Leaf`

### Bags
- **Author / Source**: `Bags`
- **Scale**: `138 images` | `N/A` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `Backpack`, `Duffel Bags`, `Handbags`, `Trolley Bags`

### trainseg 2
- **Author / Source**: `railseg`
- **Scale**: `226 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `railways`

### mask
- **Author / Source**: `Lazman`
- **Scale**: `801 images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `object`

### IDE
- **Author / Source**: `Benjamin Sylvanus`
- **Scale**: `416 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `IDE-MAIN`, `LeftTab`, `Main`, `Right Tab`, `Terminal`

### waste
- **Author / Source**: `Community`
- **Scale**: `N/A` | `N/A` | `N/A downloads/stars`
- **Classes / Segmentation Masks**: `by`, `1.75k images`, `2 models`, `29`, `book`, `can`, `pencil`, `scissor`, `shoe`, `applecore` ... (+9 more)

### semantic test
- **Author / Source**: `Max O`
- **Scale**: `289 images` | `1 model` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `bishop`, `black-bishop`, `black-king`, `black-knight`, `black-pawn`, `black-queen`, `black-rook`, `white-bishop`, `white-king`, `white-knight` ... (+3 more)

### mainboard-v2
- **Author / Source**: `Hanoi University of Science and Tecnology`
- **Scale**: `98 images` | `N/A` | `16 downloads/stars`
- **Classes / Segmentation Masks**: `cpu`, `mainboard`, `pci`, `power`, `ram`, `sata`

### 3
- **Author / Source**: `ffferwf`
- **Scale**: `1.1k images` | `N/A` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `object`

### animal classification
- **Author / Source**: `mona`
- **Scale**: `3.94k images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `Bison`, `Deer`, `Elephant`, `Leopard`, `Lion`, `Tiger`

### Tennis Lines 2
- **Author / Source**: `test`
- **Scale**: `29 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `2`, `3`

### countertop_reco
- **Author / Source**: `objectdetect`
- **Scale**: `1k images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `countertop`, `main-countertop`, `sub-countertop`

### Maethon
- **Author / Source**: `Yam`
- **Scale**: `74 images` | `N/A` | `13 downloads/stars`
- **Classes / Segmentation Masks**: `Line`

### Traffic Sign
- **Author / Source**: `black tear`
- **Scale**: `732 images` | `2 models` | `15 downloads/stars`
- **Classes / Segmentation Masks**: `DeadEnd`, `Forward`, `Left`, `NoEntry`, `Right`, `STOP`

### Potato Crops
- **Author / Source**: `Project University`
- **Scale**: `250 images` | `1 model` | `18 downloads/stars`
- **Classes / Segmentation Masks**: `Camino`, `Derecha`, `Izquierda`, `Path-potato-plants`, `Surco`

### needle segmentation
- **Author / Source**: `Gauges`
- **Scale**: `3.95k images` | `N/A` | `12 downloads/stars`
- **Classes / Segmentation Masks**: `gauge-needles`

### names
- **Author / Source**: `Thesis`
- **Scale**: `48 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `calças`, `calções`, `camisa`, `camisola`, `polo`, `vestido`

### HandballLineDetection
- **Author / Source**: `USP`
- **Scale**: `195 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `line`

### ASL
- **Author / Source**: `Shivakumar`
- **Scale**: `527 images` | `N/A` | `4 downloads/stars`
- **Classes / Segmentation Masks**: `apple`, `can`, `good`, `I`, `get`, `have`, `help`, `how`, `like`, `love` ... (+8 more)

### bikini_102-201
- **Author / Source**: `Viacheslav Stadnichuk`
- **Scale**: `96 images` | `N/A` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `lower_clothes`, `upper_clothes`

### sf 2
- **Author / Source**: `Test1`
- **Scale**: `800 images` | `N/A` | `5 downloads/stars`
- **Classes / Segmentation Masks**: `hand`, `0`, `고무장갑`, `라텍스`

### NOVODATASIZE_648²_4²_3CLASSES
- **Author / Source**: `TCCdatasetpinkpeper`
- **Scale**: `352 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `Em amadurecimento`, `Maduro`, `Verde`

### test
- **Author / Source**: `rail detection`
- **Scale**: `891 images` | `N/A` | `2 downloads/stars`
- **Classes / Segmentation Masks**: `runway`

### H-Mobility-Class
- **Author / Source**: `HMobility`
- **Scale**: `827 images` | `N/A` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `load`, `traffic-light`

### prueba1
- **Author / Source**: `TFG`
- **Scale**: `5.95k images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `acera`, `baldosas podotactiles`, `banco`, `carretera`, `pared`, `paso de cebra`, `vegetacion`

### tap-gpt
- **Author / Source**: `Mostafa H`
- **Scale**: `208 images` | `2 models` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `screw-holes`

### gastrixc-sem-seg-22
- **Author / Source**: `Escuela Superior politecnica del chimborazo`
- **Scale**: `1.01k images` | `N/A` | `14 downloads/stars`
- **Classes / Segmentation Masks**: `Actividad-Leve`, `Actividad-Moderada`, `Actividad-Severa`, `Metaplasia`

### Rural data
- **Author / Source**: `Aero`
- **Scale**: `86 images` | `2 models` | `30 downloads/stars`
- **Classes / Segmentation Masks**: `roof`

### car rails
- **Author / Source**: `Car Parts Detection`
- **Scale**: `388 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `rails`

### 2
- **Author / Source**: `ffferwf`
- **Scale**: `406 images` | `N/A` | `7 downloads/stars`
- **Classes / Segmentation Masks**: `object`, `word`

### Semantic Segmentation
- **Author / Source**: `MRL030216`
- **Scale**: `251 images` | `N/A` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `background`, `ball`, `field`, `line`

### TA Jenis Sampah Plastik (Botol)
- **Author / Source**: `TA Lulus`
- **Scale**: `200 images` | `1 model` | `41 downloads/stars`
- **Classes / Segmentation Masks**: `Plastic-Bottle`

### Ferret 2
- **Author / Source**: `Uni`
- **Scale**: `465 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `Ferret`

### needles
- **Author / Source**: `needles`
- **Scale**: `3.45k images` | `1 model` | `11 downloads/stars`
- **Classes / Segmentation Masks**: `gauge-needles`

## Industrial, Energy, Solar & Utilities (17 Projects)

### ElectricPoleFull
- **Author / Source**: `ElectricPoleFull`
- **Scale**: `1.52k images` | `2 models` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `KoniecIzolatora`, `Luk`, `NiskieNapiecie`, `PreIzolator`, `RamkaIzolator`, `TabliczkaInna`, `TabliczkaL`, `izolator`, `lina`, `slup` ... (+1 more)

### Machinery
- **Author / Source**: `Worksite`
- **Scale**: `153 images` | `1 model` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `car`, `crane`, `excavator`, `tractor`, `truck`, `bulldozer`, `crusher`, `driller`, `lowloader`, `scissorsLift`

### Semantic_Segmentation
- **Author / Source**: `Solar Panel`
- **Scale**: `182 images` | `1 model` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `diode`, `Solar-panel`, `hotspot`

### Container Components Detection
- **Author / Source**: `ContainerDamage`
- **Scale**: `318 images` | `2 models` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `B`, `D_Inner`, `D_Outer`, `F_Inner`, `F_Outer`, `L_Inner`, `L_Outer`, `R`, `R_Inner`, `R_Outer` ... (+2 more)

### solarPanel
- **Author / Source**: `AIRenewableEnergy`
- **Scale**: `212 images` | `1 model` | `15 downloads/stars`
- **Classes / Segmentation Masks**: `solar-panels`

### New-Bolts-Dataset
- **Author / Source**: `Bolt`
- **Scale**: `502 images` | `1 model` | `23 downloads/stars`
- **Classes / Segmentation Masks**: `Bolt`

### Harness Segmentation
- **Author / Source**: `Sement`
- **Scale**: `642 images` | `1 model` | `51 downloads/stars`
- **Classes / Segmentation Masks**: `Harness`

### Porcelin
- **Author / Source**: `FYDP`
- **Scale**: `2.55k images` | `2 models` | `13 downloads/stars`
- **Classes / Segmentation Masks**: `Broken-Insulators`

### industry_Segmention
- **Author / Source**: `Community`
- **Scale**: `N/A` | `N/A` | `N/A downloads/stars`
- **Classes / Segmentation Masks**: `by`, `882 images`, `23`, `meter-1-pointer`, `meter-1-scale`, `meter-2-pointer`, `meter-2-scale`, `meter-3-pointer`, `meter-3-scale`, `meter-4-pointer` ... (+1 more)

### meter-segment
- **Author / Source**: `meterreaderocr`
- **Scale**: `631 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `ROI`

### pcb
- **Author / Source**: `pcb`
- **Scale**: `94 images` | `1 model` | `32 downloads/stars`
- **Classes / Segmentation Masks**: `0`, `silk`, `solder`

### ElectricPoleFull
- **Author / Source**: `ElectricPoleFull2`
- **Scale**: `1.01k images` | `3 models` | `6 downloads/stars`
- **Classes / Segmentation Masks**: `KoniecIzolatora`, `Luk`, `NiskieNapiecie`, `PreIzolator`, `RamkaIzolator`, `TabliczkaInna`, `TabliczkaL`, `izolator`, `lina`, `slup` ... (+1 more)

### Pipeline Segmentation
- **Author / Source**: `Aqua`
- **Scale**: `202 images` | `N/A` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `pipeline`

### Bootcamp Project
- **Author / Source**: `Soman Tariq`
- **Scale**: `256 images` | `1 model` | `1 downloads/stars`
- **Classes / Segmentation Masks**: `empty_roof`, `obstacles_on_roof`, `shadow_on_roof`, `solar_panel`

### powerlines
- **Author / Source**: `dronetreepruningpowerlineavoidance`
- **Scale**: `207 images` | `1 model` | `9 downloads/stars`
- **Classes / Segmentation Masks**: `powerline`

### pcb_single_mold
- **Author / Source**: `saiyond`
- **Scale**: `288 images` | `N/A` | `8 downloads/stars`
- **Classes / Segmentation Masks**: `mold`

### ElectricPoleTop
- **Author / Source**: `ElectricPoleTop`
- **Scale**: `315 images` | `3 models` | `3 downloads/stars`
- **Classes / Segmentation Masks**: `slup`
