* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-include-directives.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Writing HLSL shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)
  * Include another HLSL file in a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SamplerStates.html)
Texture samplers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-programs-pragma-directives.html)
Pass information to the shader compiler in HLSL
# Include another HLSL file in a shader
In HLSL, `#include` directives are a type of [preprocessor directive](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-programs-pragma-directives.html). They instruct the compiler to include the contents of one HLSL file inside another. The file that they include is called an **include file**.
In Unity, regular `#include` directives work the same as in standard HLSL. For more information on regular `#include` directives, see the HLSL documentation: [include Directive](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-appendix-pre-include).
Unity also provides an additional, Unity-specific `#include_with_pragmas` directive. The `#include_with_pragmas` directive works the same as a regular `#include` directive, but it also allows you to use `#pragma` directives in the include file. This means that the `#include_with_pragmas` directive allows you to share `#pragma` directives between multiple files.
## Using the include_with_pragmas directive
**Note:** To use `#include_with_pragmas` directives, you must enable the [Caching Shader Preprocessor](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-compilation.html#preprocessor).
This example demonstrates how to use the Unity-specific `#include_with_pragmas` directive to enable a common workflow improvement: the ability to toggle **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) debugging on and off for multiple shaders, without needing to edit every shader source file every time.
The following line demonstrates the contents of the include file. It contains a single pragma directive that enables shader debugging:
```
// Comment out the following line to disable shader debugging
#pragma enable_d3d11_debug_symbols

```

In each shader that you want to debug, add an `#include_with_pragmas` directive that points to the include file. Put the directive near the other `#pragma` directives, like this:
```
// Example pragma directives
#pragma target 4.0
#pragma vertex vert
#pragma fragment frag

// Replace path-to-include-file with the path to the include file 
#include_with_pragmas "path-to-include-file"

// The rest of the HLSL code goes here

```

Now, when you want to toggle shader debugging on and off for all shaders that use the include file, you only need to change a single line in the include file. When Unity recompiles the shaders, it includes the amended line.
**Note:** If a shader file uses `#include` to import a file that contains an `#include_with_pragmas` directive, Unity ignores the `#pragma` directives in the file the `#include_with_pragmas` directive references.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SamplerStates.html)
Texture samplers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-programs-pragma-directives.html)
Pass information to the shader compiler in HLSL
