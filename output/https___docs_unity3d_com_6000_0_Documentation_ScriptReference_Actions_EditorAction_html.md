* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html

# EditorAction
class in UnityEditor.Actions
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
An EditorAction is a temporary tool that can represent either an atomic action or an interactive utility.
When started, an EditorAction temporarily overrides the currently active [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) and remains active until either cancelled or completed. The action can complete itself, or rely on user input to resolve. When the action is finished, the previously active [EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) is re-enabled.  
  
During an `EditorAction`, press **Enter** (macOS: **Return**) to validate the action. To cancel an `EditorAction`, press **Esc**.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Actions;
using UnityEngine;

// Add a menu item to the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) View context menu that creates a cube where-ever the mouse clicks.
public class CreateCube : EditorAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html)
{
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_GameObject;
    int m_UndoStart;

    // Prefixing the menu item path with "CONTEXT" indicates that this is a context menu item. Context menu items are
    // not added to the application menu bar. The second section of the menu path is the name of the type that this
    // menu item is applicable to. The context menu in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) View for example will look for context menu items for
    // each of the following types:
    //    1. The active EditorToolContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html) type.
    //    2. The active EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) type.
    //    3. All component types in the selection. Ex, Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html), MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html), BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html), etc...
    // As an example, to create a context menu item that is shown when context clicking in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) View with a
    // GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) selected that has a MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) component, use "CONTEXT/MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)/My Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)".
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CONTEXT/GameObjectToolContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.GameObjectToolContext.html)/Create Cube")]
    static void Init()
    {
        EditorAction.Start[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.Start.html)<CreateCube>();
    }

    public CreateCube()
    {
        // Show a preview cube at the cursor.
        m_GameObject = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        // If the action is cancelled, we'll clean up the unused resource by calling Undo.PerformUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.PerformUndo.html)().
        Undo.RegisterCreatedObjectUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html)(m_GameObject, "Create Cube");
        // To avoid an unsightly "jump" when the cursor first moves, disable the preview until we have a valid
        // intersection point to place the object.
        m_GameObject.SetActive(false);
        m_UndoStart = Undo.GetCurrentGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.GetCurrentGroup.html)();
    }

    public override void OnSceneGUI(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) view)
    {
        var evt = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
        var id = GUIUtility.GetControlID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetControlID.html)(FocusType.Passive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FocusType.Passive.html));

        if (evt.type == EventType.MouseMove[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseMove.html))
        {
            HandleUtility.AddControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.AddControl.html)(id, 0);
            // Disable preview object so that we don't intersect with object placement ray.
            m_GameObject.SetActive(false);
            var intersected = HandleUtility.PlaceObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PlaceObject.html)(evt.mousePosition, out var position, out var normal);
            m_GameObject.SetActive(true);
            if (intersected)
            {
                Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(m_GameObject, "Create Cube");
                m_GameObject.transform.position = position;
                m_GameObject.transform.rotation = Quaternion.LookRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html)(normal);
            }
        }

        // By checking that no mouse modifiers are active, we can allow for camera movement without breaking the
        // action.
        if (evt.type == EventType.MouseDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html) && evt.modifiers == EventModifiers.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventModifiers.None.html))
        {
            GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) = id;
            evt.Use();
        }

        if (GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) == id && evt.type == EventType.MouseUp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseUp.html))
        {
            evt.Use();
            GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) = 0;
            Finish(EditorActionResult.Success[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorActionResult.Success.html));
        }
    }

    // Since the object we want to instantiate is already in the scene, there is nothing more to do in the OnFinish
    // function if the action exits successfully. If the action is cancelled however, we'll remove the instantiated
    // object from the scene by calling undo.
    protected override void OnFinish(EditorActionResult[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorActionResult.html) result)
    {
        if (result == EditorActionResult.Canceled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorActionResult.Canceled.html))
        {
            Undo.PerformUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.PerformUndo.html)();
            return;
        }

        Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) = m_GameObject;
        // Merge the selection change and GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) creation/placement to a single undo entry.
        Undo.CollapseUndoOperations[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.CollapseUndoOperations.html)(m_UndoStart);
    }
}

```

### Public Methods
Method | Description  
---|---  
[Finish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.Finish.html) | Finishes an EditorAction with a specific result.  
[OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.OnSceneGUI.html) | Callback raised when the Scene view calls OnGUI.  
### Protected Methods
Method | Description  
---|---  
[OnFinish](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.OnFinish.html) | Callback raised when the EditorAction is finished.  
### Static Methods
Method | Description  
---|---  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.Start.html) | Starts an EditorAction that spans over multiple frames.  
* * *
