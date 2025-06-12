* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.RestoreOverlay.html

#  [OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html).RestoreOverlay
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
public void RestoreOverlay([Overlays.Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) overlay, [Overlays.SaveData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.SaveData.html) data); 
### Parameters
Parameter | Description  
---|---  
overlay | The [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) to restore.  
data | The [SaveData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.SaveData.html) that contains the state to restore.  
### Description
Restores [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) state according to the data parameter.
Call this method to set the overlay's position, visibility, dock area, etc. according to the values in data.
* * *
