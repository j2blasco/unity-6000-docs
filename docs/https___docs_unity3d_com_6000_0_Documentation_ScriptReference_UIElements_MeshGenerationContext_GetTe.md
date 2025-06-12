* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.GetTempMeshAllocator.html

#  [MeshGenerationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.html).GetTempMeshAllocator
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
public void GetTempMeshAllocator(out [UIElements.TempMeshAllocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TempMeshAllocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
allocator | The allocator.  
### Description
Returns an allocator that can be used to safely allocate temporary meshes from the job system. The meshes have the same scope as those allocated by AllocateTempMesh. 
* * *
