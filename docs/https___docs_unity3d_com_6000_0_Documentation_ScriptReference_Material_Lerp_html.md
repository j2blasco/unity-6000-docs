* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.Lerp.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).Lerp
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
public void Lerp([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) start, [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) end, float t); 
### Description
Interpolate properties between two materials.
Makes all color and float values of a material be interpolated from `start` to `end`, based on `t`.  
When `t` is 0, all values are taken from `start`.  
When `t` is 1, all values are taken from `end`.  
  
Most often you want the materials that are interpolated between to be the same (use the same shaders and textures) except for colors and floats. Then you use `Lerp` to blend between them.  
  
Additional resources: [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Blends between two materials  
  
    Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material1;
    Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material2;
    float duration = 2.0f;
    Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend;  
  
    void Start()
    {
        rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)> ();  
  
        // At start, use the first material
        rend.material = material1;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // ping-pong between the materials over the duration
        float lerp = Mathf.PingPong[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PingPong.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html), duration) / duration;
        rend.material.Lerp(material1, material2, lerp);
    }
}
```

* * *
