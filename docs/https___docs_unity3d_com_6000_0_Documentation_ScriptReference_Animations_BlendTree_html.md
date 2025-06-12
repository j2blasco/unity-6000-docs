* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.html

# BlendTree
class in UnityEditor.Animations
/
Inherits from:[Motion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Motion.html)
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
Blend trees are used to blend continuously animation between their children. They can either be 1D or 2D.
### Properties
Property | Description  
---|---  
[blendParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree-blendParameter.html) | Parameter that is used to compute the blending weight of the children in 1D blend trees or on the X axis of a 2D blend tree.  
[blendParameterY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree-blendParameterY.html) | Parameter that is used to compute the blending weight of the children on the Y axis of a 2D blend tree.  
[blendType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree-blendType.html) | The Blending type can be either 1D or different types of 2D.  
[children](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree-children.html) | A copy of the list of the blend tree child motions.  
[maxThreshold](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree-maxThreshold.html) | Sets the maximum threshold that will be used by the ChildMotion. Only used when useAutomaticThresholds is true.  
[minThreshold](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree-minThreshold.html) | Sets the minimum threshold that will be used by the ChildMotion. Only used when useAutomaticThresholds is true.  
[useAutomaticThresholds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree-useAutomaticThresholds.html) | When active, the children's thresholds are automatically spread between 0 and 1.  
### Public Methods
Method | Description  
---|---  
[AddChild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.AddChild.html) | Utility function to add a child motion to a blend trees.  
[CreateBlendTreeChild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.CreateBlendTreeChild.html) | Utility function to add a child blend tree to a blend tree.  
[RemoveChild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.RemoveChild.html) | Utility function to remove the child of a blend tree.  
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
