* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * Shader methods in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-reconstruct-world-position.html)
Reconstruct world space positions in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-import.html)
Import a file from the URP shader library
# Shader methods in URP
Resources for the library of High-Level **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Language (HLSL) shader files that contain helper methods.
**Page** | **Description**  
---|---  
[Import a file from the URP shader library](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-import.html) | Use the `#include` directive in HLSL to import a URP shader file.  
[Transform positions in a custom URP shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-transformations.html) | Transform vertex, fragment, normal and tangent positions between coordinate spaces.  
[Use the camera in a custom URP shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-camera.html) | Get the position and direction of the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera).  
[Use lighting in a custom URP shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-lighting.html) | Get the lights in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), and calculate lighting.  
[Use indirect lighting in a custom URP shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-indirect-lighting.html) | Use **reflection probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) or Adaptive Probe Volumes in a URP shader.  
[Use shadows in a custom URP shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-shadows.html) | Get shadow data from lights in the scene, and calculate shadows.  
[ShaderLab Pass tags in URP reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html) | Find the Pass tags URP uses to determine which shader passes to run in different parts of the **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).  
## Additional resources
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * [Upgrade custom shaders for URP compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/birp-urp-custom-shader-upgrade-guide.html)
  * [HLSL in Unity](https://docs.unity3d.com/Manual/SL-ShaderPrograms.html)
  * [Shader methods in Scriptable Render Pipeline (SRP) Core](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/built-in-shader-methods.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-reconstruct-world-position.html)
Reconstruct world space positions in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-import.html)
Import a file from the URP shader library
