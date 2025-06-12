* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CopyFrom.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).CopyFrom
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
## Declaration
public void CopyFrom([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) other); 
### Parameters
Parameter | Description  
---|---  
other | Copy camera settings to the other camera.  
### Description
Makes this camera's settings match other camera.
This will copy all camera's variables (field of view, clear flags, culling mask, ...) from the other camera. It will also set this camera's transform to match the other camera, as well as this camera's layer to match the layer of the other camera.  
  
This can be useful if you want one camera to match the other camera's setup, when doing custom rendering effects. For example when using [RenderWithShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RenderWithShader.html).
```
// Two cameras.  One based on the Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) and the other on a new camera that takes over.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        // Set the current camera's settings from the main Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) camera
        cam.CopyFrom(Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html));
    }
}

```

* * *
