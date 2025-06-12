* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html

# EditorToolContext
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
Use this class to implement specialized versions of the built-in transform tools. Built-in transform tools include Move, Rotate, Scale, Rect, and Transform.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.EditorTools;
using UnityEngine;
// EditorToolContextAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContextAttribute.html) is what registers a context with the UI.
[EditorToolContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html)("Wobbly Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html)")]
// The icon path can also be used with packages. Ex "Packages/com.wobblestudio.wobblytools/Icons/Transform.png".
[Icon("Assets/Examples/Icons/TransformIcon.png")]
public class WobbleContext : EditorToolContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html)
{
    // Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) contexts can also implement an OnToolGUI function that is invoked before tools. This is a good place to
    // add any custom selection logic, for example.
    public override void OnToolGUI(EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) _) { }
    protected override Type GetEditorToolType(Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) tool)
    {
        switch (tool)
        {
            // Return the type of tool to be used for Tool.Move[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.Move.html). The Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) Manager will handle instantiating and
            // activating the tool.
            case Tool.Move[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.Move.html):
                return typeof(WobblyMoveTool);
            // For any tools that are not implemented, return null to disable the tool in the menu.
            default:
                return null;
        }
    }
}
// Note that tools used by an EditorToolContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html) do not need to use EditorToolAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolAttribute.html).
class WobblyMoveTool : EditorTool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)
{
    struct Selected
    {
        public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform;
        public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) localScale;
    }
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Origin;
    List<Selected> m_Selected = new List<Selected>();
    void StartMove(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) origin)
    {
        m_Origin = origin;
        m_Selected.Clear();
        foreach(var trs in Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html))
            m_Selected.Add(new Selected() { transform = trs, localScale = trs.localScale });
        Undo.RecordObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObjects.html)(Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html), "Wobble Move Tool[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html)");
    }
    // This is silly example that oscillates the scale of the selected objects as they are moved.
    public override void OnToolGUI(EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) _)
    {
        var evt = Event.current.type;
        var hot = GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html);
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        var p = Handles.PositionHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html)(Tools.handlePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools-handlePosition.html), Tools.handleRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools-handleRotation.html));
        if (evt == EventType.MouseDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.MouseDown.html) && hot != GUIUtility.hotControl[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html))
            StartMove(p);
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            foreach (var selected in m_Selected)
            {
                selected.transform.position += (p - Tools.handlePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools-handlePosition.html));
                var scale = Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html) * (Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(Mathf.Abs[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Abs.html)(Vector3.Distance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html)(m_Origin, p))) * .5f);
                selected.transform.localScale = selected.localScale + scale;
            }
        }
    }
}

```

### Properties
Property | Description  
---|---  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext-target.html) | The object being inspected.  
[targets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext-targets.html) | An array of the objects being inspected.  
### Public Methods
Method | Description  
---|---  
[GetAdditionalToolTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.GetAdditionalToolTypes.html) | Get an additional collection of tools to display in the same category as the built-in transform tools.  
[OnActivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.OnActivated.html) | Invoked after this EditorToolContext becomes the active tool context.  
[OnToolGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.OnToolGUI.html) | Implements any common functionality for the set of manipulation tools available for this context.  
[OnWillBeDeactivated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.OnWillBeDeactivated.html) | Invoked before this EditorToolContext stops being the active tool context.  
[PopulateMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.PopulateMenu.html) | Adds menu items to the Scene view context menu.  
[ResolveTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.ResolveTool.html) | Returns the matching EditorTool type for the specified Tool given the context.  
### Protected Methods
Method | Description  
---|---  
[GetEditorToolType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.GetEditorToolType.html) | Defines the EditorTool type for a given Tool.  
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
