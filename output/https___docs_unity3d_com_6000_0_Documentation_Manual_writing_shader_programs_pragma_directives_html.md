* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-programs-pragma-directives.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Writing HLSL shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)
  * Pass information to the shader compiler in HLSL


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-include-directives.html)
Include another HLSL file in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html)
Writing shaders for different graphics APIs
# Pass information to the shader compiler in HLSL
In HLSL, you can use the following types of preprocessor directive to provide information to the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) compiler:
  * `#pragma`
  * `#define_for_platform_compiler`


## Pragma directives
`#pragma` directives provide additional information to the shader compiler that isn’t covered by other types of preprocessor directive.
You can put `#pragma` directives anywhere in your HLSL code, but it is a common convention to put them at the start, like this:
```
#pragma target 3.0
#pragma exclude_renderers vulkan
#pragma vertex vert
#pragma fragment frag

// The rest of your HLSL code goes here


```

### Limitations
There are some limitations around the use of `#pragma` directives:
  * You can use `#pragma`directives inside conditional (`#if`) directives if the expression depends only on: 
    * Any custom `#define` directives in your own code
    * The following platform keywords: `SHADER_API_MOBILE`, `SHADER_API_DESKTOP`, `UNITY_NO_RGBM`, `UNITY_USE_NATIVE_HDR`, `UNITY_FRAMEBUFFER_FETCH_AVAILABLE`, `UNITY_NO_CUBEMAP_ARRAY`
    * The `UNITY_VERSION` macro
  * You can only use Unity-specific `#pragma` directives in `.shader` files, and in files that you include with the `#include_with_pragmas` directive. Unity does not support them in files that you include with the `#include` directive; the compiler ignores them.
  * You can only use standard HLSL `#pragma` directives in files that you include with the `#include` directive. Unity does not support them in `.shader` files, or in files that you include with an `#include_with_pragmas` directive; the compiler ignores them.


**Note:** If a shader file uses `#include` to import a file that contains an `#include_with_pragmas` directive, Unity ignores the `#pragma` directives in the file the `#include_with_pragmas` directive references.
## Use a define_for_platform_compiler directive
Use a `#define_for_platform_compiler` directive in your shader code to send a `#define` directive to the shader compiler.
For example, `#define_for_platform_compiler EXAMPLE_SYMBOL` sends a `#define EXAMPLE_SYMBOL` directive to the shader compiler that defines a symbol called `EXAMPLE_SYMBOL`. Refer to external shader compiler documentation, for example [Microsoft’s documentation on the FXC compiler](https://learn.microsoft.com/en-us/windows/win32/direct3dtools/fxc), for more information about symbols that shader compilers use.
The Unity preprocessor doesn’t use symbols you define with `#define_for_platform_compiler`, so you can’t use the symbols in your own shader code. For example, in the above example, if you add shader code inside an `#if (EXAMPLE_SYMBOL)` statement, the code won’t run.
## Additional resources
  * [Shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-compilation.html)
  * [HLSL pragma directives reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PragmaDirectives.html)
  * [HLSL pragma target command reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pragma-target.html)
  * [HLSL pragma require command reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pragma-require.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-include-directives.html)
Include another HLSL file in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html)
Writing shaders for different graphics APIs
