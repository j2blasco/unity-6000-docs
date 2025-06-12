* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.UpdateNavMeshDataAsync.html

#  [NavMeshBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.html).UpdateNavMeshDataAsync
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
public static [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) UpdateNavMeshDataAsync([AI.NavMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshData.html) data, [AI.NavMeshBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSettings.html) buildSettings, List<NavMeshBuildSource> sources, [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) localBounds); 
### Parameters
Parameter | Description  
---|---  
data | The NavMeshData to update.  
buildSettings | The build settings used to update the NavMeshData. The build settings are also hashed along with the data, so changing the settings is likely to cause a full rebuild.  
sources | List of input geometry used for baking, they describe the surfaces to walk on or obstacles to avoid.  
localBounds | Bounding box relative to position and rotation which describes to volume where the NavMesh should be built.  
### Returns
**AsyncOperation** Can be used to check the progress of the update. 
### Description
Asynchronously and incrementally updates the NavMeshData based on the sources.
Each time NavMeshData is built or updated, the source data is hashed, and the hashes are stored along with the NavMeshData.  
  
When UpdateNavMeshDataAsync() is called, first the hashes are compared and only changed portions are rebuilt. For this reason, the list of sources should always contain all the input geometry, even if they haven't moved or changed. If the list of sources is modified between calls to UpdateNavMeshDataAsync the missing/added sources are considered changes. Try to provide the sources that have not changed since the last update in the same relative order as before because their sequence can affect the values of the hashes. This measure ensures that unchanged portions don't get rebuilt unnecessarily.  
  
You must supply a [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-ctor.html) struct for the `localBounds` parameter.  
  
Additional resources: [NavMeshBuilder.Cancel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.Cancel.html).
* * *
