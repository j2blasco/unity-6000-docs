* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html

# EditorTool
class in UnityEditor.EditorTools
/
Inherits from:[ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
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
Use this class to implement editor tools. This is the base class from which all editor tools are inherited.
Use this class with [EditorToolAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolAttribute.html) to register custom editor tools with the Editor.  
  
There are two basic types of tools, Global and Component. See [EditorToolAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolAttribute.html) for information on how to designate a tool as Global or Component.  
  
Global tools are like the built-in Move, Rotate, Scale tools. They are always available, and work with whatever is in the current [Selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html).  
  
Component tools, similar to [CustomEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html), are specific to a [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html). These tools are made available when the active selection contains an editable type.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.EditorTools;
using UnityEditor.ShortcutManagement;
using UnityEngine;  
  
// Example MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) that oscillates a transform position between two points.
public class Platform : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Start = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-10, 0f, 0f);  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_End = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(10f, 0f, 0f);  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    float m_Speed = .2f;  
  
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) start
    {
        get => m_Start;
        set => m_Start = value;
    }  
  
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) end
    {
        get => m_End;
        set => m_End = value;
    }  
  
    public float speed
    {
        get => m_Speed;
        set => m_Speed = value;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        SnapToPath(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
    }  
  
    public void SnapToPath(float time)
    {
        transform.position = Vector3.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html)(m_Start, m_End, (Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(time * m_Speed) + 1) * .5f);
    }
}  
  
// The second argument in the EditorToolAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolAttribute.html) flags this as a Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) tool. That means that it will be instantiated
// and destroyed along with the selection. EditorTool.targets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool-targets.html) will contain the selected objects matching the type.
[EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)("Platform Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html)", typeof(Platform))]
class PlatformTool : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html), IDrawSelectedHandles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.IDrawSelectedHandles.html)
{
    // Enable or disable preview animation
    bool m_AnimatePlatforms;  
  
    // Global tools (tools that do not specify a target type in the attribute) are lazy initialized and persisted by
    // a ToolManager[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.html). Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) tools (like this example) are instantiated and destroyed with the current selection.
    void OnEnable()
    {
        // Allocate unmanaged resources or perform one-time set up functions here
    }  
  
    void OnDisable()
    {
        // Free unmanaged resources, state teardown.
    }  
  
    // The second "context" argument accepts an EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) type.
    [Shortcut("Activate Platform Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html)", typeof(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html)), KeyCode.P[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.P.html))]
    static void PlatformToolShortcut()
    {
        if (Selection.GetFiltered[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.GetFiltered.html)<Platform>(SelectionMode.TopLevel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.TopLevel.html)).Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html) > 0)
            ToolManager.SetActiveTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.SetActiveTool.html)<PlatformTool>();
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("No platforms selected!");
    }  
  
    // Called when the active tool is set to this tool instance. Global tools are persisted by the ToolManager[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.html),
    // so usually you would use OnEnable and OnDisable to manage native resources, and OnActivated/OnWillBeDeactivated
    // to set up state. See also `EditorTools.{ activeToolChanged, activeToolChanged }` events.
    public override void OnActivated()
    {
        SceneView.lastActiveSceneView.ShowNotification(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Entering Platform Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html)"), .1f);
    }  
  
    // Called before the active tool is changed, or destroyed. The exception to this rule is if you have manually
    // destroyed this tool (ex, calling `Destroy(this)` will skip the OnWillBeDeactivated invocation).
    public override void OnWillBeDeactivated()
    {
        SceneView.lastActiveSceneView.ShowNotification(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Exiting Platform Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html)"), .1f);
    }  
  
    // Equivalent to Editor.OnSceneGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html).
    public override void OnToolGUI(EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window)
    {
        if (!(window is SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) sceneView))
            return;  
  
        Handles.BeginGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.BeginGUI.html)();
        using (new GUILayout.HorizontalScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalScope.html)())
        {
            using (new GUILayout.VerticalScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.VerticalScope.html)(EditorStyles.helpBox[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-helpBox.html)))
            {
                m_AnimatePlatforms = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("Animate Platforms", m_AnimatePlatforms);
                // To animate platforms we need the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) View to repaint at fixed intervals, so enable `alwaysRefresh`
                // and scene FX (need both for this to work). In older versions of Unity this is called `materialUpdateEnabled`
                sceneView.sceneViewState.alwaysRefresh = m_AnimatePlatforms;
                if (m_AnimatePlatforms && !sceneView.sceneViewState.fxEnabled)
                    sceneView.sceneViewState.fxEnabled = true;  
  
                if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Snap to Path"))
                    foreach (var obj in targets)
                        if (obj is Platform platform)
                            platform.SnapToPath((float)EditorApplication.timeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-timeSinceStartup.html));
            }  
  
            GUILayout.FlexibleSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html)();
        }
        Handles.EndGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.EndGUI.html)();  
  
        foreach (var obj in targets)
        {
            if (!(obj is Platform platform))
                continue;  
  
            if (m_AnimatePlatforms && Event.current.type == EventType.Repaint[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html))
                platform.SnapToPath((float)EditorApplication.timeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-timeSinceStartup.html));  
  
            EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
            var start = Handles.PositionHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html)(platform.start, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
            var end = Handles.PositionHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html)(platform.end, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
            if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
            {
                Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(platform, "Set Platform Destinations");
                platform.start = start;
                platform.end = end;
            }
        }
    }  
  
    // IDrawSelectedHandles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.IDrawSelectedHandles.html) interface allows tools to draw gizmos when the target objects are selected, but the tool
    // has not yet been activated. This allows you to keep MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) free of debug and gizmo code.
    public void OnDrawHandles()
    {
        foreach (var obj in targets)
        {
            if (obj is Platform platform)
                Handles.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html)(platform.start, platform.end, 6f);
        }
    }
}

```

### Properties
Property | Description  
---|---  
[gridSnapEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool-gridSnapEnabled.html) | Use this property to allow the current EditorTool to enable/disable grid snapping.  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool-target.html) | The object being inspected.  
[targets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool-targets.html) | An array of the objects being inspected.  
[toolbarIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool-toolbarIcon.html) | The icon and tooltip for this custom editor tool. If this function is not implemented, the toolbar displays the Inspector icon for the target type. If no target type is defined, the toolbar displays the Tool Mode icon.  
### Public Methods
Method | Description  
---|---  
[IsAvailable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.IsAvailable.html) | Checks whether the custom editor tool is available based on the state of the editor.  
[OnActivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.OnActivated.html) | Invoked after this EditorTool becomes the active tool.  
[OnToolGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.OnToolGUI.html) | Use this method to implement a custom editor tool.  
[OnWillBeDeactivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.OnWillBeDeactivated.html) | Invoked before this EditorTool stops being the active tool.  
[PopulateMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.PopulateMenu.html) | Adds menu items to Scene view context menu.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
* * *
