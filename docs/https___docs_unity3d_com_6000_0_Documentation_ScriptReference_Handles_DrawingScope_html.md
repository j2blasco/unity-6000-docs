* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawingScope.html

# DrawingScope
struct in UnityEditor
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
Disposable helper struct for automatically setting and reverting [Handles.color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) and/or [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html).
This struct allows you to temporarily set the value of [Handles.color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) and/or [Handles.matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-matrix.html) inside of a block of code and automatically revert them to their previous values when the scope is exited.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
// a custom editor that draws a labeled circle around the selected MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) in the scene view
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)))]
public class MeshRendererEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    protected virtual void OnSceneGUI()
    {
        MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) meshRenderer = (MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html))target;  
  
        // get an orientation pointing from the selected object to the camera
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) cameraToTarget = Camera.current.transform.position - meshRenderer.transform.position;
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) billboardOrientation = Quaternion.LookRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html)(cameraToTarget, Camera.current.transform.up);  
  
        // set the handle matrix to the target's position, oriented facing the camera
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix = Matrix4x4.TRS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html)(meshRenderer.transform.position, billboardOrientation, Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html));
        using (new Handles.DrawingScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawingScope.html)(Color.magenta[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-magenta.html), matrix))
        {
            // draw a magenta circle around the selected object with a label at the top
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) size = meshRenderer.bounds.size;
            float radius = Mathf.Max[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Max.html)(size.x, size.y, size.z);
            Handles.DrawWireArc[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawWireArc.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html), Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html), 360f, radius);
            Handles.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.Label.html)(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * radius, meshRenderer.name);
        }
    }
}

```

### Properties
Property | Description  
---|---  
[originalColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawingScope-originalColor.html) | The value of Handles.color at the time this DrawingScope was created.  
[originalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawingScope-originalMatrix.html) | The value of Handles.matrix at the time this DrawingScope was created.  
### Constructors
Constructor | Description  
---|---  
[Handles.DrawingScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawingScope-ctor.html) | Create a new DrawingScope and set Handles.color and/or Handles.matrix to the specified values.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawingScope.Dispose.html) | Automatically reverts Handles.color and Handles.matrix to their values prior to entering the scope, when the scope is exited. You do not need to call this method manually.  
* * *
