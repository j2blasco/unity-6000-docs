* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.DestroyObjectImmediate.html

#  [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html).DestroyObjectImmediate
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
public static void DestroyObjectImmediate([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) objectToUndo); 
### Parameters
Parameter | Description  
---|---  
objectToUndo | The object that will be destroyed.  
### Description
Destroys the object and records an undo operation so that it can be recreated.
Destroys the object with the same behaviour as DestroyImmediate (objectToUndo, true); Also stores all destroyed objects in the undo buffer so that they can be fully recreated.
* * *
