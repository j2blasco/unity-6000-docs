* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.SyncTexture.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).SyncTexture
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
public void SyncTexture(string textureName); 
### Parameters
Parameter | Description  
---|---  
textureName | The name of the Terrain texture to synchronize.  
### Description
Performs synchronization queued by previous calls to [CopyActiveRenderTextureToTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.CopyActiveRenderTextureToTexture.html) and [DirtyTextureRegion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.DirtyTextureRegion.html), which makes CPU data of the Terrain textures up to date.
* * *
