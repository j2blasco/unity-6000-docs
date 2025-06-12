* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/ShaderGraph.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * Create a 2D sprite lit Shader Graph in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DShadows.html)
Create shadows with Shadow Caster 2D in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-visual-effect-graph-compatibility.html)
Light a VFX Graph asset with 2D lights in URP
# Create a 2D sprite lit Shader Graph in URP
Create a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that reacts to 2D lights when applied to materials.
## Create a Sprite Lit Shader Graph
  1. Create a new asset by selecting **Assets > Create > Shader Graph > URP > Sprite Lit Shader Graph**. The Shader Graph asset is then created in the asset window.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2d-urp12-create-lit-shader.png)
  2. Double-click the new asset to open the **Shader Graph**.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2d-urp12-open-shader-graph.png)
  3. Create three **Sample Texture 2D** Nodes by right-clicking on the Shader Graph window and selecting **Create Node** , then search for and select the **Sample Texture 2D** option.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2d-urp12-create-node.png)
  4. Change the **Type** of one of the Nodes to **Normal**.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2d-urp12-3-node-normal.png)
  5. Attach the RGBA(4) **Output Slot** of the **Default Type** Nodes as shown below. Note that you should attach the **Normal Type** Node’s Output Slot to the **Normal(Tangent Space)(3)** Input Slot.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2d-urp12-attach-textures.png)
  6. Create three **Texture 2D** properties by selecting the **+** on the [Blackboard](http://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Blackboard.html), and then select **Texture 2D**. Name them ‘MainTex’, ‘MaskTex’, and ‘NormalMap’ for this example.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2d-urp12-3-create-texture-2D.png) ![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2d-urp12-3-three-textures.png)
  7. Drag each of the **Texture 2D** properties onto the editor window. Attach each of the properties to the **Input Slots** of the Sample Texture 2D Nodes as shown below. Note that the ‘NormalMap’ property must be attached to the **Normal Type** Node only.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2d-urp12-3-attach-properties.png)
  8. Select the **NormalMap** property, then in the **Graph**Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** set **Mode** to ****Normal Map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap)**.
  9. If your **sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) texture has transparency, attach the alpha (**A**) output of the **Base Color** texture to the **Alpha** input of the **Fragment** context.
  10. Select **Save Asset** to save the Shader.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2d-urp12-3-save-shader.png)


You can now apply the newly built Shader to materials.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DShadows.html)
Create shadows with Shadow Caster 2D in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-visual-effect-graph-compatibility.html)
Light a VFX Graph asset with 2D lights in URP
