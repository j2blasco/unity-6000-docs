* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.CreateBlendTreeChild.html

#  [BlendTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.html).CreateBlendTreeChild
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
public [Animations.BlendTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.html) CreateBlendTreeChild(float threshold); 
## Declaration
public [Animations.BlendTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.html) CreateBlendTreeChild([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position); 
### Parameters
Parameter | Description  
---|---  
position | The position of the child. When using 2D blend trees.  
threshold | The threshold of the child. When using 1D blend trees.  
### Description
Utility function to add a child blend tree to a blend tree.
The blend tree asset that is created is added as a sub asset of the blend tree. This function pushes an Undo operation.
* * *
