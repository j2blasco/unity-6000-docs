* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ISupportsOverlays.html

# ISupportsOverlays
interface in UnityEditor.Overlays
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
Implement this interface to enable overlays in the [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).
When [ISupportsOverlays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ISupportsOverlays.html) is implemented, an Overlay Canvas is automatically added to the [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) tree for your [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html). [OverlayAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayAttribute.html) will now be able to specify this window type as a valid target for registering an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Overlays;
using UnityEngine;
using UnityEngine.UIElements;

class EditorWindowOverlayExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html), ISupportsOverlays[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ISupportsOverlays.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) Supported Window Example")]
    static void Init() => GetWindow<EditorWindowOverlayExample>();

    void OnGUI()
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Here is some text");
        GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Plus some more text, but on the bottom of the screen.");
    }
}

[Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)(typeof(EditorWindowOverlayExample), "Is Mouse Hovering Me?", true)]
class IsMouseHoveringMe : Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)
{
    Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) m_MouseLabel;

    public override VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreatePanelContent()
    {
        m_MouseLabel = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)();
        m_MouseLabel.style.minHeight = 40;
        m_MouseLabel.RegisterCallback<MouseEnterEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseEnterEvent.html)>(evt => m_MouseLabel.text = "Mouse is hovering this Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) content!");
        m_MouseLabel.RegisterCallback<MouseLeaveEvent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseLeaveEvent.html)>(evt => m_MouseLabel.text = "Mouse is not hovering this Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) content.");
        return m_MouseLabel;
    }
}

```

* * *
