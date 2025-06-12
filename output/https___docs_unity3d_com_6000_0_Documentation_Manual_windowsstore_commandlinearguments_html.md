* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-commandlinearguments.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
  * [Develop for Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-developing.html)
  * Command line arguments for UWP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-appcallbacks.html)
AppCallbacks class reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-assocation-launching.html)
Association launching for UWP
# Command line arguments for UWP
You can launch Unity Players from the command line and pass in arguments to change how the Player executes. Universal Windows Platform (UWP) apps don’t accept command line arguments by default, so you have to pass them to an AppCallbacks constructor in `App.xaml.cpp` or `App.cpp` to specify them.
This code example demonstrates how to do this:
```
m_AppCallbacks = 
    ref new AppCallbacks
    (
        ref new Platform::Array<Platform::String\^> 
        {
            L"-force-gfx-direct" 
        }
    );

```

For more information on command line arguments for UWP, refer to [Unity Standalone Player command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-appcallbacks.html)
AppCallbacks class reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-assocation-launching.html)
Association launching for UWP
