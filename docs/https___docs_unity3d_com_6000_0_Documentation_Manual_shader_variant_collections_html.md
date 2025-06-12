* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-collections.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Fixing hitches or stalls](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reduce-stalling.html)
  * Create a shader variant collection


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-prewarm.html)
Prewarm shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html)
Asynchronous shader compilation in the Editor
# Create a shader variant collection
A **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) variant collection is effectively a list of [shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadervariant). Use shader variant collections to [prewarm shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html), or to ensure that shader variants that are required at runtime but not referenced in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) are not excluded (“stripped”) from your build.
## Create a shader variant collection asset
You can create a shader variant collection asset in the following ways:
  * In the Create Asset menu, choose **Shader** > **Shader Variant Collection**.
  * The Unity Editor can track which shader variants your application uses when it runs, and automatically create a shader variant collection asset that contains them. For more information, see [Graphics Settings: Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#shader-loading).


## View and edit a shader variant collection
![Shader variant collection inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ShaderVariantCollection.png) Shader variant collection inspector
When you select a shader variant collection asset in your project, you can view and edit it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
Use the controls to build a list of [Pass types](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.html) and [shader keyword](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html) combinations to load in advance.
You can also configure a shader variant collection asset using the [ShaderVariantCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.html) API.
## Prewarm a shader variant collection
To avoid visible stalls at performance-intensive times, Unity can ask the graphics driver to create GPU representations of shader variants before they are first needed. This is called **prewarming**. For more information on prewarming the shader variants in a shader variant collection, see [Shader loading: Prewarming shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-prewarm.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-prewarm.html)
Prewarm shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html)
Asynchronous shader compilation in the Editor
