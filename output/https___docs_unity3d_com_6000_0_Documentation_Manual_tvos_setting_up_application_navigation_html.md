* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-setting-up-application-navigation.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [tvOS](https://docs.unity3d.com/6000.0/Documentation/Manual/tvOS-introducing.html)
  * [Developing for tvOS](https://docs.unity3d.com/6000.0/Documentation/Manual/tvOS-developing.html)
  * Setting up app navigation from the Unity UI


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-supporting-input-devices.html)
Supporting input devices on tvOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-debugging.html)
Debugging your tvOS application
# Setting up app navigation from the Unity UI
You must provide custom visual resources to the Apple Game Center for its native leaderboard **UI**. Here’s how to set them up in Xcode:
  1. Open the [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html) window in the Unity Editor. Find the first occurrence of the **Submit** virtual input, expand it, and change its **Alt Positive Button** to [**joystick button 14**](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-handle-game-controller-input.html#InputMapping).
  2. Select the EventSystem appObject in your ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)**. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)**, find the EventSystem component, and set a reference to the UI appObject that should receive initial focus in the **First Selected** property. You might need to enable the **Force input module** property in the **Standalone Input Module** component.#


**Note** : Apple TV Remote navigation doesn’t work while your app is running in the TV Simulator.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-supporting-input-devices.html)
Supporting input devices on tvOS
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tvos-debugging.html)
Debugging your tvOS application
