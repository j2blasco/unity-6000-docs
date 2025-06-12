* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Android-SinglePassStereoRendering.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Graphics for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-graphics.html)
  * Single-pass stereo rendering for Android


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-screen-configuration.html)
Screen configuration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/vulkan-swapchain-pre-rotation.html)
Framebuffer orientation
# Single-pass stereo rendering for Android
Unity supports [single-pass stereo rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/SinglePassInstancing.html) for Android devices that support multiview. Multiview consists of the [GL_OVR_multiview2](https://www.khronos.org/registry/OpenGL/extensions/OVR/OVR_multiview2.txt) and [GL_OVR_multiview_multisampled_render_to_texture](https://www.khronos.org/registry/OpenGL/extensions/OVR/OVR_multiview_multisampled_render_to_texture.txt) OpenGL ES extensions. These extensions require **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to use a 2D texture array that consists of two slices, one slice per eye.
## Shader code requirements
To use single-pass stereo rendering with custom shaders, you may need to include additional shader code. You don’t need to include additional code if your custom shaders are:
  * **Surface Shaders** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) that don’t have custom vertex processing.
  * Fixed-function pipeline shaders.


**Note** : These shader changes are compatible with multi-pass stereo rendering.
### Modify your shaders
If you want to use the `unity_StereoEyeIndex` built-in shader variable to know which eye the GPU is rendering to, you must declare `UNITY_VERTEX_OUTPUT_STEREO` in any shader stage output structs that you have. For example:
```
struct v2f {
    float2 uv : TEXCOOR0;
    float4 vertex : SV_POSITION;
    UNITY_VERTEX_OUTPUT_STEREO
};

```

To initialize the output data, use `UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO()` in the **vertex shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader) function. For example:
```
v2f vert (appdata v)
{
    v2f o;
    UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(o);
    o.vertex = UnityObjectToClipPos(v.vertex);
    o.uv = TRANSFORM_TEX(v.uv, _MainTex);
    return o;
}

```

To initialize `unity_StereoEyeIndex` in subsequent stages, add `UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX()` at the beginning. For example:
```
fixed4 frag (v2f i) : SV_Target
{
    UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX(i);
    // sample the texture
    fixed4 col = tex2D(_MainTex, i.uv);
    // apply fog
    UNITY_APPLY_FOG(i.fogCoord, col);
    return col;
}

```

If your shaders use other shader stages, use the `UNITY_TRANSFER_VERTEX_OUTPUT_STEREO()` macro to transfer the eye index to the subsequent stages.
**Tip** : To calculate the final position of the object, it’s best practice to use `UnityObjectToClipPos(IN.vertex)` instead of `mul(UNITY_MATRIX_MVP, IN.vertex)`.
## Post-Processing Shaders
You must update **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) shaders to deal with the eye textures being a 2D texture array. To help with this, Unity includes the `UNITY_DECLARE_SCREENSPACE_TEXTURE()` macro. To make textures work in both multi-pass and single-pass modes, wrap each textures in this macro. Also, when you sample the texture, use the `UNITY_SAMPLE_SCREENSPACE_TEXTURE()` macro.
This macro requires that you call `UNITY_SETUP_STEREO_EYE_INDEX_POST_VERTEX()` beforehand when in single-pass mode. Unity also includes similar macros for depth textures and screen space shadow maps. You can see the full list at the bottom of `HLSLSupport.cginc`.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-screen-configuration.html)
Screen configuration
[](https://docs.unity3d.com/6000.0/Documentation/Manual/vulkan-swapchain-pre-rotation.html)
Framebuffer orientation
