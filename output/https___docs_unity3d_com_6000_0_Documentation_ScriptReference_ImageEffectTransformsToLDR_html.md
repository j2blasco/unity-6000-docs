* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectTransformsToLDR.html

# ImageEffectTransformsToLDR
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
When using HDR rendering it can sometime be desirable to switch to LDR rendering during ImageEffect rendering.
Using this Attribute on an image effect will cause the destination buffer to be an LDR buffer, and switch the rest of the Image Effect pipeline into LDR mode. It is the responsibility of the Image Effect that this Attribute is associated to ensure that the output is in the LDR range.
* * *
