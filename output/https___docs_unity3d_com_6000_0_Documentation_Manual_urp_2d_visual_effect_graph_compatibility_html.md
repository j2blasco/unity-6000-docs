* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-visual-effect-graph-compatibility.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * Light a VFX Graph asset with 2D lights in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/ShaderGraph.html)
Create a 2D sprite lit Shader Graph in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-optimize.html)
Optimizing 2D lights
# Light a VFX Graph asset with 2D lights in URP
Create a Visual Effect Graph asset and then light it with a 2D light by using [Shader Graphs](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest).
[Visual Effect Graph assets](https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@latest?subfolder=/manual/VisualEffectGraphAsset.html) are compatible with the 2D Renderer by using [Shader Graphs](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest). Follow the steps below to first [create a Visual Effect Graph asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-visual-effect-graph-compatibility.html#create-a-visual-effect-graph-asset) and then [light it with a 2D light](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-visual-effect-graph-compatibility.html#light-a-visual-effect-with-2d-lights).
## Prerequisites
Refer to the Visual Effect Graph’s [requirements and compatibility](https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@latest?subfolder=/manual/System-Requirements.html) for the required versions of packages for your Project.
## Create a Visual Effect Graph asset 
To create a Visual Effect Graph asset (VFX Asset):
  1. Create a new VFX asset by selecting **Assets > Create > Visual Effects > Visual Effect Graph**. 
  2. In the **Create new VFX Asset** window, select **Simple Loop**. Unity creates the VFX Asset in the **Asset** folder in the **Project** window. 
  3. Double-click the asset to open the VFX Graph.
  4. Replace the **Output Particle Unlit** node with an **Output Particle**Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Graph **Quad** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad)** node.
  5. In the **Output Particle Shader Graph Quad** node, select the **Shader Graph** picker (⊙).
  6. In the **Select Shader Graph Vfx Asset** window, select the eye icon to show hidden packages.
  7. Select **VFXSpriteLit** to light the visual effect.


## Light a Visual Effect with 2D lights 
To light a Visual Effect:
  1. To create a Visual Effect GameObject, select **GameObject** > **Visual Effects** > **Visual Effect**.
  2. In the **Visual Effect** properties, locate **Asset Template** and select the asset picker (circle). In the **Select VisualEffectAsset** window, select the VFX asset created earlier. 
  3. To light the Visual Effect, add [2D light](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Lights-2D-intro.html) to the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 

![An example of a VFX Graph asset with 2D lights.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/visual-effect-3.png) An example of a VFX Graph asset with 2D lights.
## Additional resources
  * [Using a Shader Graph in a visual effect](https://docs.unity3d.com/Packages/com.unity.visualeffectgraph@latest?subfolder=/manual/sg-working-with.html#using-a-shader-graph-in-a-visual-effect)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/ShaderGraph.html)
Create a 2D sprite lit Shader Graph in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-optimize.html)
Optimizing 2D lights
