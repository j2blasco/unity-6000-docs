* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Burst.BurstAuthorizedExternalMethodAttribute.html

# BurstAuthorizedExternalMethodAttribute
class in Unity.Burst
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
The BurstAuthorizedExternalMethod attribute lets you mark a function as being authorized for Burst to call from within a static constructor.
Normally, Burst will not call into an external method while in a static constructor, because the static constructor may be called multiple times and there is no guarantee that any particular external function is "pure" (has no side effects when called twice). The BurstAuthorizedExternalMethod signifies that a function is "pure," in the sense that the end result of calling it multiple times, is the same as if you had called it only once. This indicates that it is safe for Burst to call from a static constructor. 
* * *
