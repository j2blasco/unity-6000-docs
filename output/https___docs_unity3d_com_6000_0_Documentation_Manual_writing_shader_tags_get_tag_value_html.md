* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-get-tag-value.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Configure when and if Unity uses a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
  * Get tag values in a script


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-disable-dynamic-batching.html)
Disable dynamic batching of a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-require-package-troubleshooting.html)
Troubleshooting package requirement definitions
# Get tag values in a script
## Using SubShader tags with C# code
You can read SubShader tags from a C# script using the [Material.GetTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetTag.html) API, like this:
```
using UnityEngine;

public class Example : MonoBehaviour
{
    // Attach this to a gameObject that has a Renderer component
    string tagName = "ExampleTagName";

    void Start()
    {
        Renderer myRenderer = GetComponent<Renderer>();
        string tagValue = myRenderer.material.GetTag(ExampleTagName, true, "Tag not found");
        Debug.Log(tagValue);
    }
}

```

### Queue tag
You can use [Shader.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-renderQueue.html) to read the Queue tag value of a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object’s active SubShader.
By default, Unity renders geometry in the render queue specified in the [Queue] tag. You can override this value on a per-material basis. In the Unity Editor, you can do this in the [material Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html) by setting the **Render Queue** property. In a C# script, you can do this by setting the value of [Material.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-renderQueue.html) using the [Rendering.RenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.html) enum.
## Using Pass tags with C# code
To access the value of a Pass tag from C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), you can use the [Shader.FindPassTagValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.FindPassTagValue.html) API. This works for Unity’s predefined Pass tags, and for custom Pass tags that you have created.
### Using the LightMode tag with C# scripts
[Material.SetShaderPassEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetShaderPassEnabled.html) and [ShaderTagId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderTagId.html) use the value of the `LightMode` tag to determine how Unity handles a given Pass.
In the Scriptable **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), you can create custom values for the `LightMode` tag. You can then use these custom values to determine which Passes to draw during a given call to [ScriptableRenderContext.DrawRenderers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.DrawRenderers.html), by configuring a [DrawingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings.html) struct. For more information and a code example, see [Creating a simple render loop in a custom Scriptable Render Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/index.html).
## Additional resources
  * [SubShader tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html)
  * [Pass tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-disable-dynamic-batching.html)
Disable dynamic batching of a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-require-package-troubleshooting.html)
Troubleshooting package requirement definitions
