* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html

# Tile
class in UnityEngine.WSA
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Represents tile on Windows start screen 
This class can be used to create or update secondary tiles on start screen and get instances of tiles to send notifications to them.
### Static Properties
Property | Description  
---|---  
[main](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile-main.html) | Returns applications main tile   
### Properties
Property | Description  
---|---  
[exists](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile-exists.html) | Whether secondary tile is pinned to start screen.   
[hasUserConsent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile-hasUserConsent.html) | Whether secondary tile was approved (pinned to start screen) or rejected by user.   
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile-id.html) | A unique string, identifying secondary tile  
### Public Methods
Method | Description  
---|---  
[Delete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.Delete.html) | Show a request to unpin secondary tile from start screen.  
[PeriodicBadgeUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.PeriodicBadgeUpdate.html) | Starts periodic update of a badge on a tile.   
[PeriodicUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.PeriodicUpdate.html) | Starts periodic update of a tile.   
[RemoveBadge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.RemoveBadge.html) | Remove badge from tile.  
[StopPeriodicBadgeUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.StopPeriodicBadgeUpdate.html) | Stops previously started periodic update of a tile.  
[StopPeriodicUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.StopPeriodicUpdate.html) | Stops previously started periodic update of a tile.  
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.Update.html) | Send a notification for tile (update tiles look).  
[UpdateBadgeImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.UpdateBadgeImage.html) | Sets or updates badge on a tile to an image.  
[UpdateBadgeNumber](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.UpdateBadgeNumber.html) | Set or update a badge on a tile to a number.  
### Static Methods
Method | Description  
---|---  
[CreateOrUpdateSecondary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.CreateOrUpdateSecondary.html) | Creates new or updates existing secondary tile.  
[DeleteSecondary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.DeleteSecondary.html) | Show a request to unpin secondary tile from start screen.  
[Exists](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.Exists.html) | Whether secondary tile is pinned to start screen.  
[GetSecondaries](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.GetSecondaries.html) | Gets all secondary tiles.  
[GetSecondary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.GetSecondary.html) | Returns the secondary tile, identified by tile id.  
[GetTemplate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.GetTemplate.html) | Get template XML for tile notification.  
* * *
