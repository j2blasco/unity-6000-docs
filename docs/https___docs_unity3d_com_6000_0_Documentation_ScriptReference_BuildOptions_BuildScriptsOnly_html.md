* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.BuildScriptsOnly.html

#  [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html).BuildScriptsOnly
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Only build the scripts in a project.
Before you can use `BuildScriptsOnly`, you need to build the whole Project. Then you can run builds that only have script changes. Rebuilding the player data will be skipped for faster iteration speed.  
  
Platforms which support the incremental build pipeline will automatically run scripts only builds if Unity detects that the data files have not changed, even if `BuildScriptsOnly` is not used. You can still use `BuildScriptsOnly` to force a script only build and ignore any pending player data changes.  
  
The following script example uses `BuildScriptsOnly`. The script builds the entire Project initially. After you've run the script for the first time, you can use the script to only compile any changes you make to the script. To try this out, add the following Editor script and the game script to your project.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class EditorExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Build scripts")]
    public static void MyBuild()
    {
        BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) buildPlayerOptions = new BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html)();
        buildPlayerOptions.scenes = new[] { "Assets/scene.unity" };
        buildPlayerOptions.locationPathName = "scriptBuilds";
        buildPlayerOptions.target = BuildTarget.StandaloneOSX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneOSX.html);  
  
        // use these options for the first build
        buildPlayerOptions.options = BuildOptions.Development[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html);  
  
        // use these options for building scripts
        // buildPlayerOptions.options = BuildOptions.BuildScriptsOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.BuildScriptsOnly.html) | BuildOptions.Development[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html);  
  
        BuildPipeline.BuildPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)(buildPlayerOptions);
    }
}

```

Attach the following simple script to an empty GameObject in the scene:
```
using UnityEngine;  
  
// Change the camera to the usual blue color and display a label.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Awake()
    {
        cam = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);
        cam.clearFlags = CameraClearFlags.SolidColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraClearFlags.SolidColor.html);
    }  
  
    void OnGUI()
    {
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 100, 100, 50), "ExampleClass");
    }
}

```

Now run the `Build/Build scripts` example. This builds an executable. Run that executable and a dark blue window with the label appears. Next add some cubes and spheres to the Project. Make the following script changes:
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    // added line
    private float delay;  
  
    void Awake()
    {
        delay = 0.0f;
        cam = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);
        cam.clearFlags = CameraClearFlags.SolidColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraClearFlags.SolidColor.html);
    }  
  
    // added script code
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        delay = delay + Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        if (delay > 0.5f)
        {
            cam.backgroundColor = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.0f, 0.0f, Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0.0f, 0.25f));
            delay = 0.0f;
        }
    }  
  
    void OnGUI()
    {
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 100, 100, 50), "ExampleClass");
    }
}

```

Finally, swap the commented lines in the `EditorExample` script:
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class EditorExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build/Build scripts")]
    public static void MyBuild()
    {
        BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) buildPlayerOptions = new BuildPlayerOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html)();
        buildPlayerOptions.scenes = new[] { "Assets/scene.unity" };
        buildPlayerOptions.locationPathName = "scriptBuilds";
        buildPlayerOptions.target = BuildTarget.StandaloneOSX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneOSX.html);  
  
        // use these options for the first build
        // buildPlayerOptions.options = BuildOptions.Development[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html);  
  
        // use these options for building scripts
        buildPlayerOptions.options = BuildOptions.BuildScriptsOnly[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.BuildScriptsOnly.html) | BuildOptions.Development[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html);  
  
        BuildPipeline.BuildPlayer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildPlayer.html)(buildPlayerOptions);
    }
}

```

Use the `Build/Build scripts` to regenerate the application and then launch it. The application will now show random changes to the background color. However the added cubes and spheres are not visible.
* * *
