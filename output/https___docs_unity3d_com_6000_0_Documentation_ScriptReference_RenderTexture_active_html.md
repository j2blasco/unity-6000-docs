* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).active
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html "Go to RenderTexture Component in the Manual")
[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) active; 
### Description
Currently active render texture.
All rendering goes into the active RenderTexture. If the active RenderTexture is `null` everything is rendered in the main window.  
  
Setting [RenderTexture.active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) is the same as calling [Graphics.SetRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRenderTarget.html). Typically you change or query the active render texture when implementing custom graphics effects; if all you need is to make a Camera render into a texture then use [Camera.targetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-targetTexture.html) instead.  
  
When a RenderTexture becomes active its hardware rendering context is automatically created if it hasn't been created already.  
  
Additional resources: [Graphics.SetRenderTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRenderTarget.html), [GraphicsTexture.active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture-active.html).
```
using UnityEngine;
using System.Collections;  
  
// Get the contents of a RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) into a Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    static public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetRTPixels(RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) rt)
    {
        // Remember currently active render texture
        RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) currentActiveRT = RenderTexture.active[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html);  
  
        // Set the supplied RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) as the active one
        RenderTexture.active[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) = rt;  
  
        // Create a new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) and read the RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) image into it
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(rt.width, rt.height);
        tex.ReadPixels(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, tex.width, tex.height), 0, 0);
        tex.Apply();  
  
        // Restore previously active render texture
        RenderTexture.active[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html) = currentActiveRT;
        return tex;
    }
}

```

* * *
