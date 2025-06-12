* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectAfterScale.html

# ImageEffectAfterScale
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
Any Image Effect with this attribute will be rendered after Dynamic Resolution stage.
If you wish your image effect to be applied after the Dynamic Resolution has scaled back up add this attribute. The effect will be rendered at full resolution, important for effects that are in some way dependant on the screen width and height being a certain size.
* * *
