* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ConvertToPrefabInstances.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).ConvertToPrefabInstances
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
public static void ConvertToPrefabInstances(GameObject[] plainGameObjects, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAssetRoot, [ConvertToPrefabInstanceSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings.html) settings, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
plainGameObjects | The array of GameObjects that will be converted to Prefab instances.  
prefabAssetRoot | The Prefab Asset used to create the Prefab instances from.  
settings | Settings to control the conversion.  
mode | Using UserAction will record undo and show dialogs if needed.  
### Description
Convert an array of GameObjects to Prefab instances of the given Prefab Asset.
This function is similar to the [ConvertToPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ConvertToPrefabInstance.html) method, except it will perform the operation on each of the GameObjects in the input.
* * *
