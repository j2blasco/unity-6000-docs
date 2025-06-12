* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickGameObject.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).PickGameObject
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) PickGameObject([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, out int materialIndex); 
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) PickGameObject([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, GameObject[] ignore, out int materialIndex); 
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) PickGameObject([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, GameObject[] ignore, GameObject[] selection, out int materialIndex); 
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) PickGameObject([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, bool selectPrefabRoot); 
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) PickGameObject([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, bool selectPrefabRoot, GameObject[] ignore); 
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) PickGameObject([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, bool selectPrefabRoot, GameObject[] ignore, GameObject[] filter); 
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) PickGameObject([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, bool selectPrefabRoot, GameObject[] ignore, GameObject[] filter, out int materialIndex); 
### Parameters
Parameter | Description  
---|---  
selectPrefabRoot | Select Prefab.  
materialIndex | Returns index into material array of the Renderer component that is closest to specified position.  
position | A position in screen coordinates. The top-left of the window is (0,0), and the bottom-right is (Screen.width, Screen.height).  
ignore | An array of GameObjects that will not be considered when selecting the nearest GameObject.  
filter | An array of GameObjects to be exclusively considered for selection. If null, all GameObjects in open scenes are eligible for selection.  
selection | An array of GameObjects to be exclusively considered for selection. If null, all GameObjects in open scenes are eligible for selection.  
### Returns
**GameObject** The GameObject that is under the requested position. 
### Description
Pick game object closest to specified position.
HandleUtility.PickGameObject must not be called during a repaint. In most cases it is appropriate to call during [EventType.MouseDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html) or [EventType.MouseUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseUp.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
static class ShowHovered
{
    static GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_LastHoveredObject, m_LastClickedObject;  
  
    [InitializeOnLoadMethod]
    static void Init()
    {
        SceneView.duringSceneGui[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-duringSceneGui.html) += OnSceneGUI;
    }  
  
    static void OnSceneGUI(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) view)
    {
        var evt = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);  
  
        // Register a control so that if no other handle is engaged, we can use the event.
        var pickingControlId = GUIUtility.GetControlID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetControlID.html)(FocusType.Passive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.Passive.html));
        HandleUtility.AddDefaultControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.AddDefaultControl.html)(pickingControlId);  
  
        switch (evt.type)
        {
            case EventType.MouseMove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseMove.html):
            {
                var picked = HandleUtility.PickGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickGameObject.html)(evt.mousePosition, false);  
  
                if (picked != m_LastHoveredObject)
                {
                    m_LastHoveredObject = picked;
                    SceneView.RepaintAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.RepaintAll.html)();
                }  
  
                break;
            }  
  
            case EventType.MouseDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html):
            {
                // Make sure to check Tools.viewToolActive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools-viewToolActive.html) before consuming a mouse event, otherwise Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) navigation
                // controls will not work.
                if (!Tools.viewToolActive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools-viewToolActive.html) && HandleUtility.nearestControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-nearestControl.html) == pickingControlId)
                {
                    GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) = pickingControlId;
                    evt.Use();
                }  
  
                break;
            }  
  
            case EventType.MouseUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseUp.html):
            {
                // If the hotControl is not pickingControlId, that means another control has the rights to this event.
                if (GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) != pickingControlId)
                    return;  
  
                var picked = HandleUtility.PickGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickGameObject.html)(evt.mousePosition, false);  
  
                if (picked != m_LastClickedObject)
                {
                    m_LastClickedObject = picked;
                    SceneView.RepaintAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.RepaintAll.html)();
                }  
  
                // Make sure to Use() and reset the hotControl the event if we are the active control ID.
                evt.Use();
                GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) = 0;
                break;
            }
        }  
  
        Handles.BeginGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.BeginGUI.html)();
        GUILayout.BeginVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginVertical.html)(EditorStyles.helpBox[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-helpBox.html), GUILayout.ExpandWidth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html)(false));
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)($"Last Hovered Object: {m_LastHoveredObject}");
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)($"Last Clicked Object: {m_LastClickedObject}");
        GUILayout.EndVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndVertical.html)();
        Handles.EndGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.EndGUI.html)();
    }
}

```

* * *
