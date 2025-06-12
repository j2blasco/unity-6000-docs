* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.AddClip.html

#  [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html).AddClip
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animation.html "Go to Animation Component in the Manual")
## Declaration
public void AddClip([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, string newName); 
### Description
Adds a `clip` to the animation with name `newName`.
* * *
## Declaration
public void AddClip([AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) clip, string newName, int firstFrame, int lastFrame, bool addLoopFrame = false); 
### Parameters
Parameter | Description  
---|---  
addLoopFrame | Should an extra frame be inserted at the end that matches the first frame? Turn this on if you are making a looping animation.  
### Description
Adds `clip` to the only play between `firstFrame` and `lastFrame`. The new clip will also be added to the animation with name `newName`.
If a clip with that name already exists it will be replaced with the new clip.  
  

* * *
