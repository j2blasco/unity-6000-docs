* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.UpdateTile.html

#  [SparseTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.html).UpdateTile
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
public void UpdateTile(int tileX, int tileY, int miplevel, Color32[] data); 
### Parameters
Parameter | Description  
---|---  
tileX | Tile X coordinate.  
tileY | Tile Y coordinate.  
miplevel | Mipmap level of the texture.  
data | Tile color data.  
### Description
Update sparse texture tile with color values.
This function makes a tile at (tileX,tileY) coordinates resident in memory, and updates its pixels. If a tile is already resident, then only the pixels are updated.  
  
Data passed should have enough pixels for the tile (tileWidth*tileHeight elements). Exception can be small mipmap levels that are smaller than tile size; then it's ok to pass enough data for the mip level size.  
  
UpdateTile only works for non-compressed color formats. If you use a sparse texture with a compressed format, use [UpdateTileRaw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.UpdateTileRaw.html) and pass raw tile data bytes (e.g. DXT/BCn-compressed data). UpdateTileRaw can also be more efficient if texture format is not RGBA32, as then Unity does not have to convert from Color32 data into the underlying texture format.  
  
Additional resources: [UnloadTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.UnloadTile.html), [UpdateTileRaw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.UpdateTileRaw.html).
* * *
