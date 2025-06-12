* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.Remove.html

#  [OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html).Remove
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
public bool Remove([Overlays.Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) overlay); 
### Parameters
Parameter | Description  
---|---  
overlay | The Overlay to remove.  
### Returns
**bool** Returns true if Overlay was found and removed, false if Overlay was not present in OverlayCanvas. 
### Description
Remove an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) from this canvas. Removed Overlays are disassociated from [OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html) and the related [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html), but not destroyed. This means you are able to move a single [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) between multiple windows.
An [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) may only belong to a single [OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html). To display an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) in multiple windows, you must instantiate an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) for each window.
* * *
