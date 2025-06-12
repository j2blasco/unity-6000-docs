* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.UpdateNavMeshData.html

#  [NavMeshBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.html).UpdateNavMeshData
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
public static bool UpdateNavMeshData([AI.NavMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshData.html) data, [AI.NavMeshBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSettings.html) buildSettings, List<NavMeshBuildSource> sources, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) localBounds); 
### Parameters
Parameter | Description  
---|---  
data | The NavMeshData to update.  
buildSettings | The build settings which is used to update the NavMeshData. The build settings is also hashed along with the data, so changing settings will cause a full rebuild.  
sources | List of input geometry used for baking, they describe the surfaces to walk on or obstacles to avoid.  
localBounds | Bounding box relative to position and rotation which describes the volume where the NavMesh should be built.  
### Returns
**bool** Returns true if the update was successful. 
### Description
Incrementally updates the NavMeshData based on the sources.
Each time NavMeshData is built or updated, the source data is hashed, and the hashes are stored along with the [NavMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshData.html).  
  
When called, first the hashes are recomputed and compared and only changed portions are rebuilt. For this reason, the list of sources should always contain all the input geometry, even if they haven't moved or changed. If the list of sources is modified between calls to UpdateNavMeshData the missing/added sources are considered changes. Try to provide the sources that have not changed since the last update in the same relative order as before because their sequence can affect the values of the hashes. This measure ensures that unchanged portions don't get rebuilt unnecessarily.  
  
You must supply a [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-ctor.html) struct for the `localBounds` parameter.  
  
Additional resources: [NavMeshBuilder.UpdateNavMeshDataAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.UpdateNavMeshDataAsync.html).
* * *
