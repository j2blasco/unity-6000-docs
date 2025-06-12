* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-cullingMask.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).cullingMask
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
cullingMask; 
### Description
This is used to light certain objects in the Scene selectively.
A [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) will only be illuminated by a light if that light's `cullingMask/` includes the layer chosen for the GameObject (ie, the mask bit for the layer must be set to 1 for the object to receive any light). See [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) for more information about layer masking. Additional resources: [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html).
* * *
