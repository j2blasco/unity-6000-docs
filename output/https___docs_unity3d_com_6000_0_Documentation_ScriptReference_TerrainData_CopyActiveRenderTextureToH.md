* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.CopyActiveRenderTextureToHeightmap.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).CopyActiveRenderTextureToHeightmap
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
public void CopyActiveRenderTextureToHeightmap([RectInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.html) sourceRect, [Vector2Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html) dest, [TerrainHeightmapSyncControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainHeightmapSyncControl.html) syncControl); 
### Parameters
Parameter | Description  
---|---  
sourceRect | The part of the active Render Texture to copy.  
dest | The X and Y coordinates of the heightmap texture to copy into.  
syncControl | Controls how CPU synchronization is performed.  
### Description
Copies the specified part of the active [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) to the Terrain heightmap texture.
This functions calls [DirtyHeightmapRegion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.DirtyHeightmapRegion.html) internally and sends out the OnTerrainChanged message accordingly. The range of expected height values for the active [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) is between `0` and `0.5`. This is unlike [TerrainData.SetHeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SetHeights.html), which expects height values between `0` and `1`. Additional resources: [TerrainHeightmapSyncControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainHeightmapSyncControl.html), [DirtyHeightmapRegion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.DirtyHeightmapRegion.html), [SyncHeightmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SyncHeightmap.html).
* * *
