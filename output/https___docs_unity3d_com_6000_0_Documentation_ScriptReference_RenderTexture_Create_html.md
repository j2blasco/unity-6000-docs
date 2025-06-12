* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.Create.html

#  [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).Create
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
## Declaration
public bool Create(); 
### Returns
**bool** True if the texture is created, else false. 
### Description
Actually creates the RenderTexture.
RenderTexture constructor does not actually create the hardware texture; by default the texture is created the first time it is set [active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-active.html). Calling `Create` lets you create it up front. `Create` does nothing if the texture is already created.  
  
The initial contents of a newly created render texture are undefined. On some platforms and APIs the contents will default to black, but you shouldn't depend on this. You can use [LoadStoreActionDebugModeSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LoadStoreActionDebugModeSettings.html) to highlight undefined areas of the display, to help you debug rendering problems on mobile platforms.  
  
Additional resources: [Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.Release.html), [IsCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.IsCreated.html) functions.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) rt;  
  
    void  Start()
    {
        rt = new RenderTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html)(256, 256, 16, RenderTextureFormat.ARGB32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html));
        rt.Create();  
  
        // Add code here to work on the render texture  
  
        // Release the hardware resources used by the render texture
        rt.Release();
    }
}

```

* * *
