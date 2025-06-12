* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/test-conditional-compilation.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * [Conditional compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/conditional-compilation.html)
  * Test conditional compilation


[](https://docs.unity3d.com/6000.0/Documentation/Manual/custom-scripting-symbols.html)
Custom scripting symbols
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
Organizing scripts into assemblies
# Test conditional compilation
The following example shows how to test your conditionally compiled code. It also prints a message based on the platform selected for the target build.
## Sample code
```

  using UnityEngine;
  using System.Collections;
  public class PlatformDefines : MonoBehaviour {
  void Start () {

    #if UNITY_EDITOR
      Debug.Log("Unity Editor");
    #endif

    #if UNITY_IOS
      Debug.Log("Unity iOS");
    #endif

    #if UNITY_STANDALONE_OSX
        Debug.Log("Standalone OSX");
    #endif

    #if UNITY_STANDALONE_WIN
      Debug.Log("Standalone Windows");
    #endif

  }          
  } 

```

## Test instructions
  1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
  2. Check that the platform you want to test your code on is the Active platform profile. If it isn’t, select your preferred platform and click **Switch Profile**.
  3. Create a [script](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html) and copy and paste the [sample code](https://docs.unity3d.com/6000.0/Documentation/Manual/test-conditional-compilation.html#Sample).
  4. In the [Game view](https://docs.unity3d.com/6000.0/Documentation/Manual/GameView.html) **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar), click the Play button to enter Play mode. Confirm that the code works by checking for messages relevant to the platform selected in the Unity console. For example, if you choose iOS, the messages `Unity Editor` and `Unity iOS` appear in the console.


## Additional resources
  * [Unity scripting symbol reference](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-symbol-reference.html)
  * [Custom scripting symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/custom-scripting-symbols.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/custom-scripting-symbols.html)
Custom scripting symbols
[](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html)
Organizing scripts into assemblies
