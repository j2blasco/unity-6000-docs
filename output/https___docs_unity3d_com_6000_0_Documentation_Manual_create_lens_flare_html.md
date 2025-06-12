* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/create-lens-flare.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html)
  * [Lens flares in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lens-flare-birp.html)
  * Create a lens flare


[](https://docs.unity3d.com/6000.0/Documentation/Manual/lens-flare-birp.html)
Lens flares in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-flare-elements.html)
Configuring Flare elements
# Create a lens flare
Create a flare and apply it to a **lens flare** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare) component, then configure it to be visible by cameras. 
**Note:** This workflow is compatible only with the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline). For similar functionality in other render pipelines, see [Lens flares and halos](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html).
## Apply a Flare asset
  1. Assign the Flare asset to a [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html) or a [Lens flare component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html). 
     * If you assign it to the **Flare** property of a [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html), Unity automatically tracks the position and direction of the Light and uses those values to configure the appearance of the lens flare.
     * If you assign it to the **Flare** property of a [Lens flare component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html), you can use the Lens Flare component to configure additional values for more precise control.
  2. If you want a [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) to see lens flares, select the camera then select **Add Component** > **Flare Layer**.
**Note:** The Flare Layer component has no properties.
  3. To see the lens flare effect in the **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView), enable the Effect toggle in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) View **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) and, in the drop-down, enable **Flares**.


## Create a lens flare with the Lens Flare component
  1. Create a new **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) (menu bar: **GameObject > Create Empty**). 
  2. In the Inspector, click **Add Component > Effects > Lens Flare**.
  3. Assign a [Flare Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Flare.html) to the **Flare** property.
  4. If you want a [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html) to see lens flares, select the camera then select **Add Component** > **Flare Layer**.
**Note:** The Flare Layer component has no properties.
  5. To see the lens flare effect in the **Scene View** , enable the Effect toggle in the Scene View toolbar and, in the drop-down, enable **Flares**.

![Enable the Effect toggle to view lens flares in the Scene view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LensFlare-FXButton.png) Enable the Effect toggle to view lens flares in the Scene view
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lens-flare-birp.html)
Lens flares in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-flare-elements.html)
Configuring Flare elements
