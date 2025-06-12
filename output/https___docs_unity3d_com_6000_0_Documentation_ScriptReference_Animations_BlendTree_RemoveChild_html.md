* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.RemoveChild.html

#  [BlendTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.html).RemoveChild
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
public void RemoveChild(int index); 
### Parameters
Parameter | Description  
---|---  
index | The index of the blend tree to remove.  
### Description
Utility function to remove the child of a blend tree.
If the blend tree is a sub asset of the blend tree, it will be deleted. This function pushes an Undo operation.
* * *
