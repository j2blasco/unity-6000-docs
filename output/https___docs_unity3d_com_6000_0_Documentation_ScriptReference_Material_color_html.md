* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-color.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).color
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color; 
### Description
The main color of the Material.
By default, Unity considers a color with the property name name `"_Color"` to be the main color. Use the `[MainColor]` [ShaderLab Properties attribute](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html) to make Unity consider a color with a different property name to be the main color.  
  
This is the same as calling [GetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetColor.html) or [SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColor.html) with the property name of the main color as a parameter.  
  
Additional resources: [SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColor.html), [GetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetColor.html), [ShaderLab: Properties](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html), [ShaderPropertyFlags.MainColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyFlags.MainColor.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Fade the color from red to green
    // back and forth over the defined duration  
  
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) colorStart = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) colorEnd = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
    float duration = 1.0f;
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend;  
  
    void Start()
    {
        rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)> ();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float lerp = Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html), duration) / duration;
        rend.material.color = Color.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Lerp.html)(colorStart, colorEnd, lerp);
    }
}
```

* * *
