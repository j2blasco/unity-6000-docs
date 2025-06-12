* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-move-elements-at-runtime.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Support for runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-runtime-ui.html)
  * [UI Toolkit runtime examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-examples.html)
  * Move elements at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-examples.html)
UI Toolkit runtime examples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
Work with text
# Move elements at runtime
This example demonstrates how to dynamically set the position of a **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) at runtime. The recommended best practice to move elements at runtime is to use `style.translate` and set the `DynamicTransform` usage hint on the moving element. This approach is optimal for performance as it avoids dirtying the layout and keeps updates confined to the transform stage. For more information, refer to [Optimize performance of moving elements at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html).
## Example overview
This example creates a **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). The prefab represents a non-player character (NPC) that moves randomly within a specified range. The NPC has a name tag that follows it and scales based on the distance from the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera).
![Move elements at runtime](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uitk/move-elements-runtime.gif) Move elements at runtime
You can find the completed files that this example creates in this [GitHub repository](https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples/tree/master/move-elements-at-runtime).
## Prerequisites
This guide is for developers familiar with the Unity Editor, UI Toolkit, and C# scripting. Before you start, get familiar with the following:
  * [Structure UI with UXML](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html)
  * [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html)
  * [USS transform](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transform.html)
  * [`UsageHints.DynamicTransform`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.DynamicTransform.html)


## Create the UI container
Create a UXML in your project and define a VisualElement within it. The VisualElment acts as the parent container for any child elements that you plan to move dynamically during runtime.
  1. Create a Unity project with any template.
  2. In the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), create a folder named `UI` to store the UXML and USS files.
  3. In the `UI` folder, create a UXML file named `NameTagContainer.uxml`.
  4. Double-click the `NameTagContainer.uxml` file to open it in the UI Builder.
  5. Add a VisualElement to the **Hierarchy** panel and name it as `BaseContainer`.
  6. Save your changes.


The finished `NameTagContainer.uxml` file looks like this:
```
<engine:UXML xmlns:engine="UnityEngine.UIElements" >
    <engine:VisualElement name="BaseContainer" style="flex-grow: 1;" />
</engine:UXML>

```

## Create the name tag UXML template
Create a USS file to style the name tag and a UXML file to define the name tag template. The name tag template is a Label element that displays the name of the NPC. The name tag follows the NPC in the Scene.
  1. In the `UI` folder, create a USS file named `NameTag.uss` with the following content:
```
 #NameTag {
     /* This sets the position of the Label element to be absolute, rather than relative to the parent container. */
     position: absolute;
     /* This ensures that the pivot point of the Label element is centered, rather than in the top left corner.*/
     translate: -50% -50%;
     -unity-font-style: bold;
     color: rgb(181, 210, 248);
     -unity-text-outline-width: 1px;
     -unity-text-outline-color: rgb(11, 60, 123);
 }

```

  2. In the `UI` folder, create a UXML file named `NameTag.uxml`.
  3. Double-click the `NameTag.uxml` file to open it in the UI Builder.
  4. Add a Label to the **Hierarchy** panel and name it `NameTag`.
  5. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** panel, do the following:
     * Set **Text** to `NPC`. This value represents the name of the NPC.
     * Set **Picking Mode** to `Ignore`. This prevents the Label element from responding to mouse events, which is more optimal for performance.
  6. In the **StyleSheets** panel, select **+** > **Add Existing USS**.
  7. Follow the instruction to add the `NameTag.uss` file.
  8. Check the Label element in the **Viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport). The `translate: -50% -50%` style centers the pivot point of the Label element, causing it to appear in the top-left corner of the Viewport. This is expected behavior. The name tag will be positioned relative to the NPC **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the scene.
![NameTag in the Viewport](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uitk/name-tag-viewport.png)
  9. Save your changes.


The finished `NameTag.uxml` file might look like this:
```
<engine:UXML xmlns:engine="UnityEngine.UIElements">
    <Style src="NameTag.uss" />
    <engine:Label text="NPC" name="NameTag" picking-mode="Ignore" />
</engine:UXML>

```

## Create the random movement script
Create a `RandomMovement` class that handles random movement of the NPC prefab. The NPC moves within a specified range and changes direction when it reaches the boundary. 
Set the `DynamicTransform` usage hint on the moving element to optimize performance.
**Note** : The recommended best practice is to apply the usage hint to the transformed element which in this case is the name tag template container rather than the child label.
  1. In the Project window, create a folder named `Scripts` to store the C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
  2. In the `Scripts` folder, create a C# script named `RandomMovement.cs` with the following content:

