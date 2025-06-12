* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnRenderObject.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).OnRenderObject()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
### Description
OnRenderObject is called after camera has rendered the Scene.
This can be used to render your own objects using [Graphics.DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html) or other functions. This function is similar to [OnPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPostRender.html), except OnRenderObject is called on any object that has a script with the function; no matter if it's attached to a Camera or not.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mainMesh;
    Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) miniMapMesh;  
  
    void OnRenderObject()
    {
        // Render different meshes for the object depending on whether
        // the main camera or minimap camera is viewing.
        if (Camera.current.name == "MiniMapcam")
        {
            Graphics.DrawMeshNow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html)(miniMapMesh, transform.position, transform.rotation);
        }
        else
        {
            Graphics.DrawMeshNow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html)(mainMesh, transform.position, transform.rotation);
        }
    }
}

```

* * *
