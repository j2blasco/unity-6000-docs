* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-custom-effect-render-objects.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Adding pre-built effects via Renderer Features in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature-landing.html)
  * Example of creating a custom rendering effect via the Render Objects Renderer Feature in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html)
Add a Renderer Feature to a URP Renderer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/renderer-feature-render-objects.html)
Render Objects Renderer Feature reference for URP
# Example of creating a custom rendering effect via the Render Objects Renderer Feature in URP
URP draws objects in the **DrawOpaqueObjects** and **DrawTransparentObjects** passes. You might need to draw objects at a different point in the frame rendering, or interpret and write rendering data (like depth and stencil) in alternate ways. The [Render Objects Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/renderer-feature-render-objects.html) lets you do such customizations by letting you draw objects on a certain layer, at a certain time, with specific overrides.
The example on this page describes how to create a custom rendering effect with the Render Objects Renderer Feature.
## Example overview
The example on this page demonstrates how to implement the following effect:
  * There is a character in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
![Character](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/character.png) Character
  * When the character goes behind **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), Unity draws the character silhouette with a different Material.
![Character goes behind GameObjects](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/character-goes-behind-object.gif) Character goes behind GameObjects


## Prerequisites
This example requires the following:
  * A Unity project with the URP package installed.
  * The **Scriptable Render Pipeline Settings** property refers to a URP asset (**Project Settings** > **Graphics** > **Scriptable Render Pipeline Settings**).


## Create example Scene and GameObjects
To follow the steps in this example, create a new scene with the following GameObjects:
  1. Create a Cube. Set its **Scale** values so that it looks like a wall.
![Cube that represents a wall](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-cube-wall.png) Cube that represents a wall
  2. Create a Material and assign it the `Universal Render Pipeline/Lit` **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). Select the base color (for example, red). Call the Material `Character`.
  3. Create a basic character and assign it the Character Material. In this example, the character consists of three capsules: the big capsule in the center represents the body, and the two smaller capsules represent the hands.
![The character consisting of three capsules](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/character-views-side-top-persp.png) The character consisting of three capsules
To make it easier to manipulate the character in the scene, add the three Capsules as child GameObjects under the Character GameObject.
![Character objects in Hierarchy](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/character-in-hierarchy.png) Character objects in Hierarchy
  4. Create a Material and assign it the `Universal Render Pipeline/Unlit` shader. Select the base color that you would like the character to have when it’s behind GameObjects (for example, blue). Call the Material `CharacterBehindObjects`.


Now you have the setup necessary to follow the steps in this example.
## Example implementation
This section assumes that you created a scene as described in section [Example scene and GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-custom-effect-render-objects.html#example-objects).
The example implementation uses two Render Objects Renderer Features: one to draw parts of the character that are behind other GameObjects, and another one to draw the parts of the character that are in front of other GameObjects.
### Create a Renderer Feature to draw the character behind GameObjects
Follow these steps to create a Renderer Feature to draw the character behind GameObjects.
  1. Select a URP Renderer.
![Select a URP Renderer](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-select-urp-renderer.png) Select a URP Renderer
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), click **Add Renderer Feature** and select **Render Objects**.
![Add Render Object Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-add-rend-obj.png) Add Render Object Renderer Feature
Select the **Name** field and enter the name of the new Renderer Feature, for example, **DrawCharacterBehind**.
  3. This example uses Layers to filter the GameObjects to render. Create a new Layer and call it **Character**.
![Create new Layer called Character](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-new-layer-character.png) Create new Layer called Character
  4. Select the **Character** GameObject and assign it to the `Character` Layer. To do this, open the Layer drop down and select `Character`. ![Assign Character GameObject to Character Layer](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-assign-character-gameobject-layer.png)
  5. In the `DrawCharacterBehind` Renderer Feature, in **Filters** > **Layer Mask** , select `Character`. With this setting, this Renderer Feature renders GameObjects only in the Layer `Character`.
  6. In **Overrides** > **Material** , select the `CharacterBehindObjects` Material.
The Renderer Feature overrides the Material of a GameObject with the selected Material.
![Layer Mask, Material Override](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-change-layer-override-material.png) Layer Mask, Material Override
  7. The intended behavior is that the Renderer Feature renders the character with the `CharacterBehindObjects` Material only when the character is behind other GameObjects.
