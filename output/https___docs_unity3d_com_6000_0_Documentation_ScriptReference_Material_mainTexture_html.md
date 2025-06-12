* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTexture.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).mainTexture
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
[Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) mainTexture; 
### Description
The main texture.
By default, Unity considers a texture with the property name `"_MainTex"` to be the main texture. Use the `[MainTexture]` [ShaderLab Properties attribute](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html) to make Unity consider a texture with a different property name to be the main texture. When the main texture is set using the `[MainTexture]` attribute, it is not visible in the Game view when you use the texture streaming [debugging view mode](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-API#DebuggingAPI.html) or a custom debug tool.  
  
This is the same as calling [Material.GetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTexture.html) or [Material.SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html) with the property name of the main texture as a parameter.  
  
Additional resources: [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html), [GetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTexture.html), [ShaderLab: Properties](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html), [ShaderPropertyFlags.MainTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyFlags.MainTexture.html).
```
// Change main texture each changeInterval/
// seconds from the texture array defined in the inspector.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)[] textures;
    public float changeInterval = 0.33F;
    public Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend;  
  
    void Start()
    {
        rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (textures.Length == 0)
            return;  
  
        int index = Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) / changeInterval);
        index = index % textures.Length;
        rend.material.mainTexture = textures[index];
    }
}

```

* * *
