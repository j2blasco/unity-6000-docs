* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CustomEditor.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [Shader in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader-object.html)
  * Custom Editor block in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html)
Fallback block in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-object.html)
SubShader in ShaderLab reference
# Custom Editor block in ShaderLab reference
This page contains information on using a `CustomEditor` or `CustomEditorForRenderPipeline` block in your **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) code to assign [custom editors](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-CustomEditors.html).
## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: CustomEditor block** | Yes | Yes | Yes | Yes  
**ShaderLab: CustomEditorForRenderPipeline block** | Yes | Yes | Yes | No  
## Syntax
**Signature** | **Function**  
---|---  
`CustomEditor "[custom editor class name]"` | Unity uses the custom editor defined in the named class, unless this is overridden by a `CustomEditorForRenderPipeline` block.  
`CustomEditorForRenderPipeline "[custom editor class name]" "[render pipeline asset class name]"` | When the active Render Pipeline Asset is the named type, Unity uses the custom editor defined in the named class.  
## Additional resources
  * [Adding material properties to shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-change-properties.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html)
Fallback block in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-object.html)
SubShader in ShaderLab reference
