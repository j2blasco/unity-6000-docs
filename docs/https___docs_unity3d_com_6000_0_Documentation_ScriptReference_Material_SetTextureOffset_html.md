* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTextureOffset.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetTextureOffset
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
## Declaration
public void SetTextureOffset(string name, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) value); 
## Declaration
public void SetTextureOffset(int nameID, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) value); 
### Parameters
Parameter | Description  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | The name of the texture property as defined in the shader. For example: "_MainTex".  
value | Texture placement offset.  
### Description
Sets the placement offset of a given texture. The `name` parameter is defined in the shader. This method creates a new Material instance.
Additional resources: [mainTextureOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTextureOffset.html) property, [GetTextureOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTextureOffset.html), [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Scroll main texture based on time  
  
    float scrollSpeed = 0.5f;
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend;  
  
    void Start()
    {
        rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)> ();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float offset = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) * scrollSpeed;
        rend.material.SetTextureOffset("_TextureName", new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(offset, 0));
    }
}
```

* * *
