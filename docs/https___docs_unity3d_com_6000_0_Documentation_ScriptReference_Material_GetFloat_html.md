* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetFloat.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).GetFloat
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
public float GetFloat(string name); 
## Declaration
public float GetFloat(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
name | The name of the property.  
### Description
Get a named float value.
Additional resources: [SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetFloat.html), [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html), [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html), [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)> ();
        rend.material.shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular");
        print(rend.material.GetFloat("_Shininess"));
    }
}
```

* * *
