* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/use-editor.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
  * Use the editor


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/open-sprite-editor.html)
Open the sprite editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/automatic-slicing.html)
Automatic slicing
# Use the editor
The most direct way to use the editor is to identify the elements manually. If you click on the image, you will see a rectangular selection area appear with handles in the corners. You can drag the handles or the edges of the SpriteRect to resize it around a specific element. Having isolated an element, you can add another by dragging a new SpriteRect in a separate part of the image. You’ll notice that when you have a SpriteRect selected, a panel appears in the bottom right of the window.
The controls in the panel let you choose a name for the **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) graphic and set the position and size of the SpriteRect by its coordinates. A border width, for left, top, right and bottom can be specified in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel). The borders are useful when [9-Slicing](https://docs.unity3d.com/Manual/9-slice.html) sprites. There are also settings for the Sprite’s pivot, which Unity uses as the coordinate origin and main “anchor point” of the graphic. You can choose from a number of default SpriteRect-relative positions (for example, Center, Top Right, etc) or use custom coordinates.
The **Trim** button next to the Slice menu item will resize the SpriteRect so that it fits tightly around the edge of the graphic based on transparency.
**Note:** Borders are only supported for the UI system, not for the 2D **Sprite Renderer** A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteRenderer).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/open-sprite-editor.html)
Open the sprite editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/automatic-slicing.html)
Automatic slicing
