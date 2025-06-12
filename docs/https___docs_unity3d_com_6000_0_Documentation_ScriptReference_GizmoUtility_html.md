* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.html

# GizmoUtility
class in UnityEditor
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
A static class for interacting with the Scene View icons and gizmos for types.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;

// An Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window that lets you edit the gizmo and icon properties for each selected component.
public class GizmoUtilityExample  : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Gizmo Window")]
    static void Init() => GetWindow<GizmoUtilityExample>();

    Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_Scroll;

    void OnEnable()
    {
        autoRepaintOnSceneChange = true;
    }

    void OnGUI()
    {
        GizmoUtility.use3dIcons[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility-use3dIcons.html) = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("3D Icons", GizmoUtility.use3dIcons[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility-use3dIcons.html));

        EditorGUI.BeginDisabled(!GizmoUtility.use3dIcons[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility-use3dIcons.html));
        GizmoUtility.iconSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility-iconSize.html) = EditorGUILayout.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Slider.html)("3D Icon Size", GizmoUtility.iconSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility-iconSize.html), 0f, 1f);
        EditorGUI.EndDisabled();

        m_Scroll = EditorGUILayout.BeginScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginScrollView.html)(m_Scroll);

        foreach (var go in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
        {
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)($"{go.name} Gizmos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html)", EditorStyles.boldLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-boldLabel.html));

            EditorGUI.indentLevel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-indentLevel.html)++;
            foreach (var component in go.GetComponents<Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)>())
            {
                // A component can have gizmos, an icon, both, or neither. A gizmo can also be disabled (the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
                // is collapsed in the Inspector).
                if (GizmoUtility.TryGetGizmoInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.TryGetGizmoInfo.html)(component.GetType(), out GizmoInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoInfo.html) info))
                {
                    EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();

                    if (info.hasGizmo)
                        info.gizmoEnabled = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)($"{info.name} Gizmo", info.gizmoEnabled);

                    if (info.hasIcon)
                        info.iconEnabled = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)($"{info.name} Icon", info.iconEnabled);

                    if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
                        GizmoUtility.ApplyGizmoInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.ApplyGizmoInfo.html)(info);
                }
            }
            EditorGUI.indentLevel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-indentLevel.html)--;
        }

        EditorGUILayout.EndScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndScrollView.html)();
    }
}

```

### Static Properties
Property | Description  
---|---  
[iconSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility-iconSize.html) | Control the size that 3D icons render in the Scene View.  
[use3dIcons](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility-use3dIcons.html) | Determines whether icons in the Scene View are a fixed size (false) or scaled relative to distance from the camera and iconSize.  
### Static Methods
Method | Description  
---|---  
[ApplyGizmoInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.ApplyGizmoInfo.html) | Apply gizmoEnabled and iconEnabled for a GizmoInfo object.  
[GetGizmoInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.GetGizmoInfo.html) | Get GizmoInfo for all components with gizmos or icons in the project.  
[SetGizmoEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.SetGizmoEnabled.html) | Enable or disable gizmo rendering in the Scene View for a component type. Gizmos are the simple lines and guides drawn by component editors. For example, the Camera frustum guidelines are gizmos.  
[SetIconEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.SetIconEnabled.html) | Enable or disable icon rendering for all objects in the Scene View for a component type.  
[TryGetGizmoInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.TryGetGizmoInfo.html) | Get a GizmoInfo for a type if it exists.  
* * *
