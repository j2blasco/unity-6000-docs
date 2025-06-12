* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.html

# SortingLayer
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
SortingLayer allows you to set the render order of multiple sprites easily. There is always a default SortingLayer named "Default" which all sprites are added to initially. Added more SortingLayers to easily control the order of rendering of groups of sprites. Layers can be ordered before or after the default layer.
Additional resources: [Tags and Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html).
### Static Properties
Property | Description  
---|---  
[layers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer-layers.html) | Returns all the layers defined in this project.  
[onLayerAdded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer-onLayerAdded.html) | Delegate for sorting layer events when a layer is added.  
[onLayerRemoved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer-onLayerRemoved.html) | Delegate for sorting layer events when a layer is removed.  
### Properties
Property | Description  
---|---  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer-id.html) | This is the unique id assigned to the layer. It is not an ordered running value and it should not be used to compare with other layers to determine the sorting order.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer-name.html) | Returns the name of the layer as defined in the TagManager.  
[value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer-value.html) | This is the relative value that indicates the sort order of this layer relative to the other layers.  
### Static Methods
Method | Description  
---|---  
[GetLayerValueFromID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.GetLayerValueFromID.html) | Returns the final sorting layer value. To determine the sorting order between the various sorting layers, use this method to retrieve the final sorting value and use CompareTo to determine the order.  
[GetLayerValueFromName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.GetLayerValueFromName.html) | Returns the final sorting layer value. Additional resources: GetLayerValueFromID.  
[IDToName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.IDToName.html) | Returns the unique id of the layer. Will return "<unknown layer>" if an invalid id is given.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.IsValid.html) | Returns true if the id provided is a valid layer id.  
[NameToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.NameToID.html) | Returns the id given the name. Will return 0 if an invalid name was given.  
### Delegates
Delegate | Description  
---|---  
[LayerCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.LayerCallback.html) | Calls the methods in its invocation list when a sorting layer is added or removed.  
* * *
