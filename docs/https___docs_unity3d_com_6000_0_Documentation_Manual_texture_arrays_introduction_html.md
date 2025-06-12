* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/texture-arrays-introduction.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [2D texture arrays](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html)
  * Introduction to 2D texture arrays


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html)
2D texture arrays
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-import.html)
Create a 2D texture array
# Introduction to 2D texture arrays
A texture array is a collection of 2D textures with the same size, format, and flags. The individual texture in the array are called slices or layers. In a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), you can use an index to sample each slice. 
Texture arrays are useful for implementing custom **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) rendering systems or other special effects where you need an efficient way to access many textures of the same size and format. 
## Platform support
Texture arrays are supported if the platform supports one of the following graphics APIs:
  * DirectX11 and DirectX12 (Windows)
  * Metal (iOS, macOS)
  * OpenGL Core (macOS, Linux)
  * OpenGL ES 3.0 (Android, WebGL 2.0)
  * Vulkan (Windows, Linux)


To check if a platform supports texture arrays, use the [SystemInfo.supports2DArrayTextures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supports2DArrayTextures.html) API at runtime.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html)
2D texture arrays
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-import.html)
Create a 2D texture array
