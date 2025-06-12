* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/open-sprite-editor.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
  * Open the sprite editor


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
Sprite editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/use-editor.html)
Use the editor
# Open the sprite editor
To open the ****Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) Editor**:
  1. Select the 2D image you want to edit from the **Project View** _(Fig 1: Project View)_.   
**Note** : You can’t edit a sprite by selecting it in the **Scene View**.
  2. Click on the **Sprite Editor** button in the **Texture Import**Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** _(Fig 2: Texture Import Inspector)_ and the **Sprite Editor** displays _(Fig 3: Sprite Editor)_.


**Notes:**
  * You can only see the **Sprite Editor** button if the **Texture Type** on the image you have selected is set to **Sprite (2D and UI)**.
  * Set the **Sprite Mode** to **Multiple** in the ****Texture Import Inspector** An Inspector that allows you to define how your images are imported from your project’s `Assets` folder into the Unity Editor. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureImportInspector)** if your image has several elements.


Along with the composite image, you will see a number of controls in the bar at the top of the window. The slider at the top right controls the zoom, while the color bar button to its left chooses whether you view the image itself or its alpha levels. The right-most slider controls the pixilation (mipmap) of the Texture. Moving the slider to the left reduces the resolution of the Sprite Texture. The most important control is the **Slice** menu at the top left, which gives you options for separating the elements of the image automatically.
Select the **Apply** and **Revert** buttons to keep or discard any changes you have made in the Sprite Editor window respectively. You set these buttons to display a confirmation dialog before applying their effects in Unity’s [Preferences window](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html). In the Preferences window, go to **2D > Sprite Editor Window** to open the Sprite Editor window options.
Select the respective option to have a dialog appear after selecting **Apply** or **Revert** to confirm your selection, preventing accidental saving or discarding of changes made.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
Sprite editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/use-editor.html)
Use the editor
