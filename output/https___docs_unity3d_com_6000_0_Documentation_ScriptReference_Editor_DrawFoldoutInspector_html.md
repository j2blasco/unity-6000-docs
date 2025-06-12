* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawFoldoutInspector.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).DrawFoldoutInspector
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
public static void DrawFoldoutInspector([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target, ref [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) editor); 
### Parameters
Parameter | Description  
---|---  
target | The object to display the Inspector for.  
editor | The reference to a variable of type [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).  
### Description
Draws the inspector GUI with a foldout header for `target`.
Unity tracks the fold status for each different object type. Unity caches the created Editor object in the `editor` variable, eliminating the need to create it repeatedly. Make sure to destroy the Editor object using [Object.DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) after you have finished using it.
* * *
