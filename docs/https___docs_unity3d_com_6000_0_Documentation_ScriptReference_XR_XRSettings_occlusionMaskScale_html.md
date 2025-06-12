* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-occlusionMaskScale.html

#  [XRSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings.html).occlusionMaskScale
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
A scale applied to the standard occulsion mask for each platform.
Occlusion masks are used to increase performance by not rendering to pixels that cannot be seen through the XR headset. Some post-processing effects require data from pixels that cannot be seen through the XR headset's restricted field of vision (blur effects, for example) in order to avoid visual artifacts and other display errors. This property scales up the occlusion mask to ensure pixels outside of the XR headset's field of vision are rendered to, allowing post-processing effects to access the required texture data. Scaling up the occlusion mask will incur a performance penalty on the GPU due to the extra pixels being rendered.
* * *
