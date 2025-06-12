* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/SecondaryTextures.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * [Blend Modes in 2D lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-blending.html)
  * Add normal map and mask textures to a sprite in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-masking.html)
Masking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/HDREmulationScale.html)
HDR emulation scale
# Add normal map and mask textures to a sprite in URP
Assign **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) and mask textures to **sprites** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) by using the [Sprite Editor](https://docs.unity3d.com/Manual/SpriteEditor.html)’s [Secondary Textures](https://docs.unity3d.com/Manual/SpriteEditor-SecondaryTextures.html) module to create advanced lighting effects with 2D lights. 
First select a Sprite, and open the [Sprite Editor](https://docs.unity3d.com/Manual/SpriteEditor.html) from its **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. Then select the **Secondary Textures** module from the drop-down menu at the top left of the editor window.
## Adding a Secondary Texture
In the Secondary Textures editor, select a Sprite to add Secondary Textures to. With a Sprite selected, the **Secondary Textures** panel appears at the bottom right of the editor window. The panel displays the list of Secondary Textures currently assigned to the selected Sprite. To add a new Secondary Texture to the Sprite, select + at the bottom right of the list.
This adds a new entry to the list with the ‘Name’ and ‘Texture’ boxes. Enter a custom name into the Name box, or select the arrow to the right of the Name box to open the drop-down list of suggested names. These suggested names can include suggestions from installed Unity packages, as the Secondary Textures may need to have specific names to interact correctly with the **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in these packages to produce their effects.
The 2D Lights package suggests the names ‘MaskTex’ and ‘NormalMap’. Select the name that matches the function of the selected Texture - select ‘MaskTex’ for a masking Texture, or ‘NormalMap’ for a normal map Texture. Naming these Textures correctly allow them to interact with the 2D Lights Shaders to properly produce the various lighting effects.
To select the Texture Asset for this Secondary Texture entry, drag the Texture Asset directly onto the Texture field, or open the **Object Picker** window by selecting the circle to the right of the Texture box.
Secondary Textures are sampled with the same UV coordinates as the Texture of the selected Sprite. Align the Secondary Textures with the main Sprite Texture to ensure that additional Texture effects are displayed correctly.
![The main texture and the secondary texture with the same position and alignment.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/ST_Align.png) The main texture and the secondary texture with the same position and alignment.
To preview the Secondary Texture in the **Sprite Editor** window, select an entry in the list. This automatically hides the Sprite’s main Texture. Click outside of the Secondary Textures list to deselect the entry, and the main Sprite Texture becomes visible again.
## Deleting a Secondary Texture
To delete a Secondary Texture, select it from the list and then select - at the bottom right of the window. This automatically removes the entry.
## Applying
Select **Apply** at the top of the editor to save your entries. Invalid entries without a Name or an assigned Texture are automatically removed when changes are applied.
## Additional resources
  * [Work with sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Use the Sprite Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/use-editor.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-masking.html)
Masking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/HDREmulationScale.html)
HDR emulation scale
