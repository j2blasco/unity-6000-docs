* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UI-system-compare.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * Comparison of UI systems in Unity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
UI systems
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
UI Toolkit
# Comparison of UI systems in Unity
[UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html) is intended to become the recommended UI system for you to develop UI in your projects. However, in its current release, UI Toolkit does not have some features that [uGUI (Unity UI)](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.ugui.html) and [IMGUI (Immediate Mode GUI)](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html) support. uGUI and IMGUI are more appropriate for certain use cases, and are required to support legacy projects.
This page provides a high-level feature comparison of UI Toolkit, uGUI, and IMGUI, and their respective approaches to UI design. 
## General consideration
The following table lists the recommended and alternative system for runtime and Editor:
**Unity 6** | **Recommendation** | **Alternative**  
---|---|---  
**[Runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/UI-system-compare.html#runtime)** | uGUI (Unity UI) | UI Toolkit  
**[Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/UI-system-compare.html#editor)** | UI Toolkit | IMGUI  
## Roles and skill sets
Your team’s skill set and comfort level with different technologies is also an important consideration.
The following table lists the recommended system for different roles:
**Roles** | **UI Toolkit** | **uGUI (Unity UI)** | **IMGUI** | **Skill sets**  
---|---|---|---|---  
**Programmer** | Yes | Yes | Yes | Programmers can use any game development tool or API.  
**Technical Artist** | Partial | Yes | No | Technical artists who are familiar with Unity’s GameObject-based tools and workflows are likely to be comfortable working with GameObjects, Components, and the Scene view.   
  
They might not be comfortable with UI Toolkit’s web-like approach or IMGUI’s pure C# approach.  
**UI Designer** | Yes | Partial | No | UI designers who are familiar with UI creation tools are likely to be comfortable with UI Toolkit’s document-based approach and can use the [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html) to visually edit their UI.  
  
If they are not familiar with GameObject-based workflows, they might require help from programmers or level designers.  
## Innovation and development
UI Toolkit is in active development and releases new features frequently. uGUI and IMGUI are established and production-proven UI systems that are updated infrequently.
uGUI and IMGUI might be better choices if you need features that are not yet available in UI Toolkit, or you need to support or reuse older UI content.
## Runtime
UI Toolkit is an alternative to uGUI (Unity UI) if you create a screen overlay UI that runs on a wide variety of screen resolutions. Consider UI Toolkit to do the following:
  * Produce work with a significant amount of user interfaces
  * Require familiar authoring workflows for artists and designers
  * Seek textureless UI rendering capabilities


uGUI is the recommended solution for the following:
  * UI positioned and lit in a 3D world
  * VFX with custom **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) and materials
  * Easy referencing from `MonoBehaviours`


### Use Cases
The following table lists the recommended system for major runtime use cases:
**Unity 6** | **Recommendation**  
---|---  
**Multi-resolution menus and HUD in intensive UI projects** | UI Toolkit  
**World space UI and**VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR)** | uGUI  
**UI that requires customized shaders and materials** | uGUI  
### In details
The following table lists the recommended system for detailed runtime features:
**Unity 6** | **UI Toolkit** | **uGUI**  
---|---|---  
****WYSIWYG** What You See Is What You Get. A term used to describe a system where the user interface closely resembles the final output.   
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WYSIWYG) authoring** | Yes | Yes  
**Nesting reusable components** | Yes | Yes  
**Global style management** | Yes | No  
**Layout and Styling Debugger** | Yes | Yes  
****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) integration** | Yes | Yes  
**Rich text tags** | Yes | Yes*  
**Scalable text** | Yes | Yes*  
**Font fallbacks** | Yes | Yes*  
**Adaptive layout** | Yes | Yes  
**[Input system](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.inputsystem.html) support** | Yes | Yes  
**Serialized events** | No | Yes  
**[Visual Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.visualscripting.html) support** | No | Yes  
**Compatible with[Rendering pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)** | Yes | Yes  
**Screen-space (2D) rendering** | Yes | Yes  
**World-space (3D) rendering** | No | Yes  
**Custom materials and shaders** | No | Yes  
**[Sprites](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html) A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) / [Sprite atlas](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/atlas-landing.html)A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/atlas/v2/v2-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteAtlas) support** | Yes | Yes  
**Dynamic texture atlas** | Yes | No  
**Textureless elements** | Yes | No  
**UI anti-aliasing** | Yes | No  
**Rectangle clipping** | Yes | Yes  
**Mask clipping** | No | Yes  
**Nested masking** | Yes | Yes  
**[UI transition animations](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transitions.html)** | Yes | No  
**Integration with**Animation Clips** Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnimationClip) and Timeline** | No | Yes  
*_Requires[the TextMesh Pro package](https://learn.unity.com/tutorial/textmesh-pro-importing-the-package)_
## Editor
UI Toolkit is recommended if you create complex editor tools. UI Toolkit is also recommended for the following reasons: 
  * Better reusability and decoupling
  * Visual tools for authoring UI
  * Better scalability for code maintenance and performance


IMGUI is an alternative to UI Toolkit for the following:
  * Unrestricted access to editor extensible capabilities
  * Light API to quickly render UI on screen


### Use Cases
The following table lists the recommended system for major Editor use cases:
**Unity 6** | **Recommendation**  
---|---  
**Complex editor tool** | UI Toolkit  
****Property drawers** A Unity feature that allows you to customize the look of certain controls in the Inspector window by using attributes on your scripts, or by controlling how a specific Serializable class should look [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-PropertyDrawers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PropertyDrawer)** | UI Toolkit  
**Collaboration with designers** | UI Toolkit  
### In details
The following table lists the recommended system for detailed Editor features:
**Unity 6** | **UI Toolkit** | **IMGUI**  
---|---|---  
**WYSIWYG authoring** | Yes | No  
**Nesting reusable components** | Yes | No  
**Global style management** | Yes | Yes  
**Layout and Styling Debugger** | Yes | No  
**Rich text tags** | Yes | Yes  
**Scalable text** | Yes | No  
**Font fallbacks** | Yes | Yes  
**Adaptive layout** | Yes | Yes  
**Default**Inspectors** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** | Yes | Yes  
**Inspector: Edit custom object types** | Yes | Yes  
**Inspector: Edit custom property types** | Yes | Yes  
**Inspector: Mixed values (multi-editing) support** | Yes | Yes  
**[Array and list-view control](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ListView.html)** | Yes | Yes  
**[Data binding: Serialized properties](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Binding.html)** | Yes | Yes  
## Additional resources
  * [Migrate from uGUI to UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transitioning-From-UGUI.html)
  * [Migrate from IMGUI to UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-IMGUI-migration.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
UI systems
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
UI Toolkit
