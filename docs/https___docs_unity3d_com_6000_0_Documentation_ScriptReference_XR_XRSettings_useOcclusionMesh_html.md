* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-useOcclusionMesh.html

#  [XRSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings.html).useOcclusionMesh
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
useOcclusionMesh; 
### Description
Specifies whether or not the occlusion mesh should be used when rendering. Enabled by default.
The occlusion mesh prevents GPU work from happening on portions of the eye texture that won't be visible in the HMD. Disabling this will lead to a decrease in GPU rendering performance. However, this may be needed to deal with certain features such as the grab pass.
* * *
