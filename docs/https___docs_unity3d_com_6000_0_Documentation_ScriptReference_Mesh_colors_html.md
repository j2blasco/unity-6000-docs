* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).colors
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
colors; 
### Description
Vertex colors of the Mesh.
If no vertex colors are available, an empty array will be returned.
```
// Sets the vertex color to be red at the y=0 and green at y=1.
// (Note that most built-in Shaders don't display vertex colors. Use one that does, such as a Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html), to see vertex colors)  
  
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) mesh = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>().mesh;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] vertices = mesh.vertices;  
  
        // create new colors array where the colors will be created.
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] colors = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[vertices.Length];  
  
        for (int i = 0; i < vertices.Length; i++)
            colors[i] = Color.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Lerp.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), vertices[i].y);  
  
        // assign the array of colors to the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).
        mesh.colors = colors;
    }
}

```

For performance reasons, consider using [colors32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-colors32.html) instead. This will avoid byte-to-float conversions in colors, and use less temporary memory.
* * *
