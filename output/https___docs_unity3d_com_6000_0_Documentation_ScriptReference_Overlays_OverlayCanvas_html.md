* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html

# OverlayCanvas
class in UnityEditor.Overlays
Leave feedback
  

Implements interfaces:[ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html)
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
OverlayCanvas is a container for collections of [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)s.
Every [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) has an [OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html), but only windows that opt-in to Overlay support will display Overlays. See [ISupportsOverlays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ISupportsOverlays.html) for more information.
### Properties
Property | Description  
---|---  
[overlays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas-overlays.html) | The Overlays in this canvas.  
[overlaysEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas-overlaysEnabled.html) | Returns true if overlays display in the window, or false if overlays are hidden.  
### Public Methods
Method | Description  
---|---  
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.Add.html) | Add an Overlay to this canvas. Added Overlays will be displayed in the associated EditorWindow until they are removed.  
[OnAfterDeserialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.OnAfterDeserialize.html) | Invoked after OverlayCanvas is deserialized.  
[OnBeforeSerialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.OnBeforeSerialize.html) | Invoked before OverlayCanvas will be serialized. This is used to store Overlay layout data.  
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.Remove.html) | Remove an Overlay from this canvas. Removed Overlays are disassociated from OverlayCanvas and the related EditorWindow, but not destroyed. This means you are able to move a single Overlay between multiple windows.  
[ResetOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.ResetOverlay.html) | Resets the overlay to its default state.  
[RestoreOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.RestoreOverlay.html) | Restores Overlay state according to the data parameter.  
[ShowPopup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.ShowPopup.html) | Displays an overlay as a pop-up in a EditorWindow.  
[ShowPopupAtMouse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.ShowPopupAtMouse.html) | Displays an overlay as a pop-up in a EditorWindow at the mouse position.  
* * *
