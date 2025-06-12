* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-frameRate.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).frameRate
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
frameRate; 
### Description
The frame rate of the clip or URL in frames/second. (Read Only)
For URL sources, this is only set once the source preparation is completed. See [VideoPlayer.Prepare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.Prepare.html). This property is most accurate after the video does a complete playthrough.   
  
**Note:** On WebGL, the frame rate is always set to 24FPS because the underlying implementation, the javascript API for HTML5 <video>, does not expose frame rate information.
* * *
