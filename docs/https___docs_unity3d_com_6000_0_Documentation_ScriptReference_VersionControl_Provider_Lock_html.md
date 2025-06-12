* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Lock.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).Lock
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Lock([VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets, bool locked); 
## Declaration
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Lock([VersionControl.Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) asset, bool locked); 
### Parameters
Parameter | Description  
---|---  
asset | Asset to lock/unlock.  
assets | List of assets to lock/unlock.  
locked | True to lock assets, false to unlock assets.  
### Description
Attempt to lock an asset for exclusive editing.
Depending on version control system and server setup this might be an exclusive lock preventing other people from even modifing the asset (for example: Plastic SCM or Git) or it might simply prevent other people from submitting the asset to the version control server (Perforce).
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/Lock")]
    public static void ExampleLock()
    {
        AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets = new AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html)();
        assets.Add(Provider.GetAssetByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t1 = Provider.Checkout[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Checkout.html)(assets, CheckoutMode.Exact[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.CheckoutMode.Exact.html));
        t1.Wait();
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t2 = Provider.Lock[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Lock.html)(assets, locked: true);
        t2.Wait();
    }
}

```

* * *
