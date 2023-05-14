###### tags: `CoachAI` `TrackNetV2` `GitLab` `Shot Segmentation`

# Event Detection with TrackNet predict (GitLab)

## :gear: 1. Install
### System Environment

        
        $ sudo apt-get install git
        $ sudo apt-get install python3-pip
        $ pip3 install scipy
        $ pip3 install numpy
        $ pip3 install pandas
        $ git clone https://gitlab.com/lukelin/shot_segmentation_with_tracknet_predict
        
## :clapper: 2. Event Detection with TrackNet Result

### Step 1 : Get TrackNet Result

TrackNetV2 : https://gitlab.com/lukelin/pytorch-tracknetv2-6-in-6-out

### Step 2 : Denoise TrackNet Coordinates

`python3 denoise.py --input_csv=<csvPath>`
    
Just put the predict csv file of TrackNetV2 on `<csvPath>`. It will filter out the noise and apply linear interpolation if missing frames less than 5.

#### The csv after apply `denoise.py` should look like : ####

![](https://i.imgur.com/6FcPJE4.png)
### . ###
### . ###
### . ###
![](https://i.imgur.com/siw8T0W.png)


### Step 3 : Shot segmentation ###

`python3 event_detection.py --input_csv=<csvPath>`

The code will recognize each Event
- First event is Serve.
- Last event is Dead.
- The others are Shot. 

#### The result should look like : ####
![](https://i.imgur.com/hr5MDSi.png)