To achieve this, select the **Depth** check box, and set the **Depth Test** property to **Greater**.
![Set Depth Test to Greater](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-depth-greater.png) Set Depth Test to Greater


With these settings, Unity renders the character with the `CharacterBehindObjects` Material only when the character is behind another GameObject. However, Unity also renders parts of the character using the `CharacterBehindObjects` Material, because some parts of the character occlude the character itself.
![Unity renders parts of the character using the CharacterBehindObjects Material](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/character-depth-test-greater.gif) Unity renders parts of the character using the `CharacterBehindObjects` Material
### Create an extra Renderer Feature to avoid the self see-through effect
The settings in the previous section result in the self see-through effect for the following reason:
  * When performing the Opaque rendering pass of the URP Renderer, Unity renders all GameObjects belonging to the character with the `Character` Material and writes depth values to the **Depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer). This happens before Unity starts executing the `DrawCharacterBehind` Renderer Feature, because, by default, new Render Objects Renderer Features have the value **AfterRenderingOpaques** in the **Event** property.
The **Event** property defines the injection point where Unity injects Render Passes from the Render Objects Renderer Feature. The event when URP Renderer draws GameObjects in the **Opaque**Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask)** is the **BeforeRenderingOpaques** event.
  * When executing the `DrawCharacterBehind` Renderer Feature, Unity performs the depth test using the condition specified in the **Depth Test** property. In the following screenshot, a bigger capsule occludes part of the smaller capsule, and the depth test passes for that part of the smaller capsule. The Renderer Feature overrides the Material for that part.
![Self see-through effect](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-depth-greater-see-through.png) Self see-through effect


The following steps describe how to avoid such behavior and ensure that Unity draws all parts of the character with proper Materials.
  1. In the URP asset, in **Filtering** > **Opaque Layer Mask** , clear the check mark next to the `Character` Layer.
![Clear the check mark next to the Character Layer](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-in-urp-asset-clear-character.png) Clear the check mark next to the `Character` Layer
Now Unity does not render the character unless it’s behind a GameObject.
![Unity does not render the character unless its behind an object](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-character-only-behind.png) Unity does not render the character unless it’s behind an object
  2. Add a new Render Objects Renderer Feature, and call it `Character`.
  3. In the `Character` Renderer Feature, in **Filters** > **Layer Mask** , select the `Character` Layer.
![Set Layer Mask Filter to Character Layer](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-render-objects-character.png) Set Layer Mask Filter to Character Layer
Now Unity renders the character with the `Character` Material even when the character is behind GameObjects.
This happens because the `DrawCharacterBehind` Renderer Feature writes values to the depth buffer. When Unity executes the `Character` Renderer Feature, the **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) on the character appear to be in front of the pixels that Unity has drawn previously, and Unity draws on top of those pixels.
  4. In the `DrawCharacterBehind` Renderer Feature, In **Overrides** > **Depth** , clear the **Write Depth** check box. With this setting, the `DrawCharacterBehind` Renderer Feature does not make changes to the depth buffer and the `Character` Renderer Feature does not draw the character when it’s behind GameObjects.
![Clear Write Depth](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/rendobj-render-objects-no-write-depth.png) Clear Write Depth


The example is complete. When the character goes behind GameObjects, Unity draws the character silhouette with the `CharacterBehindObjects` Material.
![Character goes behind objects](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/how-to-render-objects/character-goes-behind-object.gif) Character goes behind objects
With the extra `Character` Renderer Feature, Unity renders GameObjects as follows:
  1. URP Renderer does not render the `Character` GameObject in the **BeforeRenderingOpaques** event, because the `Character` Layer is excluded from the **Opaque Layer Mask** list.
  2. The `DrawCharacterBehind` Renderer Feature draws parts of the character that are behind other GameObjects. This happens in the **AfterRenderingOpaques** event.
  3. The `Character` Renderer Feature draws parts of the character that are in front of other GameObjects. This happens in the **AfterRenderingOpaques** event, and after executing the `DrawCharacterBehind` Renderer Feature.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html)
Add a Renderer Feature to a URP Renderer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/renderer-feature-render-objects.html)
Render Objects Renderer Feature reference for URP
