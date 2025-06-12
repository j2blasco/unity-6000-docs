* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-reconstruct-world-position.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * [Examples of writing a custom shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-landing.html)
  * Reconstruct world space positions in a shader in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-depth-only.html)
Write a depth-only pass in a Universal Render Pipeline shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods.html)
Shader methods in URP
# Reconstruct world space positions in a shader in URP
The Unity **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in this example reconstructs the world space positions for **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) using a depth texture and screen space UV coordinates. The shader draws a checkerboard pattern on a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) to visualize the positions.
The following illustration shows the end result:
![Checkerboard pattern visualizing the reconstructed world space positions.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/urp-shader-tutorial-reconstruct-world-positions-from-depth.png) Checkerboard pattern visualizing the reconstructed world space positions.
This page contains the following sections:
  * [Create the sample scene](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-reconstruct-world-position.html#create-the-sample-scene)
  * [Edit the ShaderLab code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-reconstruct-world-position.html#edit-the-shaderlab-code)
  * [The complete ShaderLab code](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-reconstruct-world-position.html#the-complete-shaderlab-code)


## Create the sample scene
Create the sample **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) to follow the steps in this section:
  1. Install URP into an existing Unity project, or create a new project using the [**Universal Project Template**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/creating-a-new-project-with-urp.html).
  2. In the sample Scene, create a plane **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) and place it so that it occludes some of the GameObjects.
![Create a plane](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/urp-shader-tutorial-create-place-gameobj.png) Create a plane
  3. Create a new Material and assign it to the plane.
  4. Create a new shader and assign it to the material. Copy and paste the Unity shader source code from the page [URP unlit basic shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-unlit-structure.html).
  5. Select the URP Asset.
  6. In the URP Asset, in the General section, enable `Depth Texture`.
![In URP Asset, enable Depth Texture](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/urp-asset-depth-texture.png) In URP Asset, enable Depth Texture
  7. Open the shader you created on step 4.


## Edit the ShaderLab code
This section assumes that you copied the source code from the page [URP unlit basic shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-basic-unlit-structure.html).
Make the following changes to the **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) code:
  1. In the `HLSLPROGRAM` block, add the include declaration for the depth texture shader header. For example, place it under the existing include declaration for `Core.hlsl`.
```
#include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

// The DeclareDepthTexture.hlsl file contains utilities for sampling the Camera
// depth texture.
#include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/DeclareDepthTexture.hlsl"

```

The `DeclareDepthTexture.hlsl` file contains functions for sampling the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) depth texture. This example uses the `SampleSceneDepth` function for sampling the Z coordinate for pixels.
  2. In the fragment shader definition, add `Varyings IN` as input.
```
half4 frag(Varyings IN) : SV_Target

```

In this example, the fragment shader uses the `positionHCS` property from the `Varyings` struct to get locations of pixels.
  3. In the fragment shader, to calculate the UV coordinates for sampling the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer), divide the pixel location by the render target resolution `_ScaledScreenParams`. The property `_ScaledScreenParams.xy` takes into account any scaling of the render target, such as **Dynamic Resolution** A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution).
```
float2 UV = IN.positionHCS.xy / _ScaledScreenParams.xy;

```

  4. In the fragment shader, use the `SampleSceneDepth` functions to sample the depth buffer.
```
#if UNITY_REVERSED_Z
    real depth = SampleSceneDepth(UV);
#else
    // Adjust z to match NDC for OpenGL
    real depth = lerp(UNITY_NEAR_CLIP_VALUE, 1, SampleSceneDepth(UV));
#endif

```



The `SampleSceneDepth` function comes from the `DeclareDepthTexture.hlsl` file. It returns the Z value in the range `[0, 1]`.
For the reconstruction function (`ComputeWorldSpacePosition`) to work, the depth value must be in the normalized device coordinate (NDC) space. In D3D, Z is in range `[0,1]`, in OpenGL, Z is in range `[-1, 1]`.
This example uses the `UNITY_REVERSED_Z` constant to determine the platform and adjust the Z value range. Check step 6 in this example for more explanations.
The `UNITY_NEAR_CLIP_VALUE` variable is a platform independent near **clipping plane** A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#clippingplane) value for the clip space.
For more information, refer to [Platform-specific rendering differences](https://docs.unity3d.com/Manual/SL-PlatformDifferences.html).
  1. Reconstruct world space positions from the UV and Z coordinates of pixels.
```
float3 worldPos = ComputeWorldSpacePosition(UV, depth, UNITY_MATRIX_I_VP);

```

`ComputeWorldSpacePosition` is a utility function that calculates the world space position from the UV and the depth (Z) values. This function is defined in the `Common.hlsl` file of the SRP Core package.
`UNITY_MATRIX_I_VP` is an inverse view projection matrix which transforms points from the clip space to the world space.
  2. To visualize the world space positions of pixels, create the checkboard effect.
```
uint scale = 10;
uint3 worldIntPos = uint3(abs(worldPos.xyz * scale));
bool white = (worldIntPos.x & 1) ^ (worldIntPos.y & 1) ^ (worldIntPos.z & 1);
half4 color = white ? half4(1,1,1,1) : half4(0,0,0,1);

```

The `scale` is the inverse scale of the checkboard pattern size.
The `abs` function mirrors the pattern to the negative coordinate side.
The `uint3` declaration for the `worldIntPos` variable snaps the coordinate positions to integers.
The `AND` operator in the expresion `<integer value> & 1` checks if the value is even (0) or odd (1). The expression lets the code divide the surface into squares.
The `XOR` operator in the expresion `<integer value> ^ <integer value>` flips the square color.
The depth buffer might not have valid values for areas where no geometry is rendered. The following code draws black color in such areas.
```
#if UNITY_REVERSED_Z
    if(depth < 0.0001)
        return half4(0,0,0,1);
#else
    if(depth > 0.9999)
        return half4(0,0,0,1);
#endif

```

Different platforms use different Z values for **far clipping planes** The maximum draw distance for a camera. Geometry beyond the plane defined by this value is not rendered. The plane is perpendicular to the camera’s forward (Z) direction.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Farclippingplane) (0 == far, or 1 == far). The `UNITY_REVERSED_Z` constant lets the code handle all platforms correctly.
Save the shader code, the example is ready.


