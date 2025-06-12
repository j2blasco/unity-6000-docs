* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.BuildNavMeshData.html

#  [NavMeshBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.html).BuildNavMeshData
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
public static [AI.NavMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshData.html) BuildNavMeshData([AI.NavMeshBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSettings.html) buildSettings, List<NavMeshBuildSource> sources, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) localBounds, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
### Parameters
Parameter | Description  
---|---  
buildSettings | Settings for the bake process, see [NavMeshBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSettings.html).  
sources | List of input geometry used for baking, they describe the surfaces to walk on or obstacles to avoid.  
localBounds | Bounding box relative to position and rotation which describes the volume where the NavMesh should be built. Empty bounds is treated as no bounds, i.e. the NavMesh will cover all the inputs.  
position | Center of the NavMeshData. This specifies the origin for the NavMesh tiles (Additional resources: [NavMeshBuildSettings.tileSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSettings-tileSize.html)).  
rotation | Orientation of the NavMeshData, you can use this to generate NavMesh with an arbitrary up-vector – e.g. for walkable vertical surfaces.  
### Returns
**NavMeshData** Returns a newly built NavMeshData, or null if the NavMeshData was empty or an error occurred. The newly built NavMeshData, or null if the NavMeshData was empty or an error occurred. 
### Description
Builds a NavMesh data object from the provided input sources.
Note: that [NavMeshBuilder.BuildNavMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.BuildNavMeshData.html) has same effect as creating a new empty [NavMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshData.html) and calling [NavMeshBuilder.UpdateNavMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.UpdateNavMeshData.html).
* * *
