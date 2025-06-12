* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html

  * [Get started with Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/get-started-with-unity.html)
  * [Quickstart guides](https://docs.unity3d.com/6000.0/Documentation/Manual/QuickstartGuides.html)
  * [3D game development quickstart guide](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3D.html)
  * Creating a 3D game


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3D.html)
3D game development quickstart guide
[](https://docs.unity3d.com/6000.0/Documentation/Manual/best-practice-guides.html)
Advanced best practice guides
# Creating a 3D game
To create a 3D game, [set up your Unity project](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3D.html#3DInitialSetup) and then familiarize yourself with the relevant concepts in the following order:
  * [Fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#Fundamentals)
  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#Scripting)
  * [3D Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#3Dassets)
  * [Building in-game environments](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#Environments)
  * [Animation](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#Animation)
  * [Graphics](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#Graphics)
  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#Audio)
  * [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#Physics)
  * [User interface](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#UI)


## Fundamentals
[GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) are fundamental objects in Unity that represent characters, props, scenery, and more. Every object in your game is a GameObject.
GameObjects live in 3D environments called [scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). You can think of a scene as a game level, but it might also represent a menu, the credits at the end of the game or something else entirely.
The behavior of GameObjects is defined by blocks of functionality called components. You can attach multiple components to GameObjects. The following components are fundamental for 3D games:
  * [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html): the **Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TransformComponent) determines the Position, Rotation, and Scale of each GameObject in the scene. Every GameObject has a Transform component.
  * [Mesh Filter](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)A mesh component that takes a mesh from your assets and passes it to the Mesh Renderer for rendering on the screen. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshFilter): this component defines the shape of a 3D GameObject.
  * [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer): this component defines how the 3D shape defined by the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Filter looks.
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera): specially-configured GameObjects that capture and display the world to the player.
  * [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rigidbody): Rigidbodies allow GameObjects to interact with the Physics system, including gravity and **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision). See the [Physics](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#Physics) section of this guide.
  * [Colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider): this component defines the shape of a 3D GameObject for the purpose of physical collisions.


[Back to Top](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#TopOfPage)
## Scripting
Unity allows you to create your own Components using ****scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts)**. Scripts let you trigger game events, modify Component properties over time and respond to user input. Unity supports the C# programming language natively. Here some examples of how you can use scripts in your game:
  * To receive input from the player and have a GameObject move or act based on that input.
  * To set win and lose states which open relevant win or lose scenes to create a full game loop.
  * To affect the components of GameObjects, such as their transform, animation, or renderer, based on other variables.


For details on how to use scripts in Unity, see [Scripting Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html). To learn the fundamentals of scripting, follow the [Unity Learn Beginner Scripting course](https://learn.unity.com/course/beginner-scripting). For more in-depth guidance, see the example projects [Create with Code](https://learn.unity.com/course/create-with-code) and [Creator Kit: Beginner Code](https://learn.unity.com/project/creator-kit-beginner-code).
[Back to Top](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#TopOfPage)
## 3D Assets
Models are 3D representations of objects. The majority of the visuals for 3D games consist of models, such as characters, interactable objects, and the world around the player.
You can use tools like [Probuilder](https://unity3d.com/unity/features/worldbuilding/probuilder) to create models in Unity. However, these work best for prototyping, rather than for the final product.
To add more polished 3D assets to your final product, create 3D Models, Materials and Textures in 3D modeling software and then import them into Unity.
![Left: A 3D polygon mesh for a player character. Right: The player mesh rendered in Unity with materials](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/quickstart-3D-Graphics.png) Left: A 3D polygon mesh for a player character. Right: The player mesh rendered in Unity with materials
### Importing 3D Model Files
Unity uses the .fbx model format. You can also use other common native [model formats](https://docs.unity3d.com/6000.0/Documentation/Manual/3D-formats.html) (for example, .max, .blend, .mb, .ma), and Unity converts them into .fbx once they are imported.
[Import models](https://docs.unity3d.com/6000.0/Documentation/Manual/ImportingModelFiles.html) into Unity to use them in your project.
### Rendering Meshes
A 3D mesh is the structural build of a 3D model. It is made up of multiple polygon shapes. To add a 3D model to a GameObject, add a [Mesh Filter](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshFilter.html) to the GameObject. The [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html) component renders meshes in your scene; to ensure models appear in your game, add a Mesh Renderer to any GameObject that has a Mesh Filter component.
### Materials
[Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material) combine information about the visual appearance of a surface, such as [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture), color tints, and [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). Use Materials to define how to render surfaces.
  * Textures are any 2D image files that you import into Unity. Use [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html) to wrap a mesh and add fine detail to a model.
  * Use Color tints to alter the color of the texture.
  * Shaders are a series of instructions which determine how Unity displays GameObjects on screen. Use [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html) to affect how Unity renders each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) based on lighting input and Material configuration.


See the Learn Tutorial on [Material Design](https://learn.unity.com/tutorial/shading-material-design).
[Back to Top](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#TopOfPage)
## Building in-game environments
![An environment has been created by adding models and other assets to the scene.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/quickstart-3D-environment.png) An environment has been created by adding models and other assets to the scene.
Environment design is the process of creating an environment for gameplay to take place in. You might design and build your environment at the same time in the Unity Editor, or you might design an environment outside of Unity and then build it in Unity.
To build an in-game environment, you add GameObjects to the scene and position them to suit your preference and design. In addition to hand-placing your models in the scene, the Unity Editor includes a built-in set of **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) features that allow you to add landscapes to your game. In the Editor, you can create multiple Terrain tiles, adjust the height or appearance of your landscape, and add trees or grass to it. Read more about [Creating and Using Terrains](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html).
[Back to Top](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#TopOfPage)
## Animation
You can import animations made in other programs, or animate your assets directly in the Editor. For more information on 3D animation, see the Unity Learn Course [Introduction to 3D Animation Systems](https://learn.unity.com/course/introduction-to-3d-animation-systems?uv=2019.4).
![The player is standing still so the idle animation is playing.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/quickstart-3D-animation.png) The player is standing still so the idle animation is playing.
### Importing Animations
Unity can [import animation clips](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html) when you import a model with animation. This means you can animate models in another program and then access and manipulate the clips in Unity.
### Animating Models in Unity
Use the [Animation window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationEditorGuide.html) to create and modify Animation Clips directly inside Unity. Use **Keyframe** A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#keyframe) animation to add simple animations to a GameObject within your scene, such as changing its position, size, or rotation.
### Controlling animations
To control which [Animation Clips](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) play, you can call them directly in a script with the [Animator](https://docs.unity3d.com/ScriptReference/Animator.html) Class, or create and modify the [Animator Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorController) in the [Animator window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)The window where the Animator Controller is visualized and edited. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimatorWindow).
You can use the [Animator window](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimatorWindow.html) to:
  * Create and set up the [Animation Controller](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimatorController.html)
  * Create [Animator States](https://docs.unity3d.com/6000.0/Documentation/Manual/class-State.html) with [Animation Clips](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationClips.html)
  * Create [Animator Parameters](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationParameters.html), which scripts can access or assign values to
  * Create [Animator Transitions](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transition.html) which specify conditions (based on parameters) for when a State should change and how long the blend between states should take


[Back to Top](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#TopOfPage)
## Graphics
### Lighting
Light your Scenes to add depth and mood to your environments and to help the player experience the game world you’ve created. To set up lighting:
  1. Create a Light. Right-click in the Hierarchy window to open the GameObject menu, select **Light** , and select a type of Light to add to your scene. See [Types of Light](https://docs.unity3d.com/6000.0/Documentation/Manual/Lighting.html).
  2. Place your Lights in the Scene. Adjust the color, intensity, and placement of your Lights until you achieve the desired effect. See [Using Lights](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingLights.html).
  3. Perfect your lighting. For example, you can choose a different [Light mode](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes.html)A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightMode), or add a [cookie](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html) mask to create shadows.

![A Spot Light creates atmospheric lighting in this scene](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/quickstart-3D-lights.png) A Spot Light creates atmospheric lighting in this scene
Refer to the Unity Learn [Lighting in URP](https://learn.unity.com/project/creative-core-lighting) tutorial.
[Back to Top](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#TopOfPage)
## Audio
You can add background music and sound effects to your game in Unity; see [Audio Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioOverview.html). Use third-party software to create your audio and import it into Unity with the recommended settings.
[Back to Top](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#TopOfPage)
## Physics
![The Player character has a capsule collider component which uses the Physics system to allow the character to collide with the walls. ](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/quickstart-3D-physics.png) The Player character has a capsule collider component which uses the Physics system to allow the character to collide with the walls. 
Use Unity’s **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicsEngine) to control how GameObjects interact. You can use this to replicate forces such as gravity and mechanics, which define how GameObjects behave on collision in the real world. You can also configure the physics settings to create custom physics to fit the design of your game, which might not be an accurate simulation of the real world. To learn how to use Unity’s physics engine, see the Unity Learn tutorial [Ruby’s Adventure: 2D Beginner](https://learn.unity.com/project/ruby-s-2d-rpg). Refer to the [Physics section](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicsSection.html) of the User Manual for more information.
To set up Physics for your GameObjects:
  1. To allow your GameObject to be affected by the Physics system, and react to things like gravity and collisions, add a [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/Manual/RigidbodiesOverview.html) component.
  2. Use [Colliders](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html) to enable GameObjects to interact with other GameObjects in the scene. For example, GameObjects with a collider can move or be moved by another GameObject with a collider.
  3. To be able to call a function in code when two GameObjects intersect, add a [Collider](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html) and make it a [trigger](https://docs.unity3d.com/6000.0/Documentation/Manual/collider-interactions-other-events.html).


[Back to Top](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#TopOfPage)
## User Interface
If you want to add a menu or help to your game, you need to set up a [user interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html). To set up a user interface, use [Unity UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html).
[Back to Top](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3DCreate.html#TopOfPage)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Quickstart3D.html)
3D game development quickstart guide
[](https://docs.unity3d.com/6000.0/Documentation/Manual/best-practice-guides.html)
Advanced best practice guides
