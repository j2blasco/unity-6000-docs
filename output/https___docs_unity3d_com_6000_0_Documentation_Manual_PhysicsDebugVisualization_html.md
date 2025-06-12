* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsDebugVisualization.html

  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)
  * [Built-in 3D Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsOverview.html)
  * Physics Debug window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/physics-multi-scene.html)
Multi-scene physics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerPhysics.html)
Physics Profiler module
# Physics Debug window reference
Use the Physics Debug window to configure and generate visual representations of 3D physics activity in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). These visualizations appear in the [Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView).
To open the Physics Debug window in the Unity Editor, go to **Window** > **Analysis** > **Physics Debugger**.
Physics Debugger inserts a [Physics debug panel](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsDebugVisualization.html#physics-debug-panel) in the Scene view, and opens a Physics Debug window that contains the following tabs:
  * **[Info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsDebugVisualization.html#physics-debug-info)** : Track Rigidbody and Articulation Body information. **Center of Mass** Represents the average position of all mass in a Rigidbody for the purposes of physics calculations. By default it is computed from all colliders belonging to the Rigidbody, but can be modified via script. [More info](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-centerOfMass.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CenterofMass) and Inertia Tensor visualization can also be found here.
  * **[Filtering](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsDebugVisualization.html#physics-debug-filtering)** : Determine which physics objects should be shown.
  * **[Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsDebugVisualization.html#physics-debug-rendering)** : Settings that define how Unity renders and displays the physics visualization.
  * **[Contacts](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsDebugVisualization.html#physics-debug-contacts)** : Select whether or not contacts should be visualized.
  * **[Queries](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsDebugVisualization.html#physics-debug-queries)** : Select whether or not queries should be visualized.


To revert the Physics Debug window back to its default settings, select **Reset**.
For more information on improving physics performance in your project, see documentation on the [Physics Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerPhysics.html).
## Physics debug panel
When the Physics Debug window is open in Unity, the Physics Debug panel appears in the Scene view. By default, it appears in the bottom-right corner of the Scene view; however, you can click and drag to move it around. 
**Property** | **Description**  
---|---  
****Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) Geometry** | Enable **Collision Geometry** to visualize collision information in the Scene view. Disable **Collision Geometry** to hide collision information in the Scene view.  
**Mouse Select** | Enable **Mouse Select** to enable mouse-over highlighting and mouse selection. This is useful if you have large **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that obstruct each other in the visualization.  
## Info
The **Info** tab contains data about any selected [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody) or [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html) GameObjects. You can use this data to monitor the physics body’s behavior. You cannot edit the property values in this tab. You can modify them via script, but it is not recommended; in most cases, you should apply forces via the physics system to change these values instead.
To keep a specific GameObject permanently docked in the **Info** tab, enable **Lock** for that GameObject. You can lock an infinite number of GameObjects. Use the **Number of items per row** property to arrange the **Info** tab in a way that is easiest for you to navigate.
The Info tab always displays the following properties.
**Property** | **Description**  
---|---  
**Number of items per row** | Define how many selected GameObjects to display horizontally in the top row of the **Info** tab.   
  
By default, if you select or lock multiple GameObjects, Unity displays them all vertically. However, you can arrange them horizontally instead. Use **Number of items per row** to define how many GameObjects to display next to each other on one horizontal row, up to a maximum of 10.   
  
If the number of selected or locked GameObjects exceeds this number, the more recently selected GameObjects appear on a new row underneath the first.  
  
GameObjects always appear in the **Info** tab in the order of selection. The default value for this property is 1.  
**Tracked objects** | Displays the total number of unique GameObjects that currently appear in the **Info** tab. This includes selected GameObjects and locked GameObjects. It does not include duplicates.  
**Clear locked objects** | Select **Clear locked objects** to disable **Lock** for all GameObjects. This removes any GameObjects from the **Info** tab that are not already selected in the Hierarchy window.  
The **Info** tab displays the following properties when you select a GameObject in the Hierarchy that has a physics body (that is, a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html) or an [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html)). 
**Property** | **Description**  
---|---  
**GameObject** | Displays the name of the selected or locked GameObject that the following properties refer to.  
**Draw Gizmos for** | Select which physics property the Physics Debug should display a **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) for.  
- **Center of Mass** | Display a gizmo that indicates the location of the physics body’s global center of mass (see **World Center of Mass**).  
- **Inertia Tensor** | Display a gizmo that indicates the rotation and scale of the physics body’s Inertia Tensor (see **Inertia Tensor**).  
**Lock** | Enable **Lock** to keep the GameObject in the **Info** tab even when it is not selected in the Hierarchy window.  
**Speed** | The speed at which the physics body is moving, measured in meters per second (m/s).  
**Velocity** | The velocity of the physics body along each vector, measured in meters per second (m/s).  
**Angular Velocity** | The velocity of the physics body along each vector, measured in degrees per second.  
**Inertia Tensor** | The inertia tensor of this physics body. Like mass, an inertia tensor defines how much force or torque is required to make a physics body move; however, while mass affects linear movement, inertia tensor affects rotational movement. The higher the **Inertia Tensor** value is, the more torque is required to make the physics body rotate on its axis.  
**Inertia Tensor Rotation** | The rotation of the inertia tensor. By default, Unity calculates inertia tensor rotation automatically, based on all of the **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider) attached to the physics body.  
**Local Center of Mass** | The local location of the physics body’s center of mass along each vector. To change the center of mass via script, use `centerOfMass`. Unity can also change it based on collider placement.  
**World Center of Mass** | The global location of the physics body’s center of mass along each vector. To change the center of mass via script, use `worldCenterOfMass`. Unity can also change it based on collider placement.  
**Sleep State** | The sleep state of the physics body. Displays **Awake** if the physics body is awake and included in physics calculations. Displays **Asleep** if the physics body is asleep, and not included in physics calculations.  
**Sleep Threshold** | The energy threshold for the physics body, below which the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine) stops including the body in physics updates. By default, this is the **Sleep Threshold** value defined in the [global Physics settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PhysicsManager.html).  
**Max Linear Velocity** | The maximum linear velocity the physics body can reach, defined by `maxLinearVelocity`.  
**Max Angular Velocity** | The maximum rotational velocity the physics body can reach, defined by `maxAngularVelocity`.  
**Solver Iterations** | The number of iterations that the physics system solver needs to perform on this physics body.  
**Solver Velocity Iteration** | The number of velocity iterations that the physics system solver needs to perform on this physics body. These bring the exit velocity of overlapping GameObjects closer to the correct value, taking into account the contact bounciness.  
**Body Index** | The Articulation Body index in the tree. This property only appears for Articulation Bodies.  
## Filtering
The **Filtering** tab contains properties to configure which physics elements appear in the Physics Debug visualization. 
**Property** | **Description**  
---|---  
**Show Physics Scene** | Select which Physics Scenes to include in the visualization, if you have [multiple physics scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/physics-multi-scene.html) loaded at once.  
**Show Unity Scene** | Select which Unity Scenes to include in the visualization, if you have [multiple scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/MultiSceneEditing.html) loaded at once.  
**Show Layers** | Select which [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Layer) to display in the visualization.  
**Show Static Colliders** | Enable **Show Static Colliders** to display visualization for Colliders that have no Rigidbody component. Disable **Show Static Colliders** to remove visualization for Colliders that have no Rigidbody component.  
**Show Triggers** | Enable **Show Triggers** to display visualization for Colliders that are Triggers. Disable **Show Triggers** to remove visualization for Colliders that are Triggers.  
**Show Rigidbodies** | Enable **Show Rigidbodies** to display visualization for [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html) components. Disable **Show Rigidbodies** to remove visualization for Rigidbody components.  
**Show Kinematic Bodies** | Enable **Show Kinematic Bodies** to display visualization for Colliders that have Kinematic Rigidbody components. Disable **Show Kinematic Bodies** to remove visualization for Colliders that have Kinematic Rigidbody components.  
**Show Articulation Bodies** | Enable **Show Articulation Bodies** to display visualization for [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html) components. Disable **Show Articulation Bodies** to remove visualization for ArticulationBody components.  
**Show Sleeping Bodies** | Enable **Show Sleeping Bodies** to display visualization for Colliders that have Sleeping Rigidbody components. Disable **Show Sleeping Bodies** to remove visualization for Colliders that have Sleeping Rigidbody components.  
**Collider Types** | Use these options to show specific Collider types in the physics visualization.  
- **Show BoxColliders** | Enable **Show BoxColliders** to display visualization for [Box Colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)A cube-shaped collider component that handles collisions for GameObjects like dice and ice cubes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#boxcollider). Disable **Show BoxColliders** to remove visualization for Box Colliders.  
- **Show SphereColliders** | Enable **Show SphereColliders** to display visualization for [Sphere Colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SphereCollider.html)A sphere-shaped collider component that handles collisions for GameObjects like balls or other things that can be roughly approximated as a sphere for the purposes of physics. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SphereCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SphereCollider). Disable **Show SphereColliders** to remove visualization for Sphere Colliders.  
- **Show CapsuleColliders** | Enable **Show CapsuleColliders** to display visualization for [Capsule Colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html)A capsule-shaped collider component that handles collisions for GameObjects like barrels and character limbs. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CapsuleCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#capsulecollider). Disable **Show CapsuleColliders** to remove visualization for Capsule Colliders.  
- **Show MeshColliders (convex)** | Enable **Show MeshColliders (convex)** to display visualization for [Mesh Colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)A free-form collider component which accepts a mesh reference to define its collision surface shape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshCollider) that have their **Is Convex** property enabled. Disable **Show MeshColliders (convex)** to remove visualization for **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Colliders that have their **Is Convex** property enabled.  
- **Show MeshColliders (concave)** | Enable **Show MeshColliders (concave)** to display visualization for [Mesh Colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshCollider.html) that have their **Is Convex** property disabled. Disable **Show MeshColliders (concave)** to remove visualization for Mesh Colliders that have their **Is Convex** property disabled.  
- **Show TerrainColliders** | Enable **Show TerrainColliders** to display visualization for [Terrain Colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainCollider.html)A terrain-shaped collider component that handles collisions for collision surface with the same shape as the Terrain object it is attached to. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TerrainCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TerrainCollider). Disable **Show TerrainColliders** to remove visualization for Terrain Colliders.  
- **Show None** | Select **Show None** to clear all filtering criteria and remove all Colliders from the visualization.  
- **Show All** | Select **Show All** to enable all filters and display visualization for all Colliders.  
## Rendering
The **Rendering** tab contains properties to configure how Unity renders and displays the physics visualization. 
**Property** | **Description**  
---|---  
**Static Colliders** | Select a color to represent static Colliders (Colliders with no Rigidbody component) in the visualization.  
**Triggers** | Select a color to represent Colliders that are also Triggers in the visualization.  
**Rigidbodies** | Select a color to represent [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html) components in the visualization.  
**Kinematic Bodies** | Select a color to represent kinematic Rigidbody components from the visualization. The physics system does not control kinematic Rigidbody components.  
**Articulation Bodies** | Select a color to represent [Articulation Body components](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html) in the visualization.  
**Sleeping Bodies** | Select a color to represent Sleeping Rigidbody components (which are not currently engaging with the physics engine) from the visualization.  
**Variation** | Define to what extent the selected colors blend with a random color. Use this to visually separate Colliders by color, and to see the structure of the GameObjects. The value is between 0 and 1, and is set to 0.15 by default.  
**Transparency** | Set the transparency of drawn collision geometry in the visualization. The value is between 0 and 1, and is set to 0.5 by default.  
**Force Overdraw** | Enable **Force Overdraw** to display collider geometry on top of render geometry in the visualization. This is useful if render geometry is obscuring collider visualizations. Disable **Force Overdraw** to display collider geometry as it appears in relation to the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera).  
**View Distance** | Set the view distance of the visualization. This is set to 1000 by default. The value is measured in units, which are assumed to be 1m by default in Unity.  
**Terrain Tiles Max** | Set the maximum number of [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) tiles in the visualization. This is set to 60 by default.  
**Gizmos settings** | Configure the Physics Debug gizmos that the **Info** tab controls.  
- **Constant screen size** | Enable **Constant screen size** to make Physics Debug gizmos appear the same size on the screen at any distance from the camera. Disable **Constant screen size** to make the gizmos’ size scale with perspective.  
- **Inertia Tensor scale** | Define the value by which to multiply the Inertia Tensor vector 3. This is useful if the Inertia Tensor is especially large; for example, if you need to visualize and observe the ratio of the vector’s components.  
## Contacts
The **Contacts** tab contains properties to configure which contact data appears in the Physics Debug visualization, and the colors used for different types of contact. 
**Property** | **Description**  
---|---  
**Show Contacts** | Enable **Show Contacts** to display visualization for contacts.  
- **Show All Contacts** | Enable **Show All Contacts** to display visualization for all collision contact data in the Physics Debug visualization. Disable **Show All Contacts** to limit the contact data that appears in the Physics Debug visualization.   
When **Show All Contacts** is disabled, only the following contacts appear in the visualization:   
- Colliders with `MonoBehaviour` scripts that receive messages from `OnCollisionEnter`, `OnCollisionSay`, or `OnCollisionExit`   
- Colliders that have the `providesContact` property set to true.  
- **Show Impulse** | Enable **Show Impulse** to display an arrow in the visualization that represents the contact point impulse. Disable **Show Impulse** to remove impulse visualization.  
- **Show Separation** | Enable **Show Separation** to display a segment and disc in the visualization that represents contact point separation. Disable **Show Separation** to remove separation visualization.  
- **Use Filtering settings** | Enable **Use Filtering settings** to use the settings in the **Filtering** tab to filter incoming contact visualization. Disable **Use filtering settings** to use only the settings in the **Contacts** tab.  
**Contact colors** | Select the colors Unity should use in the visualization to indicate collision contact data.  
**Use varied colors** | Enable **Use varied colors** to use random colors for each contacting Collider pair. Disable **Use varied colors** to use the three colors defined in the following properties (**Contact color** , **Contact separation color** , and **Contact impulse color**).  
**Contact color** | Select a color to represent the contact. This appears in the visualization as an arrow that starts in the contact point and faces the contact normal.  
**Contact separation color** | Select a color to represent the contact separation. This appears in the visualization as a segment and disc.  
**Contact impulse color** | Select a color to represent the contact impulse. This appears in the visualization as an arrow that points in the normal direction, with a length equal to the length of the impulse.  
## Queries
The **Queries** tab contains properties to configure which query types appear in the Physics Debug visualization, and how they appear. For information on PhysX queries, see the NVIDIA PhysX documentation on [Scene Queries](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Manual/SceneQueries.html) and [Geometry Queries](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Manual/GeometryQueries.html).
**Property** | **Description**  
---|---  
**Show queries** | Enable **Show queries** to display visualization for physics queries.  
**Query color** | Select the color Unity should use in the visualization to indicate physics queries.  
**Show shapes** | Choose which query shapes to display in the Physics Debug visualization. Enable a query shape to display queries of that shape in the visualization. Disable a query shape to remove queries of that shape from the visualization.   
  
The options are:   
- **Box** -shape queries   
- **Capsule** -shape queries   
- **Collider** -shape queries   
- **Ray** -shape queries  
**Show types** | Choose which query types to display in the visualization. Enable a query type to display queries of that type in the visualization. Disable a query type to remove queries of that type from the visualization. For information on PhysX query types, see the NVIDIA PhysX documentation on [Geometry Queries](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Manual/GeometryQueries.html).   
  
The options are:   
- **Overlap** queries   
- **Check** queries   
- **Cast** queries  
**Max Queries** | Define the maximum number of queries that Physics Debug can visualize at once. This is set to 100 by default.  
**Show None** | Select **Show None** to clear all filtering criteria and hide all query shapes and types from the visualization.  
**Show All** | Select **Show All** to enable all filters and show all query shapes and types in the visualization.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/physics-multi-scene.html)
Multi-scene physics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerPhysics.html)
Physics Profiler module
