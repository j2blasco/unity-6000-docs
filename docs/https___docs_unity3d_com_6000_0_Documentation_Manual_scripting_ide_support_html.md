* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-ide-support.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Environment and tools](https://docs.unity3d.com/6000.0/Documentation/Manual/environment-and-tools.html)
  * Integrated development environment (IDE) support


[](https://docs.unity3d.com/6000.0/Documentation/Manual/environment-and-tools.html)
Environment and tools
[](https://docs.unity3d.com/6000.0/Documentation/Manual/testing-editortestsrunner.html)
Automated testing
# Integrated development environment (IDE) support
An integrated development environment (IDE) is an application that combines a range of tools for developing software, typically including a code editor, code completion, code analysis and diagnostics, running tests, and debugging. Unity supports the following C# IDEs:
  * [Visual Studio](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-ide-support.html#visual-studio)
  * [Visual Studio Code](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-ide-support.html#vs-code)
  * [JetBrains Rider](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-ide-support.html#rider)


## External script editor preference
The **External Script Editor** setting in the [Preferences window](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html) determines which IDE Unity C# script files open in for editing. To change this setting, go to **Unity** > **Preferences** > **External Tools** > **External Script Editor**.
This setting is enough if all you want to do is open, view, or make simple edits to C# source files. A full IDE experience including code analysis and debugging typically requires additional plugins or extensions. Refer to the sections for each supported IDE below for more details.
## Visual Studio (Windows)
[Visual Studio](https://visualstudio.microsoft.com/downloads/) is the recommended IDE for Unity on Windows and is available in several editions, including a free Community tier for individual use. It’s recommended to always use the latest version where possible.
### Visual Studio configuration for debugging
In addition to your installation of Visual Studio, the full IDE experience including debugging Unity C# code requires:
For your Visual Studio IDE:
  * [Visual Studio Tools for Unity](https://docs.microsoft.com/en-us/visualstudio/gamedev/unity/get-started/visual-studio-tools-for-unity)


For your Unity Editor:
  * Unity [Visual Studio Editor package](https://docs.unity3d.com/Packages/com.unity.ide.visualstudio@latest/) (Included in a Unity Editor installation as part of the [Engineering feature set](https://docs.unity3d.com/6000.0/Documentation/Manual/DeveloperToolsFeature.html))
  * Visual Studio set as the external script editor (menu: **Unity** > **Preferences** > **External Tools** > **External Script Editor**).


New installations of the Unity Editor on Windows include Visual Studio Community and the other debugging requirements listed above by default. If you’re using a pre-existing installation of Visual Studio or the Unity Editor, you might need to install or configure some of the items manually.
For more information on the debugging features of the Unity Editor, refer to [Debug C# code in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html).
For more information on using Visual Studio with Unity, refer to [Using Visual Studio Tools for Unity](https://docs.microsoft.com/en-us/visualstudio/gamedev/unity/get-started/using-visual-studio-tools-for-unity?pivots=windows)
## Visual Studio Code (Windows, macOS, Linux)
[Visual Studio Code](https://code.visualstudio.com/download) is the recommended free IDE for Unity projects on macOS and Linux. It’s recommended to always use the latest version where possible.
### VS Code configuration for debugging
In addition to your installation of Visual Studio Code itself, the full IDE experience including debugging Unity C# code requires:
For your Visual Studio Code IDE:
  * [C# For Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
  * [C# Dev Kit for Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
  * [Unity for Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=visualstudiotoolsforunity.vstuc)


For your Unity Editor:
  * [Unity Visual Studio Editor package](https://docs.unity3d.com/Packages/com.unity.ide.visualstudio@latest/) 2.0.20+ (Included in a Unity Editor installation as part of the [Engineering feature set](https://docs.unity3d.com/6000.0/Documentation/Manual/DeveloperToolsFeature.html))
  * Visual Studio Code set as the external script editor (menu: **Unity** > **Preferences** > **External Tools** > **External Script Editor**).


New installations of the Unity Editor on macOS include Visual Studio Code and the other debugging requirements listed above by default. If you’re using a pre-existing installation of VS Code or the Unity Editor, you might need to install or configure some of the items manually.
**Note** : The Unity **Visual Studio Code** Editor package [com.unity.ide.vscode](https://docs.unity3d.com/Packages/com.unity.ide.vscode@latest) is no longer supported and should not be used. The **Visual Studio Editor** package [com.unity.ide.visualstudio](https://docs.unity3d.com/Packages/com.unity.ide.visualstudio@latest/) now supports Visual Studio Code in addition to Visual Studio.
For more information on the debugging features of the Unity Editor, refer to [Debug C# code in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html).
For information on using VS Code with Unity, refer to the VS Code documentation on [Unity Development with VS Code](https://code.visualstudio.com/docs/other/unity).
## JetBrains Rider (Windows, macOS, Linux)
[JetBrains Rider](https://www.jetbrains.com/rider/) is a feature-rich, paid C# IDE with comprehensive C# language and debugging support. It’s recommended to always use latest version where possible.
### Rider configuration for debugging
In addition to your installation of Rider itself, the full IDE experience including debugging Unity C# code requires:
For your Unity Editor:
  * [Unity JetBrains Rider package](https://docs.unity3d.com/Packages/com.unity.ide.rider@latest/) (Included in a Unity Editor installation as part of the [Engineering feature set](https://docs.unity3d.com/6000.0/Documentation/Manual/DeveloperToolsFeature.html)).
  * Rider set as the external script editor (menu: **Unity** > **Preferences** > **External Tools** > **External Script Editor**).


For more information on the debugging features of the Unity Editor, refer to [Debug C# code in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html).
For more information on using JetBrains Rider with Unity, refer to [Rider for Unity](https://www.jetbrains.com/lp/dotnet-unity/).
## Additional resources
  * [Debug C# code in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/environment-and-tools.html)
Environment and tools
[](https://docs.unity3d.com/6000.0/Documentation/Manual/testing-editortestsrunner.html)
Automated testing
