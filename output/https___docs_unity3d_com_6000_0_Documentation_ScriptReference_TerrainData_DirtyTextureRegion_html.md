* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.DirtyTextureRegion.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).DirtyTextureRegion
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
public void DirtyTextureRegion(string textureName, [RectInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.html) region, bool allowDelayedCPUSync); 
### Parameters
Parameter | Description  
---|---  
textureName | The name of the Terrain texture.  
region | The rectangular region to mark as dirty.  
allowDelayedCPUSync | Specifies whether to allow delayed CPU synchronization of the texture.  
### Description
Marks the specified part of the Terrain texture as dirty.
Use this function only after you manually change the GPU part of the Terrain texture, such as by using [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html). Set the `allowDelayedCPUSync` parameter to `true` if you want Unity to perform immediate synchronization of the CPU part. If you set it to `false`, Unity queues the reading back of the dirty region until the next call to [SyncTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SyncTexture.html).  
  
If the current active [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) contains your changes, and you want to copy a part of it into the Terrain texture, use [CopyActiveRenderTextureToTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.CopyActiveRenderTextureToTexture.html) instead.
* * *
