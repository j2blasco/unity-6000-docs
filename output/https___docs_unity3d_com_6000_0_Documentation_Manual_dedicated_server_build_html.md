* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-build.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Dedicated Server](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server.html)
  * Build your application for Dedicated Server 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-optimizations.html)
Dedicated Server optimizations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-assetbundles.html)
Dedicated Server AssetBundles
# Build your application for Dedicated Server
You can create a Dedicated Server build in either of the following ways:
  * [Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-build.html#unity-editor)
  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-build.html#scripting)
  * [Command line](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-build.html#command-line)


## Unity Editor
To create a Dedicated Server build in the Unity Editor, use the following steps:
  1. Open the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) window from **File** > **Build Profiles**.
  2. Select **Add Build Profile** to open the **Platform Browser** window.
  3. Select the type of server to build from the list of available platforms. For example, select **Linux Server** to build a Linux server.
  4. If the server type isn’t available, select **Install with Unity Hub** and follow the installation instructions. For information on how to install modules, refer to [Add modules](https://docs.unity3d.com/hub/manual/AddModules.html).
  5. Select **Switch Profile** to set the new build profile as the active profile.
  6. Click **Build**.


**Tip** : You can further configure the Dedicated Server build in the [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-player-settings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings).
## Scripting
To create a Dedicated Server build using a script, set `buildPlayerOptions.subtarget` to `(int)StandaloneBuildSubtarget.Server`. 
```
buildPlayerOptions.target = BuildTarget.StandaloneWindows;
// SubTarget expects an integer.
buildPlayerOptions.subtarget = (int)StandaloneBuildSubtarget.Server;

```

## Command line
To create a Dedicated Server build through the command line, use the `-standaloneBuildSubtarget Server` [argument](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html).
```
-buildTarget Linux64 -standaloneBuildSubtarget Server

```

## Code sign macOS Dedicated Server builds
Dedicated Server builds that aren’t code signed might display security warnings when deployed on macOS systems. To avoid such warnings, make sure you code sign the build before distribution. For more information, refer to the documentation on [Code sign and notarize your macOS application](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-building-notarization.html). 
## Additional resources
  * [macOS build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/macosbuildsettings.html)
  * [Windows build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStandaloneBinaries.html)
  * [Linux build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/Buildsettings-linux.html)
  * [Creating and Using Scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-optimizations.html)
Dedicated Server optimizations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-assetbundles.html)
Dedicated Server AssetBundles
