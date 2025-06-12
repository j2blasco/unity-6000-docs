* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-forceIntoRenderTexture.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).forceIntoRenderTexture
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
forceIntoRenderTexture; 
### Description
Should camera rendering be forced into a RenderTexture.
If set to true camera rendering will always happen into a RenderTexture instead of direct into the backbuffer. This can be useful if you have no image effects but want to use command buffers to act on the current rendering target.
* * *
