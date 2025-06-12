* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.html

# DockZone
enumeration
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
DockZone describes the area of the screen that an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) is displayed in.
Use [DockZone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.html) in an [OverlayAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayAttribute.html) to set the default location for an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Overlays;
using UnityEngine;
using UnityEngine.UIElements;  
  
// Use OverlayAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayAttribute.html) to specify that in new Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Views, when this Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) is first opened it will be in the
// top toolbar, aligned to the left side.
[Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)(typeof(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html)), "Docked Top Toolbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toolbar.html), Left Aligned", defaultDockZone = DockZone.TopToolbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.TopToolbar.html), defaultDockPosition = DockPosition.Top[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockPosition.Top.html))]
class MyOverlay : Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)
{
    public override VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreatePanelContent() => new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)("Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) Contents");
}

```

### Properties
Property | Description  
---|---  
[LeftToolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.LeftToolbar.html) | Overlays are displayed in the left toolbar.  
[RightToolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.RightToolbar.html) | Overlays are displayed in the right toolbar.  
[TopToolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.TopToolbar.html) | Overlays are displayed in the top toolbar.  
[BottomToolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.BottomToolbar.html) | Overlays are displayed in the bottom toolbar.  
[LeftColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.LeftColumn.html) | Overlays are displayed in the left column.  
[RightColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.RightColumn.html) | Overlays are displayed in the right column.  
[Floating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.Floating.html) | Overlays are not bound to a toolbar or column.  
* * *
