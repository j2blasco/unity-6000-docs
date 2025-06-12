* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-reflections.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
  * Reflections shader example in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-mesh-normals.html)
Mesh normals shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-environment-reflections.html)
Normal map texturing shader example in the Built-In Render Pipeline
# Reflections shader example in the Built-In Render Pipeline
![A cat-like character with a metallic surface that reflects the scene.](https://docs.unity3d.com/6000.0/Documentation/uploads/SL/ExampleSkyReflection.png) A cat-like character with a metallic surface that reflects the scene.
When a [Skybox](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) is used in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) as a reflection source (see [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html)), then essentially a “default” [Reflection Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) is created, containing the skybox data. A reflection probe is internally a [Cubemap](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) texture; we will extend the world-space normals **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) above to look into it.
The code is starting to get a bit involved by now. Of course, if you want shaders that automatically work with lights, shadows, reflections and the rest of the lighting system, it’s way easier to use [surface shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader). This example is intended to show you how to use parts of the lighting system in a “manual” way.
```
Shader "Unlit/SkyReflection"
{
    SubShader
    {
        Pass
        {
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"

            struct v2f {
                half3 worldRefl : TEXCOORD0;
                float4 pos : SV_POSITION;
            };

            v2f vert (float4 vertex : POSITION, float3 normal : NORMAL)
            {
                v2f o;
                o.pos = UnityObjectToClipPos(vertex);
                // compute world space position of the vertex
                float3 worldPos = mul(_Object2World, vertex).xyz;
                // compute world space view direction
                float3 worldViewDir = normalize(UnityWorldSpaceViewDir(worldPos));
                // world space normal
                float3 worldNormal = UnityObjectToWorldNormal(normal);
                // world space reflection vector
                o.worldRefl = reflect(-worldViewDir, worldNormal);
                return o;
            }
        
            fixed4 frag (v2f i) : SV_Target
            {
                // sample the default reflection cubemap, using the reflection vector
                half4 skyData = UNITY_SAMPLE_TEXCUBE(unity_SpecCube0, i.worldRefl);
                // decode cubemap data into actual color
                half3 skyColor = DecodeHDR (skyData, unity_SpecCube0_HDR);
                // output it!
                fixed4 c = 0;
                c.rgb = skyColor;
                return c;
            }
            ENDHLSL
        }
    }
}

```

The example above uses several things from the built-in [shader include files](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html):
  * **unity_SpecCube0** , **unity_SpecCube0_HDR** , **Object2World** , **UNITY_MATRIX_MVP** from the [built-in shader variables](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UnityShaderVariables.html). **unity_SpecCube0** contains data for the active reflection probe.
  * **UNITY_SAMPLE_TEXCUBE** is a [built-in macro](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SamplerStates.html) to sample a cubemap. Most regular cubemaps are declared and used using standard HLSL syntax (**samplerCUBE** and **texCUBE**), however the reflection probe cubemaps in Unity are declared in a special way to save on sampler slots. If you don’t know what that is, don’t worry, just know that in order to use **unity_SpecCube0** cubemap you have to use **UNITY_SAMPLE_TEXCUBE** macro.
  * **UnityWorldSpaceViewDir** function from **UnityCG.cginc** , and **DecodeHDR** function from the same file. The latter is used to get actual color from the reflection probe data – since Unity stores reflection probe cubemap in specially encoded way.
  * **reflect** is just a built-in HLSL function to compute vector reflection around a given normal.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-mesh-normals.html)
Mesh normals shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-environment-reflections.html)
Normal map texturing shader example in the Built-In Render Pipeline
