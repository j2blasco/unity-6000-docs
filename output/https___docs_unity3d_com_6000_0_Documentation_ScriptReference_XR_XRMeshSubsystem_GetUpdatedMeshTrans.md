* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GetUpdatedMeshTransforms.html

#  [XRMeshSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.html).GetUpdatedMeshTransforms
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
public NativeArray<MeshTransform> GetUpdatedMeshTransforms([Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
allocator | The allocator to use for the returned NativeArray.  
### Returns
**NativeArray <MeshTransform>** A new NativeArray of [MeshTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform.html)s. 
### Description
Gets the updated mesh transforms.
Use this to get updated transforms for each mesh tracked by the subsystem. The number of transforms returned may be less than the total number of tracked meshes. The results may be affected by previous calls to this method. That is, only transforms that have changed since the last call to this method may be returned.  
  
Typically, you should call this at regular intervals, for example, once per frame, in order to update the transform of each mesh. When a mesh is generated using [XRMeshSubsystem.GenerateMeshAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GenerateMeshAsync.html), the [MeshGenerationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationResult.html) also contains a transform and timestamp. Because generation is asynchronous, you can compare timestamps to ensure you are using the most recent transform. Larger values indicate newer transforms.  
  
This method always returns a new NativeArray, even when there are no updated transforms. The caller is responsible for disposing the returned NativeArray.  
  
Additional resources: [MeshTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform.html), [XRMeshSubsystem.GenerateMeshAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.GenerateMeshAsync.html), [MeshGenerationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationResult.html)
* * *