```
using UnityEngine;
using Random = UnityEngine.Random;

public class RandomMovement : MonoBehaviour
{
    public float moveSpeed;

    public float movementRange;

    public Vector3 targetPosition;

    private float m_PositionY;

    // Initialize the starting position and target position of the GameObject.
    void Start()
    {
        m_PositionY = transform.position.y;
        targetPosition = new Vector3(0, m_PositionY, 0);
    }

    // Updates the position of the GameObject at fixed intervals.
    // Move the GameObject towards the target position, and sets a new random target position when the current target is reached.
    void FixedUpdate()
    {
        if (transform.position != targetPosition)
        {
            transform.position = Vector3.MoveTowards(transform.position, targetPosition, moveSpeed * Time.deltaTime);
        }
        else
        {
            targetPosition = new Vector3(Random.Range(-movementRange, movementRange), m_PositionY, Random.Range(-movementRange, movementRange));
        }
    }
}

```

## Create the moving name tag script
Create a `MovingNameTag` class that manages the position and scale of the name tag. The name tag follows the NPC GameObject in the scene. The name tag scales based on the distance from the Camera and is culled when it is too far away or behind the camera. 
  * In the `Scripts` folder, create a C# script named `MovingNameTag.cs` with the following content:

```
using System;
using UnityEngine;
using UnityEngine.UIElements;

public class MovingNameTag : MonoBehaviour
{
    [SerializeField]
    VisualTreeAsset m_NameTagTemplate;

    [SerializeField]
    UIDocument m_BaseContainerDocument;

    [SerializeField]
    Transform m_UITransform;

    [SerializeField]
    float m_ScaleMultiplier;

    [SerializeField]
    float m_DistanceCullingRange;

    VisualElement m_Root;
    VisualElement m_BaseContainer;
    VisualElement m_NpcNameTag;
    
    Camera m_MainCamera;
    
    void Awake()
    {
        m_MainCamera = Camera.main;
        
        m_BaseContainer = m_BaseContainerDocument.rootVisualElement.Q<VisualElement>("BaseContainer");
        
        m_NpcNameTag = m_NameTagTemplate.Instantiate();

        // Set DynamicTransform hint on the moving element to optimize performance.
        m_NpcNameTag.usageHints = UsageHints.DynamicTransform;
        m_BaseContainer.Add(m_NpcNameTag);
        m_NpcNameTag.style.position = new StyleEnum<Position>(Position.Absolute);
    }

    void Update()
    {
        SetNameTagPositionAndScale();
    }

    void SetNameTagPositionAndScale()
    {
        var cameraSpaceLocation = GetCameraSpaceLocation(m_UITransform);
        
        // Use style.translate to set the position of the name tag.
        m_NpcNameTag.style.translate = new Translate(cameraSpaceLocation.x, cameraSpaceLocation.y);

        // Get distance of NPC from camera.
        var distance = Vector3.Distance(m_UITransform.position, m_MainCamera.transform.position);
        
        // Calculate 1/distance so the name tag get smaller as the distance gets bigger.
        var scale = 1 / distance * m_ScaleMultiplier;

        m_NpcNameTag.style.scale = new Scale(new Vector2(scale, scale));
        
        // Display name tag based on whether it's in front of the camera and within culling range.
        if (cameraSpaceLocation.z < 0 || distance > m_DistanceCullingRange)
        {
            m_NpcNameTag.style.display = DisplayStyle.None;
        }
        else
        {
            m_NpcNameTag.style.display = DisplayStyle.Flex;
        }
    }

    Vector3 GetCameraSpaceLocation(Transform objectTransform)
    {
        // Get the size of the parent visual element of the name tag.
        var containerSize = m_BaseContainer.layout.size;
        var screenPoint = m_MainCamera.WorldToViewportPoint(objectTransform.position);
        var output = new Vector3(screenPoint.x * containerSize.x, (1 - screenPoint.y) * containerSize.y, screenPoint.z);
        
        return output;
    }
}

```

## Create the sort elements script
Create a `SortElements` class that sorts the name tags based on their scale, which is based on the distance of the objects they follow.
  * In the `Scripts` folder, create a C# script named `SortElements.cs` with the following content:

```
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

public class SortElements : MonoBehaviour
{
    [SerializeField]
    UIDocument m_MovingElements;

    VisualElement m_BaseContainer;

    MovingNameTag[] m_MovingNameTags;
    
    void Start()
    {
        m_MovingNameTags = FindObjectsByType<MovingNameTag>(FindObjectsSortMode.None);
        m_BaseContainer = m_MovingElements.rootVisualElement.Q<VisualElement>("BaseContainer");
    }

    void Update()
    {
        m_BaseContainer.Sort(CompareOrder);
    }

    static int CompareOrder(VisualElement x, VisualElement y)
    {
        // Compare the scale of the visual elements in the base container, which is
        // determined by the distance of the object it follows in the MovingNameTag component
        return x.style.scale.value.value.x.CompareTo(y.style.scale.value.value.x);
    }
}

```

