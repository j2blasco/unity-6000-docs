* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.OnSceneGUI.html

#  [EditorAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html).OnSceneGUI
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
public void OnSceneGUI([SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) sceneView); 
### Parameters
Parameter | Description  
---|---  
sceneView | The Scene view that `Actions.EditorAction.OnSceneGUI` is called in.  
### Description
Callback raised when the Scene view calls OnGUI.
Use this method to implement any handles or interactive code. This is equivalent in functionality to [EditorTool.OnToolGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.OnToolGUI.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Actions;
using UnityEditor.Overlays;
using UnityEngine;
using UnityEngine.UIElements;

public class EditorActionSampleOverlay : Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)
{
    Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector3Field.html) m_Field;

    public Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)> positionChanged;

    public void SetPosition(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position)
    {
        m_Field?.SetValueWithoutNotify(position);
    }

    public override VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreatePanelContent()
    {
        m_Field = new Vector3Field[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector3Field.html)();
        m_Field.RegisterValueChangedCallback((evt) => positionChanged?.Invoke(evt.newValue));
        return m_Field;
    }
}

public class EditorActionSample : EditorAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Test/Start Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) Sample[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html)")]
    static void StartEditorActionSample()
    {
        Start(new EditorActionSample());
    }

    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) handlePosition = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);

    EditorActionSampleOverlay m_Overlay;

    public EditorActionSample()
    {
        // Create the overlay when the action is created
        m_Overlay = new EditorActionSampleOverlay();
        m_Overlay.SetPosition(handlePosition);
        m_Overlay.positionChanged += (value) => handlePosition = value;
        SceneView.AddOverlayToActiveView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.AddOverlayToActiveView.html)(m_Overlay);
        m_Overlay.displayed = true;
    }

    protected override void OnFinish(EditorActionResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorActionResult.html) result)
    {
        // Remove the overlay when the action is finished
        SceneView.RemoveOverlayFromActiveView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.RemoveOverlayFromActiveView.html)(m_Overlay);

        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) Finished [{result}] with position: {handlePosition}");
    }

    public override void OnSceneGUI(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) sceneView)
    {
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        handlePosition = Handles.PositionHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html)(handlePosition, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));

        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            m_Overlay.SetPosition(handlePosition);
        }
    }
}

```

* * *
