* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.CreateBlendTreeInController.html

#  [AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html).CreateBlendTreeInController
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
public [Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) CreateBlendTreeInController(string name, out [Animations.BlendTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.html) tree); 
## Declaration
public [Animations.AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) CreateBlendTreeInController(string name, out [Animations.BlendTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.html) tree, int layerIndex); 
### Parameters
Parameter | Description  
---|---  
name | The name of the BlendTree.  
tree | The created BlendTree.  
layerIndex | The index where the BlendTree will be created.  
### Description
Creates a BlendTree in a new AnimatorState.
The BlendTree will be a sub asset of the AnimatorController. This function pushes an Undo operation.
* * *
