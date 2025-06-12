* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-fullscreen-blit.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Compatibility Mode in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html)
  * Example of a Scriptable Renderer Feature in Compatibility mode in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
Write a Scriptable Render Pass in Compatibility Mode in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)
Scriptable Render Pass Compatibility Mode API reference for URP
# Example of a Scriptable Renderer Feature in Compatibility mode in URP
The example on this page performs a full-screen **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit) that tints the screen green.
**Note:** Unity no longer develops or improves the rendering path that doesn’t use the [render graph API](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html). Use the render graph API instead when developing new graphics features. To use the instructions on this page, enable **Compatibility Mode (Render Graph Disabled)** in URP graphics settings (**Project Settings** > **Graphics**).
To use the examples, follow these steps:
  1. To create the custom render pass, create a new C# script called `ColorBlitPass.cs`, then paste in the code from the [Example custom render pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-fullscreen-blit.html#render-pass) section.
**Note:** The example uses the `Blitter` API. Don’t use the `CommandBuffer.Blit` API in Compatibility Mode. Refer to [Blit in Compatibility Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/blit-overview.html) for more information.
  2. To create the Scriptable Renderer Feature that adds the custom render pass to the render loop, create a new C# script called `ColorBlitRendererFeature.cs`, then paste in the code from the [Example Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-fullscreen-blit.html#scriptable-renderer-feature) section.
  3. To create the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code that tints the **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) green, [create a shader file](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html), then paste in the code from the [Example shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-fullscreen-blit.html#shader) section.
**Note:** The shader you use with the `Blitter` API must be a hand-coded shader. [Shader Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-graph.html) shaders aren’t compatible with the `Blitter` API.
  4. Add the `ColorBlitRendererFeature` to the current URP Renderer asset. For more information, refer to [Add a Renderer Feature to a URP Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html).


To change the brightness, adjust the **Intensity** property in the **Color Blit Renderer Feature** component.
**Note:** To visualize the example if your project uses **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR), install the [MockHMD XR Plugin](https://docs.unity3d.com/Packages/com.unity.xr.mock-hmd@latest/) package in your project, then set the **Render Mode** property to **Single Pass Instanced**.
## Example custom render pass
```
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;

internal class ColorBlitPass : ScriptableRenderPass
{
    ProfilingSampler m_ProfilingSampler = new ProfilingSampler("ColorBlit");
    Material m_Material;
    RTHandle m_CameraColorTarget;
    float m_Intensity;

    public ColorBlitPass(Material material)
    {
        m_Material = material;
        renderPassEvent = RenderPassEvent.BeforeRenderingPostProcessing;
    }

    public void SetTarget(RTHandle colorHandle, float intensity)
    {
        m_CameraColorTarget = colorHandle;
        m_Intensity = intensity;
    }

    public override void OnCameraSetup(CommandBuffer cmd, ref RenderingData renderingData)
    {
        ConfigureTarget(m_CameraColorTarget);
    }

    public override void Execute(ScriptableRenderContext context, ref RenderingData renderingData)
    {
        var cameraData = renderingData.cameraData;
        if (cameraData.camera.cameraType != CameraType.Game)
            return;

        if (m_Material == null)
            return;

        CommandBuffer cmd = CommandBufferPool.Get();
        using (new ProfilingScope(cmd, m_ProfilingSampler))
        {
            m_Material.SetFloat("_Intensity", m_Intensity);
            Blitter.BlitCameraTexture(cmd, m_CameraColorTarget, m_CameraColorTarget, m_Material, 0);
        }
        context.ExecuteCommandBuffer(cmd);
        cmd.Clear();

        CommandBufferPool.Release(cmd);
    }
}

```

## Example Scriptable Renderer Feature
The Scriptable Renderer Feature adds the render pass to the render loop.
```
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;

internal class ColorBlitRendererFeature : ScriptableRendererFeature
{
    public Shader m_Shader;
    public float m_Intensity;

    Material m_Material;

    ColorBlitPass m_RenderPass = null;

    public override void AddRenderPasses(ScriptableRenderer renderer,
                                    ref RenderingData renderingData)
    {
        if (renderingData.cameraData.cameraType == CameraType.Game)
            renderer.EnqueuePass(m_RenderPass);
    }

    public override void SetupRenderPasses(ScriptableRenderer renderer,
                                        in RenderingData renderingData)
    {
        if (renderingData.cameraData.cameraType == CameraType.Game)
        {
            // Calling ConfigureInput with the ScriptableRenderPassInput.Color argument
            // ensures that the opaque texture is available to the Render Pass.
            m_RenderPass.ConfigureInput(ScriptableRenderPassInput.Color);
            m_RenderPass.SetTarget(renderer.cameraColorTargetHandle, m_Intensity);
        }
    }

    public override void Create()
    {
        m_Material = CoreUtils.CreateEngineMaterial(m_Shader);
        m_RenderPass = new ColorBlitPass(m_Material);
    }

    protected override void Dispose(bool disposing)
    {
        CoreUtils.Destroy(m_Material);
    }
}

```

## Example shader
The shader performs the GPU side of the rendering. It samples the color texture from the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), then outputs the color with the green value set to the chosen intensity.
```
Shader "ColorBlit"
{
    SubShader
    {
        Tags { "RenderType"="Opaque" "RenderPipeline" = "UniversalPipeline"}
        LOD 100
        ZWrite Off Cull Off
        Pass
        {
            Name "ColorBlitPass"

            HLSLPROGRAM
            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
            
            // The Blit.hlsl file provides the vertex shader (Vert),
            // the input structure (Attributes) and the output structure (Varyings)
            #include "Packages/com.unity.render-pipelines.core/Runtime/Utilities/Blit.hlsl"

            #pragma vertex Vert
            #pragma fragment frag

            // Set the color texture from the camera as the input texture
            TEXTURE2D_X(_CameraOpaqueTexture);
            SAMPLER(sampler_CameraOpaqueTexture);

            // Set up an intensity parameter
            float _Intensity;

            half4 frag (Varyings input) : SV_Target
            {
                UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(input);

                // Sample the color from the input texture
                float4 color = SAMPLE_TEXTURE2D_X(_CameraOpaqueTexture, sampler_CameraOpaqueTexture, input.texcoord);

                // Output the color from the texture, with the green value set to the chosen intensity
                return color * float4(0, _Intensity, 0, 1);
            }
            ENDHLSL
        }
    }
}

```

## Additional resources
  * [Custom render pass workflow](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html)
  * [Injecting a render pass via a Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
Write a Scriptable Render Pass in Compatibility Mode in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html)
Scriptable Render Pass Compatibility Mode API reference for URP
