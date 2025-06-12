* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.SetSiblingIndex.html

#  [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html).SetSiblingIndex
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
public static void SetSiblingIndex([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform, int siblingIndex, string name); 
### Parameters
Parameter | Description  
---|---  
transform | Transform that will have its sibling index changed.  
siblingIndex | New sibling index.  
name | Undo operation name.  
### Description
Sets the sibling index of transform and records an undo operation.
* * *
