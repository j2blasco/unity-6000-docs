* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectUsesCommandBuffer.html

# ImageEffectUsesCommandBuffer
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Use this attribute when image effects are implemented using Command Buffers.
When you use this attribute, Unity renders the Scene into a RenderTexture instead of the actual target. Please note that Camera.forceIntoRenderTexture may have the same effect, but only in some cases.
* * *
