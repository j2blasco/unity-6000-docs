* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-sample.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Motion vectors in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-landing.html)
  * Sample motion vectors in a shader in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-custom-shader.html)
Output a motion vector texture in a custom shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-troubleshooting.html)
Troubleshooting motion vectors in URP
# Sample motion vectors in a shader in URP
Any `ScriptableRenderPass` implementation can request the motion vector texture as input. To do that, add the `ScriptableRenderPassInput.Motion` flag in the [ScriptableRenderPass.ConfigureInput](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.2/api/UnityEngine.Rendering.Universal.ScriptableRenderPass.html#UnityEngine_Rendering_Universal_ScriptableRenderPass_ConfigureInput_UnityEngine_Rendering_Universal_ScriptableRenderPassInput_) method in the [AddRenderPasses](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.2/api/UnityEngine.Rendering.Universal.ScriptableRendererFeature.html#UnityEngine_Rendering_Universal_ScriptableRendererFeature_AddRenderPasses_UnityEngine_Rendering_Universal_ScriptableRenderer_UnityEngine_Rendering_Universal_RenderingData__) callback of your custom Renderer Feature. If no other effect in the frame is using motion vectors, setting this input flag forces the URP renderer to inject the motion vector render pass into the frame.
To sample the motion vector texture in your **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) pass, declare the shader resource for it in the `HLSLPROGRAM` section:
```
    TEXTURE2D_X(_MotionVectorTexture);
    SAMPLER(sampler_MotionVectorTexture);

```

To perform the sampling, use the following macro:
```
    SAMPLE_TEXTURE2D_X(_MotionVectorTexture, sampler_MotionVectorTexture, uv);

```

The `_X` postfix ensures that the texture is correctly declared and sampled when targeting **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) platforms.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-custom-shader.html)
Output a motion vector texture in a custom shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-troubleshooting.html)
Troubleshooting motion vectors in URP
