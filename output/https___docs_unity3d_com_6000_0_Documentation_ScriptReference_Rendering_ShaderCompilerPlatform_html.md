* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerPlatform.html

# ShaderCompilerPlatform
enumeration
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Shader compiler used to generate player data shader variants.
In Unity, [shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderPrograms.html) are written in a variant of [HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShadingLanguage.html) language.  
  
Each [platform](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html) supports one or multiple graphics APIs. For example, Vulkan and Direct3D 12 are both supported in Windows. When building a standalone player, for each supported graphics API, Unity runs a corresponding shader compiler which generates the shader variants and cross-compiles the shader snippet into the shading language natively supported by the graphics API.  
  
Additional resources: [IPreprocessShaders.OnProcessShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessShaders.OnProcessShader.html), [Shader language](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShadingLanguage.html). 
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerPlatform.None.html) | Provide a reasonable value for non initialized variables.  
[D3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerPlatform.D3D.html) | Compiler used with Direct3D 11 and Direct3D 12 graphics API on Windows platforms.  
[GLES3x](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerPlatform.GLES3x.html) | Compiler used with OpenGL ES 3.x and WebGL 2.0 graphics APIs on Android, iOS, Windows and WebGL platforms.  
[Metal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerPlatform.Metal.html) | Compiler used with Metal graphics API on macOS, iOS and tvOS platforms.  
[OpenGLCore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerPlatform.OpenGLCore.html) | Compiler used with OpenGL core graphics API on macOS, Linux and Windows platforms.  
[Vulkan](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerPlatform.Vulkan.html) | Compiler used with Vulkan graphics API on Android, Linux and Windows platforms.  
[WebGPU](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerPlatform.WebGPU.html) | Compiler used with WebGPU graphics API.  
* * *
