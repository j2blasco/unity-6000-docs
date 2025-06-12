* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-ctor.html

# Material Constructor
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
public Material([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader); 
## Declaration
public Material([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) source); 
### Parameters
Parameter | Description  
---|---  
shader | Create a material with a given [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).  
source | Create a material by copying all properties from another material.  
### Description
Create a temporary Material.
If you have a script which implements a custom special effect, you implement all the graphic setup using shaders & materials. Use this function to create a custom shader & material inside your script. After creating the material, use [SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetColor.html), [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html), [SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetFloat.html), [SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetVector.html), [SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetMatrix.html) to populate the shader property values.  
  
Additional resources: [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html), [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Creates a material from shader and texture references.
    Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader;
    Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) texture;
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color;  
  
    void Start()
    {
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)> ();  
  
        rend.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(shader);
        rend.material.mainTexture = texture;
        rend.material.color = color;
    }
}
```

```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Creates a cube and assigns a material with a builtin Specular shader.
    void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = cube.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)> ();
        rend.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular"));
    }
}
```

* * *
