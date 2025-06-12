* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.Add.html

#  [OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html).Add(Overlay,bool)
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
### Parameters
Parameter | Description  
---|---  
overlay | The Overlay to add.  
show | True to display the Overlay immediately, false to add without displaying.  
### Description
Add an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) to this canvas. Added Overlays will be displayed in the associated [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) until they are removed.
In most cases, Overlays are instantiated automatically using [OverlayAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayAttribute.html). However, it is also possible to add and remove Overlays from an [OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html) directly. This is useful for short-lived Overlays that require some context. E.g., as an extension of an Editor.  
  
Overlays added using this method must implement [ITransientOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ITransientOverlay.html). An [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) may only belong to a single [OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html). To display an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) in multiple windows, you must instantiate an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) for each window.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEditor.Overlays;
using UnityEngine.UIElements;  
  
// Attach this MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to view the example Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) in the last active Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) View
class OverlayCanvasExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {}  
  
// An Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) for our OverlayCanvasExample MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html). This will show and hide the example Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) when a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
// with the OverlayCanvasExample component is selected and deselected.
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(OverlayCanvasExample))]
class OverlayCanvasExampleEditor : UnityEditor.Editor
{
    ExampleEditorOverlay m_Overlay;  
  
    void OnEnable()
    {
        // Create a new Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) with a label indicating the selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) name.
        m_Overlay = new ExampleEditorOverlay(name);
        SceneView.lastActiveSceneView.overlayCanvas.Add(m_Overlay);
    }  
  
    void OnDisable()
    {
        // If the Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) has not already been closed, close it when this editor is disabled. Added Overlays will
        // persist until they are closed.
        m_Overlay?.Close();
    }
}  
  
class ExampleEditorOverlay : Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html), ITransientOverlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ITransientOverlay.html)
{
    // Overlays added directly to the canvas must implement ITransientOverlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ITransientOverlay.html), meaning they control their own lifecycle.
    public bool visible => true;  
  
    string m_Message;  
  
    public ExampleEditorOverlay(string message)
    {
        m_Message = message;
    }  
  
    public override VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreatePanelContent()
    {
        var root = new VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)();
        root.Add(new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)(m_Message));
        root.Add(new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)(Close) { text = "Close" });
        return root;
    }
}

```

* * *
