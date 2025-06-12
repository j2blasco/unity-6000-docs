* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-wireframe.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).wireframe
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
wireframe; 
### Description
Should rendering be done in wireframe?
Turning on wireframe mode will affect all objects rendered after the call, until you turn wireframe back off. In the Unity editor, wireframe mode is always turned off before repainting any window.  
  
Note that some platforms, for example mobile (OpenGL ES) does not support wireframe rendering.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Attach this script to a camera, this will make it render in wireframe
    void OnPreRender()
    {
        GL.wireframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-wireframe.html) = true;
    }  
  
    void OnPostRender()
    {
        GL.wireframe[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-wireframe.html) = false;
    }
}

```

* * *
