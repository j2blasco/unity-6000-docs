* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-build-command-line.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Embedded systems](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-systems.html)
  * [Embedded Linux](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux.html)
  * [Build and deliver for Embedded Linux](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-build-and-deliver.html)
  * Build for Embedded Linux from the command line 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-build-settings.html)
Embedded Linux build settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-deploy.html)
Deploy an Embedded Linux project
# Build for Embedded Linux from the command line
To build a Unity project for the Embedded Linux system on the command line interface (CLI), you must have the Unity Editor installed on the build host. The build host can be a Linux, Windows, or macOS machine.
The following example uses the Linux variant of the executable (`Unity`), but you can replace it with an equivalent executable for your preferred build host’s operating system.
## Command line arguments
To instruct Unity to start in CLI mode and build the project at `<path-to-unity-project-root>` for Embedded Linux, run the following command:
```
Unity -quit -batchmode -nographics -buildTarget EmbeddedLinux -executeMethod Builder.Build -projectPath <path-to-unity-project-root>

```

The build process also calls the function `Builder.Build` to continue with the build setup process.
## Build script
You can put the example build script `Assets/Editor/` for the project to be built from the command line. Use the `-executeMethod` option to call the `Build()` method of this class, which sets up the build options and triggers the build.
For more information, refer to the [`BuildPipeline.BuildPlayer` API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html).
```
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEngine;

public class Builder
{
    private static void BuildEmbeddedLinux(EmbeddedLinuxArchitecture architecture)
    {
        // Set architecture in BuildSettings
        EditorUserBuildSettings.selectedEmbeddedLinuxArchitecture = architecture;

        // Setup build options (e.g. scenes, build output location)
        var options = new BuildPlayerOptions
        {
            // Change to scenes from your project
            scenes = new[]
            {
                "Assets/Scenes/SampleScene.unity",
            },
            // Change to location the output should go
            locationPathName = "../EmbeddedLinuxPlayer/",
            options =  BuildOptions.CleanBuildCache | BuildOptions.StrictMode,
            target = BuildTarget.EmbeddedLinux
        };

        var report = BuildPipeline.BuildPlayer(options);

        if (report.summary.result == BuildResult.Succeeded)
        {
            Debug.Log($"Build successful - Build written to {options.locationPathName}");
        }
        else if (report.summary.result == BuildResult.Failed)
        {
            Debug.LogError($"Build failed");
        }
    }

    // This function will be called from the build process
    public static void Build()
    {
        // Build EmbeddedLinux ARM64 Unity player
        BuildEmbeddedLinux(EmbeddedLinuxArchitecture.Arm64);
    }
}

```

## Additional resources:
  * [BuildPipeline.BuildPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-build-settings.html)
Embedded Linux build settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-deploy.html)
Deploy an Embedded Linux project
