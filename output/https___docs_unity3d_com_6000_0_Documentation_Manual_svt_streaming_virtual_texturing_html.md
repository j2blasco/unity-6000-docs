* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/svt-streaming-virtual-texturing.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Texture optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureLoading.html)
  * Streaming Virtual Texturing


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SparseTextures.html)
Sparse Textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-requirements-compatibility.html)
Streaming Virtual Texturing requirements and compatibility
# Streaming Virtual Texturing
This feature is experimental and not ready for production use. The feature and documentation might be changed or removed in the future.
Streaming Virtual Texturing (SVT) is a feature that reduces GPU memory usage and texture loading times when you have many high resolution textures in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). It splits textures into tiles, and progressively uploads these tiles to GPU memory when they are needed.
SVT lets you set a fixed memory cost. For full texture quality, the required GPU cache size depends mostly on the frame resolution, and not the number or resolution of textures in the Scene. The more high resolution textures you have in your Scene, the more GPU memory you can save with SVT.
The workflow requires no additional import time, no additional build step, and no additional streaming files. You work with regular Unity Textures in the Unity Editor.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SparseTextures.html)
Sparse Textures
[](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-requirements-compatibility.html)
Streaming Virtual Texturing requirements and compatibility
