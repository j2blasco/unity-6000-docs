* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDevice.UpdateEyeTextureMSAASetting.html

#  [XRDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDevice.html).UpdateEyeTextureMSAASetting
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
## Declaration
public static void UpdateEyeTextureMSAASetting(); 
### Returns
**void** Nothing. 
### Description
Recreates the XR platform's eye texture swap chain with the appropriate anti-aliasing sample count. The reallocation of the eye texture will only occur if the MSAA quality setting's sample count is different from the sample count of the current eye texture. Reallocations of the eye textures will happen at the beginning of the next frame. This is an expensive operation and should only be used when necessary.
* * *
