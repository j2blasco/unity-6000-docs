* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.AddOverlayToActiveView.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).AddOverlayToActiveView
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
public static void AddOverlayToActiveView(T overlay); 
### Parameters
Parameter | Description  
---|---  
overlay | The [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) to add.  
### Description
Add an [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) to be displayed in the last focused Scene View. Overlays added to this static list will be automatically moved to the last active Scene View, and are displayed until removed.
See also [SceneView.RemoveOverlayFromActiveView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.RemoveOverlayFromActiveView.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.EditorTools;
using UnityEditor.Overlays;
using UnityEditor.UIElements;
using UnityEngine;
using UnityEngine.UIElements;  
  
// An EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) that shows an Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) in the active scene view while enabled.
[EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)("Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) Example", typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)))]
class ToolWithOverlay : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)
{
    ActiveSceneViewOverlay m_Overlay;  
  
    void OnEnable()
    {
        m_Overlay = new ActiveSceneViewOverlay(targets.Cast<Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)>().ToArray());
        SceneView.AddOverlayToActiveView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.AddOverlayToActiveView.html)(m_Overlay);
    }  
  
    void OnDisable()
    {
        SceneView.RemoveOverlayFromActiveView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.RemoveOverlayFromActiveView.html)(m_Overlay);
    }
}  
  
// A simple Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) that moves a collection of transforms by some translation.
class ActiveSceneViewOverlay : Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)
{
    Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector3Field.html) m_Translation;
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)[] m_Selection;  
  
    public ActiveSceneViewOverlay(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)[] selection)
    {
        m_Selection = selection;
    }  
  
    public override VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreatePanelContent()
    {
        var root = new VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)();
        root.Add(m_Translation = new Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector3Field.html)("Translation"));
        root.Add(new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)(MoveSelectionUp) { text = "Move Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) Up" });
        m_Translation.SetValueWithoutNotify(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
        m_Translation.style.minWidth = 300;
        return root;
    }  
  
    void MoveSelectionUp()
    {
        Undo.RecordObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObjects.html)(m_Selection.ToArray(), "Move Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html)");
        foreach (var transform in m_Selection)
            transform.position += m_Translation.value;
    }
}

```

* * *
