* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.TryGetOverlay.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).TryGetOverlay
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
public bool TryGetOverlay(string id, out [Overlays.Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) match); 
### Parameters
Parameter | Description  
---|---  
id | ID of the overlay to retrieve.  
match | Contains the overlay with matching id, or null if no matching overlay was found.  
### Returns
**bool** Returns true if the overlay was found, false otherwise. 
### Description
Get an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) with matching ID from an EditorWindow canvas.
* * *