The following illustration shows the end result:
![3D Checkerboard](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/urp-shader-tutorial-reconstruct-world-positions-from-depth.png) 3D Checkerboard
## The complete ShaderLab code
Below is the complete ShaderLab code for this example.
```
// This Unity shader reconstructs the world space positions for pixels using a depth
// texture and screen space UV coordinates. The shader draws a checkerboard pattern
// on a mesh to visualize the positions.
Shader "Example/URPReconstructWorldPos"
{
    Properties
    { }

    // The SubShader block containing the Shader code.
    SubShader
    {
        // SubShader Tags define when and under which conditions a SubShader block or
        // a pass is executed.
        Tags { "RenderType" = "Opaque" "RenderPipeline" = "UniversalPipeline" }

        Pass
        {
            HLSLPROGRAM
            // This line defines the name of the vertex shader.
            #pragma vertex vert
            // This line defines the name of the fragment shader.
            #pragma fragment frag

            // The Core.hlsl file contains definitions of frequently used HLSL
            // macros and functions, and also contains #include references to other
            // HLSL files (for example, Common.hlsl, SpaceTransforms.hlsl, etc.).
            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            // The DeclareDepthTexture.hlsl file contains utilities for sampling the
            // Camera depth texture.
            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/DeclareDepthTexture.hlsl"

            // This example uses the Attributes structure as an input structure in
            // the vertex shader.
            struct Attributes
            {
                // The positionOS variable contains the vertex positions in object
                // space.
                float4 positionOS   : POSITION;
            };

            struct Varyings
            {
                // The positions in this struct must have the SV_POSITION semantic.
                float4 positionHCS  : SV_POSITION;
            };

            // The vertex shader definition with properties defined in the Varyings
            // structure. The type of the vert function must match the type (struct)
            // that it returns.
            Varyings vert(Attributes IN)
            {
                // Declaring the output object (OUT) with the Varyings struct.
                Varyings OUT;
                // The TransformObjectToHClip function transforms vertex positions
                // from object space to homogenous clip space.
                OUT.positionHCS = TransformObjectToHClip(IN.positionOS.xyz);
                // Returning the output.
                return OUT;
            }

            // The fragment shader definition.
            // The Varyings input structure contains interpolated values from the
            // vertex shader. The fragment shader uses the `positionHCS` property
            // from the `Varyings` struct to get locations of pixels.
            half4 frag(Varyings IN) : SV_Target
            {
                // To calculate the UV coordinates for sampling the depth buffer,
                // divide the pixel location by the render target resolution
                // _ScaledScreenParams.
                float2 UV = IN.positionHCS.xy / _ScaledScreenParams.xy;

                // Sample the depth from the Camera depth texture.
                #if UNITY_REVERSED_Z
                    real depth = SampleSceneDepth(UV);
                #else
                    // Adjust Z to match NDC for OpenGL ([-1, 1])
                    real depth = lerp(UNITY_NEAR_CLIP_VALUE, 1, SampleSceneDepth(UV));
                #endif

                // Reconstruct the world space positions.
                float3 worldPos = ComputeWorldSpacePosition(UV, depth, UNITY_MATRIX_I_VP);

                // The following part creates the checkerboard effect.
                // Scale is the inverse size of the squares.
                uint scale = 10;
                // Scale, mirror and snap the coordinates.
                uint3 worldIntPos = uint3(abs(worldPos.xyz * scale));
                // Divide the surface into squares. Calculate the color ID value.
                bool white = ((worldIntPos.x) & 1) ^ (worldIntPos.y & 1) ^ (worldIntPos.z & 1);
                // Color the square based on the ID value (black or white).
                half4 color = white ? half4(1,1,1,1) : half4(0,0,0,1);

                // Set the color to black in the proximity to the far clipping
                // plane.
                #if UNITY_REVERSED_Z
                    // Case for platforms with REVERSED_Z, such as D3D.
                    if(depth < 0.0001)
                        return half4(0,0,0,1);
                #else
                    // Case for platforms without REVERSED_Z, such as OpenGL.
                    if(depth > 0.9999)
                        return half4(0,0,0,1);
                #endif

                return color;
            }
            ENDHLSL
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-depth-only.html)
Write a depth-only pass in a Universal Render Pipeline shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods.html)
Shader methods in URP
