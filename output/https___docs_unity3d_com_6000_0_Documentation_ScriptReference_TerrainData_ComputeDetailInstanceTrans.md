* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.ComputeDetailInstanceTransforms.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).ComputeDetailInstanceTransforms
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
public DetailInstanceTransform[] ComputeDetailInstanceTransforms(int patchX, int patchY, int layer, float density, out [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds); 
### Parameters
Parameter | Description  
---|---  
patchX | The x index of the patch.  
patchY | The y index of the patch.  
layer | The prototype index.  
density | The density setting of the detail.  
bounds | Returns the bounds of the detail objects.  
### Description
This function computes and returns an array of detail object transforms for the specified patch and the specified prototype. You can use this function to retrieve the exact same transform data the Unity engine uses for detail rendering.
Additional resources: [DetailInstanceTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DetailInstanceTransform.html).
* * *
