* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-pickGameObjectCustomPasses.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).pickGameObjectCustomPasses
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
Subscribe to this event to add additional picking objects to the [HandleUtility.PickGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickGameObject.html) method.
[PickGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickGameObject.html) invokes this delegate when clicking in the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).  
  
An example use case for this event would be if you are rendering meshes with [Graphics.RenderMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html), and would like to be able to select the GameObject that represents these meshes.
* * *
