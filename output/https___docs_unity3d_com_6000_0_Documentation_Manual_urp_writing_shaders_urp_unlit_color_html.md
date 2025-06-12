* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-color.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * [Examples of writing a custom shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-landing.html)
  * Write an unlit shader with color input in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-unlit-structure.html)
Write an unlit basic shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-texture.html)
Draw a texture in a shader in URP
# Write an unlit shader with color input in URP
The Unity **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in this example adds the **Base Color** property to the Material. You can select the color using that property and the shader fills the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) shape with the color.
Use the Unity shader source file from section [URP unlit basic shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-unlit-structure.html) and make the following changes to the **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) code:
  1. Add the `_BaseColor` property definition to the Properties block:
```
Properties
{
    [MainColor] _BaseColor("Base Color", Color) = (1, 1, 1, 1)
}

```

This declaration adds the `_BaseColor` property with the label **Base Color** to the Material:
![Base Color property on a Material](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/urp-material-prop-base-color.png) Base Color property on a Material
When you declare a property with the `[MainColor]` attribute, Unity uses this property as the [main color](https://docs.unity3d.com/ScriptReference/Material-color.html) of the Material.
> **Note** : For compatibility reasons, the `_Color` property name is a reserved name. Unity uses a property with the name `_Color` as the [main color](https://docs.unity3d.com/ScriptReference/Material-color.html) even it does not have the `[MainColor]` attribute.
  2. When you declare a property in the Properties block, you also need to declare it in the HLSL code.
> **Note** : To ensure that the Unity shader is SRP Batcher compatible, declare all Material properties inside a single `CBUFFER` block with the name `UnityPerMaterial`. For more information on the SRP Batcher, refer to the documentation on the [Scriptable Render Pipeline (SRP) Batcher](https://docs.unity3d.com/Manual/SRPBatcher.html).
Add the following code before the **vertex shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader):
```
CBUFFER_START(UnityPerMaterial)
    half4 _BaseColor;
CBUFFER_END

```

  3. Change the code in the fragment shader so that it returns the `_BaseColor` property.
```
half4 frag() : SV_Target
{
    return _BaseColor;
}

```



Now you can select the color in the **Base Color** field in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. The fragment shader fills the mesh with the color you select.
![Base Color field on a Material](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/unlit-shader-tutorial-color-field-with-scene.png) Base Color field on a Material
Below is the complete ShaderLab code for this example.
```
// This shader fills the mesh shape with a color that a user can change using the
// Inspector window on a Material.
Shader "Example/URPUnlitShaderColor"
{
    // The _BaseColor variable is visible in the Material's Inspector, as a field
    // called Base Color. You can use it to select a custom color. This variable
    // has the default value (1, 1, 1, 1).
    Properties
    {
        [MainColor] _BaseColor("Base Color", Color) = (1, 1, 1, 1)
    }

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
            };

            struct Varyings
            {
                float4 positionHCS  : SV_POSITION;
            };

            // To make the Unity shader SRP Batcher compatible, declare all
            // properties related to a Material in a a single CBUFFER block with
            // the name UnityPerMaterial.
            CBUFFER_START(UnityPerMaterial)
                // The following line declares the _BaseColor variable, so that you
                // can use it in the fragment shader.
                half4 _BaseColor;
            CBUFFER_END

            Varyings vert(Attributes IN)
            {
                Varyings OUT;
                OUT.positionHCS = TransformObjectToHClip(IN.positionOS.xyz);
                return OUT;
            }

            half4 frag() : SV_Target
            {
                // Returning the _BaseColor value.
                return _BaseColor;
            }
            ENDHLSL
        }
    }
}

```

Section [Drawing a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-texture.html) shows how to draw a texture on the mesh.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-unlit-structure.html)
Write an unlit basic shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-texture.html)
Draw a texture in a shader in URP
