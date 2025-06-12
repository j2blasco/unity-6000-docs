* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Scripting with assets](https://docs.unity3d.com/6000.0/Documentation/Manual/ScriptingAssets.html)
  * Stream assets directly into a build


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingResourcesatRuntime.html)
Load assets at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ModifyingSourceAssetsThroughScripting.html)
Modify source assets from code
# Stream assets directly into a build
`StreamingAssets` is a [reserved folder](https://docs.unity3d.com/6000.0/Documentation/Manual/SpecialFolders.html) that you can use to make files available to a Player build directly and bypass the standard project build process. The standard build process serializes **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and assets into binary files inside the generated Player. `StreamingAssets` allows you to add files that are already in the correct format for the target platform and that your application can load directly.
Example usages include:
  * Configuration files in JSON, XML, SQLite, or other formats.
  * Video files, for example movie files on iOS devices.
  * Files required by plugins.
  * AssetBundles (described below).


The `StreamingAssets` folder must be in the root of the `Assets` folder at `Assets/StreamingAssets`. The name is case sensitive and must be `StreamingAssets` exactly. Any files in this directory are copied without modification into the Player output. When deployed to a target device the files are copied to a location appropriate for the platform.
**Tip** : To avoid the overhead of Unity automatically importing every file from `StreamingAssets`, you can add content from other directories during the build process by calling [`AddAdditionalPathToStreamingAssets`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerContext.AddAdditionalPathToStreamingAssets.html) from a callback that implements [`BuildPlayerProcessor.PrepareForBuild`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerProcessor.PrepareForBuild.html). This is useful if, for example, your content is large and generated.
## Accessing streaming assets
The location of the `StreamingAssets` folder in your deployed application varies between platforms. To retrieve the path to the `StreamingAssets` folder reliably, use the [`Application.streamingAssetsPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html) property because it always points to the correct location on the current host platform.
On most platforms [`Application.streamingAssetsPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html) is a directory accessible using regular file system APIs.
On Android and the Web platform, it’s not possible to access the streaming asset files directly via file system APIs because these platforms return a URL. Use the [`UnityWebRequest`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) class to access the content instead.
The following example loads a file from the `StreamingAssets` folder:
```
using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

// Example of loading a file from the StreamingAssets folder
// This assumes that a file "config.json" has been placed in the Assets/StreamingAssets folder
public class LoadStreamingAssets : MonoBehaviour
{
    void Start()
    {
        StartCoroutine(LoadFile());
    }

    IEnumerator LoadFile()
    {
        string jsonData = "";
        string filePath = System.IO.Path.Combine(Application.streamingAssetsPath, "config.json");

        if (filePath.StartsWith("jar") || filePath.StartsWith("http"))
        {
            // Special case to access StreamingAsset content on Android and Web
            UnityWebRequest request = UnityWebRequest.Get(filePath);
            yield return request.SendWebRequest();

            if (request.result == UnityWebRequest.Result.Success)
            {
                jsonData = request.downloadHandler.text;
            }
        }
        else
        {
            // This is a regular file path on most platforms and in playmode of the editor
            jsonData = System.IO.File.ReadAllText(filePath);
        }

        Debug.Log("Loaded JSON Data: " + jsonData);
    }
}

```

### StreamingAssets folder limitations
  * At runtime the `StreamingAssets` location is read-only and you can’t modify or write new files to it. To write files, you can use [`Application.persistentDataPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.persistentDataPath.html) instead.
  * Don’t put Unity files (.unity, .prefab, .asset, etc.) into the `StreamingAssets` folder. These file types must be processed by a Player or AssetBundle build in order to be loadable at runtime.
  * .dll and script files located in the `StreamingAssets` folder aren’t included during script compilation.


## AssetBundles and the StreamingAssets folder
The `StreamingAssets` folder is useful if you intend to distribute `AssetBundles` directly in the Player installation, rather than downloading them on-demand.
To do this:
  1. Build the [AssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) to an output path inside `Assets/StreamingAssets`. **Note** : the .manifest files generated alongside the AssetBundle files are not required in the runtime and can be removed. For more information, refer to [AssetBundles file format](https://docs.unity3d.com/6000.0/Documentation/Manual/assetbundles-file-format.html).
  2. Build the Player. The AssetBundles are included in the platform-specific output.
  3. Write loading code that uses the `Application.streamingAssetsPath` to determine the path to the AssetBundles. Depending on the platform, you can load them as a local file path, or with [UnityWebRequestAssetBundle](ScriptingRef:Networking.UnityWebRequestAssetBundle.GetAssetBundle). **Note** : On Android it’s not necessary to cache the AssetBundle or to perform CRC checks, because the file is already present on local storage.


The [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html?preview=1) package uses this mechanism automatically for local content.
Alternatively, AssetBundles and Addressables can be hosted on a remote server and downloaded on-demand rather than using the `StreamingAssets` folder. This is preferred for situations where the content is large, or frequently updated, or where you want to avoid the overhead of releasing new Player builds when you want to change or add new content.
## Additional resources
  * [Loading resources at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingResourcesatRuntime.html)
  * [Modifying source assets from code](https://docs.unity3d.com/6000.0/Documentation/Manual/ModifyingSourceAssetsThroughScripting.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingResourcesatRuntime.html)
Load assets at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ModifyingSourceAssetsThroughScripting.html)
Modify source assets from code
