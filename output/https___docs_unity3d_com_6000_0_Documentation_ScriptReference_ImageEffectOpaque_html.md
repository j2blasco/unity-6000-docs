* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectOpaque.html

# ImageEffectOpaque
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
Any Image Effect with this attribute will be rendered after opaque geometry but before transparent geometry.
This allows for effects which extensively use the depth buffer (SSAO, etc) to affect only opaque pixels. This attribute can be used to reduce the amount of visual artifacts in a Scene with post processing.
* * *
