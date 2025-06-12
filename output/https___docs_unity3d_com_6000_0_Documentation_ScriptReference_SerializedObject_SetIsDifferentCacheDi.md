* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.SetIsDifferentCacheDirty.html

#  [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).SetIsDifferentCacheDirty
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
public void SetIsDifferentCacheDirty(); 
### Description
Update `hasMultipleDifferentValues` cache on the next /Update()/ call.
Normally, you should not need to call this, as the SerializedProperty setters take care of this. However, when you change an object bypassing the SerializedProperty class, you will need to manually call this to force the difference cache to be updated.
* * *
