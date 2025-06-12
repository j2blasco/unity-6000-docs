* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-occlusionMaskScale.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).occlusionMaskScale
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
occlusionMaskScale; 
### Description
A scale applied to the standard occulsion mask.
This property scales up the occlusion mask to allow pixels outside of the XR headset's field of vision are rendered to, allowing effects to access the required texture data. Scaling up the occlusion mask could incur a performance penalty on the GPU due to the extra pixels being rendered.
* * *
