* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-normals.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * [Examples of writing a custom shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-landing.html)
  * Visualize normal vectors in a shader in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-texture.html)
Draw a texture in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-depth-only.html)
Write a depth-only pass in a Universal Render Pipeline shader
# Visualize normal vectors in a shader in URP
The Unity **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in this example visualizes the normal vector values on the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh).
Use the Unity shader source file from section [URP unlit basic shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-unlit-structure.html) and make the following changes to the **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) code:
  1. In `struct Attributes`, which is the input structure for the **vertex shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader) in this example, declare the variable containing the normal vector for each vertex.
```
struct Attributes
{
    float4 positionOS   : POSITION;
    // Declaring the variable containing the normal vector for each vertex.
    half3 normal        : NORMAL;
};

```

  2. In `struct Varyings`, which is the input structure for the fragment shader in this example, declare the variable for storing the normal vector values for each fragment:
```
struct Varyings
{
    float4 positionHCS  : SV_POSITION;
    // The variable for storing the normal vector values.
    half3 normal        : TEXCOORD0;
};

```

This example uses the three components of the normal vector as RGB color values for each fragment.
  3. To render the normal vector values on the mesh, use the following code as the fragment shader:
```
half4 frag(Varyings IN) : SV_Target
{
    half4 color = 0;
    color.rgb = IN.normal;
    return color;
}

```

  4. Unity renders the normal vector values on the mesh:
![Rendering normals without compression](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/unlit-shader-tutorial-normals-uncompressed.png) Rendering normals without compression
A part of the capsule is black. This is because in those points, all three components of the normal vector are negative. The next step shows how to render values in those areas as well.
  5. To render negative normal vector components, use the **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) technique. To compress the range of normal component values `(-1..1)` to color value range `(0..1)`, change the following line:
```
color.rgb = IN.normal;

```

to this line:
```
color.rgb = IN.normal * 0.5 + 0.5;

```



Now Unity renders the normal vector values as colors on the mesh.
![Rendering normals with compression](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/unlit-shader-tutorial-normals.png) Rendering normals with compression
Below is the complete ShaderLab code for this example.
```
// This shader visuzlizes the normal vector values on the mesh.
Shader "Example/URPUnlitShaderNormal"
{
    Properties
    { }

    SubShader
    {
        Tags { "RenderType" = "Opaque" "RenderPipeline" = "UniversalPipeline" }

        Pass
        {
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            struct Attributes
            {
                float4 positionOS   : POSITION;
                // Declaring the variable containing the normal vector for each
                // vertex.
                half3 normal        : NORMAL;
            };

            struct Varyings
            {
                float4 positionHCS  : SV_POSITION;
                half3 normal        : TEXCOORD0;
            };

            Varyings vert(Attributes IN)
            {
                Varyings OUT;
                OUT.positionHCS = TransformObjectToHClip(IN.positionOS.xyz);
                // Use the TransformObjectToWorldNormal function to transform the
                // normals from object to world space. This function is from the
                // SpaceTransforms.hlsl file, which is referenced in Core.hlsl.
                OUT.normal = TransformObjectToWorldNormal(IN.normal);
                return OUT;
            }

            half4 frag(Varyings IN) : SV_Target
            {
                half4 color = 0;
                // IN.normal is a 3D vector. Each vector component has the range
                // -1..1. To show all vector elements as color, including the
                // negative values, compress each value into the range 0..1.
                color.rgb = IN.normal * 0.5 + 0.5;
                return color;
            }
            ENDHLSL
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-texture.html)
Draw a texture in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-depth-only.html)
Write a depth-only pass in a Universal Render Pipeline shader
