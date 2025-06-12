* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-resolution-birp.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
  * [Shadows in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shadows-in-birp.html)
  * Configure shadow resolution in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadows-in-birp.html)
Shadows in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingBakedAmbientOcclusion.html)
Add ambient occlusion in the Built-In Render Pipeline
# Configure shadow resolution in the Built-In Render Pipeline
To calculate the resolution of a shadow map, Unity:
  1. Determines the area of the screen view that the Light can illuminate. For directional lights, the whole screen can be illuminated. For Spot Lights and Point Lights, the area is the onscreen projection of the shape of the light’s extent: a sphere for point lights, or a cone for Spot Lights. The projected shape has a width and height in pixels on the screen; the larger of those two values is then taken. This value is called the Light’s **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) size.
  2. Determines the shadow quality multiplier. Unity uses the **Shadow Resolution** setting for this, which is set in the [Quality Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html) window). The quality settings correspond to the following values: 
     * Very High: 1.0
     * High: 0.5
     * Medium: 0.25
     * Low: 0.125
  3. Performs the following calculation, and then clamps the result to the maximum size:

**Light type:** | **Formula:** | **Maximum resolution, in pixels:**  
---|---|---  
Directional |  [NextPowerOfTwo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html) (pixel size * shadow quality multiplier * 3.8) | 4096 x 4096 when Shadow Resolution is Very High Quality and/or if the GPU has 512MB or more of RAM, 2048 x 2048 otherwise.  
Spot Lights |  [NextPowerOfTwo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html) (pixel size * shadow quality multiplier * 2.0) | 2048 x 2048 if the GPU has 512MB or more of RAM, 1024 x 1024 otherwise.  
Point Lights |  [NextPowerOfTwo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html) (pixel size * shadow quality multiplier * 1.0) | 1024 x 1024 if the GPU has 512MB or more of RAM, 512 x 512 otherwise.  
## Override shadow map resolution
In the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), you can set the resolution of a Light’s shadow map by setting the [Light.shadowCustomResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowCustomResolution.html) property to a value greater than 0. When this value is greater than 0, Unity performs the following calculation for all Light types:
[NextPowerOfTwo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.NextPowerOfTwo.html) (shadowCustomResolution)
It then clamps the maximum resolution based on Light type and hardware, as shown in the table above.
## Additional resources
  * [Shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html)A UI component that adds a simple outline effect to graphic components such as Text or Image. It must be on the same GameObject as the graphic component. [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Shadow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadow)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadows-in-birp.html)
Shadows in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingBakedAmbientOcclusion.html)
Add ambient occlusion in the Built-In Render Pipeline
