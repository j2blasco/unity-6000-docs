* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html

#  [SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html).LoadScene
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
## Declaration
public static void LoadScene(int sceneBuildIndex, [SceneManagement.LoadSceneMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.html) mode = LoadSceneMode.Single); 
## Declaration
public static void LoadScene(string sceneName, [SceneManagement.LoadSceneMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.html) mode = LoadSceneMode.Single); 
### Parameters
Parameter | Description  
---|---  
sceneName | Name or path of the Scene to load.  
sceneBuildIndex | Index of the Scene in the Build Settings to load.  
mode | Allows you to specify whether or not to load the Scene additively. See [LoadSceneMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.html) for more information about the options.  
### Description
Loads the Scene by its name or index in Build Settings.
**Note:** In most cases, to avoid pauses or performance hiccups while loading, you should use the asynchronous version of this command which is: [LoadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html).  
  
When using [SceneManager.LoadScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html), the scene loads in the next frame, that is it does not load immediately. This semi-asynchronous behavior can cause frame stuttering and can be confusing because load does not complete immediately.  
  
Because loading is set to complete in the next rendered frame, calling [SceneManager.LoadScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html) forces all previous AsyncOperations to complete, even if [AsyncOperation.allowSceneActivation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-allowSceneActivation.html) is set to false. To avoid this, use [LoadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html) instead.  
  
The given `sceneName` can either be the Scene name only, without the `.unity` extension, or the path as shown in the BuildSettings window still without the `.unity` extension. If only the Scene name is given this will load the first Scene in the list that matches. If you have multiple Scenes with the same name but different paths, you should use the full path.  
  
Note that `sceneName` is case insensitive, except when you load the Scene from an [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).  
  
For opening Scenes in the Editor see [EditorSceneManager.OpenScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.OpenScene.html). `SceneA` can additively load `SceneB` multiple times. The regular name is used for each loaded scene. If `SceneA` loads `SceneB` ten times each `SceneB` will have the same name. Finding a particular added scene is not possible.  
  
If a single mode scene is loaded, Unity calls Resources.UnloadUnusedAssets automatically.
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Only specifying the sceneName or sceneBuildIndex will load the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) with the Single mode
        SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("OtherSceneName", LoadSceneMode.Additive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html));
    }
}

```

```
// Load an assetbundle which contains Scenes.
// When the user clicks a button the first Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) in the assetbundle is
// loaded and replaces the current Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).  
  
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class LoadScene : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) myLoadedAssetBundle;
    private string[] scenePaths;  
  
    // Use this for initialization
    void Start()
    {
        myLoadedAssetBundle = AssetBundle.LoadFromFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html)("Assets/AssetBundles/scenes");
        scenePaths = myLoadedAssetBundle.GetAllScenePaths();
    }  
  
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 30), "Change Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)"))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Scene2 loading: " + scenePaths[0]);
            SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)(scenePaths[0], LoadSceneMode.Single[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Single.html));
        }
    }
}

```

The following two script examples show how [LoadScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html) can load Scenes from Build Settings. `LoadSceneA` uses the name of the Scene to load. `LoadSceneB` uses the number of the Scene to load. The scripts work together.  
  
`LoadSceneA` file.
```
// SceneA.
// SceneA is given the sceneName which will
// load SceneB from the Build Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Settings.html)  
  
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class LoadScenesA : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("LoadSceneA");
    }  
  
    public void LoadA(string scenename)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("sceneName to load: " + scenename);
        SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)(scenename);
    }
}

```

`LoadSceneB` file.
```
// SceneB.
// SceneB is given the sceneBuildIndex of 0 which will
// load SceneA from the Build Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Settings.html)  
  
using UnityEngine;
using UnityEngine.SceneManagement;  
  
public class LoadScenesB : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("LoadSceneB");
    }  
  
    public void LoadB(int sceneANumber)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("sceneBuildIndex to load: " + sceneANumber);
        SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)(sceneANumber);
    }
}

```

* * *
## Declaration
public static [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) LoadScene(int sceneBuildIndex, [SceneManagement.LoadSceneParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneParameters.html) parameters); 
## Declaration
public static [SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) LoadScene(string sceneName, [SceneManagement.LoadSceneParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneParameters.html) parameters); 
### Parameters
Parameter | Description  
---|---  
sceneName | Name or path of the Scene to load.  
sceneBuildIndex | Index of the Scene in the Build Settings to load.  
parameters | Various parameters used to load the Scene.  
### Returns
**Scene** A handle to the Scene being loaded. 
### Description
Loads the Scene by its name or index in Build Settings.
An example using two scenes called `Scene1` and `Scene2`. ExampleScript1.cs is for `scene1` and ExampleScript2.cs is for `scene2`.
```
using UnityEngine;
using UnityEngine.SceneManagement;  
  
// This is scene1.  It loads 3 copies of scene2.
// Each copy has the same name.  
  
public class ExampleScript1 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene;  
  
    private void Start()
    {
        var parameters = new LoadSceneParameters[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneParameters.html)(LoadSceneMode.Additive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html));  
  
        scene = SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("scene2", parameters);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Load 1 of scene2: " + scene.name);
        scene = SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("scene2", parameters);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Load 2 of scene2: " + scene.name);
        scene = SceneManager.LoadScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html)("scene2", parameters);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Load 3 of scene2: " + scene.name);
    }
}

```

Scene2:
```
using UnityEngine;  
  
// create a randomly placed cube  
  
public class ExampleScript2 : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        cube.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-5.0f, 5.0f), 0.0f, Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-5.0f, 5.0f));
    }
}

```

* * *
