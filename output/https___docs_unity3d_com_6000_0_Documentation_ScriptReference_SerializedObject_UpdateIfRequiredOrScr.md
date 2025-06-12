* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.UpdateIfRequiredOrScript.html

#  [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).UpdateIfRequiredOrScript
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
public bool UpdateIfRequiredOrScript(); 
### Description
Update serialized object's representation, only if the object has been modified since the last call to Update or if it is a script.
In which case it is not safe to assume that SetDirty has been called. Return true if an Update was done. 
* * *