## Set up the scene basics
Set up the scene with a floor and a UI Document GameObject. A floor is a [Plane GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html) that represents the floor of the scene.
The UI Document GameObject is the UI that contains the visual elements that moves at runtime. The UI contains the `SortElements` component, which sorts the name tags based on their scale.
  1. In the SampleScene, add a Plane GameObject named `Floor`. 
  2. Add a material to the floor.
  3. In the **Hierarchy** window, select **UI Toolkit** > **UIDocument** and name it as `UI`.
  4. In the **Inspector** window of the UI Document GameObject, do the following:
     * Set the **Source Asset** to `NameTagContainer`.
     * Add the `SortElements` component.
  5. In the **Sort Elements** component field, set **Moving Elements** to `UI`. This makes the `SortElements` component reference the UI Document Component, which in turn references the `NameTagContainer` source asset.


## Set up the NPC prefab
Create an NPC prefab that moves randomly within a specified range. It contains three child GameObjects:
  * A Capsule GameObject that represents the NPC
  * A UI Document GameObject called `UI_NameTag` that represents the name tag that follows the NPC
  * An empty GameObject called `UI_Transform` that represents the position of the name tag


The `UI_Transform` GameObject acts as a reference point for the name tag. The `MovingNameTag` component moves the name tag based on the position of the `UI_Transform` GameObject. This setup allows for better organization and flexibility. If you need to adjust the position of the name tag, you can simply modify the `UI_Transform` GameObject’s position without affecting the NPC GameObject or other components.
  1. In the SampleScene, create an empty GameObject named `NPC`. 
  2. In the **Inspector** window of the `NPC` GameObject, add the `RandomMovement` component. This component manages the random movement of the NPC.
  3. In the **Random Movement** component field, do the following:
  4. Set the **Speed** to `2`. This value determines the speed at which the NPC moves.
  5. Set the **Range** to `10`. This value determines the range within which the NPC moves.


**Note** : The **Random Movement** component contains a ****Target Position** A joint property to set the target position that the joint’s drive force should move it to. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TargetPosition)** field that represents the NPC’s next target position, which is set randomly in the script. This field is primarily for debugging purposes and does not need to be manually set.
## Set up children of the NPC prefab
The NPC prefab contains three child GameObjects: a Capsule GameObject and two GameObjects.
The Capsule GameObject represents the NPC in the scene. One GameObject represents the name tag that follows the NPC. The second GameObject represents the position of the name tag relative to the NPC. This GameObject acts as a reference point or anchor for the name tag, defining where the name tag is positioned in relation to the NPC.
  1. Right-click the `NPC` GameObject and select **Create Empty** to add a child GameObject and name it `UI_NameTag`.
  2. Add the `MovingNameTag` component to the `UI_NameTag` GameObject. This component manages the position and scale of the name tag.
  3. In the **Moving Name Tag** component field, do the following:
     * Set the **Name Tag Template** to `NameTag`.
     * Set the **Base Container Document** to `UI (UI Document)`. This value represents the container for the UI elements that are moved at runtime.
     * Set the **UI Transform** to `UI_Transform`. This value represents the position of the name tag.
     * Set the **Scale Multiplier** to `50`. This value scales the name tag based on the distance from the camera.
     * Set the **Distance Culling Range** to `20`. This value culls the name tag when it’s too far away or behind the camera.
  4. Right-click the `NPC` GameObject and select **3D Object** > **Capsule** to add a child Capsule GameObject. Then set its Y position to `1` so that it doesn’t clip into the floor plane.
  5. Add a desired material to the Capsule GameObject, such as a blue surface material if you have one.
  6. Right-click the `NPC` GameObject and select **Create Empty** to add another empty child GameObject and name it `UI_Transform`.
  7. In the **Inspector** window of the `UI_Transform` GameObject, select the arrow icon on the top-right corner and select an icon for it. This icon allows you to easily identify the GameObject in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) for debugging purposes.
![Set an icon for UI_Transform](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/uitk/ui_transform_icon.png)
  8. In the **Inspector** window of the `UI_Transform` GameObject, set the position to `(0, 3, 0)`. This value represents the position of the name tag relative to the NPC GameObject.


## Test the example
Duplicate the NPC prefab to create multiple NPCs in the scene. The name tags follow the NPCs and scale based on the distance from the camera.
  1. In the **Hierarchy** window, right-click the `NPC` GameObject and select **Duplicate**.
  2. Repeat the previous steps a few times to create multiple NPCs in the scene.
  3. Move the NPCs to different positions in the scene.
  4. Enter Play mode. The name tags follow the NPCs and scale based on the distance from the Camera.
  5. Pause the game.
  6. Select **Window** > **UI Toolkit** > **Debugger** to open the **UI Toolkit Debugger** window.
  7. In the **UI Toolkit Debugger** window, from the **Select a Panel** list, select **PanelSettings**.
  8. Select **PanelRootElement** > **TemplateContainer** > **VisualElement** > **TemplateContainer** to view the style properties of the name tag.
  9. Un-pause the game. The translate properties of the name tag is updated dynamically as the NPC moves.


## Additional resources
  * [Get started with runtime UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-get-started-with-runtime-ui.html)
  * [Create a UI Document component](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-ui-document-component.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-examples.html)
UI Toolkit runtime examples
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-work-with-text.html)
Work with text
