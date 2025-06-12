* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-introduction.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Configure when and if Unity uses a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
  * Introduction to shader tags


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
Configure when and if Unity uses a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/add-shader-tag.html)
Add a shader tag to a SubShader or Pass
# Introduction to shader tags
Tags are key-value pairs of data. Unity uses predefined keys and values to determine how and when to use a given SubShader or Pass, or you can also create your own custom SubShader and Pass tags with custom values. You can access SubShader and Pass tags from C# code.
The most commonly used predefined Pass tag is the `LightMode` tag; this is used in all render pipelines. Other Pass tags vary by **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline). For more information, see the following pages:
  * For predefined Pass tags in the Built-in Render Pipeline, see [Predefined Pass tags in the Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html).
  * For predefined Pass tags in the Universal Render Pipeline (URP), see [URP Pass tags](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html#urp-pass-tags-lightmode).


## Additional resources
  * [SubShader tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html)
  * [Pass tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
Configure when and if Unity uses a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/add-shader-tag.html)
Add a shader tag to a SubShader or Pass
