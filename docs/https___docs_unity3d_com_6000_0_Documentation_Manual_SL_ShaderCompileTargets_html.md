* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Configure when and if Unity uses a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
  * Set a shader to require a shader model or GPU feature


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompilationAPIs.html)
Set a shader to require a graphics API or platform
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-require-package.html)
Set a shader to require a package
# Set a shader to require a shader model or GPU feature
You can use [`#pragma` directives](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PragmaDirectives.html) to indicate that a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) requires certain GPU features. At runtime, Unity uses this information to determine whether a shader program is compatible with the current hardware.
You can specify individual GPU features with the `#pragma require` directive, or specify a **shader model** with the `#pragma target` directive. A shader model is a shorthand for a group of GPU features; internally, it is the same as a `#pragma require` directive with the same list of features.
It is important to correctly describe the GPU features that your shader requires. If your shader uses features that are not included in the list of requirements, this can result in either compile time errors, or in devices failing to support shaders at runtime. 
## Default behavior
By default, Unity compiles shaders with `#pragma require derivatives`, which corresponds to `#pragma target 2.5`.
## Special requirements for shader stages
If your shader defines certain shader stages, Unity automatically adds items to the list of requirements.
  * If a shader defines a geometry stage (with `#pragma geometry`), Unity automatically adds `geometry` to the list of requirements.
  * If a shader defines a tessellation stage (with `#pragma hull` or `#pragma domain`), Unity automatically adds `tessellation` to the list of requirements.


If the list of requirements (or the equivalent target value) does not already include these values, Unity displays a warning message when it compiles the shader, to indicate that it has added these requirements. To avoid seeing this warning message, explicitly add the requirements or use an appropriate target value in your code.
## Specifying GPU features or a shader model
To specify required features, use the `#pragma require` directive, followed by a list of space-delimited values. For example:
```
#pragma require integers mrt8

```

You can also use the `#pragma require` directive followed by a colon and a list of space-delimited [shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html). This means that the requirement applies only to variants that are used when any of the given keywords are enabled.
For example:
```
#pragma require integers mrt8 : EXAMPLE_KEYWORD OTHER_EXAMPLE_KEYWORD

```

You can use multiple `#pragma require` lines. In this example, the shader requires `integers` in all cases, and `mrt8` if EXAMPLE_KEYWORD is enabled.
```
#pragma require integers
#pragma require integers mrt8 : EXAMPLE_KEYWORD

```

To specify a shader model, use `#pragma target` directive. For example:
```
#pragma target 4.0

```

You can also use the `#pragma target` directive followed by a list of space-delimited [shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html). This means that the requirement applies only to variants that are used when any of the given keywords are enabled.
For example:
```
#pragma target 4.0 EXAMPLE_KEYWORD OTHER_EXAMPLE_KEYWORD

```

**Note:** The syntax for specifying keywords for `#pragma require` and `#pragma target` is slightly different. When you specify keywords for `#pragma require`, you use a colon. When you specify keywords for `#pragma target`, you do not use a colon.
## DirectX12 (DX12), Vulkan and Metal graphics APIs features
**Note:** If you use the following shader keywords, Unity compiles shaders using the DXC compiler. DXC support in Unity is experimental, not supported on all platforms, and not ready for production use.
If you use the DirectX12 (DX12), Vulkan or Metal graphics APIs, you can use a shader keyword to target the following GPU features:
  * Support for 16-bit data types.
  * Support for wave operations in [compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html).


Use the following syntax:
```
#pragma multi_compile _ <keyword>

```

You don’t need to add a `pragma require` directive.
Unity then does the following:
  * Uses a compatible shader compiler and turns on compiler flags related to the feature.
  * Automatically compiles both a shader variant with the keyword on and a shader variant with the keyword off.
  * At runtime, automatically checks if the hardware supports the feature and selects the correct variant.


You can use an `#if` statement to make parts of your shader code conditional on whether the GPU supports the feature.
### Keywords
multi-compile keyword | GPU feature | Keyword for conditional shader code  
---|---|---  
`UNITY_DEVICE_SUPPORTS_NATIVE_16BIT` | Supports 16-bit data types. If you use this keyword, the layout of shader buffers might change, because data types such as `half` and `min16float` convert to 16-bit. | `UNITY_DEVICE_SUPPORTS_NATIVE_16BIT`  
`UNITY_DEVICE_SUPPORTS_WAVE_ANY` | Supports wave operations of any size. Use this keyword only if you use wave operations where the size of the waves doesn’t matter. | `UNITY_HW_SUPPORTS_WAVE`  
`UNITY_DEVICE_SUPPORTS_WAVE_8` | Supports wave operations with a wave size of 8. | `UNITY_HW_SUPPORTS_WAVE`  
`UNITY_DEVICE_SUPPORTS_WAVE_16` | Supports wave operations with a wave size of 16. | `UNITY_HW_SUPPORTS_WAVE`  
`UNITY_DEVICE_SUPPORTS_WAVE_32` | Supports wave operations with a wave size of 32. | `UNITY_HW_SUPPORTS_WAVE`  
`UNITY_DEVICE_SUPPORTS_WAVE_64` | Supports wave operations with a wave size of 64. | `UNITY_HW_SUPPORTS_WAVE`  
`UNITY_DEVICE_SUPPORTS_WAVE_128` | Supports wave operations with a wave size of 128. | `UNITY_HW_SUPPORTS_WAVE`  
If you use a keyword that targets a specific wave size, Unity sets a `UNITY_HW_WAVE_SIZE` define to the same wave size so you can use it in shader code.
Refer to [Declaring and using shader keywords in HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html) for more information.
## Additional resources
  * [HLSL pragma directives reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PragmaDirectives.html)
  * [HLSL pragma target command reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pragma-target.html)
  * [HLSL pragma require command reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pragma-require.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompilationAPIs.html)
Set a shader to require a graphics API or platform
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-require-package.html)
Set a shader to require a package
