* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.ShowPopup.html

#  [OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html).ShowPopup
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
public void ShowPopup(); 
## Declaration
public void ShowPopup([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position); 
### Parameters
Parameter | Description  
---|---  
position | The GUI position relative to the window.  
### Description
Displays an overlay as a pop-up in a [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Overlays;
using UnityEditor.ShortcutManagement;
using UnityEngine;
using UnityEngine.UIElements;

class PopUpOnlyOverlay : Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)
{
    public PopUpOnlyOverlay()
    {
        displayName = "Pop Me Up";
    }

    public override VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreatePanelContent()
    {
        return new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)("I'm a pop-up overlay!");
    }

    [Shortcut("PopUpOnlyOverlayExample/Pop Up Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)",typeof(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html)), KeyCode.P[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.P.html), ShortcutModifiers.Shift[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutModifiers.Shift.html))]
    static void ShowOverlay(ShortcutArguments[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutArguments.html) args)
    {
        var window = args.context as EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html);
        if (window is ISupportsOverlays[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ISupportsOverlays.html))
            window.overlayCanvas.ShowPopup<PopUpOnlyOverlay>();
    }
}
.
```

* * *
