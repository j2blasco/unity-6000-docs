* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/custom-lighting-change-light-falloff.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Custom lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/custom-lighting-landing.html)
  * Change how lights fade using light falloff in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)
Render additional lights in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universal-additional-light-data.html)
Universal Additional Light Data component in URP
# Change how lights fade using light falloff in URP
To create a unique visual style in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), you can change the light falloff function in URP for real-time and baked lighting.
This example replaces the default URP light falloff function with a quadratic falloff function, which has a different visual style. You can modify the functions mentioned on this page to achieve other visual styles. The quadratic light falloff function has a similar behavior to the falloff function in the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
## Prepare URP source code for modification
This customization requires modifying URP source code. For instructions, refer to [Modify URP source code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/modify-urp-source-code.html).
## Change light falloff for real-time lights
To modify the light falloff behavior for real-time lights:
  1. Open the following HLSL file:
```
Packages/com.unity.render-pipelines.universal/ShaderLibrary/RealtimeLights.hlsl

```

  2. Modify the `DistanceAttenuation` method. Use the following code:
```
// The quadratic falloff function provides a visual style
// similar to the Built-In Render Pipeline light falloff.
float DistanceAttenuation(float distanceSqr, float2 distanceAndSpotAttenuation)
{
    // Calculate the linear distance from the squared distance value.
    float distance = sqrt(distanceSqr);

    // Calculate the range of the light by taking the inverse square root of the attenuation parameter.
    float range = rsqrt(distanceAndSpotAttenuation.x);

    // Normalize the distance to a value between 0 and 1 (1 at the source, 0 at the max range).
    float distance01 = saturate(1.0f - (distance / range));

    // Apply quadratic falloff.
    float lightAtten = pow(distance01, 2.0f);

    // Smooth the falloff across the entire range for a more gradual and natural fade.
    float smoothFactor = smoothstep(0.0f, 1.0f, distance01);
    lightAtten *= smoothFactor;
        
    return lightAtten;
}

```

  3. Modify the `AngleAttenuation` method. Use the following code:
```
float AngleAttenuation(float3 spotDirection, float3 lightDirection, float2 spotAttenuation)
{
    // Compute the cosine of the angle between spotlight and surface.
    float SdotL = dot(spotDirection, lightDirection); 

    // Linearly interpolate attenuation between the inner and the outer cone.
    float atten = saturate(SdotL * spotAttenuation.x + spotAttenuation.y);

    // Apply cubic smoothing for a gradual edge falloff.
    atten = atten * atten * (3.0f - 2.0f * atten);

    return atten;
}

```



The following illustration compares the default URP light falloff, the custom light falloff function in this example, and the light falloff in the Built-In Render Pipeline. 
![A: URP default falloff. B: Built-In Render Pipeline quadratic falloff. C: URP quadratic falloff \(this example\)](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/customizing-urp/urp-custom-light-falloff.png) A: URP default falloff. B: Built-In Render Pipeline quadratic falloff. C: URP quadratic falloff (this example)
## Change light falloff for baked lights
To ensure that the look of the baked lighting in your project matches the look of real-time lighting, change the light falloff of the **baked lights** Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html#baked)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#BakedLights).
  1. Open the following file:
```
Packages/com.unity.render-pipelines.universal/Runtime/UniversalRenderPipelineCore.cs

```

  2. Change the `lightData.falloff` value to [FalloffType.Legacy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.html):
```
lightData.falloff = FalloffType.Legacy;

```



The value [FalloffType.Legacy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.html) uses quadratic attenuation, which matches the real-time falloff in this example. You can use other values to match the real-time lighting in your project.
For more information on changing the light falloff function in baked lighting, refer to [Change the fade distance of lights with fall-off](https://docs.unity3d.com/6000.0/Documentation/Manual/ProgressiveLightmapper-CustomFallOff.html)
## Additional resources
  * [Modify URP source code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/modify-urp-source-code.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * [Upgrading from the Built-In Render Pipeline to URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/upgrading-from-birp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html)
Render additional lights in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universal-additional-light-data.html)
Universal Additional Light Data component in URP
