* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UsingCustomEditorTools.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * Custom Editor tools


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewContextMenu.html)
Scene view context menu
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GameView.html)
The Game view
# Custom Editor tools
You can create Editor tools with the [EditorTool API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html). 
An Editor tool’s context determines what that tool affects in the Editor. Tools can be either global tools or component tools.
Access Editor tools in the [Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) from these [overlays](https://docs.unity3d.com/6000.0/Documentation/Manual/overlays.html): 
  * The Tools overlay
  * The Tools Settings overlay


## Tool context
The [`EditorToolContext API`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html) changes what the Editor’s [built-in Transform tools](https://docs.unity3d.com/6000.0/Documentation/Manual/PositioningGameObjects.html) affect.
The default tool context is [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.GameObjectToolContext.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). A tool with the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.GameObjectToolContext.html) tool context affects the [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) values of a GameObject. Other contexts can affect different elements. For example, the [Spline tool context](https://docs.unity3d.com/Packages/com.unity.splines@latest/) makes it so the **Move** , **Rotate** , and **Scale** tools affect Spline knots and tangents.
If your project contains multiple tool contexts, you can use the first button in the Tools overlay to select a tool context. If the tool context button isn’t selected, then the default GameObject tool context is active. The tool context button isn’t available from the Tools overlay if there are no extra tool contexts in your project. 
## Global tools vs. component tools
Tools you create with the [EditorTool API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) can either be global or component tools.
### Global tools
A global tool affects any GameObject. 
A global tool is always available regardless of the type of GameObject you select. For example, you can always access a Transform tool because the Transform tool works with any GameObject. 
The Tools overlay displays global tools in the section after the built-in Transform tools, such as **Move** , **Rotate** , **Scale** , and **Rect**. 
### Component tools
A component tool affects a specific [component](https://docs.unity3d.com/6000.0/Documentation/Manual/Components.html)A functional part of a GameObject. A GameObject can contain any number of components. Unity has many built-in components, and you can create your own by writing scripts that inherit from MonoBehaviour. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingComponents.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#component). 
A component tool is only available when you select a GameObject with the component the tool comes from attached to it. For example, you can only use a custom manipulator tool for lights when you select a GameObject with a Light component.
The last buttons in the Tools overlay are component tools. Component tools are divided into groups based on their component. The availability of component tools depends on what you have [actively selected](https://docs.unity3d.com/6000.0/Documentation/Manual/SelectGameObjects.html) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view or Hierarchy window. 
## Additional resources
  * [Overlays](https://docs.unity3d.com/6000.0/Documentation/Manual/overlays.html)
  * [`EditorTool`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html)
  * [`EditorToolContext`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html)
  * [`GameObjectToolContext`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.GameObjectToolContext.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewContextMenu.html)
Scene view context menu
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GameView.html)
The Game view
