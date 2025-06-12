* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html

# AssetBundle
class in UnityEngine
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
/
Implemented in:[UnityEngine.AssetBundleModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AssetBundleModule.html)
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
API for accessing the content of AssetBundle files.
This class exposes an API, via static methods, for loading and managing AssetBundles.  
  
This same class offers non-static methods and properties that expose the contents of a specific loaded AssetBundle, including the ability to load an Asset from within an AssetBundle.  
  
Create AssetBundles by calling [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html) or using the [Addressables package](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html). The build process generates one or more AssetBundle files, and each AssetBundle file contains a serialized instance of this class.  
  
Note: AssetBundle.LoadAsset, and the other Load methods, do not support loading Scenes from AssetBundles. Instead, in runtime you load the streamed scene AssetBundle and then call [SceneManager.LoadScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadScene.html) or [SceneManager.LoadSceneAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html) with the Scene name. In the Editor it is not supported to load Scenes from AssetBundles so calls to [EditorSceneManager.OpenScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.OpenScene.html) will fail with an error that the Scene file is not found.  
  
Additional resources: [Intro to AssetBundles](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html), [UnityWebRequestAssetBundle.GetAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html), [BuildPipeline.BuildAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html).
```
using System.Collections;
using UnityEngine;
using UnityEngine.Networking;  
  
public class SampleBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator Start()
    {
        var uwr = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)("https://myserver/myBundle.unity3d");
        yield return uwr.SendWebRequest();  
  
        // Get an asset from the bundle and instantiate it.
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundle = DownloadHandlerAssetBundle.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)(uwr);
        var loadAsset = bundle.LoadAssetAsync<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>("Assets/Players/MainPlayer.prefab");
        yield return loadAsset;  
  
        Instantiate(loadAsset.asset);  
  
        bundle.Unload(true);
    }
}

```

### Static Properties
Property | Description  
---|---  
[memoryBudgetKB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle-memoryBudgetKB.html) | Controls the size of the shared AssetBundle loading cache. Default value is 1MB.   
### Properties
Property | Description  
---|---  
[isStreamedSceneAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle-isStreamedSceneAssetBundle.html) | Return true if the AssetBundle contains Unity Scene files  
### Public Methods
Method | Description  
---|---  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.Contains.html) | Check if an AssetBundle contains a specific object.  
[GetAllAssetNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.GetAllAssetNames.html) | Return all Asset names in the AssetBundle.  
[GetAllScenePaths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.GetAllScenePaths.html) | Return all the names of Scenes in the AssetBundle.  
[LoadAllAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAllAssets.html) | Loads all Assets contained in the AssetBundle synchronously.  
[LoadAllAssetsAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAllAssetsAsync.html) | Loads all Assets contained in the AssetBundle asynchronously.  
[LoadAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAsset.html) | Synchronously loads an Asset from the AssetBundle.  
[LoadAssetAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAssetAsync.html) | Asynchronously loads an Asset from the bundle.  
[LoadAssetWithSubAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAssetWithSubAssets.html) | Loads Asset and sub Assets from the AssetBundle synchronously.  
[LoadAssetWithSubAssetsAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAssetWithSubAssetsAsync.html) | Loads Asset and sub Assets from the AssetBundle asynchronously.  
[Unload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.Unload.html) | Unloads an AssetBundle freeing its data.  
[UnloadAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.UnloadAsync.html) | Unloads assets in the bundle.  
### Static Methods
Method | Description  
---|---  
[GetAllLoadedAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.GetAllLoadedAssetBundles.html) | Get an enumeration of all the currently loaded AssetBundles.  
[LoadFromFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html) | Synchronously loads an AssetBundle from a file on disk.  
[LoadFromFileAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFileAsync.html) | Asynchronously loads an AssetBundle from a file on disk.  
[LoadFromMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemory.html) | Synchronously load an AssetBundle from a memory region.  
[LoadFromMemoryAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromMemoryAsync.html) | Asynchronously load an AssetBundle from a memory region.  
[LoadFromStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromStream.html) | Synchronously loads an AssetBundle from a managed Stream.  
[LoadFromStreamAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromStreamAsync.html) | Asynchronously loads an AssetBundle from a managed Stream.  
[RecompressAssetBundleAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.RecompressAssetBundleAsync.html) | Asynchronously recompress a downloaded/stored AssetBundle from one BuildCompression to another.  
[UnloadAllAssetBundles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.UnloadAllAssetBundles.html) | Unloads all currently loaded AssetBundles.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
