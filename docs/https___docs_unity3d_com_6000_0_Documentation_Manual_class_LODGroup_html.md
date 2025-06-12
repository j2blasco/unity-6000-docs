* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html)
  * LOD Group component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-lod-meshes.html)
Import a mesh with LOD settings
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-images-lod.html)
2D images for low level of detail (LOD)
# LOD Group component reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODGroup.html "Go to LODGroup page in the Scripting Reference")
The **LOD Group** component manages [level of detail](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#levelofdetail) (LOD) for **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). 
![LOD Group inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/InspectorLODGroup.png) LOD Group inspector
![A](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LetterA.png) Controls for [transitioning between LOD levels](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#transitions)
![B](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LetterB.png) [LOD Group selection bar](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#LODGroup) for switching between LOD levels and previewing LOD rendering
![C](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LetterC.png) Information about the [Lod Bias](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#LODBias) Quality setting. This message appears if the **Lod Bias** property is set to anything other than 1.
![D](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LetterD.png) [Fade Transition Width](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#width) setting for the selected LOD level. This property only appears if you disable the **Animate Cross-fading** property: that is, when you choose to set a transition zone by width instead of time.
![E](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LetterE.png) **Mesh** [Renderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#renderers) set for the selected LOD level
In addition there are two buttons at the bottom of the component:
  * Click **Recalculate Bounds** to recalculate the **bounding volume** A closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Boundingvolume) of all LOD Mesh GameObjects after a new LOD level is added.
  * Click **Recalculate**Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) Scale** to update the [Scale in Lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html#lightmapping) property on all LOD **Mesh Renderers** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer), based on the changes you made to the LOD level boundaries.


## LOD Group selection bar
The LOD Group selection bar represents the different LOD levels as colored boxes. 
The percentage that appears in each LOD level box represents the threshold at which that level becomes active, based on the ratio of the GameObject’s screen space height to the total screen height. For example, if the threshold for LOD 1 is set to 50%, then LOD 1 becomes active when the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) pulls back far enough that the GameObject’s height fills half of the view.
![LOD Group selection bar](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-selectionbar.png) LOD Group selection bar
![A](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LetterA.png) The playhead for [the LOD preview](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#preview). You can scrub the camera icon back and forth to test the LOD levels and their transitions. At the bottom of the playhead you can see the current percentage. 
![B](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LetterB.png) To select a level, click on the level box. For each LOD level you select, you can [pick the Renderer to use](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#renderers) or [customize the transition zone](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#width).
![C](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LetterC.png) To add and remove LOD levels from the selection bar, right-click the LOD level box and then choose **Insert Before** or **Delete** from the context menu. 
![D](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LetterD.png) Level adjustment control. To change the percentage value for the LOD level, drag the left border of the LOD level box’s boundary.
**Note** : If the [Lod Bias](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#LODBias) property is not set to 1, the Camera position might not match the position where each LOD level actually transitions from the next. In this case, a warning message appears below the selection bar.
![Lod Bias warning](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-BiasWarning.png) Lod Bias warning
## Previewing the LOD transitions
The **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view displays a preview of the transitions between LOD levels when you move the camera icon on the LOD Group selection bar. The camera icon acts like a playhead which you can use to scrub back and forth to control the exact position to preview along the LOD Group selection bar. The preview shows what the Camera will render at each LOD level. 
![Control transition previews on the LOD Group selection bar](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-previewing.png) Control transition previews on the LOD Group selection bar
The LOD preview playhead shows the exact position as a percentage along the LOD Group selection bar from 100% on the left to 0% on the right. The percentage represents the ratio of the GameObject’s screen space height to the total screen height.
As you move through the levels, the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) displays the bounding box of the Tree Asset and the overlay indicates which LOD is active:
![Overlays displaying the active LOD levels](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-levels.png) Overlays displaying the active LOD levels
**Note:** Unity only displays the LOD label when a single GameObject is selected. It is not displayed when multiple GameObjects are selected.
## Renderers for LOD Meshes
When you select an LOD level box on the **LOD Group** selection bar, a **Renderers** panel appears. 
![Renderers panel with the Billboard Renderer for LOD 3](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-renderers.png) Renderers panel with the Billboard Renderer for LOD 3
The ‘Renderers’ are actually GameObjects that hold the Mesh for that LOD level. Usually this is a child of the GameObject that has the **LODGroup** component. 
To set a renderer Mesh for the current LOD level, click the **Add** box and choose the GameObject for that LOD level from the object picker. 
You can choose any GameObject for the renderer, but if you choose a GameObject that isn’t already a child, Unity prompts you to parent it to the **LODGroup** GameObject.
## Transitioning between LOD levels
Smooth transitions between LOD levels improves the player’s experience of your game. As the Camera moves closer or farther away, you don’t want players to see an obvious switchover (sometimes called _popping_) from the current LOD level to the next. 
Smooth transitions take place inside _transition zones_ , where Unity renders both the current and next LOD levels separately, and then cross-fades them together. 
_Cross-fading_ is the technique of rendering two levels at the same time, with a weighting of 1 to 0 for the _current_ LOD level and 0 to 1 for the _next_ LOD level:
![Cross-fading between the current LOD level and the next](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-blending.png) Cross-fading between the current LOD level and the next
Unity usually implements the cross-fading by using either screen-space dithering or transparency. For the last LOD level, there is no cross-fading: the current level just fades out.
To set up smooth transitions on your LOD levels:
  1. Select the **Fade Mode** drop-down menu and choose **Cross Fade** :
![Fade Mode drop-down menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-transitions.png) Fade Mode drop-down menu
**Note:** If your Tree Asset was made with [SpeedTree](https://store.speedtree.com/unity/), choose the **Speed Tree** mode instead. For more information, see [Working with SpeedTree Models](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#SpeedTreeModels).
  2. By default, the **Animate Cross-fading** option is enabled, meaning that Unity performs a time-based transition. If you want to define your own transition zone based on the Camera’s position, disable the **Animate Cross-fading** option and set the **Fade Transition Width** property. 
For more information, see [Customizing the transition zone](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html#width) value. 


### Customizing the transition zone
The transition between two LOD levels begins the moment the Model’s height ratio crosses the next LOD threshold. For example, if the LOD 1 threshold is set at 60%, the transition between the LOD 0 and LOD 1 levels always begins as soon as the height of the Model is 60%. The transition lasts for a short period of time:
![Animate Cross-fading \(by time\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-AnimateCrossFading.png) Animate Cross-fading (by time)
This behavior is animated by time, so you don’t need to set any properties once you enable the **Animate Cross-fading** property. The exact duration of the cross-fade is the same for every LOD level.
Alternatively, you can manually define transition zones inside each LOD level by its position. Each zone begins and ends before the next LOD level’s threshold. You define what proportion of each LOD level to use as the transition zone; that is, you set how far before the next level’s threshold the transition begins:
![Fade Transition Width \(by position\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-FadeTransitionWidth.png) Fade Transition Width (by position)
Use the **Fade Transition Width** property to define the transition zone on each LOD level:
  1. Disable the **Animate Cross-fading** option.
  2. Click on the specific LOD level box that you want to set. 
The **Fade Transition Width** property appears below the **LOD Group** selection bar.
![The Fade Transition Width property appears](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-width.png) The Fade Transition Width property appears
  3. Set the **Fade Transition Width** property to define the width of the cross-fade transition zone as a proportion (between 0.0 and 1.0) of the current LOD level’s entire length. For example, specify a smaller value to delay the onset of the blending and create a faster transition. 


### Working with SpeedTree Models
SpeedTree geometries store the _next_ LOD position for each vertex. Every vertex then knows how to interpolate between the current LOD position and the next LOD position. When Unity imports Models created in SpeedTree, it automatically sets them to the **Speed Tree** mode. 
![Speed Tree Fade Mode for a SpeedTree Model](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-SpeedTreeModels.png) Speed Tree Fade Mode for a SpeedTree Model
Unity only needs to render the current LOD geometry and provide a value from 0 to 1 to instruct each vertex to gradually _move_ to the next LOD position. At the end of the transition, the geometries of the current LOD and the next LOD match perfectly.
Blending between two LOD levels begins at 0 and ends at 1. Any point along this zone is the blend factor, which represents the weighting between the current LOD level and the next LOD level:
![Blending for SpeedTree Models](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODGroup-blend_factor.png) Blending for SpeedTree Models
The **Speed Tree** mode uses the blend factor to interpolate the vertex positions between the current **Mesh LOD level** and the next Mesh LOD level, and then renders the geometry at that position. 
**Note:** The **Speed Tree** mode is only used for blending between two _Mesh LOD levels_ : that is, when both current and next LOD levels have a Mesh Renderer. When transitioning to a _**Billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) LOD level_ or when fading out entirely, Unity performs **Cross Fade** -style blending. 
### Blend Factors in Shader code
Unity doesn’t provide a default built-in technique to blend LOD geometries. You need to implement your own technique according to your game type and Asset production pipeline. 
Unity calculates a blend factor from the GameObject’s screen size and passes it to your **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in the [unity_LODFade.x uniform](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UnityShaderVariables.html#unity_LODFade) variable. Depending on the **Fade Mode** you choose, use either the `LOD_FADE_PERCENTAGE` or `LOD_FADE_CROSSFADE` keyword for GameObjects rendered with LOD fading.
For time-based (animated) transitions, you can set the exact duration of the transition globally for every LOD level with the [LODGroup.crossFadeAnimationDuration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODGroup-crossFadeAnimationDuration.html) member.
For information on LOD naming conventions, see [Import a mesh with LOD settings](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-lod-meshes.html).
LODGroup
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/importing-lod-meshes.html)
Import a mesh with LOD settings
[](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-images-lod.html)
2D images for low level of detail (LOD)
