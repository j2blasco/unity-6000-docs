* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.DrawHandle.html

#  [PrimitiveBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.html).DrawHandle
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
public void DrawHandle(); 
### Description
A function to display this instance in the current handle camera using its current configuration.
Always write properties to the handle before calling this function. Place the calls to this function inside [EditorGUI.BeginChangeCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html) and [EditorGUI.EndChangeCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html) to detect user interaction and read the updated properties from the handle.  
  
The following component defines an object with a [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) property.
```
using UnityEngine;  
  
public class BoundsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds { get { return m_Bounds; } set { m_Bounds = value; } }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) m_Bounds = new Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html));
}

```

The following Custom Editor allows the user to edit the bounds property for this component in the Scene view.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.IMGUI.Controls;
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(BoundsExample)), CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class BoundsExampleEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    private BoxBoundsHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.BoxBoundsHandle.html) m_BoundsHandle = new BoxBoundsHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.BoxBoundsHandle.html)();  
  
    // the OnSceneGUI callback uses the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view camera for drawing handles by default
    protected virtual void OnSceneGUI()
    {
        BoundsExample boundsExample = (BoundsExample)target;  
  
        // copy the target object's data to the handle
        m_BoundsHandle.center = boundsExample.bounds.center;
        m_BoundsHandle.size = boundsExample.bounds.size;  
  
        // draw the handle
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        m_BoundsHandle.DrawHandle();
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            // record the target object before setting new values so changes can be undone/redone
            Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(boundsExample, "Change Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)");  
  
            // copy the handle's updated data back to the target object
            Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) newBounds = new Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)();
            newBounds.center = m_BoundsHandle.center;
            newBounds.size = m_BoundsHandle.size;
            boundsExample.bounds = newBounds;
        }
    }
}

```

Additional resources: [Editor.OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html), [Handles.SetCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SetCamera.html).
* * *
