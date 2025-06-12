* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.PeriodicBadgeUpdate.html

#  [Tile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html).PeriodicBadgeUpdate
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
public void PeriodicBadgeUpdate(string uri, float interval); 
### Parameters
Parameter | Description  
---|---  
uri | A remote location from where to retrieve tile update  
interval | A time interval in minutes, will be rounded to a value, supported by the system  
### Description
Starts periodic update of a badge on a tile. 
A remote uri will be checked periodically to retrieve an update for a badge.
* * *
