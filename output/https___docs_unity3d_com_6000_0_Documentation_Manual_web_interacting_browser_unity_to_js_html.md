* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-unity-to-js.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * Call Unity C# script functions from JavaScript


[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html)
Call JavaScript functions from Unity C# scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html)
Call C/C++/C# functions from Unity C# scripts
# Call Unity C# script functions from JavaScript
You might want to call some Unity code from your JavaScript **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) or browser code. For example, you might want a JavaScript UI element that triggers a Unity behaviour and needs access to that method. 
The recommended way to send data or notifications to the Unity C# script from the browser’s JavaScript is to use the `SendMessage` function to call methods on **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in your Unity project.
## Use the SendMessage helper function
Use `SendMessage` to call a Unity method of the Unity scripting API from JavaScript code. 
There are some restrictions for what sort of methods you can pass. You can only call methods of a GameObject, not general C# methods attached to other objects. Also, only use `SendMessage` to call a method if one of the following is true: 
  * The method takes no parameters.
  * The method has one parameter and that parameter is a single string.
  * The method has one parameter and that parameter is a single number.


Methods with more than one parameter or with parameters of other types can’t be called using `SendMessage`.
## Example SendMessage code
To make the call from a JavaScript plug-in embedded in your project, use the following code:
```
MyGameInstance.SendMessage(objectName, methodName, value);

```

  * `objectName` is the name of an object in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  * `methodName` is the name of a method in the script, currently attached to that object.
  * `value` can be a string, a number, or can be empty.


The following code is a further example that shows each of the types of methods that you can call with different parameters. 
```
MyGameInstance.SendMessage('MyGameObject', 'MyFunction');
MyGameInstance.SendMessage('MyGameObject', 'MyFunction', 5);
MyGameInstance.SendMessage('MyGameObject', 'MyFunction', 'MyString');

```

To make a call from the global scope of the embedding page, refer to [Call JavaScript functions from global scope](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html#global-scope).
## Additional resources
  * [Interaction with browser scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-interactingwithbrowserscripting.html)
  * [Set up your JavaScript plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js.html)
  * [Call JavaScript functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html)
  * [Call C/C++/C# functions from Unity C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html)
  * [Create callbacks between Unity C#, JavaScript, and C/C++/C# code](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-example.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browser-js-to-unity.html)
Call JavaScript functions from Unity C# scripts
[](https://docs.unity3d.com/6000.0/Documentation/Manual/web-interacting-browsers-c-to-unity.html)
Call C/C++/C# functions from Unity C# scripts
