* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttribute.html

# OnOpenAssetAttribute
class in UnityEditor.Callbacks
/
Inherits from:[CallbackOrderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CallbackOrderAttribute.html)
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
Invokes a static callback method when the Unity Editor attempts to open an asset.
Unity calls any static method decorated with `[OnOpenAssetAttribute]` when attempting to open an asset, such as when double-clicking the asset in the Editor. This offers the opportunity to implement custom asset opening logic or to verify that an asset can open in the Unity Editor as opposed to an external program.  
  
The attribute targets methods and accepts two optional positional parameters: 
  * `callbackOrder`: The first parameter represents the index of the callback invocation order and must be of type `int`. This is useful if you have more than one [OnOpenAssetAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttribute.html) callbacks, and you would like them to be called in a certain order. Methods are called in ascending numerical order, starting from 0.
  * `attributeMode`: The second parameter is an `enum` value from [OnOpenAssetAttributeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttributeMode.html) that indicates whether the decorated method is called in `Execute` or `Validate` mode. `Execute` mode is intended for callbacks that implement some custom asset-opening behavior. `Validate` mode is intended to check if the Editor can open the asset. If not specified the default mode is [OnOpenAssetAttributeMode.Execute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttributeMode.Execute.html).


A method decorated with `[OnOpenAssetAttribute]` and in `Execute` mode must have one of the following signatures: 
  * `static bool OnOpenAsset(int instanceID)`
  * `static bool OnOpenAsset(int instanceID, int line)`
  * `static bool OnOpenAsset(int instanceID, int line, int column)`


**Note:** The callback method does not have to be named `OnOpenAsset` but its signature must match one of those shown.  
  
A method decorated with `[OnOpenAssetAttribute]` and in `Validate` mode must have the following signature:  
  
`static bool OnOpenAsset(int instanceID)`  
  
In [OnOpenAssetAttributeMode.Validate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttributeMode.Validate.html) mode, the method does not open the asset but checks to see if the Editor can open it. It returns `true` if the Editor can open the asset or `false` otherwise. This is equivalent to the check [AssetDatabase.CanOpenAssetInEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CanOpenAssetInEditor.html) performs.  
  
Version control system integrations primarily use this validation function to determine what files to check out. Native assets like GameObjects, Scenes, or user-made assets return `true` because they are opened and edited in the Editor. Assets like sound clips and textures return `false` because they're opened and edited in an external program.   
  
See Also: [OnOpenAssetAttributeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttributeMode.html), [AssetDatabase.CanOpenAssetInEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CanOpenAssetInEditor.html)
```
// Return true if you handled the opening of the asset or false if an external tool should open it.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Callbacks;  
  
public class MyAssetHandler : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [OnOpenAssetAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttribute.html)(1)]
    public static bool step1(int instanceID, int line)
    {
        string name = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(instanceID).name;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Open Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) step: 1 (" + name + ")");
        return false; // we did not handle the open
    }  
  
    // step2 has an attribute with index 2, so will be called after step1
    [OnOpenAssetAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttribute.html)(2)]
    public static bool step2(int instanceID, int line)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Open Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) step: 2 (" + instanceID + ")");
        return false; // we did not handle the open
    }  
  
    [OnOpenAsset(OnOpenAssetAttributeMode.Validate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttributeMode.Validate.html))]
    public static bool WillOpenInUnity(int instanceID)
    {
        if (AssetDatabase.GetMainAssetTypeAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetMainAssetTypeAtPath.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(instanceID)) == typeof(MyAssetHandler))
        {
            // We can open MyAssetHandler asset using MyAssetHandler opening method
            return true;
        }
        else  return false; // The passed instance doesn't belong to MyAssetHandler type asset so we won't be able to open it using opening method inside MyAssetHandler
    }
}

```

### Inherited Members
* * *
