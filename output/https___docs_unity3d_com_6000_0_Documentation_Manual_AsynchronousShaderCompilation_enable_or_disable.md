* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-enable-or-disable.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Fixing hitches or stalls](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reduce-stalling.html)
  * [Asynchronous shader compilation in the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html)
  * Enable or disable asynchronous shader compilation


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-introduction.html)
Introduction to asynchronous shader compilation
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-detect.html)
Detect asynchronous shader compilation
# Enable or disable asynchronous shader compilation
Asynchronous **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) compilation is enabled by default.
To enable or disable asynchronous shader compilation:
  1. Go to **Edit > Project Settings > Editor**.
  2. At the bottom of the Editor settings, under **Shader Compilation** , check or uncheck the **Asynchronous Shader Compilation** checkbox.


**Note:** Enabling and disabling asynchronous shader compilation in this way affects only the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and Game views by default. If you want to use it in other parts of the Editor, see [Custom Editor tools and asynchronous shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-enable-or-disable.html#using-it-in-custom-editor-tools).
## Enable or disable asynchronous shader compilation for specific rendering calls
You can enable or disable asynchronous shader compilation for specific rendering commands in your C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
The following instructions show you how to enable or disable the feature in an immediate scope, and a [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) scope.
#### In an immediate scope
In an immediate scope, you can use [`ShaderUtil.allowAsyncCompilation`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-allowAsyncCompilation.html).
To do this:
  1. Store the current state of `ShaderUtil.allowAsyncCompilation` in a variable.
  2. Before you call the rendering commands, set `ShaderUtil.allowAsyncCompilation` to `false`.
  3. Call the rendering commands.
  4. After calling the rendering commands, restore `ShaderUtil.allowAsyncCompilation` back to its previous state.


Here is a pseudo-code example:
```
// Store the current state
bool oldState = ShaderUtil.allowAsyncCompilation;

// Disable async compilation
ShaderUtil.allowAsyncCompilation = false;

// Enter your rendering code that should never use the placeholder shader, for example UI elements or characters.
Graphics.RenderMesh(...);

// Restore the old state
ShaderUtil.allowAsyncCompilation = oldState;

```

#### In a CommandBuffer scope
In a `CommandBuffer` scope, you can use [`ShaderUtil.SetAsyncCompilation`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.SetAsyncCompilation.html) and [`ShaderUtil.RestoreAsyncCompilation`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.RestoreAsyncCompilation.html).
  1. Immediately before you call the rendering commands, call `ShaderUtil.SetAsyncCompilation`, and set it to `false`. Subsequent commands in the CommandBuffer won’t allow asynchronous compilation.
  2. Add the rendering commands to the CommandBuffer.
  3. After the rendering commands, call [`Shader.Util.RestoreAsyncCompilation`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.RestoreAsyncCompilation.html) to restore the state of asynchronous shader compilation.


Here is an example:
```
// Create the CommandBuffer
CommandBuffer cmd = new CommandBuffer();

// Disable async compilation for subsequent commands
ShaderUtil.SetAsyncCompilation(cmd, false);

/// Enter your rendering commands that should never use the placeholder shader, for example UI elements or characters.
cmd.DrawMesh(...);

// Restore the old state
ShaderUtil.RestoreAsyncCompilation(cmd);

```

## Disable asynchronous compilation for specific Shader objects
You can disable asynchronous shader compilation for specific **Shader objects** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject) by forcing the Editor to always compile them synchronously. This is a good option for data generating Shader objects that are always present at the start of your rendering, and which are relatively quick to compile. You would most likely need this if you are performing [advanced rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-avoid-cyan-placeholder-shaders.html).
To force synchronous compilation for a Shader object, add the `#pragma editor_sync_compilation` [directive](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html) to your shader source code.
**Note:** You should not force synchronous compilation for complex Shader objects that encounter new shader variants during rendering; this can stall rendering in the Editor.
## Custom Editor tools and asynchronous shader compilation
By default, asynchronous Shader compilation works in the Game and **Scene views** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView). If you want to use it in custom Editor tools, you can enable it via C# for your custom tool.
To do this, you can [enable asynchronous shader compilation for specific rendering calls](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-enable-or-disable.html#enabling-disabling-calls).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-introduction.html)
Introduction to asynchronous shader compilation
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-detect.html)
Detect asynchronous shader compilation
