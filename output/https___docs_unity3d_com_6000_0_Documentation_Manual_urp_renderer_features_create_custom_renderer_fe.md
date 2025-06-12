* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/inject-a-render-pass.html)
  * [Injecting a render pass via a Scriptable Renderer Feature in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html)
  * Example of a complete Scriptable Renderer Feature in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)
Apply a Scriptable Renderer Feature to a specific camera type in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
Scriptable Renderer Feature API reference for URP
# Example of a complete Scriptable Renderer Feature in URP
This section describes how to create a complete [Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/intro-to-scriptable-renderer-features.html) for a URP renderer.
This walkthrough contains the following sections:
  * [Overview of this example implementation](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#example-implementation-overview)
  * [Create example Scene and GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#example-scene)
  * [Create a scriptable Renderer Feature and add it to the Universal Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#scriptable-renderer-feature)
    * [Add the Renderer Feature to the Universal Renderer asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#add-renderer-feature-to-asset)
  * [Create the scriptable Render Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#scriptable-render-pass)
  * [Implement the settings for the custom render pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#implement-the-settings-for-the-custom-render-pass)
  * [Implement the render passes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#implement-the-render-passes)
  * [Enqueue the render pass in the custom renderer feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#enqueue-the-render-pass-in-the-custom-renderer-feature)
  * [Implement the volume component](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#volume-component)
  * [All complete code for the scripts in this example](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#all-complete-code-for-the-scripts-in-this-example)
    * [Custom renderer feature code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#code-renderer-feature)
    * [Custom render pass code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#code-render-pass)
    * [Volume Component code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#code-volume-component)
  * [The custom shader for the blur effect](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#example-shader)


##  Overview of this example implementation
The example workflow on this page implements a custom renderer feature that uses [custom Render Passes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html) to add a blur effect to the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) output.
The implementation consists of the following parts:
  * A `ScriptableRendererFeature` instance that enqueues a `ScriptableRenderPass` instance every frame.
  * A `ScriptableRenderPass` instance that performs the following steps:
    * Creates a temporary **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) using the `RenderTextureDescriptor` API.
    * Applies two passes of the [custom shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#example-shader) to the camera output using the `TextureHandle` and the [AddBlitPass](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.RenderGraphModule.Util.RenderGraphUtils.html#UnityEngine_Rendering_RenderGraphModule_Util_RenderGraphUtils_AddBlitPass_UnityEngine_Rendering_RenderGraphModule_RenderGraph_UnityEngine_Rendering_RenderGraphModule_Util_RenderGraphUtils_BlitMaterialParameters_System_String_) API.


##  Create example Scene and GameObjects
To set your project up for this example workflow:
  1. Create a new **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  2. Create two GameObjects: a Cube **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) called `Cube`, and a Sphere GameObject called `Sphere`.
  3. Create two Materials with a shader that lets you specify the base color (for example, the `Universal Render Pipeline/Lit` shader). Call the Materials `Blue` and `Red`, and set the base colors of the Materials to blue and red respectively.
  4. Assign the `Red` Material to the cube and the `Blue` Material to the sphere.
  5. Position the camera so that it has the cube and the sphere in its view.
  6. In the URP Asset, set the property **Quality** > **Anti Aliasing (MSAA)** to **Disabled**. The purpose of this step is to simplify the example implementation.


The sample scene looks like the following image:
![Sample scene](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/customizing-urp/custom-renderer-feature/sample-scene.png) Sample scene
##  Create a scriptable Renderer Feature and add it to the Universal Renderer
  1. Create a new C# script and name it `BlurRendererFeature.cs`.
  2. In the script, remove the code that Unity inserted in the `BlurRendererFeature` class.
  3. Add the following `using` directive:
```
using UnityEngine.Rendering.Universal;

```

  4. Create the `BlurRendererFeature` class that inherits from the **ScriptableRendererFeature** class.
```
public class BlurRendererFeature : ScriptableRendererFeature    

```

  5. In the `BlurRendererFeature` class, implement the following methods:
     * `Create`: Unity calls this method on the following events:
       * When the Renderer Feature loads the first time.
       * When you enable or disable the Renderer Feature.
       * When you change a property in the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) of the Renderer Feature.
     * `AddRenderPasses`: Unity calls this method every frame, once for each camera. This method lets you inject `ScriptableRenderPass` instances into the scriptable Renderer.


Now you have the custom `BlurRendererFeature` Renderer Feature with its main methods.
Here’s the complete code for this step:
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Rendering.Universal;

public class BlurRendererFeature : ScriptableRendererFeature
{
    public override void Create()
    {

    }

    public override void AddRenderPasses(ScriptableRenderer renderer,
        ref RenderingData renderingData)
    {

    }
}

```

###  Add the Renderer Feature to the Universal Renderer asset
Add the Renderer Feature you created to the Universal Renderer asset. For information on how to do this, refer to the page [How to add a Renderer Feature to a Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html).
##  Create the scriptable Render Pass
This section demonstrates how to create a scriptable Render Pass and enqueue its instance into the scriptable Renderer.
  1. Create a new C# script and name it `BlurRenderPass.cs`.
  2. In the script, remove the code that Unity inserted in the `BlurRenderPass` class. Add the following `using` directive:
```
using UnityEngine.Rendering;
using UnityEngine.Rendering.RenderGraphModule;
using UnityEngine.Rendering.RenderGraphModule.Util;
using UnityEngine.Rendering.Universal;

```

  3. Create the `BlurRenderPass` class that inherits from the **ScriptableRenderPass** class.
```
public class BlurRenderPass : ScriptableRenderPass

```

  4. Add the `RecordRenderGraph` method to the class. This method adds and configures render passes in the render graph. This process includes declaring render pass inputs and outputs, but doesn’t include adding commands to command buffers. Unity calls this method every frame, once for each camera.
```
public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameData)
{ }

```



Here’s the complete code for the `BlurRenderPass.cs` file from this section:
```
using UnityEngine.Rendering;
using UnityEngine.Rendering.RenderGraphModule;
using UnityEngine.Rendering.RenderGraphModule.Util;
using UnityEngine.Rendering.Universal;

public class BlurRenderPass : ScriptableRenderPass
{
    public override void RecordRenderGraph(RenderGraph renderGraph,
    ContextContainer frameData)
    {
        
    }
}

```

## Implement the settings for the custom render pass
This section demonstrates how to implement the settings for the custom blur render pass.
  1. The Renderer Feature in this example uses the [shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#example-shader)A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that performs the blur horizontally in one pass, and vertically in another pass. To let users control the blur value for each pass, add the following `BlurSettings` class to the `BlurRendererFeature.cs` script.
```
[Serializable]
public class BlurSettings
{
    [Range(0,0.4f)] public float horizontalBlur;
    [Range(0,0.4f)] public float verticalBlur;
}

```

  2. In the `BlurRendererFeature` class, declare the following fields:
```
[SerializeField] private BlurSettings settings;
[SerializeField] private Shader shader;
private Material material;
private BlurRenderPass blurRenderPass;

```

  3. In the `BlurRenderPass` class, add the fields for the settings, the Material, and the constructor that uses those fields. Add the `TextureDesc` field as well. The `TextureDesc` class lets you specify the properties of a render texture, such as the width, height, and format.
```
private BlurSettings defaultSettings;
private Material material;

private RenderTextureDescriptor blurTextureDescriptor;

public BlurRenderPass(Material material, BlurSettings defaultSettings)
{
    this.material = material;
    this.defaultSettings = defaultSettings;
}

```

  4. In the `RecordRenderGraph` method, create the variable for storing the `UniversalResourceData` instance from the `frameData` parameter. `UniversalResourceData` contains all the texture references used by URP, including the active color and depth textures of the camera.
```
UniversalResourceData resourceData = frameData.Get<UniversalResourceData>();

```

  5. Declare the variables for interacting with the shader properties.
```
private static readonly int horizontalBlurId = Shader.PropertyToID("_HorizontalBlur");
private static readonly int verticalBlurId = Shader.PropertyToID("_VerticalBlur");
private const string k_BlurTextureName = "_BlurTexture";
private const string k_VerticalPassName = "VerticalBlurRenderPass";
private const string k_HorizontalPassName = "HorizontalBlurRenderPass";

```

  6. In the `RecordRenderGraph` method, declare the `TextureHandle` fields to store the references to the input and the output textures. Initialize the `TextureDesc` of the destination texture.
The destination texture is based on the camera color texture, so you can use the descriptor of the camera color texture as a starting point to define the destination texture. Using the same descriptor as the camera color texture ensures the source and destination textures will have the same size and color format (unless you choose to change the descriptor).
```
TextureHandle srcCamColor = resourceData.activeColorTexture;
blurTextureDescriptor = srcCamColor.GetDescriptor(renderGraph);
blurTextureDescriptor.name = k_BlurTextureName;
blurTextureDescriptor.depthBufferBits = 0;
var dst = renderGraph.CreateTexture(blurTextureDescriptor);

```

  7. In the `BlurRenderPass` class, implement the `UpdateBlurSettings` method that updates the shader values.
```
private void UpdateBlurSettings()
{
    if (material == null) return;

    material.SetFloat(horizontalBlurId, defaultSettings.horizontalBlur);
    material.SetFloat(verticalBlurId, defaultSettings.verticalBlur);
}

```

  8. In the `RecordRenderGraph` method, add the variable for storing the `UniversalCameraData` data, and make sure the pass doesn’t **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit) from the back buffer.
```
UniversalCameraData cameraData = frameData.Get<UniversalCameraData>();

// The following line ensures that the render pass doesn't blit
// from the back buffer.
if (resourceData.isActiveTargetBackBuffer)
    return;

```

  9. In the `RecordRenderGraph` method, add the function to continuously update the blur settings in the material.
```
// Update the blur settings in the material
UpdateBlurSettings();

// This check is to avoid an error from the material preview in the scene
if (!srcCamColor.IsValid() || !dst.IsValid())
    return;

```



## Implement the render passes
In the `RecordRenderGraph` method, using the `AddBlitPass` method, add the vertical and the horizontal blur render passes.
```
// The AddBlitPass method adds a vertical blur render graph pass that blits from the source texture (camera color in this case) to the destination texture using the first shader pass (the shader pass is defined in the last parameter).
RenderGraphUtils.BlitMaterialParameters paraVertical = new(srcCamColor, dst, material, 0);
renderGraph.AddBlitPass(paraVertical, k_VerticalPassName);

// The AddBlitPass method adds a horizontal blur render graph pass that blits from the texture written by the vertical blur pass to the camera color texture. The method uses the second shader pass.
RenderGraphUtils.BlitMaterialParameters paraHorizontal = new(dst, srcCamColor, material, 1);
renderGraph.AddBlitPass(paraHorizontal, k_HorizontalPassName);

```

The complete code for this part is in [Custom render pass code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#code-render-pass).
## Enqueue the render pass in the custom renderer feature
In this section, you instantiate the render pass in the `Create` method of the `BlurRendererFeature` class, and enqueue it in the `AddRenderPasses` method.
  1. In the `Create` method of the `BlurRendererFeature` class, instantiate the `BlurRenderPass` class.
In the method, use the `renderPassEvent` field to specify when to execute the render pass.
```
public override void Create()
{
    if (shader == null)
    {
        return;
    }
    material = new Material(shader);
    blurRenderPass = new BlurRenderPass(material, settings);

    blurRenderPass.renderPassEvent = RenderPassEvent.AfterRenderingSkybox;
}

```

  2. In the `AddRenderPasses` method of the `BlurRendererFeature` class, enqueue the render pass with the `EnqueuePass` method.
```
public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
{
    if (blurRenderPass == null)
    { 
        return;
    }                
    if (renderingData.cameraData.cameraType == CameraType.Game)
    {
        renderer.EnqueuePass(blurRenderPass);
    }
}

```

  3. Implement the `Dispose` method that destroys the material instance that the Renderer Feature creates.
```
protected override void Dispose(bool disposing)
{
    if (Application.isPlaying)
    {
        Destroy(material);
    }
    else
    {
        DestroyImmediate(material);
    }
}

```



For the complete Renderer Feature code, refer to [Custom renderer feature code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html#code-renderer-feature).
The Scriptable Renderer Feature is now complete. The following image shows the effect of the feature in the Game view and the example settings.
![The effect of the Scriptable Renderer Feature in the Game view](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/customizing-urp/custom-renderer-feature/final-effect.png)  
_The effect of the Scriptable Renderer Feature in the Game view._
##  Implement the volume component
This section shows how to implement a volume component that lets you control the input values for the custom renderer feature.
  1. Create a new C# script and name it `CustomVolumeComponent.cs`.
  2. Inherit the `CustomVolumeComponent` class from the `VolumeComponent` class, add the `[Serializable]` attribute to the class.
Add the `using UnityEngine.Rendering;` directive.
```
using System;
using UnityEngine.Rendering;

[Serializable]
public class CustomVolumeComponent : VolumeComponent
{

}

```

  3. Add the fields to control the blur settings defined in the custom renderer feature.
```
[Serializable]
public class CustomVolumeComponent : VolumeComponent
{
    public ClampedFloatParameter horizontalBlur =
        new ClampedFloatParameter(0.05f, 0, 0.5f);
    public ClampedFloatParameter verticalBlur =
        new ClampedFloatParameter(0.05f, 0, 0.5f);
}

```

  4. In the `BlurRenderPass` script, change the `UpdateBlurSettings` method so that it uses the settings defined in a Volume or the default settings if no Volume is set.
```
private void UpdateBlurSettings()
{
    if (material == null) return;

    // Use the Volume settings or the default settings if no Volume is set.
    var volumeComponent =
        VolumeManager.instance.stack.GetComponent<CustomVolumeComponent>();
    float horizontalBlur = volumeComponent.horizontalBlur.overrideState ?
        volumeComponent.horizontalBlur.value : defaultSettings.horizontalBlur;
    float verticalBlur = volumeComponent.verticalBlur.overrideState ?
        volumeComponent.verticalBlur.value : defaultSettings.verticalBlur;
    material.SetFloat(horizontalBlurId, horizontalBlur);
    material.SetFloat(verticalBlurId, verticalBlur);
}

```

  5. In the Unity scene, create a [local Box Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volumes.html). If a [Volume Profile](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html) is missing, create a new one by clicking **New** next to the **Profile** property. Add the `Custom Volume Component` [override](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/VolumeOverrides.html) to the Volume.
  6. Enable the settings in the `Custom Volume Component` override and set the values for this Volume. Move the Volume so that the camera is inside it. The settings from the Volume override the default settings from the custom renderer feature.


## All complete code for the scripts in this example
This section contains the complete code for all the **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) in this example.
###  Custom renderer feature code
Here’s the complete code for the custom renderer feature script:
```
using System;
using UnityEditor;
using UnityEngine;
using UnityEngine.Rendering.Universal;

public class BlurRendererFeature : ScriptableRendererFeature
{
    [SerializeField] private BlurSettings settings;
    [SerializeField] private Shader shader;
    private Material material;
    private BlurRenderPass blurRenderPass;

    public override void Create()
    {
        if (shader == null)
        {
            return;
        }
        material = new Material(shader);
        blurRenderPass = new BlurRenderPass(material, settings);
        
        blurRenderPass.renderPassEvent = RenderPassEvent.BeforeRenderingPostProcessing;
    }

    public override void AddRenderPasses(ScriptableRenderer renderer,
        ref RenderingData renderingData)
    {
        if (blurRenderPass == null)
        { 
            return;
        }    
        if (renderingData.cameraData.cameraType == CameraType.Game)
        {
            renderer.EnqueuePass(blurRenderPass);
        }
    }

    protected override void Dispose(bool disposing)
    {
        if (Application.isPlaying)
        {
            Destroy(material);
        }
        else
        {
            DestroyImmediate(material);
        }
    }
}

[Serializable]
public class BlurSettings
{
    [Range(0, 0.4f)] public float horizontalBlur;
    [Range(0, 0.4f)] public float verticalBlur;
}

```

###  Custom render pass code
Here’s the complete code for the custom Render Pass script:
```
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.RenderGraphModule;
using UnityEngine.Rendering.RenderGraphModule.Util;
using UnityEngine.Rendering.Universal;

public class BlurRenderPass : ScriptableRenderPass
{
    private static readonly int horizontalBlurId = Shader.PropertyToID("_HorizontalBlur");
    private static readonly int verticalBlurId = Shader.PropertyToID("_VerticalBlur");
    private const string k_BlurTextureName = "_BlurTexture";
    private const string k_VerticalPassName = "VerticalBlurRenderPass";
    private const string k_HorizontalPassName = "HorizontalBlurRenderPass";

    private BlurSettings defaultSettings;
    private Material material;

    private RenderTextureDescriptor blurTextureDescriptor;

    public BlurRenderPass(Material material, BlurSettings defaultSettings)
    {
        this.material = material;
        this.defaultSettings = defaultSettings;
    }

    private void UpdateBlurSettings()
    {
        if (material == null) return;

        // Use the Volume settings or the default settings if no Volume is set.
        var volumeComponent =
            VolumeManager.instance.stack.GetComponent<CustomVolumeComponent>();
        float horizontalBlur = volumeComponent.horizontalBlur.overrideState ?
            volumeComponent.horizontalBlur.value : defaultSettings.horizontalBlur;
        float verticalBlur = volumeComponent.verticalBlur.overrideState ?
            volumeComponent.verticalBlur.value : defaultSettings.verticalBlur;
        material.SetFloat(horizontalBlurId, horizontalBlur);
        material.SetFloat(verticalBlurId, verticalBlur);
    }

    public override void RecordRenderGraph(RenderGraph renderGraph,
    ContextContainer frameData)
    {
        UniversalResourceData resourceData = frameData.Get<UniversalResourceData>();

        UniversalCameraData cameraData = frameData.Get<UniversalCameraData>();

        // The following line ensures that the render pass doesn't blit
        // from the back buffer.
        if (resourceData.isActiveTargetBackBuffer)
            return;

        TextureHandle srcCamColor = resourceData.activeColorTexture;
        blurTextureDescriptor = resourceData.activeColorTexture.GetDescriptor(renderGraph);
        blurTextureDescriptor.name = k_BlurTextureName;
        blurTextureDescriptor.depthBufferBits = 0;
        var dst = renderGraph.CreateTexture(blurTextureDescriptor);

        // Update the blur settings in the material
        UpdateBlurSettings();

        // This check is to avoid an error from the material preview in the scene
        if (!srcCamColor.IsValid() || !dst.IsValid())
            return;
        
        // The AddBlitPass method adds a vertical blur render graph pass that blits from the source texture (camera color in this case) to the destination texture using the first shader pass (the shader pass is defined in the last parameter).
        RenderGraphUtils.BlitMaterialParameters paraVertical = new(srcCamColor, dst, material, 0);
        renderGraph.AddBlitPass(paraVertical, k_VerticalPassName);
        
        // The AddBlitPass method adds a horizontal blur render graph pass that blits from the texture written by the vertical blur pass to the camera color texture. The method uses the second shader pass.
        RenderGraphUtils.BlitMaterialParameters paraHorizontal = new(dst, srcCamColor, material, 1);
        renderGraph.AddBlitPass(paraHorizontal, k_HorizontalPassName);
    }
}

```

###  Volume Component code
Here’s the complete code for the Volume Component script:
```
using System;
using UnityEngine.Rendering;

[Serializable]
public class CustomVolumeComponent : VolumeComponent
{
    public ClampedFloatParameter horizontalBlur =
        new ClampedFloatParameter(0.05f, 0, 0.5f);
    public ClampedFloatParameter verticalBlur =
        new ClampedFloatParameter(0.05f, 0, 0.5f);
}

```

##  The custom shader for the blur effect
This section contains the code for the custom shader that implements the blur effect.
```
Shader "CustomEffects/Blur"
{
    HLSLINCLUDE
    
        #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
        // The Blit.hlsl file provides the vertex shader (Vert),
        // the input structure (Attributes), and the output structure (Varyings)
        #include "Packages/com.unity.render-pipelines.core/Runtime/Utilities/Blit.hlsl"

        float _VerticalBlur;
        float _HorizontalBlur;
    
        float4 BlurVertical (Varyings input) : SV_Target
        {
            const float BLUR_SAMPLES = 64;
            const float BLUR_SAMPLES_RANGE = BLUR_SAMPLES / 2;
            
            float3 color = 0;
            float blurPixels = _VerticalBlur * _ScreenParams.y;
            
            for(float i = -BLUR_SAMPLES_RANGE; i <= BLUR_SAMPLES_RANGE; i++)
            {
                float2 sampleOffset = float2 (0, (blurPixels / _BlitTexture_TexelSize.w) * (i / BLUR_SAMPLES_RANGE));
                color += SAMPLE_TEXTURE2D(_BlitTexture, sampler_LinearClamp, input.texcoord + sampleOffset).rgb;
            }
            
            return float4(color.rgb / (BLUR_SAMPLES + 1), 1);
        }

        float4 BlurHorizontal (Varyings input) : SV_Target
        {
            const float BLUR_SAMPLES = 64;
            const float BLUR_SAMPLES_RANGE = BLUR_SAMPLES / 2;
            
            UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(input);
            float3 color = 0;
            float blurPixels = _HorizontalBlur * _ScreenParams.x;
            for(float i = -BLUR_SAMPLES_RANGE; i <= BLUR_SAMPLES_RANGE; i++)
            {
                float2 sampleOffset =
                    float2 ((blurPixels / _BlitTexture_TexelSize.z) * (i / BLUR_SAMPLES_RANGE), 0);
                color += SAMPLE_TEXTURE2D(_BlitTexture, sampler_LinearClamp, input.texcoord + sampleOffset).rgb;
            }
            return float4(color / (BLUR_SAMPLES + 1), 1);
        }
    
    ENDHLSL
    
    SubShader
    {
        Tags { "RenderType"="Opaque" "RenderPipeline" = "UniversalPipeline"}
        LOD 100
        ZWrite Off Cull Off
        Pass
        {
            Name "BlurPassVertical"

            HLSLPROGRAM
            
            #pragma vertex Vert
            #pragma fragment BlurVertical
            
            ENDHLSL
        }
        
        Pass
        {
            Name "BlurPassHorizontal"

            HLSLPROGRAM
            
            #pragma vertex Vert
            #pragma fragment BlurHorizontal
            
            ENDHLSL
        }
    }
}

```

## Additional resources
  * The blit examples in the [URP RenderGraph Samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html)
  * [Custom render pass workflow in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [Textures in the Render Graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/apply-scriptable-feature-to-specific-camera.html)
Apply a Scriptable Renderer Feature to a specific camera type in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-feature-reference.html)
Scriptable Renderer Feature API reference for URP
