* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.CreateOrUpdateSecondary.html

#  [Tile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html).CreateOrUpdateSecondary
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
public static [WSA.Tile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) CreateOrUpdateSecondary([WSA.SecondaryTileData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.SecondaryTileData.html) data); 
## Declaration
public static [WSA.Tile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) CreateOrUpdateSecondary([WSA.SecondaryTileData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.SecondaryTileData.html) data, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pos); 
## Declaration
public static [WSA.Tile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) CreateOrUpdateSecondary([WSA.SecondaryTileData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.SecondaryTileData.html) data, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) area); 
### Parameters
Parameter | Description  
---|---  
data | The data used to create or update secondary tile.  
pos | The coordinates for a request to create new tile.  
area | The area on the screen above which the request to create new tile will be displayed.  
### Returns
**Tile** New Tile object, that can be used for further work with the tile. 
### Description
Creates new or updates existing secondary tile.
TileId is required to be set in data, displayName is required when creating and can not be updated. When used to create new tile, this function displays a request on the screen. Tile will be created if user agrees to pin it to start screen.
* * *
