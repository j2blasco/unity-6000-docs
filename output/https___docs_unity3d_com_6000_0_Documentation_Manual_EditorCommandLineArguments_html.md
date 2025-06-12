* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Command-line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html)
  * Unity Editor command line arguments


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html)
Command-line arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html)
Unity Standalone Player command line arguments
# Unity Editor command line arguments
You can launch the Unity Editor from the command line and pass in arguments to change how the Editor launches. You can also use the command line to execute specific methods from your project’s C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) at launch. Check the [example script for executing methods at launch](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html#example-execute-methods).
**Note** : To use the information on this page, you need to know how to use your operating system’s command line interface to launch applications and run command line arguments.
When launching the Unity Editor, the delimiter for a command-line argument value is a single space. For example, to set the window mode to borderless, use `-window-mode borderless`.
## Launching Unity
To launch a Unity project via the command prompt or Terminal, enter the directory path for the Unity application, followed by `-projectPath` and the directory path for the target project. 
The following instructions assume that the Unity Editor is installed in the default location through the Unity Hub.
On macOS, type the following into the Terminal to launch Unity:
`/Applications/Unity/Hub/Editor/<version>/Unity.app/Contents/MacOS/Unity -projectPath <project path>`
On Linux, type the following into the Terminal to launch Unity:
`/home/<user>/Unity/Hub/Editor/<version>/Editor/Unity -projectPath <project path>`
On Windows, type the following into the Command Prompt to launch Unity:
`"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -projectPath "<project path>"`
When you launch Unity like this, it receives commands and information on startup, which can be useful for test suites, automated builds and other production tasks.
**Notes** : 
  * Adjust the path in the command if you use Unity Editor installed in a different location. For more information about how to find your Editor’s location path, refer to [Install and uninstall Editor versions](https://docs.unity3d.com/hub/manual/AddEditor.html#locate-the-editor-program-file).
  * When passing arguments on the Windows platform, make sure the directory path doesn’t end with a single backslash to prevent syntax errors. Use either double backslashes (`\\`) or no backslash. For example,
    * `"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -projectPath "C:\MyUnityProjects\MyProject"`
    * `"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -createProject "C:\MyUnityProjects\MyProject\\"`


## Configuration arguments
You can run the Unity Editor and build Unity applications with additional commands and information on startup. This page lists the command line arguments you can use to launch and configure Unity Editor and Unity Player instances.
**Command** | **Details:**  
---|---  
`-createProject <pathname>` | Create an empty project at the given path.  
`-consistencyCheck` | Performs an [importer consistency check](https://docs.unity3d.com/6000.0/Documentation/Manual/ImporterConsistency.html) on Editor startup. By default Unity performs a `local` check, which forces a reimport of all assets locally. It also checks if the import differs from the previous import.  
`-consistencyCheckSourceMode string` | Sets the source to check against when Unity compares the asset imports. Choose from the following values:
  * `local`: Forces a reimport of all assets locally and checks if the import differs from the previous import.
  * `cacheserver`: If you have enabled [Unity Accelerator](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html), this option gets the [metadata for the assets](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetMetadata.html) from the cache server and compares if the results locally match what is on the cache server. This option doesn’t reimport all assets.

For more information, refer to [Check the consistency of an importer](https://docs.unity3d.com/6000.0/Documentation/Manual/ImporterConsistency.html).  
`-disable-assembly-updater <assembly1 assembly2>` | Specify a space-separated list of assembly names as parameters for Unity to ignore on automatic updates.  
  
The space-separated list of assembly names is optional: pass the command line options without any assembly names to ignore all assemblies, as in example 1.  
  
**Example 1**  
`unity.exe -disable-assembly-updater`  
  
**Example 2**  
`unity.exe -disable-assembly-updater A1.dll subfolder/A2.dll`  
  
Example 2 has two assembly names, one with a pathname. Example 2 ignores `A1.dll`, no matter what folder it is stored in, and ignores `A2.dll` only if it is stored under `subfolder` folder:  
  
If you list an assembly in the `-disable-assembly-updater` command line parameter (or if you don’t specify assemblies), Unity logs the following message to [Editor.log](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html):  
  
`[Assembly Updater] warning: Ignoring assembly [assembly_path] as requested by command line parameter.”).`  
  
Use this to avoid unnecessary [API Updater](https://docs.unity3d.com/6000.0/Documentation/Manual/APIUpdater.html) overhead when you import assemblies.  
  
This argument is useful if you want to import assemblies that access a Unity API which doesn’t need updating. It’s also useful when you import assemblies which don’t access any Unity APIs (for example, if you have built some or all of your source code outside of Unity, and you want to import the resulting assemblies into your Unity project).  
  
**Note** : If you disable the update of any assembly that needs updating, you might get errors at compile time, run time, or both, that are hard to track.  
`-disable-gpu-skinning` | Disable Graphics Processing Unit (GPU) **skinning** The process of binding bone joints to the vertices of a character’s mesh or ‘skin’. Performed with an external tool, such as Blender or Autodesk Maya. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingHumanoidChars.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skinning) at startup.  
`-executeMethod <ClassName.MethodName>` or `-executeMethod <NamespaceName.ClassName.MethodName>` | Execute the static method as soon as Unity opens the project, and after the optional Asset server update is complete. You can use this for tasks such as continuous integration, performing Unit Tests, making builds or preparing data.  
  
To return an error from the command line process, either throw an exception which causes Unity to exit with return code 1, or call [EditorApplication.Exit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.Exit.html) with a non-zero return code.  
  
To pass parameters, add them to the command line and retrieve them inside the function using `System.Environment.GetCommandLineArgs`. To use `-executeMethod`, you need to place the enclosing script in an Editor folder. The method you execute must be defined as static.  
`-exportPackage <exportAssetPath1 exportAssetPath2 ExportAssetPath3 exportFileName>` | Export a package, given a path (or set of given paths). In this example, `exportAssetPath` is a folder (relative to the Unity project root) to export from the Unity project, and `exportFileName` is the package name. This option only exports whole folders at a time. You normally need to use this command with the `-projectPath` argument.  
`-importPackage <pathname>` | Import the given [asset package](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackagesCreate.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetPackages.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Assetpackage). Unity doesn’t display any import dialog.  
`-job-worker-count <N>` | Specify the maximum thread count for the Unity JobQueue [Job Worker Count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobWorkerMaximumCount.html).  
`-gc-helper-count <N>` | Specify the number of asset garbage collector helper threads. The default value is the number of cores available.  
`-logFile <pathname>` | Specify where Unity writes the Editor or operating system’s standalone log file. To output to the console, specify `-` for the path name. On Windows, use `-logfile` to direct the output to `stdout`, which by default isn’t the console. Also refer to `-upmLogFile`.  
`-noUpm` | Disables the Unity Package Manager.  
`-openfile <path>` | Open the project from a path to a scene or package file. Alternatively, you can use the `-projectPath` argument  
`-password <password>` | Enter a password into the log-in form during the activation of the Unity Editor.  
`-projectPath <pathname>` | Open the project at the given path, which can be absolute or relative to the current working directory. If the pathname contains spaces, enclose it in quotes.  
`-quit` | Quit the Unity Editor after other commands have finished executing. This can hide some error messages, but they still appear in the Editor’s [log file](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html). The `-quit` argument has the following limitations:
  * If the Editor is connected to the Accelerator Cache Server, then the additional argument `-cacheServerWaitForUploadCompletion` is required to prevent Unity quitting before pending cache uploads can complete.
  * If the Editor is running tests with the `-runTests` argument, then `-quit` causes the Editor to quit immediately, before in-progress tests have chance to complete.
  * If the Editor is running asynchronous code, then `-quit` can cause the application to hang and become unresponsive.

  
`-releaseCodeOptimization` | Enables release code optimization mode, overriding the current default code optimization mode for the session.  
`-setDefaultPlatformTextureFormat` (Android only) | Set the default texture **compression** to the desired format before you import a texture or build the project. This is so you don’t have to import the texture again with the format you want. The available formats are dxt, pvrtc, atc, etc, etc2, and astc. This argument is ignored when [texture compression targeting](https://docs.unity3d.com/6000.0/Documentation/Manual/android-distribution-google-play.html#texture-compression-targeting) is enabled.  
**Note** : PVRTC format is deprecated. Use ASTC or ETC format instead.  
`-overrideMaxTextureSize` | Overrides the maximum texture size (in pixels) that Unity applies when importing assets. This setting affects all textures in your project, and overrides any **Max Size** configured for individual textures in the [texture import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html). The value is an integer that represents a maximum limit on either the height or width of the texture, whichever is longer. **Aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio) is always maintained when resizing. For example, if a texture is 2048x1024 **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) but `-overrideMaxTextureSize` is set to 512, Unity imports the texture at a size of 512x256 pixels. For more details, refer to [EditorUserBuildSettings.overrideMaxTextureSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-overrideMaxTextureSize.html).  
`-overrideTextureCompression` | Overrides the texture **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) settings that Unity uses when it imports assets. This is particularly useful during local development, to speed up texture importing or build target switching. For details, refer to [EditorUserBuildSettings.overrideTextureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-overrideTextureCompression.html).  
`-silent-crashes` | Prevent Unity from displaying the dialog that appears when a Standalone Player crashes. This argument is useful when you want to run the Player in automated builds or tests, where you don’t want a dialog prompt to obstruct automation.  
`-upmLogFile <pathname>` | Specify the path and file name where Unity writes the log file for the UPM background application, which runs independently of the Editor. You can specify `-upmLogFile` and `-logFile` in the same command. If you include both arguments, you can specify independent paths for the two log files.  
`-username <username>` | Enter a username into the log-in form during the activation of the Unity Editor.  
`-vcsMode <mode>` | Set the version control mode. Available modes are `"Visible Meta Files"`, `"Hidden Meta Files"`, `Perforce`, and `PlasticSCM`. You can use additional flags to fill out the configuration fields for the given version control mode. These flags are based on the [Provider.GetActiveConfigFields](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetActiveConfigFields.html) method. For example, you can use the `-vcPerforceUsername`, `-vcPerforcePassword`, `-vcPerforceWorkspace` and `-vcPerforceServer` to set the Perforce username, workspace and server fields.  
  
**Note** : `<mode>` arguments that contain spaces must be wrapped in double quotes (“).| |`-vcsModeSession <mode>`|Set the version control mode for this session. Available modes are `"Visible Meta Files"`, `"Hidden Meta Files"`, `Perforce`, and `PlasticSCM`. You can use additional flags to fill out the configuration fields for the given version control mode. These flags are based on the [Provider.GetActiveConfigFields](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetActiveConfigFields.html) method. For example, you can use the `-vcPerforceUsername`, `-vcPerforcePassword`, `-vcPerforceWorkspace` and `-vcPerforceServer` to set the Perforce username, workspace and server fields.  
  
**Note** : `<mode>` arguments that contain spaces must be wrapped in double quotes (”).  
`-version` | Print the version number of the Unity Editor in the command line, without launching the Editor.  
`-timestamps` | Prefixes every [Editor.log](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html) message with the current timestamp and thread ID.  
## Batch mode arguments
Use the following arguments to configure Unity’s batch mode. Batch mode enables Unity to run predefined tasks without user input, which makes batch mode useful for automated tasks like testing. For more information, see [Batch mode and built-in coroutine compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/CLIBatchmodeCoroutines.html).
**Command** | **Details:**  
---|---  
`-accept-apiupdate` | Use this command line option to specify that APIUpdater should run when Unity is launched in batch mode.  
  
Example:  
`unity.exe -accept-apiupdate -batchmode [other params]`  
  
The APIUpdater doesn’t run if you omit this command line argument when you launch Unity in batch mode. This might lead to compiler errors.  
`-batchmode` | Run Unity in batch mode. In batch mode, Unity runs command line arguments without the need for human interaction. It also suppresses pop-up windows that require human interaction (such as the Save Scene window). You should always run Unity in batch mode when using command line arguments, because it allows automation to run without interruption.  
  
When an exception occurs during execution of the script code, the Asset server updates fail, or other operations fail, Unity immediately exits with return code **1**.  
  
In batch mode, Unity sends a minimal version of its log output to the console. However, the [Log Files](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html) still contain the full log information. You can’t open a project in batch mode while the Editor has the same project open; only a single instance of Unity can run at a time.  
  
To check whether the Editor or Standalone Player is running in batch mode, use the [Application.isBatchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isBatchMode.html) operator.  
  
If the project has not yet been imported when using `-batchmode`, the target platform is the default one. To force a different platform, use the `-buildTarget` option.  
`‑ignorecompilererrors` | When you use this argument, Unity continues to start your application even if there are compilation errors.  
`-nographics` | When you run this in batch mode, Unity doesn’t initialize the graphics device. You can then run automated workflows on machines that don’t have a GPU. Automated workflows only work when you have a window in focus, otherwise you can’t send simulated input commands. `-nographics` does not allow you to bake GI, because Enlighten Realtime Global Illumination requires a GPU for Meta Pass rendering (See the [Meta Pass section of the Lightmapping and Shaders page](https://docs.unity3d.com/6000.0/Documentation/Manual/MetaPass.html) for more information).   
**Note** : Output logs are turned off in this mode. To enable the creation of output logs, specify a file location using the command `-logFile`.  
## Build Arguments
Use the following arguments to build players for various platforms from the command line. For more information about building players with command line arguments, refer to [Unity Standalone Player command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html).
**Command** | **Details:**  
---|---  
`-activeBuildProfile <pathname>` | Set the build profile saved at the given path as an active build profile (for example, `-activeBuildProfile "Assets/Settings/Build Profiles/WindowsDemo.asset"`).   
  
**Note:** `-activeBuildProfile <pathname>` applies custom scripting defines found in the **Build data** section of the active build profile before compilation. These scripting defines are additive and don’t override other scripting defines in your project.  
`-build <pathName>` | Build a Player from `activeBuildProfile <pathname>` to the specified target path. For some platforms, the path must end with a file extension specific to the target platform. For example, `-build path/to/your/build.exe`. For information on which platforms require the extensions, refer to [Build path requirements for target platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/build-path-requirements.html).  
`-buildLinux64Player <pathname>` | Build a 64-bit standalone Linux player (for example, `-buildLinux64Player path/to/your/build`).  
`-buildLinuxHeadlessSimulation <pathname>` | Build a 64-bit Linux headless simulation player (for example, `-buildLinuxHeadlessSimulation path/to/your/build`).  
`-buildOSXUniversalPlayer <pathname>` | Build a 64-bit standalone macOS player (for example, `-buildOSXUniversalPlayer path/to/your/build.app`).  
`-buildTarget <name>` | Select an active build target to launch the Editor in. The options available to you depend on which build targets you have enabled in the Editor. These options correspond to the options available to you via the API enumeration [`BuildTarget`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html). Possible options include:   
  
• `win64`  
• `win`  
• `osxuniversal`  
• `linux64`  
• `android`  
• `ios`  
• `webgl`  
• `tvos`  
• `windowsstoreapps`  
• `cloudrendering`  
• `visionos`  
  
If you are a developer with access to Closed platforms, you might have other `-buildTarget` options available. For details, see the documentation for your target platform.  
`-standaloneBuildSubtarget <name>` | Select an active build subtarget for the Standalone platforms before loading a project. Possible options are:   
  
• Player  
• Server  
`-buildWindowsPlayer <pathname>` | Build a 32-bit standalone Windows player (for example, `-buildWindowsPlayer path/to/your/build.exe`).  
`-buildWindows64Player <pathname>` | Build a 64-bit standalone Windows player (for example, `-buildWindows64Player path/to/your/build.exe`).  
## Unity Accelerator cache server arguments
Use the following arguments to configure Unity’s use of the [Unity Accelerator](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html) cache server. These arguments override any corresponding configuration stored in the Editor Preferences.
**Command** | **Details:**  
---|---  
`-EnableCacheServer` | Enable Unity Accelerator. You must also use `-cacheServerEndpoint <host:port>` to specify the address of the Unity Accelerator instance.  
`-cacheServerEndpoint <host:port>` | Specifies the endpoint address of the Unity Accelerator instance.  
  
Example:  
`-cacheServerEndpoint 127.0.0.1:10080`  
The default port is `10080` but can be changed during installation.  
`-cacheServerNamespacePrefix <prefix>` | Set the namespace prefix for the Unity Accelerator instance. Use this argument with a namespace name to partition data on the cache server, for example to isolate cache data for different projects or Unity versions.  
  
Example:  
`-cacheServerNamespacePrefix MyProject_Unity23LTS`   
A prefix that contains spaces must be wrapped in double quotes (`"`).  
The supplied name is used as the prefix for up to 3 namespaces in the cache which separate data by type - metadata, artifact data and shader cache data.  
`-cacheServerEnableDownload true`  
`-cacheServerEnableDownload false` | Enable or disable downloading from the Unity Accelerator instance.  
`-cacheServerEnableUpload true`  
`-cacheServerEnableUpload false` | Enable or disable uploading to the Unity Accelerator instance.  
  
Example:  
`-cacheServerEnableUpload true`  
`-cacheServerWaitForConnection <ms>` | Specify the time in milliseconds that Unity will wait for a connection to the Unity Accelerator instance while loading a project, before starting the initial project refresh.  
  
Example:  
`-cacheServerWaitForConnection 5000`  
`-cacheServerWaitForUploadCompletion` | Prevent Unity from closing until any pending Unity **Accelerator** The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Accelerator) uploads are complete. This is recommended when Unity Accelerator is used in combination with the command line argument `-quit`, which closes the Unity Editor after other scripted commands have finished executing.  
`-cacheServerDownloadBatchSize <batchSize>` | Set the number of artifacts in individual cache server download batches. Download batches are an optimization used to reduce the number of download operations by grouping individual downloads into larger batches.  
  
Example:  
`-cacheServerDownloadBatchSize 256`  
Default value is `128`.  
`-cacheServerUploadExistingImports` | Upload any existing imports that haven’t been previously uploaded when Unity begins to upload new imports to the Unity Accelerator instance. Imports that have been previously uploaded aren’t re-uploaded.  
`-cacheServerUploadAllRevisions` | Upload any existing imports including all previous revisions known to the Asset Database that haven’t previously been uploaded when Unity begins to upload new imports to the Unity Accelerator instance. Import revisions that have been previously uploaded, aren’t re-uploaded.  
`-cacheServerUploadExistingShaderCache` | Upload any existing **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) cache imports that haven’t previously been uploaded when Unity begins to upload new imports to the cache server. Shader imports that have been previously uploaded, aren’t re-uploaded.  
## Debugging arguments
**Command** | **Details:**  
---|---  
`-disableManagedDebugger` | Disables the debugger listen socket.  
`-diag-debug-shader-compiler` | Unity launches only one instance of the **Shader** Compiler, and forces its timeout to be one hour. Useful for debugging Shader Compiler issues.  
`-debugCodeOptimization` | Enables debug code optimization mode, overriding the current default code optimization mode for the session.  
`-enableCodeCoverage` | Enables code coverage and allows access to the [Coverage API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.html).  
`-force-d3d12-debug` | Enables the DX12 validation layer. This is useful for working on **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) plugins or native plugins.  
`-force-d3d12-debug-gbv` | Enables the DX12 GPU-based validation. This is useful for working on XR plugins or native plugins.  
`-force-vulkan-layers` | Enables the Vulkan validation layer. This is useful for working on XR plugins or native plugins.  
`-stackTraceLogType` | Allow detailed debugging. All settings allow **None** , **Script Only** and **Full** to be selected (for example, `-stackTraceLogType Full`).  
`-log-memory-performance-stats` | Adds detailed memory and performance reports to the main Unity Editor log file when closing the editor.  
`-wait-for-managed-debugger` | Makes the Editor wait for a managed debugger to attach before launching. Generates a dialog that displays the Editor’s process ID. For more information on managed debugging, refer to [Debug C# code in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html#DebugInEditor).  
`-wait-for-native-debugger` | Makes the Editor wait for a native debugger to attach before launching. Generates a dialog that displays the Editor’s process ID.  
## Graphics API arguments
Use the following arguments to force the Unity Editor to use a specific graphics API.
**Command** | **Details:**  
---|---  
`-force-d3d11` (Windows only) | Make the Editor use Direct3D 11 for rendering. Normally the graphics API depends on ****Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings)** (typically defaults to D3D11).  
`-force-d3d12` (Windows only) | Make the Editor use Direct3D 12 for rendering. Normally the graphics API depends on **Player Settings**.  
`-force-opengl` | Make the Editor use the legacy OpenGL back end.  
`-force-glcore` | Make the Editor use OpenGL 3/4 core profile for rendering. The Editor tries to use the best OpenGL version available and all OpenGL extensions exposed by the OpenGL drivers. If the platform isn’t supported, the editor uses Direct3D.  
`-force-glcoreXY` | Similar to`-force-glcore`, but requests a specific OpenGL context version. Accepted values for XY: 32, 33, 40, 41, 42, 43, 44, or 45. If the platform doesn’t support a specific version of OpenGL, Unity will fallback to a supported version.  
`-force-gles` (Windows only) | Make the Editor use OpenGL for Embedded Systems for rendering. The Editor tries to use the best OpenGL ES version available, and all OpenGL ES extensions exposed by the OpenGL drivers.  
`-force-glesXY` (Windows only) | Similar to `-force-gles`, but requests a specific OpenGL ES context version. Accepted values for XY: 30, 31, 31aep, or 32. If the platform doesn’t support a specific version of OpenGL ES, Unity will fallback to a supported version. If the platform doesn’t support OpenGL ES, Unity will fallback to another graphics API.  
`-force-vulkan` | Make the Editor use Vulkan for rendering. Normally the graphics API depends on **Player Settings**.  
`-force-clamped` | Use this with `-force-glcoreXY` to prevent Unity from checking for additional OpenGL extensions, allowing it to run between platforms with the same code paths. This approach helps to determine if an issue is platform-specific. For example, a driver bug.  
## License arguments
Use the following arguments to process a Unity license or run the Unity Editor with different license options.
**Command** | **Details:**  
---|---  
`-createManualActivationFile` | Step one of a [three-step process](https://docs.unity3d.com/6000.0/Documentation/Manual/ManualActivationGuide.html) to manually activate a Unity license. For more information, refer to [Manual license activation](https://docs.unity3d.com/6000.0/Documentation/Manual/ManualActivationGuide.html).  
`-manualLicenseFile <yourulffile>` | Step three of a [three-step process](https://docs.unity3d.com/6000.0/Documentation/Manual/ManualActivationGuide.html) to manually activate a Unity license. For more information, refer to [Manual license activation](https://docs.unity3d.com/6000.0/Documentation/Manual/ManualActivationGuide.html).  
`-returnlicense` | Return the currently active serial-based or named user license. Do not use `-returnlicense` to return a floating license. For more information, refer to [Returning your license](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagingYourUnityLicense.html#license-return-cli). For more information about licensing models, refer to [Licensing overview](https://docs.unity3d.com/6000.0/Documentation/Manual/LicenseOverview.html).  
`-serial <serial-key>` | Activate your paid Unity license. Include the `<serial-key>` value to activate a serial-based license, or to activate a named user license and its serial key simultaneously. Exclude the `<serial-key>` value to activate a named user license without activating its serial key. For more information, refer to [Activate a license from the command line](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagingYourUnityLicense.html#license-activation-cli). For more information about licensing models, refer to [Licensing overview](https://docs.unity3d.com/6000.0/Documentation/Manual/LicenseOverview.html).  
  
**Note** : When you use the `-serial` argument, you must also use the `-batchmode` argument. It’s also good practice to specify the `-quit` argument.  
## Metal arguments (macOS only)
Use the following arguments to configure Unity’s use of the [Metal](https://docs.unity3d.com/6000.0/Documentation/Manual/Metal.html) graphics API for Apple devices.
**Command** | **Details:**  
---|---  
`-force-device-index` | When using Metal, make the Editor use a particular GPU device by passing it the index of that GPU (macOS only).  
`-force-low-power-device` (macOS only) | If you use Metal, make the Editor use a low power device.  
`-force-metal` | Make the Editor use Metal as the default graphics API (macOS only).  
`-enable-metal-capture` | Enable the ability to take Metal captures from inside the Editor.  
## Profiler arguments
Use the following arguments to configure Unity’s use of the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler).
**Command** | **Details:**  
---|---  
`-deepprofiling` | Enable Deep Profiling option for the [CPU profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html).  
`-profiler-enable` | Profile the start-up of a Player or the Editor. When you use this argument with a Player, it has the same effect as building the Player with the **Autoconnect Profiler** option enabled in [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile).  
  
When you use this argument with the Editor, it starts collecting and displaying Profiler information in the Profiler window on start-up of the Editor.  
`-profiler-log-file <Path/To/Log/File.raw>` | This argument sets up the [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html) to stream the profile data to a .raw file on startup. It works for both Players and the Editor.  
`-profiler-capture-frame-count <NumberOfFrames>` | This argument sets how many frames the Profiler should capture in a profile when streaming to a .raw file on start-up. It only works on Players.  
`-profiler-maxusedmemory` | By default, `maxUsedMemory` for the Unity Profiler is 16MB for Players and 256MB for the Editor. You can use this argument to set the `maxUsedMemory` parameter to a custom size at start-up (for example, `-profiler-maxusedmemory 16777216`). The size is set in bytes.  
## Unity Editor special command line arguments
You should only use these under special circumstances, or when directed by Unity Support.
**Command** | **Details:**  
---|---  
`-enableIncompatibleAssetDowngrade` | Use this when you have Assets made by a newer, incompatible version of Unity, that you want to downgrade to work with your current version of Unity.  
When you enable this, Unity presents you with a dialog asking for confirmation of this downgrade if you attempt to open a project that would require it.  
  
Note: This procedure is unsupported and highly risky, and should only be used as a last resort.  
`-giCustomCacheLocation` | Sets a custom location for the [Global Illumination (GI) cache](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html) folder. The value must be an absolute path, which must be enclosed in quotes if it contains any spaces. If `-giCustomCacheLocation` is set, then for the current Editor session its value overrides any custom **Cache Folder Location** previously defined in the [GI Cache preferences](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html#gi-cache). This value does not persist after the Editor quits.  
## Unity Hub special command line arguments
You should only use these under special circumstances, or when directed by Unity Support. These arguments are used in versions of the Unity Editor that do not use the Unity Hub by default.
**Command** | **Details:**  
---|---  
`-useHub` | Launch the Unity Editor with Hub integration.  
`-hubIPC` | Enable communication and interaction between the Unity Editor and the Unity Hub.  
`-hubSessionId` | Specify a unique identifier for a Unity Hub session.  
In all supported versions of the Unity Editor, these arguments are already set by default.
## Extra Editor arguments from packages
Additional Editor command line arguments are available when these packages are installed.
**Package** | **Details:**  
---|---  
Burst | See [Burst](https://docs.unity3d.com/Packages/com.unity.burst@latest/) package documentation.  
Test Framework | See [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest/) package documentation.  
Code Coverage | See [Code Coverage](https://docs.unity3d.com/Packages/com.unity.testtools.codecoverage@1.2/manual/CoverageBatchmode.html) package documentation.  
## Example script for executing methods at launch
You can use the command line to execute specific methods from your project’s C# scripts at launch. The following examples demonstrate a C# script, and the command line arguments that execute methods from that script at launch.
An example C# script in the project:
```
using UnityEditor;
class MyEditorScript
{
     static void PerformBuild ()
     {
        BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions();
        buildPlayerOptions.scenes = new[] { "Assets/Scene1.unity", "Assets/Scene2.unity" };
        BuildPipeline.BuildPlayer(buildPlayerOptions);
     }
}

```

The following command executes Unity in batch mode, executes the `MyEditorScript.PerformBuild` method from the above script, and then quits upon completion.
**Windows:**
```
"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -quit -batchmode -projectPath "C:\Users\UserName\Documents\MyProject" -executeMethod
MyEditorScript.PerformBuild

```

**macOS:**
```
/Applications/Unity/Hub/Editor/<version>/Unity.app/Contents/MacOS/Unity -quit -batchmode -projectPath ~/UnityProjects/MyProject -executeMethod
MyEditorScript.PerformBuild

```

**Note:** In the Editor path, replace `<version>` with the version of Unity you want to launch, or replace the path entirely if your Unity Editor path is not the default. 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html)
Command-line arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerCommandLineArguments.html)
Unity Standalone Player command line arguments
