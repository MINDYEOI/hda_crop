# HDA_Crop
Crop HDA+ dataset~

## Usage
1. Clone this repo.
```
git clone https://github.com/MINDYEOI/hda_crop.git
```
2. Move to the `hda_crop` directory.
3. Run the `main.py` or `cleanMain.py`.
```
python main.py # To run main.py
python cleanMain.py # To run cleanMain.py
```



## Structure
```
hda_crop
└ hda_annotations/
└ hda_detections_all/
└ hda_detections_clean/
└ seq2img/
└ output/
└ annotation.py
└ detection.py
└ jebal.py
└ main.py
└ cleanMain.py
```
* hda_annotations/    
  It consists of the text files which is named `cam#<#camera>`.  
  It contains the label, coordinates information.   
  In `annotation.py`, we can get the **label, coordinates** information using `hda_annotations`.

* hda_detections_all/  
  It consists of the folders which is named `camera<#camera>/Detections`.
  `allD.txt` in the folders contains the list, which is composed of [#camera, #frame, x, y, w, h].  
  The person's coordinates **which has the occlusion** can be calucalated through x, y, w and h.  
  In `detection.py`, we can get the **filtered coordinates** information using `hda_detection_all`.  

* hda_detections_clean/  
   It consists of the folders which is named `camera<#camera>/Detections`.
   `allD.txt` in the folders contains the list, which is composed of [#camera, #frame, x, y, w, h].
   The person's coordinates **which has no occlusion** can be calucalated through x, y, w and h.  
   In `detection.py`, we can get the **filtered coordinates** information using `hda_detection_all`.
* seq2img/  
  It is the jpg files which is converted from the seq files in HDA+ dataset.
* output/  
  It is consists of the cropped images.
* annotation.py
* detection.py
* jebal.py  
  It crops the images and saves the cropped images.
* main.py  
   It works for the **occlusion dataset**.
* cleanMain.py  
   It works for the **no occlusion dataset**.


## Note
*  HDA+ dataset의 `cam02` seq 는 데이터 전처리에서 제외했습니다.
   *  GTAnnotationsAll 값에서 `cam02` 값이 없기 때문입니다.
