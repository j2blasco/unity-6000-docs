* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html

#  [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html).Find
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html "Go to Shader Component in the Manual")
## Declaration
public static [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) Find(string name); 
### Description
Finds a shader with the given `name`. Returns `null` if the shader is not found.
Shader.Find can be used to switch to another shader without having to keep a reference to the shader. `name` is the name you can see in the shader popup of any material, for example "Standard", "Unlit/Texture", "Legacy Shaders/Diffuse" etc.  
  
Note that a shader might be not included into the player build if nothing references it. In that case, Shader.Find will work only in the Editor, and will result in the pink [error shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-error.html) in a build. Because of that, it is advisable to use shader references instead of finding them by name. To make sure a shader is included into the game build, do either of: 1) reference it from some of the materials used in your Scene, 2) add it under "Always Included Shaders" list in ProjectSettings/Graphics or 3) put shader or something that references it (e.g. a Material) into a "Resources" folder.  
  
Additional resources: [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) class.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Create a material from code
    void Start()
    {
        // Create a material with transparent diffuse shader
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Transparent/Diffuse"));
        material.color = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);  
  
        // assign the material to the renderer
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material = material;
    }
}

```

* * *
