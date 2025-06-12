* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.UpdateTileRaw.html

#  [SparseTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.html).UpdateTileRaw
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
public void UpdateTileRaw(int tileX, int tileY, int miplevel, byte[] data); 
### Parameters
Parameter | Description  
---|---  
tileX | Tile X coordinate.  
tileY | Tile Y coordinate.  
miplevel | Mipmap level of the texture.  
data | Tile raw pixel data.  
### Description
Update sparse texture tile with raw pixel values.
This function behaves just like [UpdateTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.UpdateTile.html), except the data you pass already needs to be in the final texture format. This is mostly useful for compressed sparse textures, where you'd want to load already precompressed tile data.  
  
Additional resources: [UnloadTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.UnloadTile.html), [UpdateTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.UpdateTile.html).
* * *
