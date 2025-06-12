* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Shader methods in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/use-built-in-shader-methods-birp.html)
  * Import a file from the shader library in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/use-built-in-shader-methods-birp.html)
Shader methods in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinFunctions.html)
Use built-in shader functions in the Built-In Render Pipeline
# Import a file from the shader library in the Built-In Render Pipeline
Unity contains several files that can be used by your [shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html) to bring in predefined variables and helper functions. This is done by the standard `#include` directive, e.g.:
```
SubShader {
    Pass {
        HLSLPROGRAM

        #include "UnityCG.cginc"

        ENDHLSL
    }
}

```

Shader include files in Unity are with `.cginc` extension, and the built-in ones are:
  * `HLSLSupport.cginc`: Declares various [preprocessor macros](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-built-in-macros.html) to aid in multi-platform **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) development. Unity automatically includes this file if you use `CGPROGRAM`. For more information, refer to [Shader code blocks in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html).
  * `UnityShaderVariables.cginc`: Declares various [built-in global variables](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UnityShaderVariables.html) that are commonly used in shaders. Unity automatically includes this file if you use `CGPROGRAM`. For more information, refer to [Shader code blocks in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html).
  * `UnityCG.cginc`: Commonly used [built-in helper functions](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinFunctions.html) and data structures.
  * `AutoLight.cginc`: Lighting and shadowing functionality, for example [surface shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) use this file internally.
  * `Lighting.cginc`: Standard [surface shader](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html) lighting models. Unity automatically includes this file if your write surface shaders.
  * `TerrainEngine.cginc`: Helper functions for **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) and vegetation shaders.


**Note** : Although shader library files have a .cginc file extension, they’re written in HLSL rather than CG.
These files are found inside Unity application (**{unity install path}/Data/CGIncludes/UnityCG.cginc** on Windows, **/Applications/Unity/Unity.app/Contents/CGIncludes/UnityCG.cginc** on Mac), if you want to take a look at what exactly is done in any of the helper code.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/use-built-in-shader-methods-birp.html)
Shader methods in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinFunctions.html)
Use built-in shader functions in the Built-In Render Pipeline
