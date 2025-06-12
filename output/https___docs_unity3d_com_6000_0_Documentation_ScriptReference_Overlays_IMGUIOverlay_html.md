* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.IMGUIOverlay.html

# IMGUIOverlay
class in UnityEditor.Overlays
/
Inherits from:[Overlays.Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)
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
IMGUIOverlay is an implementation of [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) that provides a [IMGUIContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMGUIContainer.html).
Inherit IMGUIOverlay to author [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) elements implemented using the legacy IMGUI controls.
### Public Methods
Method | Description  
---|---  
[CreatePanelContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.IMGUIOverlay.CreatePanelContent.html) | CreatePanelContent is invoked by the OverlayCanvas when this Overlay is shown.  
[OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.IMGUIOverlay.OnGUI.html) | Implement IMGUI controls and logic in this method.  
### Inherited Members
### Static Properties
Property | Description  
---|---  
[ussClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-ussClassName.html) | USS class name of elements of this type.  
### Properties
Property | Description  
---|---  
[collapsed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-collapsed.html) | Defines whether the overlay is in collapsed form.  
[collapsedIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-collapsedIcon.html) | Defines a custom icon to use when that overlay is in collapsed form.  
[containerWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-containerWindow.html) | EditorWindow the overlay is contained within.  
[defaultSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-defaultSize.html) | Set defaultSize to define the size of an Overlay when it hasn't been resized by the user.  
[displayed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-displayed.html) | Shows or hides the overlay.  
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-displayName.html) | Name of overlay used as title.  
[floating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-floating.html) | Returns true if overlay is floating, returns false if overlay is docked in a corner or in a toolbar.  
[floatingPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-floatingPosition.html) | Local position of closest overlay corner to closest dockposition when floating.  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-id.html) | Overlay unique ID.  
[isInToolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-isInToolbar.html) | Returns true if overlay is docked in a toolbar.  
[layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-layout.html) | The preferred layout for the Overlay.  
[maxSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-maxSize.html) | Maximum size of the Overlay.  
[minSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-minSize.html) | Minimum size of the Overlay.  
[rootVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-rootVisualElement.html) | The root VisualElement.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-size.html) | Size of the Overlay.  
### Public Methods
Method | Description  
---|---  
[Close](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.Close.html) | Remove the Overlay from its OverlayCanvas.  
[CreateContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.CreateContent.html) | Creates a new VisualElement containing the contents of this Overlay.  
[OnCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.OnCreated.html) | OnCreated is invoked when an Overlay is instantiated in an Overlay Canvas.  
[OnWillBeDestroyed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.OnWillBeDestroyed.html) | Called when an Overlay is about to be destroyed.  
[RefreshPopup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.RefreshPopup.html) | Resize the OverlayPopup to fit the content.  
[Undock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.Undock.html) | If this Overlay is currently in a toolbar, it will be removed and return to a floating state.  
### Events
Event | Description  
---|---  
[collapsedChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-collapsedChanged.html) | Invoked when Overlay.collapsed value is changed.  
[displayedChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-displayedChanged.html) | This callback is invoked when the Overlay.displayed value has been changed.  
[floatingChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-floatingChanged.html) | Called when the value of floating has changed.  
[floatingPositionChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-floatingPositionChanged.html) | This event is invoked when Overlay.floatingPosition is changed.  
[layoutChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-layoutChanged.html) | Subscribe to this event to be notified when the Overlay.Layout property is modified.  
* * *
