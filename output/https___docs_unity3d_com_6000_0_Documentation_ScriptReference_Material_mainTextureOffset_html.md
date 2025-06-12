* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTextureOffset.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).mainTextureOffset
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) mainTextureOffset; 
### Description
The offset of the main texture.
By default, Unity considers a texture with the property name name `"_MainTex"` to be the main texture. Use the `[MainTexture]` [ShaderLab Properties attribute](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html) to make Unity consider a texture with a different property name to be the main texture.  
  
This is the same as calling [Material.GetTextureOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTextureOffset.html) or [Material.SetTextureOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTextureOffset.html) with the property name of the main texture as a parameter.  
  
Additional resources: [SetTextureOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTextureOffset.html), [GetTextureOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTextureOffset.html), [ShaderLab: Properties](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html), [ShaderPropertyFlags.MainTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyFlags.MainTexture.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Scroll the main texture based on time  
  
    float scrollSpeed = 0.5f;
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend;  
  
    void Start()
    {
        rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)> ();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float offset = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) * scrollSpeed;
        rend.material.mainTextureOffset = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(offset, 0);
    }
}
```

* * *
