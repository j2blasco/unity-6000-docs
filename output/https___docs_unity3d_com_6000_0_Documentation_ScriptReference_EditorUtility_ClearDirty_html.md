* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.ClearDirty.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).ClearDirty
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
public static void ClearDirty([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target); 
### Description
Clear `target's` dirty flag.
Unity uses the dirty flag to find changed assets that must be saved to disk. Clear the dirty flag if you make changes to an asset that don't need to be saved, such as temporary changes that you subsequently revert.
* * *
