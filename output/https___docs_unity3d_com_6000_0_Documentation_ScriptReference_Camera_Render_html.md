* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.Render.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).Render
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
public void Render(); 
### Description
Render the camera manually.
This will render the camera. It will use the camera's clear flags, target texture and all other settings.  
  
The camera will send [OnPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreCull.html), [OnPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreRender.html) and [OnPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPostRender.html) to any scripts attached, and render any eventual image filters.  
  
This is used for taking precise control of render order. To make use of this feature, create a camera and disable it. Then call Render on it.  
  
You are not able to call the Render function from a camera that is currently rendering. If you wish to do this create a copy of the camera, and make it match the original one using [CopyFrom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CopyFrom.html).  
  
Additional resources: [RenderWithShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RenderWithShader.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Take a "screenshot" of a camera's Render Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).
    Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) RTImage(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera)
    {
        // The Render Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) in RenderTexture.active[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) is the one
        // that will be read by ReadPixels.
        var currentRT = RenderTexture.active[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html);
        RenderTexture.active[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) = camera.targetTexture;  
  
        // Render the camera's view.
        camera.Render();  
  
        // Make a new texture and read the active Render Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) into it.
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) image = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(camera.targetTexture.width, camera.targetTexture.height);
        image.ReadPixels(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, camera.targetTexture.width, camera.targetTexture.height), 0, 0);
        image.Apply();  
  
        // Replace the original active Render Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).
        RenderTexture.active[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) = currentRT;
        return image;
    }
}

```

* * *
