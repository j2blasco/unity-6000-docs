* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-import.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [2D texture arrays](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html)
  * Create a 2D texture array


[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-arrays-introduction.html)
Introduction to 2D texture arrays
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-create.html)
Create a 2D texture array in a script
# Create a 2D texture array
To create a 2D texture array, import a flipbook texture. A flipbook texture contains multiple textures arranged in a grid.
Follow these steps:
  1. Import the texture into your project.
  2. In the **Project** window, select the texture. Unity displays the texture import settings in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window.
![An example flipbook texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TextureImporter-Flipbook-2D.jpg) An example flipbook texture.
  3. In the **Inspector** window, set **Texture Shape** to **2D Array**.
  4. Set **Columns** and **Rows** to the appropriate values for your flipbook texture.
  5. Select **Apply**.


Unity adds a texture array slice for each cell in the flipbook texture.
For more information, refer to [Import a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingTextures.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-arrays-introduction.html)
Introduction to 2D texture arrays
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray-create.html)
Create a 2D texture array in a script
