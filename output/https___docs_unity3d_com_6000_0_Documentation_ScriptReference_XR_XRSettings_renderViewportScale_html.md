* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-renderViewportScale.html

#  [XRSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings.html).renderViewportScale
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
renderViewportScale; 
### Description
Controls how much of the allocated eye texture should be used for rendering.
Valid range is 0.0 to 1.0. This value can be changed at runtime without reallocating eye textures. Therefore it is useful for dynamically adjusting eye render resolution. This value cannot be changed while cameras are being rendered. Attempts to change the value during rendering will be ignored and an error will be logged. Changes made during gameplay updates won't be applied until the next frame.  
  
Some XR platforms may not immediately use this value.  
  
This value does not support deferred rendering. Attempts to change the value in the presence of a camera using deferred rendering will be ignored and an error will be logged.
* * *
