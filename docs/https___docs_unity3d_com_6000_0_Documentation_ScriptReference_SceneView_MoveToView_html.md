* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.MoveToView.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).MoveToView
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
public void MoveToView(); 
## Declaration
public void MoveToView([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target); 
### Parameters
Parameter | Description  
---|---  
target | A transform to place at the scene [pivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-pivot.html).  
### Description
Transforms all selected object to the scene [pivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-pivot.html).
If no argument is passed, each selected object is moved to the [pivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-pivot.html) point, keeping their relative spacing.
* * *
