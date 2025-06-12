* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)
  * [Sprite editor](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/sprite-editor-landing.html)
  * [Custom outline](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-landing.html)
  * Custom outline editor reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/move-edges.html)
Move edges
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/custom-physics-shape-landing.html)
Custom physics shape
# Custom outline editor reference
Property | Function  
---|---  
**Snap** | Snap control points to the nearest **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel).  
**Outline Tolerance** | Use this slider to control how tightly and accurately the generated outline follows the outline of the **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) texture. At the minimum value (0), the Sprite Editor generates a basic outline around the Sprite. At the maximum value (1), the Sprite Editor generates an outline that follows the outline of the Sprite texture as closely as possible.  
**Generate** | When you click this button, Unity automatically creates an outline based on the **Outline Tolerance** value you set.  
**Copy** | After you have generated or set up a custom outline, click this **Copy** button to duplicate the custom outline. Leaving the Custom outline module or closing the Sprite Editor removes the copied outline from memory.  
**Paste** | Use this button to paste a copied outline to the currently selected Sprite. If you have not used the **Copy** function to copy an outline, this button is not available. To **Paste** a copied custom outline to another Sprite, in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow) select the Sprite while the Custom outline editor window is open. Then click the **Paste** button to paste the copied outline to the new Sprite. When you paste the outline, if a point in the outline is larger than the Sprite’s frame, Unity clamps the point to be inside the Sprite’s frame.  
**Paste All** | Use this button to paste a copied outline to all sprites in the Sprite Editor window, regardless of selection. If you have not used the **Copy** function to copy an outline, this button is unavailable. Use this function to apply the same outline to multiple sprites in the same Texture (such as when a Texture has its [Sprite Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html) set to ‘Multiple’). When you paste the outline, if a point in the outline exceeds the Sprite’s frame, Unity clamps the point to be inside that Sprite’s frame.  
**Revert** | Undoes any unsaved recent changes made in the editor window. To save changes, click **Apply** first.  
**Apply** | Select this button to save all changes made in the editor window.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-outline-editor/move-edges.html)
Move edges
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-editor/custom-physics-shape/custom-physics-shape-landing.html)
Custom physics shape
