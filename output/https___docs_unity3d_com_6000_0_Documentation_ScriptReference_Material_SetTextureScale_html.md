* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTextureScale.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetTextureScale
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
public void SetTextureScale(string name, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) value); 
## Declaration
public void SetTextureScale(int nameID, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) value); 
### Parameters
Parameter | Description  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
name | Property name, e.g. "_MainTex".  
value | Texture placement scale.  
### Description
Sets the placement scale of texture `propertyName`.
Additional resources: [mainTextureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-mainTextureScale.html) property, [GetTextureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTextureScale.html), [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html).
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
        // Animates main texture scale in a funky way!
        float scaleX = Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)) * 0.5f + 1;
        float scaleY = Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html)) * 0.5f + 1;
        rend.material.SetTextureScale("_MainTex", new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(scaleX, scaleY));
    }
}
```

* * *
