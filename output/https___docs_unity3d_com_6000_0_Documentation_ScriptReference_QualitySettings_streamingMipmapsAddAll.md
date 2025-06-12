* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsAddAllCameras.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).streamingMipmapsAddAllCameras
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
streamingMipmapsAddAllCameras; 
### Description
Process all enabled Cameras for texture streaming (rather than just those with StreamingController components).
Set to True to process all enabled Cameras for texture streaming. This is a quick way to set up an existing project. Set to False to process only those Cameras that have active StreamingController components. This allows more fine grain control.  
  
StreamingController components are always considered in the streaming system. These are considered active locations in the following cases:  
- Camera and StreamingController are enabled.  
- Camera is disabled but StreamingController is in a preloading state.  
Additional resources: [StreamingController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StreamingController.html).
* * *
